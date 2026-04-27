---
tags:
  - CSE_223B
---
From [paper](https://dl.acm.org/doi/10.1145/121133.121169).

# Harp File System
**Harp** is a distributed file system that is designed to be a drop-in replacement for [[Networked File Systems|NFS]]. It consists of a set of [[Replication|replicas]] that are homogeneous (equal to terms of power, privilege, function, etc.) and can fail independently. It is designed to be [[Networked File Systems#Definition (High Availability|highly available]] and can tolerate failures as long as at least one replica is alive. 

It uses a **replicated state machine** approach, where all operations are replicated on all machine, living in the RPC part of the NFS. 

# Design Considerations
- Harp does not have total consistency inside the system (too expensive). 
- How many failures $f$ should we be able to tolerate? We cannot tell the exact number of failures.
- No node can "know" about any other node. It can only send messages. 
- Asynchronous. Things will eventually happen. In particular, if $(n - f)$ are "alive", then we must proceed.

In the worst case scenario, if we have $f$ failures, then at minimum we need $f + 1$ replicas. 
- How does the client talk to the remaining node? (single point of failure)
- We can't possibly care, since we do not want to change the client. We need more than $f + 1$.

Given that we have two kinds of operations, reads and writes, then at any time, we can have a certain number of read nodes and a certain number of write nodes. How can we guarantee that at least one node is both a read and a write node (Venn diagram)? If we can make write nodes and read nodes have enough count, then we guarantee that least one overlap (non zero intersection). Thus, at minimum, writes nodes need to be $n/2 + 1$ and read nodes are $n/2 + 1$. By Pidgeonhole principle, $1$ node must be both. Any larger is more than sufficient.

In a harp, it uses a [[Quorum]]-based approach to ensure consistency and [[Networked File Systems#Definition (High Availability|highly available]]. All quorums are the same size (although in practice, this does not need to be true). 

At each point in time, there is a **view** of the system moving through certain configurations of quorums (the state it is in). Inside a view, there is a quorum of nodes that are alive. When a node fails, the system moves to a new view with a new quorum. The primary node is responsible for replicating data to the backup nodes. 

How does every node learn about new data? 
> [!info]
> The primary node replicates it out to the backup nodes, and the backup nodes acknowledge that they have received the data and appended it to a volatile *write-ahead-log* (for performance). The primary node can only know that the backup nodes have received the data via the acknowledgment message. If the primary node dies before receiving the acknowledgment, then the client will try again on the new view, which is not a new problem since NFS already does retransmissions.

What happens if the power goes out? 
> [!info] 
> Harp uses a Uninterruptible Power Supply (UPS) to flush the log to disk, ensuring that data is not lost. 

# Write Ahead Log
The **write-ahead-log** is a log stored in volatile memory that contains a sequence of **event records**; each record describes an operation and records at higher indices describe more recent events. There are four indices in the Harp log:
- **Commit Point** ($\text{CP}$): most recently committed event record index
- **Application Point** ($\text{AP}$): most recently applied event record index to disk
- **Lower Bound** ($\text{LB}$): pointer to the most recent event record index that has been received by all backup nodes 

To carry out a modification operation, 
1. The primary creates an event record, appends it to its log, and then sends it to the backup nodes.
2. The backup node logs will append them to its log and sends an acknowledgment back to the primary node.
	1. The `ack` contains $n$, the index where all entries up to $n$ have been received .
3. The primary receives the acknowledgment, commits the operation by advancing its $\text{CP}_p$.
4. The primary sends its $\text{CP}_p$ to the backup nodes, which then advance their $\text{CP}_{b}$ to match the $\text{CP}_p$.

But the data is not written to disk yet. A separate **apply process** is responsible for processing the committed operations to the file system and writing them to disk. It maintains a counter called the **application point** ($\text{AP}$), that records its progress. The Unix file system is the process of actually writing the data to disk. The apply process will only apply the changes to the file system once they have been committed, keeping track of the $\text{LB}$ pointer. 

Primaries and backups keep track of the $\text{GLB}$ or global lower bound pointer by exchanging messages of the $\text{LB}$ pointer. All nodes discard any event record with an index less than $\text{GLB}$, since they know that all nodes have received it and committed it to disk. In general, the following invariant is maintained:
$$
\text{GLB} \leq \text{LB} \leq \text{AP} \leq \text{CP} \leq \text{top of log}
$$

When a server recovers from failure, the log is used to bring it up to date. The server will then redo all the committed operations that have not been applied to disk.

> $\text{AP}$ and $\text{LB}$ were used at this point in time because SSDs had not been invented yet, and the disk was very slow. 

# Maintaining External Consistency 
Suppose there were a network partition where the primary and backup are now separated, and the backup forms a new [[#Design Considerations|view]] with the witness of this quorum. If the old primary processes a non-modification operation, the result may not reflect a write operation that has already been committed. 

This does not compromise the file system state, but it can lead to a loss of [[Networked File Systems#Definition (External Consistency)|external consistency]]. In Harp, this is highly unlikely by using loosely synchronized clocks. Each message from the backup to the primary contains a time equal to the backup's clock time $+ \delta$ where $\delta$ is a few hundred milliseconds. The backup essentially promises the primary to not start a new view until $\delta$ has passed. The old primary can process read operations without communicating with the backup only if $t_{p} > t_{b} + \delta$[^1]. When a new view starts, the new primary cannot process and modification operations (writes) until its clock is greater than $t_{b} + \delta$. Harp guarantees[^2] that writes in the new view happen after all reads in older views. 

[^1]: Technically, it should be $t_{p} > t_{b} + \delta - \vepsi$ where $\vepsi$ is the clock skew. This is just an extra buffer since different machines are never perfectly in sync. 
[^2]: The authors claim that this violated when clocks get out of sync, which is "highly unlikely". 

# Views 
A **view** is a configuration of the system that contains a set of nodes that are alive. When a node fails, the system moves to a new view with a new quorum. The primary node is responsible for replicating data to the backup nodes.

A view has a unique *view number* that is monotonically increasing (later views have larger numbers). When a view is formed, it contains at least two group members, the primary and the backup. The view also contains a witness (not in the quorum!) that functions similarly to a backup node, but 
1. does not store data nor 
2. does it discard log data nor
3. does not monitor the quorum (and thus never starts view changes).
It's primary role is to witness the failure of the primary and/or backup nodes and to help form a new view. 

When either the primary or backup node fails, the witness is *promoted* and act as a backup node. It is later *demoted* back to a witness when the view changes with a new primary and backup. When it promotes, it receives all log records for committed operations and appends them to its log. It retains all log records (and writes them to a non-volatile storage) until it is demoted. 

> [!info] 
> There is a chance that a view with a witness in the promoted state for a very long time may have a very large log, where it may no longer be practical. The best solution may be to reconfigure the system and changing the group membership. 

## View Changes
A view change selects the members of the new view and makes sure the members of the new view have the most up-to-date data. User operations are not processed during view changes. A view change is a two-phase process. The node that starts it acts as the **coordinator**.

In phase 1, the coordinate communicates with the other group members. If a group member agrees to form a new view (it will always agree unless another view change is in progress), it stops processing operations and sends the coordinator whatever state the coordinator does not have. The coordinator will try to form the initial state for the new view, guaranteeing that the new view reflects all committed operations. 

In phase 2, the coordinator successfully configured the new view state, and has written the new view number to its local disk. It when then send a message to the responding nodes to inform them of the new state and the new view member. When the responding nodes receive the message, they will write the new view number, establishing the new view, and resume processing operations.

The witness then demotes. 