---
tags:
  - CSE_223B
---
# Background
**ZooKeeper** is a service for coordinating processes for distributed applications. The primary engineering outcome is the wait-free (lock free) API called the **coordination kernel** that allows developers to build performant and fault-tolerant applications on top of it.

The wait-free property is not sufficient for coordination. It also guarantees [[Group Communication#Types of Ordering Semantics|FIFO client ordering]] of all operations and **linearizable writes** enables an efficient implementation of the service. 
- FIFO order enables asynchronous submission of operations
- Allows multiple outstanding operations $\to$ better performance 
- **Linearizablity** is the idea that ?

ZooKeeper comprises of an ensemble of servers with [[Replication]] to achieve high availability and performance. To guarantee linearizablity, they implement a leader-based atomic broadcast protocol called **Zab**. 
- Read operations are highly common and so increasing the throughput is ideal.
- Therefore Zab is not needed to totally order them.
- Writes OTOH require ordering. 

Caching data is important to increase performance of reads.
- ZooKeeper uses a watch mechanism (like Unix `watch`) to enable clients to cache data without managing the client cache directly. 
- A client can watch for an update to a given data object and receive a notification upon an update. 
- If ZK waited for the client instead, i.e managed the client cache directly,
	- client is slow $\implies$ ZK would block all updates $\implies$ system is slow
	- client is faulty $\implies$ ZK would block all updates $\implies$ system is delayed
- If ZK used a timed lease, it would only bound the impact of slow/faulty clients. 

ZK also contributes **coordination recipes**. We can use ZK to build higher level coordination primitives, even blocking and strongly consistent primitives.

# ZooKeeper Service
Terminology:
- **Client**: a user of the ZooKeeper service
- **Server**: a process providing the ZooKeeper Service 
- **Znode**: an in-memory data node in the ZooKeeper data, organized in a hierarchial namespace referred to as the **data tree**
- Update/write refer to any operation that modifies the state of the data tree. 
- Clients establish a **session** when they connect to ZK and obtain a **session handle**[^1] through with they issue requests.

[^1]: Very much like the `BinStorageClient` from Lab 2.

## Znodes 
Znodes are an abstraction of a set of data nodes. They are hierarchial and follow the Unix notation for file system paths. 
```
			[/app1/p_1] (X)
            /
	 {/app1}--[/app1/p_2] (Y)
	/       \
{/}          [/app1/p_3] (Z)
 	\	   
	 {/app2} ----
```
If we wanted to call node `(Y)`, its name is `/app1/p_2`. This above example only has three znodes. There are two types of znodes:
- **Regular**: Clients manipulate regular znodes by creating and deleting them specifically
- **Ephemeral**: Clients create such znodes, and they either delete them *explicitly* or the system removes them automatically.
	- Removal is by session creator termination either by deliberation or failure.

When creating a new znode, a client can set a *sequential* flag. Nodes created with this flag have the value of a [[Monotonic#Monotonically Increasing|monotonically increasing]] counter appended to its name. In particular, if $n$ is a new znode and $p$ is its parent, then $\text{seq}(n) \geq \text{seq}(m)$ for all children $m$ of parent $p$. 

## Watches
Watches allow clients to receive timely notifications of changes without requiring polling[^2]. When a client issues a read operation with a watch flag set, the operation completes as normal, except that the server promises to notify the client when the information returned has changed.

> Tell me when the data changes!

Watches are *one-time triggers* associated with a session. They disappear when the session ends or by trigger. They **do not provide the change** and only **notify** that there is a change.

[^2]: Polling is a technique where a client repeatedly checks for updates at regular intervals. 

For example, if a client issues `getData("/foo", true)`, the server will return the data associated with znode `/foo`. When (or if) there is a change, the client will receive exactly $1$ notification.

It is essentially a file system with a simplified API and only full data reads and writes OR a key/value table with hierarchial keys. 

> [!idea] Notifications
> Watches are a one-time message that the data is stale.

## Sessions
A client connects to ZK and initiates a session.
- Sessions have associated timeouts
- ZK considers a client faulty if it does not receive responses for more than the timeout period.
- A session ends with explicit termination by the client or by ZK if it considers the client faulty.
- Sessions allow transparent failover between servers in the ensemble.

# Client API 
Simple API similar to a file system.
- `create(path, data, flags) -> znode.name`
	- creates a znode at the specified `path`, stores `data[]`. `flags` sets regular/ephemeral and sequential/non-sequential.
- `delete(path, version)`
	- deletes the znode at `path` if its version matches `version`.
- `exists(path, watch) -> bool`
	- returns true if the znode at `path` exists. If `watch` is true, sets a watch on the znode
- `getData(path, watch, version) -> data, metadata`
	- returns data and metadata of znode at `path`. If `watch` is true, sets a watch on the znode. If the watch does not exist, no watch is set.
- `setData(path, data) -> [znode.children.names]`
	- returns set of names of the children of a znode
- `sync(path)`
	- waits for all updates pending at the start of the operation to propagate to the server the client is connected to

All methods have a synchronous and asynchronous version. Each request needs the full path of the znode (no extra state, less APIs, less API complexity).

The **version** number enables the implementation of conditional updates. Versions must match; otherwise throw error. If version is `-1`, it matches any version.

# ZooKeeper Guarantees
- **Linearizable Writes**: all requests that update the state of ZK are serializable (?) and respect precedence (?).
	- In ZK, they allow multiple outstanding operations, calling it A-linearizability instead of linearizability (traditionally, only one operation can be outstanding at a time).
	- All results that hold for linearizability also hold for A-linearizability.
	- ZK processes read requests locally at each replica $\implies$ service can scale linearly wrt server addition.
- **FIFO Client Order**: all requests from a given client are executed in the order they were sent by the client. 

## Example 1
Consider a system comprising of a number of processes that need to elect a leader. When a new leader is elected, it must update the configuration of the system and then notify the other processes of the new leader. We have two requirements
- **R1**: The leader must have an exclusive lock to the configuration data.
- **R2**: If the new leader dies before the configuration is fully updated, we do not want processes to use this partial configuration.

Note that we do not care if the leader dies after configuration update and before notification because a new leader will be elected and update the configuration again. A distributed lock system like in [[?]] can be used to satisfy `R1`. However, it does not satisfy `R2`. 

The idea is to have some sort of "commit" operation that is atomic and have a znode that represents this commit. We can have a "ready" znode that is deleted when the leader is ready to write. In order,
```
Leader Operations:
1. Delete "ready" znode
2. Write configuration data
3. Create "ready" znode
```
If a process sees the "ready" znode, it must also see the modified configuration state from the new leader. If the leader dies before creating the "ready" znode, the other processes know the configuration data has not been finalized.

**Error Case**: What happens if a process sees the "ready" znode exists before the new leader starts to make a change and then begins reading the configuration state while the new leader is editing it?
```
ascii timeline of how this can happen
```
The problem is solved by the ordering guarantee for the notifications. 
- if a client is [[#Watches|watching]] for a change, the client will see the notification event before it sees the new state of the system after the change. 
- if the process that reads the "ready" znode requests to be notified, it will see a notification informing the client of the change before it can ready any of the new configuration. 

**Error Case**: What if two clients $A$ and $B$ have a separate znode they use to communicate with one another? Suppose 
1. $A$ changes the shared coniguration
2. $A$ sends a notification to $B$ by changing its znode
3. $B$ receives the notification and expects to see the change when it re-reads the configuration.

If $B$'s ZK replica is slightly behind $A$ (due to cache ?), it may not see the new configuration. By issuing a write (or more efficiently, a `sync`) to ZK, $B$ can ensure that it sees the new configuration. This is similar to `flush` in [[Group Communication#Introduction & Motivation The ISIS System|ISIS]]. 

Two liveness and durability guarantees:
- if a majority of ZK servers are active and can communicate with each other, then the service is available
- if the ZK service responds successfully to a change request, the change persists across any number of failures as long as a [[Quorum|quorum]] of servers is eventually able to recover.

# ZooKeeper Implementation
ZK provides high availability by replicating the data on each server that composes the [[#ZooKeeper Service|service]]. Servers may fail by crashing and faulty servers may later recover. At a high level,
```
	        |                                    |
Write    ---+--> [Request Processor]          TXN|
Request	    |          TXN\_->[Replicated DB]----+-> Response
			|						^		     |				
------------------------------------+------------+
                              Read Request
```
Upon receiving a request, a server prepares it for execution (**request processor**). If a request requires coordination (like a write), then they use an agreement protocol (like an implementation of  [[Group Communication#ABCAST (Atomic Broadcast)|atomic broadcast]]), and finally servers commit changes to ZK DB fully replicated across the ensemble.

A read is simple (see above). Each znode is in memory and by defualt maximally 1 MB.

Recoverability, is done by logging updates to disk, and forcing writes to be on disk before application to in-memory database (kind of like a write-ahead log). 

As part of the **agreement protocol**, write requests are forwarded to sen single server, called the **leader**. The rest of the ZK servers are called **followers**. 

## Request Processor
The messaging layer is atomic, so local replicas never diverge. Some servers may have applied more **transactions** than others. 
- Unlike requests sent from clients, the transactions are idempotent. 
- When the leader receives a write request, it calculates the future state of the system when the write is applied and transforms it into a transaction that captures the new state. 
- We need to calculate the future state because of potential outstanding transactions.

## Atomic Broadcast
All requests that update ZK are forwarded to the leader. The leader executes the request and broadcasts the change to the ZK state via Zab, an atomic broadcast protocol.
- Zab uses simple majority quorums to achieve consensus.
- Minimum $2f + 1$ servers with $f$ tolerated failures.
- Because state changes are dependent on the application of previous state changes, Zab provides *stronger* order guarantees than regular atomic broadcast.
	- Zab guarantees that changes broadcast by a leader are delivered in the order they were sent and all changes from previous leaders are delivered to an established leader before it can broacast new changes.
- TCP is used. 
- Log for proposals.
- Write ahead log for in memory database and disk.

## Replicated Database
Each replica has a copy in memory of the ZK state. When it crashes, recovery is done by replaying periodic snapshots and only requires redelivery of messages since the start of the snapshot.

It is a **fuzzy snapshot** because ZK does DFS of the znode tree reading each znode data and writin them to disk. Since the snapshot is not atomic, it may capture some updates and miss others during copy. Since state changes are idempotent, we can apply them twice as long as we apply them in the right order.

## Client-Server Interactions
- When a server processes a write request, it sends and clears all notifications relative any watch that corresponds to that update.
- Servers process writes in order. No other writes nor reads are done concurrently with this write.
	- Ensures strict succession of notifications 
- Notifications are handled locally. 
- Read requests are handled locally. Each read request is processed and tagged with a `zxid` that corresponds to the last transaction seen by the server. It defines the partial order of the read requests wrt the write requests.
- Reads can return stale values, but this allows for more performance.
	- Can be fixed with `sync` + `read`. 
- To detect client session failures, it sends a heartbeat message if it has been idle for $s/3$ ms and switch if it has not received a response for $2s/3$ ms, where $s$ is the session timeout in milliseconds.
