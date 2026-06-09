---
tags:
  - CSE_223B
---
Largely from [paper](https://dl.acm.org/doi/pdf/10.1145/224057.224070). 
# Overview
**Bayou** is a [[Replication|replicated]], weakly consistent stroage system designed for a mobile computing environment that includes portable machines with less than ideal network connectivity. To maximize [[CAP Theorem#CAP Theorem|availability]], users can read and write any accessible replica. Bayou supports mechanisms to detect and resolve update conflicts to move towards [[CAP Theorem#BASE|eventual consistency]]. 

It includes novel methods for conflict detection, called **dependency checks** and **per-write conflict resolution** based on client-provided merge procedures. Bayou servers must also be able to **roll back** the effects of previously executed writes and redo them according to a global serialization order.  ^4fd496

Supporting discinnected workgroups is a central goal of the Bayou system. This can only be done with weakly consistent, replicated data. 
- [[Replication]] is desired since a single storage site may not be reachable from mobile clients or within disconnected workgroups
- [[CAP Theorem#Definition (Weak Consistency)|Weak Consistency]] is desired since any replication scheme providing only one copy such as requiring clients to access a [[Quorum]] or to acquire [[Frangipani#Lock Service|exclusive locks]] on data that they wish to update, yields unacceptably low write availability in partitioned networks. 
Therefore Bayou must allow clients to read and write to any replica without the need for explicit coordination with other replicas. 

Bayou **does not provide transparency** for existing file system and database applications. The application should instead be the one to handle conflicts. Bayou extends [[CodaFS#Conflict Handling]] by letting applications exploit domain-specific knowledge to achieve "automatic conflict resolution" (ACR).  ^8e3e68
- ACR is desirable ebcause it enables high availability. 
- Data can be read at all times, even if conflicts have not been fully resolved.

They also contribute two states of an update, committed and tentative, and mechanisms to for managing these two states of an update.  ^b56ef5

# System Model
Each **data collection** is replicated in full at a number of **servers**. Applications running as **clients** interact with the sevrers through the Bayou API, implemented as a client stub bound with the application. This API supports `read` and `write`. 
- `read` operations permit queries over a data collection
- `write` can insert, modify, delete a number of data items in a collection
	- contains metadata for conflict detection/resolution, a globally unique `writeID` assigned by the server that accepted the `write`
- both are performed at a single server, but can be done at any server 

The storage system is an ordered log of the `write`s plus data resulting frm execuitng these `write`s. Each server perofms it locally with coflicts detected and resolved as they are encountered during execution. Then he sevrer makes the effects of all known writes acaialble for `read`ing. 

With the goal of requiring as little of the network as possible, Bayou servers propagate `write`s among themselves during pair-wise contacts (when two servers contact each other), called **anti-entropy sessions**. The two servers exchange `write` operations so that when they are finished, they agree on the set of Bayou `write`s they have seen and the order to perform them. ^73fdb6

As long as no set of servers are permanently partitioned, each `write` will eventually reach all servers, even if at most one pair of servers is ever connected at once. Convergence depends on 
- network connectivity
- frequency of anti-entropy
- policies by which servers select anti-entropy partners
	- optimality is not discussed

# Conflict Detection and Resolution
Different applications have different notions of what it means for two updates to conflict, and such that conflicts cannot always be identified by simply observing conventional `read`s and `write`s submitted by the applications.

## Dependency Checks
**Dependency checks** are Bayou's way for applications to find conflicts. 

Each `write` operation includes a dependency check consisting of an application-supplied query and its expected result. A conflict is detected if the query, when run at a server against its current copy of the data does not return the expected result. It is a *precondition* for performing the `write` update. 
- Succeds -> execute `write`
- Fails -> invoke resolution procedure

> [!faq] Dependency Check at the Start
> You can also use version vectors or [[Vector Timestamps|timestamps]] to detect `write`-`write` conflicts (when a `write` occurs before seeing another `write`). 
> 
> The paper has an example of a dependency check with a meeting room scheduler. The dependency check is a SQL-like query to check if there are any other meetings at the time and place (meeting room). The expected result is an empty set. 
 
> [!faq] Dependency Check at the End
> Bayou also detects `write`-`read` conflicts. 
> 
> Sometimes an update to Data B relies entirely on information read from Data A. If someone alters Data A while you are busy updating Data B, your update might be based on obsolete information.
> 
> Bayou's solution is that a `write` can explicitly declare the expcted value of its dependencies.
> 
> **Example:** If the system is creating a new software binary, the new binary file does not care what the _old_ binary file looked like. It only depends on the source code. Bayou will check the version of the source code before writing the new binary to ensure nothing changed during compilation.

Bayou also allows smart constraints like checking for logical conditions. 
> [!example] Logical Check Example
> You want to transfer $100 from Account A to Account B. You read Account A and see a balance of $150, so you initiate the transfer.
>   
> A standard database would check if Account A still has _exactly_ $150 right before saving the transfer. If a separate automatic deposit of $10 arrived in the meantime (making the balance $160), the rigid database would flag a conflict and block your transfer simply because the balance changed.
>   
> Bayou allows a dependency check that states: "Execute this transfer as long as Account A has **at least** $100."

## Merge Procedures
Once a conflict is detected, a merge procedure is run by the Bayou server in attempt to resolve the conflict. They are general programs written in a high-level interpreted langauge. 
```
Bayou_Write(update, dependency_check, mergeproc) { 
	IF (DB_Eval (dependency_check. query) != dependency_check.expected_result) 
		resolved_update = Interpret(mergeproc); 
	ELSE 
		resolved_update = update; 
	DB_Apply (resolved_update); 
}
```

Bayou could have put dependency checks in the merge procedure, removing the need for dependency checks at all. However, this would cause extra overhead and hurt performance/scalability. After all, `write` can also not introduce a conflict. 

If [[#^8e3e68|ACR]] is not possible, the merge procedure will still run to completion, but is expected to produce an update that logs the detected conflict to enable someone to resolve it later. 

In contrast to [[CodaFS#Conflict Handling]] which locks individual files or complete file volumes when conflicts have been detected and not resolved, Bayou allows replcias to always remain accessible. The downside is that potential writes may depend on data that is in conflict which may cascade into more failures. 

# Replica Consistency
Importantly, Bayou ensures [[CAP Theorem#BASE|eventual consistency]]. All sevrers eventually receive all `write`s via the [[Bayou#^73fdb6|pair-wise anti-entropy process]] and that two servers holding the *same* same set of `write`s will have the *same* data contents. 

Two important features allow eventual consistency:
1. `write`s are performed in the same well-defined order at all servers
2. the [[#Conflict Detection and Resolution|conflict detection]] and [[#Merge Procedures|merge procedures]] are deterministic so that servers resolve the same conflicts in the same manner. 
	1. Kind of like a replicated state machine (RSM)!

When a `write` is accepted by a Bayou server from a client, it is initially deemed [[#^b56ef5|tentative]]. Tentative `write`s are ordered according to timestamps assigned to them by their accepting servers. Eventually, each write is [[#^b56ef5|committed]] which are oredeed according to the times at which they commit and before any tentative `write`s. 

Timestamps must be monotonically increasing at each server so that the pair
```
<timestamp, ID of server that assigned it>
```
produce a [[Group Communication#Types of Ordering Semantics|total order]] on `write` operations. There is no need for synchronized clocks, but keeping them reasonably close induces a `write` order consistent with a user's perception of the order. 

Because servers may receive `write`s 
- from clients other servers in an order that differs from the required execution order, and because 
- servers immediately apply all known `write`s to their replicas, 
servers must be able to **undo** the effects of some previous tentative execution of a `write` and reapply it in a different order. Interestingly, the number of times that a given `write` operation is re-executed depends only on the order in which Writes arrive via anti-entropy and not on the likelihood of conflicts involving the Write. 

Because of the ordering of the log, the server's current data can be generated by executing the log in order.

# Write Stability and Commitment
A `write` is said to be **stable** at a server when it has been executed "for the last time" by that server. [[#^73fdb6|As servers learn of new updates by performing anti-entropy]] with other servers, the effects of previously executed `write` operations may need to be undone and the `write`s re-executed. A `write` operation becomes **stable/committed** when the set of `write`s that precede it in the server's `write` log is fixed. This is like [[Group Communication#Introduction & Motivation The ISIS System|ISIS]].

Fixed means the server has already received and executed any writes that could possibly be ordered before the given write.

Bayou uses a **primary commit** scheme, where one server is designated the **primary** and is responsible for committing updates. Knowledge of which `write`s have commited and in which order they were committed then propagates to other servers during anti-entropy. Besides this, the primaryacts like any other server. 

Once a `write` is stable, it can safely discard the entry. It also tracks the **O vector** or the omitted vector so it does not accidentally reaccept that same `write` in a future sync.
 
There is no need for a [[Consensus]] nor [[Two Phase Commit]] since it would require a [[Quorum]] of servers to elect a primary. Instead, it is expected the application designates a server to be a leader effectively. 

## Aside: Write Types
A `write` is **executed** immediately after it is received by a server. 

Here it is in the **tentative** state, because the network has not agreed on the finalized order. A tentative `write`'s position is in the log (which has total ordering) is not yet guaranteed. It can be [[#^4fd496|rolled back]] and be reordered if an older update arrives from another server during a sync. 

When the *primary server* has processed the update and assigned it a permanent, global sequence number, it is **committed/stable**. The entire network does know about this permanent number yet. So it may still be viewed as tentative. In particular, a nonprimary server does not need to know 
- if other servers see it as committed
- if other servers see it as stable
but only that it was told it was committed by the primary. 

When *every* previous `write` before this particular one has been committed, and the write is committed, then the write is **locally stable** and can be safely removed from the tentative log. 

## Dual Views
Bayou allows applications to view "safe data" (`write`s that have committed) and "latest data" (all `write`s, even tentative ones) views. 

# Decentralized Security 
Since Bayou is designed for environments with weak connectivity, it cannot really on online authentication to verify passwords or permissions. Thus servers and servers need to rely on [[Lecture 9 - Cryptography I|public key cryptography]]. 