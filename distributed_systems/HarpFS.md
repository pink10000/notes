---
tags:
  - CSE_223B
---
From [paper](https://dl.acm.org/doi/10.1145/121133.121169).
# Harp File System Overview
- Harp is a highly available, reliable, persistent file system intended to be used within a file service in a distributed network, such as [[Networked File Systems|NFS]].
- It is accessed via the Virtual File System (VFS) interface, sitting as a layer between the NFS server code and the low-level Unix file system.
- Harp guarantees strong semantics: every file operation is executed atomically, meaning it either completes entirely or has no effect, in spite of concurrency and failures.
- The system masks failures by performing a failover algorithm to remove an inaccessible server from service and reorganize the remaining nodes.
# Architecture and Replication
- Each group will have a **designated primary** and $n$ **designated backups**. Some will be witnesses.
- Harp utilizes a variation of the primary copy replication technique, where client calls are directed to a single *primary* server.
- The primary communicates with backup servers and waits for their response before replying to the client for modification operations.
- To tolerate $n$ server failures, Harp requires a total of $2n+1$ servers.
- However, it only stores $n+1$ actual copies of the files on disk.
- The remaining $n$ servers act as "witnesses" to ensure a majority vote during network partitions, without storing full disk copies.
- A typical three-member replica group consists of exactly one designated primary, one designated backup, and one designated witness.
# Performance and The Write-Ahead Log
- Harp achieves high performance by trading slower disk accesses for faster network communication.
- Modifications are recorded in a volatile **write-ahead log** in memory, rather than being synchronously written to disk.
- Each server is equipped with a small uninterruptible power supply (UPS).
- If a power failure occurs, the UPS provides enough time for the server to safely flush the volatile log to the physical disk, preventing data loss.
# Log Pointers
The log contains event records that are processed strictly in sequential order.    
- **CP (Commit Point):** The index of the most recently committed event record.
- **AP (Application Point):** The index of the most recently applied event record that an asynchronous background process has sent to the Unix file system.
- **LB (Lower Bound):** The largest index where all events up to and including the LB have had their effects securely recorded on the local disk.
- **GLB (Global Lower Bound):** The lower bound on what a server knows about the current LB for both itself and its partner.
Servers safely discard log entries with indices less than or equal to their GLB. The system continuously maintains the invariant: 
$$
GLB\le LB\le AP\le CP\le \text{top of log}
$$
The primary and backup keep
- file system 
- log
But the witness only keeps the log, even if promoted.
# Normal Operation Flow
- To carry out a modification, the primary appends an event record to its log and sends the data to the backup.
- The backup appends the data to its log in order and replies with an acknowledgment message.
- Upon receiving the acknowledgment, the primary advances its CP, officially committing the operation, and replies to the client.
- The primary includes its CP in subsequent messages to the backup, allowing the backup to advance its own CP to match.
- An independent apply process writes the committed operations to the disk in the background.
# External Consistency for Reads
- Non-modification operations, such as file reads, are processed entirely at the primary to improve response times.
- To prevent external consistency violations during a network partition, Harp utilizes loosely synchronized clocks.
- Backups send a promised time to the primary, calculated as the backup's current clock time plus a small delay.
- This promised time represents a guarantee from the backup not to start a new view until that specific time has elapsed.
- The primary can safely process reads without contacting the backup as long as its current time is less than the promised time[^1].
- Harp guarantees that writes in the new view happen after all reads in older views[^2].

[^1]: Technically, it should be $t_{p} > t_{b} + \delta - \varepsilon$ where $\varepsilon$ is the clock skew. This is just an extra buffer since different machines are never perfectly in sync.

[^2]: The authors claim that this is violated when clocks get out of sync, which is "highly unlikely".
# Views and Witnesses
- A view is the result of a reorganization within the group, uniquely identified by a monotonically increasing view number that is kept on disk.
- A valid view must contain at least two active members: one acting as primary and one acting as backup.
- If a primary or backup fails, the designated witness is promoted to act as the backup in the newly formed view.
- A promoted witness receives and logs all committed operations but cannot apply them because it lacks a copy of the file system.
- Promoted witnesses store older parts of their logs on non-volatile devices, like tape drives, and never discard log entries while promoted.
- The witness has a purely passive role; it does not monitor other members and never initiates a view change itself.
## View Changes
View changes are initiated by a designated **primary or backup that detects a loss** of communication or finishes recovering from a crash. The node initiating the change acts as the coordinator for a two-phase protocol.
- **Phase 1:** The coordinator asks other members to form a view, causing them to halt normal operations and send any missing state data to the coordinator.
- The coordinator uses this data to form the initial state for the new view, guaranteeing it reflects all committed operations from previous views.
- **Phase 2:** The coordinator writes the new view number to disk and transmits the new state to the participating nodes.
- The other nodes write the new view number to disk, at which point a **promoted** witness is demoted if both the designated primary and backup have successfully rejoined the view.
- A promoted witness is just like a backup. Except
	- Since it has no copy of the file system, it cannot apply committed operations.
	- It never discards entries from its log.

# Example 1 
**Setup:**
Consider a Harp system configured to share files across five servers: $A, B, C, D, E$.
- The system is configured with $n=2$ (tolerates up to 2 failures).
- Initial view: Server $A$ is the designated primary. Servers $B,C$ are designated backups. Servers $D,E$ are designated witnesses.
- Let `*` represent primary, `!` represent backup, `_` represent witness

**Scenario A: $C$ crashes. While $C$ is still down, $A$ becomes partitioned from $B, D, E$.**
```
(A* B! C! D_ E_)1 -> (C) (A* B! D! E_)2 -> (C) (A) (B* D! E!)3
```
- Can the set of currently live servers form a new view and continue serving client requests? 
	- Yes. The partition containing $B$, $D$, and $E$ has 3 active servers. This satisfies the $n+1$ majority requirement to form a new view out of the $2n+1$ total servers.
- Which nodes make up the view and which are promoted or demoted? 
	- The new view consists of $B$, $D$, and $E$. Server $B$ is promoted to primary. Because $n+1$ copies are required to allow information to survive $n$ failures, both designated witnesses ($D$ and $E$) must be promoted to act as backups.
- What data needs to be sent to the new nodes, and from which server?
	- $B$ (acting as the new primary) will send all log entries to the newly promoted backups ($D$ and $E$) during phase 2 of the view change protocol.

**Scenario B: $C$ reboots to join $A$.**
```
(C) (A) (B* D! E!)3 -> (AC) (B* D! E!)3
```
- Can the set of currently live servers form a new view and continue serving client requests?
	- No. Servers $A$ and $C$ only constitute 2 servers, which does not meet the $n+1$ (3 servers) majority quorum required to form a view. 
- Which nodes make up the view and which are promoted or demoted?
  - None.
- What data needs to be sent to the new nodes, and from which server?
  - None.     
    
**Scenario C: $B$ crashes, and reboots in the partition with $A, C$. Its disk was lost.**
```
(AC) (B* D! E!)3 -> (AB'C) (DE)
```
- Can the set of currently live servers form a new view and continue serving client requests?
	- No. Although the group $\{A,B,C\}$ contains 3 servers (a numerical majority), they cannot form a view. 
	- A new view must reflect all committed operations from previous views. Because server $B$ suffered a media failure, the Harp protocol strictly requires it to bring itself up to date by communicating with the primary of the current view, and then with the witness. 
	- Since $B$ is partitioned from $D$ and $E$ (the members of the most recent valid view), it cannot retrieve the required state. Without intact state from the most recent view, the coordinator's attempt to form the initial state for the new view will fail.
- Which nodes make up the view and which are promoted or demoted?
	- None. Because $B$ cannot complete its mandatory recovery steps, it remains in an incomplete recovery state and cannot participate as a voting member.
- What data needs to be sent to the new nodes, and from which server?
	- None. Copying $A$ and $C$'s older data to $B$ would permanently erase any operations that were committed while $B$, $D$, and $E$ were active together. The system halts to protect data consistency, and the servers must wait until the partition heals.

**Scenario D: $C$ crashes again rebooting in the partition with $D,E$, the disk intact.**
```
(AB'C) (DE) -> (AB') (C* D! E!)4
```
- Can the set of currently live servers form a new view and continue serving client requests?
	- Yes. 
- Which nodes make up the view and which are promoted or demoted?
	- $\{C, D, E\}$. $C$ was backup, now it is primary. $D,E$ promote to backups.
- What data needs to be sent to the new nodes, and from which server?
	- $C$ needs to get info from either $D,E$ and update to GLB. 

**Scenario E: The partition is healed and all five nodes can reach other again.**
```
(AB') (C* D! E!)4 -> (A* B! C! D_ E_)5
```
- Can the set of currently live servers form a new view and continue serving client requests?
	- Yes
- Which nodes make up the view and which are promoted or demoted?
	- All of them. They return to their designated roles. 
- What data needs to be sent to the new nodes, and from which server?
	- $D,E$ have the newest data. $B$ needs to get the file $C$ since it is the designated backup. (It cannot get from $D,E$ because they are promoted designed witnesses and do not store the file system). $A$ and $B$ can update their log from $C,D,E$. 