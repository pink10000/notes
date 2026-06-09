---
tags:
  - CSE_223B
---
# Overview
Spanner is a scalable, globally-distributed database that shards (partitions, splits) data across many sets of [[Paxos Algorithm|Paxos]] state machines in data centers spread all over the world. [[Replication]] is used for global availability and geographic locality (data is near where it will be accessed). Spanner *automatically reshards data* across machines to balance load in response to failures. ^c7033a

Data is stored in schematized (?), semi-relational (?) tables, and versioned with its commit time. Garbage collection policies exist to delete older data. Spanner provides [[Networked File Systems#Definition (External Consistency)|externally consistent]] reads and writes, and globally-consistent reads across the database at a timestamp. 

Timestamps allow globally-meaningful commit timestamps to transactions, even if they are distributed. They reflect serialization order, satisfying external consistency (or linearizability). This is done via [[#TrueTime]]. 

# Hierarchy 
A Spanner deployment is called a **universe** (there are few universes). A universe is organized as a set of **zones**, administrative deployment locations across which data can be replicated. 
- Zones can be added/removed as the system is running.
- Zones are a unit of physical isolation (one or more in a datacenter).
- Zones have a **zonemaster**, and hundreds to thousands of **spanservers**. 
	- Zonemasters assign data to spanservers.
	- Spanservers serve data to clients.
- Per-zone **location proxies** are used by clients to locate the spanservers.
	- This achieves a similar purpose as [[Chord]].
- **Universe master** and **placement driver** are for debugging and moving data across zones respectively. 

A spanserver contains 100-1000 instances of a data structure called a **tablet**. A tablet contains a bag of:
```
(key: String, timestamp: i64) -> String
```
In particular, we can think of it as a collection of rows (not necessarily contiguous!) in a database. They are files stored as a set of [[B-trees|B-tree]]-like files and a [[HarpFS#Performance and The Write-Ahead Log|write-ahead-log]].

## Replication and Paxos
Spanner is designed to survive datacenter failures, so data must be [[Replication|replicated]]. 

Each spanserver implements one instance (a single state machine) of [[Paxos Algorithm|Paxos]], storing its metadata and log in its corresponding tablet. Leaders live long and have a time-based leader lease (defaults to $10$ seconds). 

The Paxos state machines are used to implement a "consistently" "replicated" bag of mappings. Writes must initiate Paxos at the leader (writes must go through the leader) and reads access state directly from that particular tablet at *any* replica that is sufficiently up-to-date[^1]. Spanner calls this a **Paxos group**. ^215196

[^1]: Up-to-date is determined by the [[#TrueTime]] API.

^b608e0

At every replica there is a **Paxos leader**. The leader must implement a **lock table** for concurrency control. The lock table maps ranges of keys to lock states. Operations that require synchronization, such as transactional reads, acquire locks in the lock table; other operations bypass the lock table.

> [!example] Example
> An example of a **transaction** is transferring money between two bank accounts. The database must acquire locks on both accounts, **read** their current balances, verify sufficient funds, debit one account, and credit the other before committing. This ensures atomicity and isolation. 
> 
> At the same time, someone could try to pull money from the account while it is doing this operation. Thus, we need a lock to ensure this operation is not interfered with.
> 
> It is up to the application to determine what is a transactional read, vs. a regular read.

At every replica that is a leader, each spanserver implements a **transaction manager** to support distributed transactions. The transaction manager is used to implement a **participant leader**, and other replicas are referred to as **participant slaves**. If a transaction only involves one Paxos group, it can bypass the transaction manager. Otherwise, the groups' leaders coordinate to perform [[Two Phase Commit]]. One of the participant groups is chosen as the **coordinator leader** and the slaves of that group as **coordinator slaves**. ^e9ff96

> [!example] Distributed Transaction Example
> An example of a **distributed transaction** is processing an e-commerce order where the `Inventory` data lives in one Paxos group and the `User Billing` data lives in another Paxos group. 
> 
> The database must acquire locks in both groups, debit the inventory, and charge the user's account. Because this transaction spans multiple Paxos groups, their leaders must coordinate using Two-Phase Commit to ensure both updates succeed together or fail together.
> 
> It is important to note that it is up to the application to determine what is a transactional read, not Spanner.

# Directories and Placement
Spanner supports a bucketing abstraction called a **directory**, a set of contiguous keys that share a common prefix (the authors say *bucket* is a better word). The primary purpose of directories is to allow applications to control the [[#^c7033a|locality]] of their data. 
- A directory is *the unit* of data placement. 
- When data is moved, the entire directory is moved. 
- Movement can be done to load balance a Paxos group. 
- Put directories that are frequently accessed together. 
	- This is application specific. 
- A directory is the smallest unit whose geographic-replication properties (or **placement**) can be specified by an application. 
- `movedir` is the background task used to move directories between Paxos groups or add/remove replicas. 
	- Movement is quick, 50 MB in a few seconds. 
	- Implemented as multiple transactions to avoid blocking ongoing reads and writes.
Spanner will shard a directory into multiple **fragments** if it grows too large. They may be served from different Paxos groups. *Technically*, `movedir` moves fragments, and not whole directories, between groups. 

# Data Model (How Applications Use Spanner)
Spanner exposes a data model based on schematized semi-relational tables, a query language (like SQL), and general purpose transactions. These are because of mistakes in previous projects. 

Tables only *look* relational. 
- Every table is required to have an ordered set of one or more primary-key columns.
- These keys form the "name" of the row (why it looks like a key-value store).
- Imposing this is necessary to control data locality through choice of keys.

Pulling data from five different servers across the country for a single query is slow. Spanner solves this by making the application declare which data should physically live together. 
- Each database is partitioned by clients into one or more hierarchies of tables.
- Client applications explicitly declare these in the database schema using `INTERLEAVE IN` declarations.
- The table at the very top of the hierarchy is called a **directory table**.
- A row in that directory table, combined with descendant rows in the interleaved tables that start with the exact same key, logically forms a directory.

```
CREATE TABLE Users {
  uid INT64 NOT NULL, email STRING
} PRIMARY KEY (uid), DIRECTORY;

CREATE TABLE Albums {
  uid INT64 NOT NULL, aid INT64 NOT NULL,
  name STRING
} PRIMARY KEY (uid, aid),
  INTERLEAVE IN PARENT Users ON DELETE CASCADE;

-------------- Directory A
A Users(1)        <-- different table!
A Albums(1,1)    
A Albums(1,2)    
-------------- Directory B
B Users(2)       <- different table!
B Albums(2,1)
B Albums(2,2)
B Albums(2,3)
--------------

Visualize photo metadata
```

The command `ON DELETE CASCADE` means if a row is deleted, the child rows are deleted. 

## The Spanner Hierarchy Tree
```
Universe
    Zone
        Spanserver
            Tablet
                Directory
                    Row
                        Column
                Fragment
                    Row
                        Column / Versioned Value
```

# TrueTime
The API consists of:
```
TT.now()     : TTinterval: [earliest, latest]
TT.after(t)  : true if t has definitely passed
TT.before(t) : true if t has definitely not arrived
```
It is an interval with bounded time uncertainty. Let $\vepsi$ be the instantaneous error bound, which is half of the `TTinterval` width. Let the absolute time of an event $e$ be the function $t_{abs}(e)$. TrueTime guarantees that for an invocation $\texttt{tt} = \texttt{TT.now()}$. That is, 
$$
\texttt{tt.earliest} \leq t_{abs}(e_{now}) \leq \texttt{tt.latest}
$$
where $e_{now}$ is the invocation event. This is possible via GPS and atomic clocks which have different, unrelated failure modes. 

A **time master** machine is given per datacenter and a **timeslave daemon** per machine. A majority of the time masters have GPS receivers with dedicated antennas. The remaining masters (called **Armageddon masters**) are equipped with atomic clocks. All time references are regularly compared against each other. Masters also cross check the rate at which its reference advances time against its own local clock, and evicts itself if there is substantial divergence. 
- Every daemon polls a variety of masters for redundancy.
- Uses [Marzullo's algorithm](https://en.wikipedia.org/wiki/Marzullo%27s_algorithm) for time interval estimation.
- $\vepsi$ slowly grows, but drops (like a sawtooth).
- $\bar{\vepsi} = 4$ ms most of the time.

# Concurrency Control
[[#TrueTime]] is used to implement:
- Externally consistent transactions, 
	- `read-write transaction`
- Lock-free read-only transactions,
	- `read-only transaction`
- Non-blocking reads in the past
	- `snapshot read, client-provided timestamp`
	- `snapshot read, client-provided bound`
This enables that a read at timestamp $t$ reads exactly the effects of every committed transaction as of $t$. **Paxos writes** are writes performed by Paxos during operation. **Spanner client writes** are writes performed by a client. For example, two-phase commit generates a Paxos write for the prepare phase that has no corresponding Spanner client write.

A `read-only transaction` is predeclared as not having any writes. This ensures that incoming writes are not blocked since they do not lock. They can proceed [[#^215196|on any replica that is sufficiently up-to-date]]. ^5f7eac

A `snapshot read` is a read in the past that:
- Executes without locking.
- Client can provide timestamp or bound (and let Spanner choose).
- Only executes [[#^215196|on any replica that is sufficiently up-to-date]]. ^31c538

## Paxos Leader Leases
Spanner's Paxos implementation uses timed leases to make leadership long-lived. A potential leader sends requests for timed **lease votes**. Upon receiving a [[Quorum]], the leader has a lease. The lease extends on a successful write.

A **lease interval** is from when it has enough votes in the quorum, to when it no longer has a quorum once the leases expire. It is invariant that each lease interval is disjointed from any other Paxos leader within the group. 
- Invariance is how it can confidently assign timestamps to transactions in monotonically increasing order without constant coordination.
- Leaders can abdicate before its lease expires by releasing its slave replicas from their lease votes.
- There is a strict constraint on when a leader can safely abdicate:
	- Leader keeps track of max timestamp it has assigned to any operation, $s_{max}$.
	- Before the leader can abdicate, it must use TrueTime and wait until `TT.after(s_max)` is true. 
	- $s_{max}$ is advanced.

Transactional reads and writes use two-phase locking. They can be assigned a time between all locks acquired and any locks released. 

## Lemma (Transaction Time Invariant)
Spanner enforces this for external consistency. If the start of a transaction $T_{2}$ occurs after the commit of a transaction $T_{1}$, then the commit timestamp must be greater than $T_{1}$. 

Let start and commit events of transaction $T_{i}$ be $e_{i}^{start}$ and $e_{i}^{commit}$. Let the commit timestamp of $T_{i}$ be $s_{i}$. Then:
$$
t_{abs}(e_{1}^{commit}) < t_{abs}(e_{2}^{start}) \implies s_{1} < s_{2}
$$
Let the *arrival* event of the commit request at the [[#^e9ff96|coordinator leader]] for a write $T_{i}$ be $e_{i}^{server}$. Transaction execution and timestamp assignment obeys:
1. Coordinator leader for write $T_{i}$ assigns commit time stamp $s_{i} \geq \texttt{TT.now().latest}$, computed after $e_{i}^{server}$. 
2. **Commit Wait**: Coordinator leader ensures that clients cannot see any data committed by $T_{i}$ until $\texttt{TT.after}(s_{i})$ is true. Ensures that $s_{i} < t_{abs}(e_{i}^{commit})$. ^f2d588

Proof: 
$$
\begin{aligned}
s_{1} &< t_{abs}(e_{1}^{commit}) && \text{Commit Wait} \\
t_{abs}(e_{1}^{commit}) &< t_{abs}(e_{2}^{start}) && \text{Assumption} \\
t_{abs}(e_{2}^{start}) &\leq t_{abs}(e_{2}^{server}) && \text{Causality} \\
t_{abs}(e_{2}^{server}) &\leq s_{2} && \text{Start} \\
s_1 &< s_{2} && \text{Transitivity}
\end{aligned}
$$
This is how Spanner correctly determines [[#^b608e0|whether a]] [[#^31c538|replica is sufficiently]] [[#^5f7eac|up-to-date]] to satisfy a read. Each replica keeps $t_{safe}$, the maximum timestamp at which a replica is up-to-date, such that a read can occur if $t \leq t_{safe}$. In particular:
$$
t_{safe} = \min\left(t_{safe}^{Paxos}, t_{safe}^{TM}\right)
$$
where each Paxos state machine has a safe time (highest-applied Paxos write), and each transaction manager has a safe time. 

$t_{safe}^{TM}$ deals with the uncertainty of the future, specifically transactions that are in the middle of a two-phase commit ("prepared", but not yet "committed"). 
- If a replica has zero prepared transactions pending, $t_{safe}^{TM} = \infty$.
- If there is a prepared transaction, the state of the data is indeterminate; the replica does not yet know if the transaction will ultimately commit or abort.
- During prepare, every participant leader for a group $g$ and transaction $T_{i}$ is assigned a prepare timestamp $\left(s_{i,g}^{prepare}\right)$.
- The coordinator leader ensures that the transaction's commit timestamp $s_{i} \geq s_{i,g}^{prepare}$ over all participant groups $g$. 
- Therefore $\forall g, \forall T_{i}, t_{safe}^{TM} = \min_{i}\left(s_{i,g}^{prepare}\right) - 1$.

Read-only transaction executes in two phases:
- Assign timestamp $s_{read}$.
- Execute transaction reads as snapshot reads at $s_{read}$. 

### Refining TM Safety
A single prepared transaction can prevent $t_{safe}$ from advancing. As a result, no reads can occur at later timestamps, even if they do not conflict. Augmenting $t_{safe}^{TM}$ with a fine-grained mapping from key ranges to prepared-transaction timestamps fixes this, by checking the range on incoming reads.

### Refining Safe Paxos Time During Idleness
If we have no Paxos writes, $t_{safe}^{Paxos}$ will never advance, thus blocking writes. Spanner fixes this by taking advantage of the [[#Paxos Leader Leases|disjointedness of leader-lease intervals]]. Each Paxos leader keeps a mapping called $\texttt{MinNextTS}(n)$ which acts as a threshold promising the minimum timestamp that could possibly be assigned to the next future write. 
- A replica is allowed to advance its $t_{safe}^{Paxos}$ to $\texttt{MinNextTS}(n) - 1$ once it has applied all writes up through sequence number $n$.
- The leader enforces this promise using its leader lease, ensuring no overlapping promises occur across different leaders.
- By default, a leader proactively advances these $\texttt{MinNextTS}()$ values every $8$ seconds. This guarantees that even completely idle Paxos groups can still serve snapshot reads without having to wait for a new write to arrive.

# Implementation Details
## Read-Write Transactions
### 1. Client Execution
Writes that occur in a transaction are *buffered* at the client until commit.
- Thus, reads in a transaction do not see the effect of the transaction's writes.
- This is because reads return a timestamp, and uncommitted writes have not yet been assigned timestamps. 
- If the client takes a long time to process the data, it sends `keepalive` messages to the participant leaders to prevent them from timing out and aborting the transaction. 

Reads within `read-write transactions` use wound-wait to avoid deadlocks.
- Wound-wait is a preemptive technique for deadlock prevention. 
- Let transaction $T_{n}$ be older than transaction $T_{k}$, i.e. $n > k$. When transaction $T_n$ requests a data item currently held by $T_{k}$ (implying $T_k$ reached the system first), $T_n$ **waits** only if it has a timestamp larger than that of $T_{k}$. 
- Same scenario, but $n < k$. Then $T_{k}$ is killed ($T_{k}$ is **wounded** by $T_n$), and $T_{n}$ starts.

### 2. Prepare Phase
When a client has finished all reads and buffered all writes, it can begin 2PC. The client chooses one of the Paxos groups to be the "coordinator" and sends a commit message and the buffered writes to the leader of all "participant" groups. Having the client drive the 2PC avoids sending data twice. 

A participant leader (except the coordinator) first acquires write locks for the incoming data. It then chooses a **prepare timestamp** (larger than $s_{max}$) and logs a prepare record through its Paxos state machine. It then notifies the coordinator of this prepare timestamp. 

### 3. Coordinator Phase & Commit-Wait
The coordinator replica cannot apply the commit record yet. It needs to wait until $\texttt{TT.after}(s)$, as defined in [[#^f2d588|commit wait]]. The coordinator typically waits at least $2\bar{\vepsi}$. After the wait, the coordinator sends the commit timestamp to the client and all other participant leaders. All participants then apply at the same timestamp and then release locks. 

## Read-Only Transactions
Assigning a timestamp requires a negotiation phase between all of the Paxos groups that are involved in the reads. Spanner requires a **scope** abstraction for every read-only transaction; it is an expression that summarizes the keys to be read. 
- Scope's values are served by a single Paxos group $\to$ client issues read-only transaction to that group's leader. 
	- It assigns a timestamp $s_{read}$ and executes it.
	- Let $\texttt{LastTS}()$ be the timestamp of the last committed write at a Paxos group. No prepared transactions, then $s_{read} = \texttt{LastTS}()$.
- Multiple Paxos groups $\to$ reads execute at $s_{read} = \texttt{TT.now().latest}$.

$\texttt{LastTS}()$ can block a non-conflicting read-only transaction while it waits for the last transaction commit. We can fix this by doing something similar to [[#Refining TM Safety]] by adding key ranges it actually conflicts with. 

## Schema-Change Transactions
Clients need to be able to change the schema of their databases. Spanner cannot use standard read-write transactions to update the schema, since a single database may have millions of participant Paxos groups (very slow!). 

A non-blocking way to do this is to register these operations in the future TrueTime timestamp $t$. Since it is in the future, the system has time to register the upcoming change across thousands of servers with minimal disruption to other concurrent activity. 

Suppose we get an operation with some timestamp $t'$. 
- If $t' < t$, then the operation proceeds normally, using the old schema.
- If $t' > t$, then the operation must block and wait for the schema-change transaction until the new schema is fully applied. 

Ultimately, this is only possible because of [[#TrueTime]], since the clocks are highly synchronized. 