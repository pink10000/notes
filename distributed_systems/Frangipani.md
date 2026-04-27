---
tags:
  - CSE_291G
---
Frangipani is a scalable distributed file system. From [paper](https://dl.acm.org/doi/epdf/10.1145/269005.266694). 

# Overview
Frangipani is a distributed file system that is aimed to be 
- scalable
- manages a collection of disks on multiple machines as a single shared pool of storage
- [[Networked File Systems#Definition (High Availability)|highly available]] despite component failures
- minimal to administer and maintain

All machines are assumed to be under a common administrative control and are able to communicate securely. It is built on top of [[#Petal Overview|Petal]]. 
```
+-----------------------+-----------------------+-----------------------+
|          User         |          User         |          User         |
|        program        |        program        |        program        |
+-----------------------+-----------+-----------+-----------------------+
|             Frangipani            |             Frangipani            |
|            file server            |            file server            |
+---------------------------+-------+-----------------------------------+
|        Distributed        |       Petal                               |
|        lock service       |       distributed virtual                 |
+---------------------------+       disk service                        |
|                                                                       |
+-----------------------------------------------------------------------+
|                            Physical disks                             |
+-----------------------------------------------------------------------+
```
Multiple *interchangeable* Frangipani servers provide access to the same files by running on top of a shared Petal virtual disk, coordinating their actions with locks to ensure coherence. 
- *Scalability* is achieved by adding more Frangipani servers. 
- *Fault tolerance* is achieved by recovering automatically from server failures and operating from the surviving servers. 
- *Load balancing* is improved by splitting up the file system and shifting it to machines that actually use it. 
- Petal and the lock service are also distributed for the above $3$ properties. 
```
  +-----------------+   +-----------------+
  |  User programs  |   |  User programs  |
  +-----------------+   +-----------------+
  |    FS switch    |   |    FS switch    |
  +-----------------+   +-----------------+
  | Frangipani mod. |   | Frangipani mod. |
  | [Petal driver]  |   | [Petal driver]  |
  +-------+---------+   +--------+--------+
          |                      |
==========+======= Network ======+===========
          |          |           |
+---------+----------+-----------+------------+
|            Petal virtual disk               |
| +-------+---+  +-------+---+  +-------+---+ |
| |Petal  |Lck|  |Petal  |Lck|  |Petal  |Lck| |
| |server |Srv|  |server |Srv|  |server |Srv| |
| +---+-+-+---+  +---+-+-+---+  +---+-+-+---+ |
|  [ D ] [ D ]    [ D ] [ D ]    [ D ] [ D ]  |
+---------------------------------------------+
```
In this diagram, the components of Frangipani need not exist on separate machines; it would make sense to couple them if the Petal instance were not heavily loaded. This distributed lock service is independent from the rest of the system. 

The Frangipani FS server module on each machine runs within the operating system kernel, registering itself as one of the available file system implementations. 
- It uses the kernel's buffer pool to cache data from recently used files. 
- All reads and writes are done using the local Petal device driver. 
- Each server keeps its own redo log of pending changes in a separate section of the Petal disk. They are kept in Petal so then when a server crashes, another server can access the log and run recovery. 

We can further abstract the client away from the Frangipani module by connecting it over a network and use a simple [[Networked File Systems|NFS]] system to connect the two. 
- Security purposes
- Since Frangipani runs in the kernel, it is not quickly portable across different OSes or even different versions of Unix. 

## Petal Overview
**Petal** is a distributed storage system that provides **virtual disks** to its clients. Like a physical disk, it can be read/written in blocks. However, unlike one, a virtual disk provides a sparse $2^{64}$ byte address space[^1], with physical storage being allocated on demand. Petal optionally [[Replication#Definition (Replication)|replicates]] data for [[Networked File Systems#Definition (High Availability)|high availability]]. 

It also has efficient snapshots to support consistent backup. 

[^1]: This means that if there were such hardware that could support $2^{64}$ bytes of address space, then this system would still scale well in it. Obviously, such a drive does not exist. That many bytes is approximately $18.4$ million TB of data. 

Petal *commits* physical disk space to virtual addresses only when they are written. It also has a *decommit* primitive that frees the physical space backing a range of virtual addresses. Petal chunks the space in $2^{16} = 64$ KB range of addresses. 
- Too large = wasteful
- Too small = risk of fragmentation

The following is the disk layout of Frangipani.
```
0      1T                        2T                  5T         6T
+------+-----+-----+-----+-------+-------------------+-----------+
|      |     |     |     |       |                   |           |
|      |  0  |  1  | ... |  255  |        ...        |    ...    |
|      |     |     |     |       |                   |           |
+------+-----+-----+-----+-------+-------------------+-----------+
 Param-                Logs       Allocation bitmaps   Inodes
 eters                                                512 B each

6T                          134T      135T       136T          2^64
+-----------------------------+---------+----------+-------------+
|                             |         |          |             |
|              ...            |         |          |     ...     |
|                             |         |          |             |
+-----------------------------+---------+----------+-------------+
    Small blocks                    Large blocks
     4 KB each                            1 TB each
```
- Parameters stores configuration and housekeeping information. Only a few KB are used.
- Logs get 1 TB ($2^{40}$ bytes) partitioned into $256$ logs. 
- Allocation bitmaps describe which remaining regions are free. Each Frangipani server locks a portion of the bitmap region for its exclusive use. 
- Inodes are used to store metadata about the files/data. There can be $2^{31}$ inodes. 
- Blocks are stored after $6$ TB. The first $64$ KB ($16$ blocks) of a file are stored in small blocks. If a file grows to more than $64$ KB, the rest is stored in one large block. 
	- $2^{47}$ bytes are allocated for small blocks
	- allows $2^{35}$ blocks, $16$ times the maximum number of inodes. 
- The remaining is for large blocks. 
- The current scheme limits Frangipani to slightly less than $2^{24}$ ($16$ million) "large files" where a "large file" is any file bigger than $64$ KB. 

# Logging and Recovery
Frangipani uses "[[HarpFS#Write Ahead Log|write-ahead]] redo" logging of metadata to simplify failure recovery and improve performance. Each Frangipani file server has its own private log which gets updated when it needs to update the metadata. They are bounded by $128$ KB, stored in a circular buffer (ring buffer) in which the next $25\%$ are reclaimed when it's full. If a server crashes, another server eventually detects the failure and runs **recovery** on that server's log. Failure is detected by either a client of the failed server or when the lock service asks the failed server to return a lock it is holding and receives no reply. 

The recovery demon (daemon)[^2] then gets control of the log and processes it. 
- The failed server can be restarted as long as the underlying Petal volumes remain available. 
- Log events have a monotonically increasing number.
- The locking protocol ensures that during a crash, RD can write and release the lock for the failed server.
- RD only applies updates updates that were logged since lock acquisition and failure.
	- RD does this by never replaying a log record describing an update that has already been completed.
	- Each metadata block has versioning
- Only one RD can execute at a time. 

The logging and recovery schemes assumes a disk write failure leaves a disk sector with old state or new state (but never a combination of both). If a sector is damaged such that reading gives a [[Data Link Layer#Error Control|CRC]] error, Petal's built-in replication can recover it. 

[^2]: We'll call this RD for now.

# Lock Service for Synchronization
Frangipani uses multiple-reader/single-writer locks to implement the necessary synchronization. 
- A **read lock** allows a server to read the associated data from disk and cache it. If a server is asked to release its read lock, it must invalidate its cache entry before complying.
- A **write lock** allows a server to read or write the associated data and cache it. A server's cached copy of a disk block can be different from the on-disk version *only if* it holds the relevant write lock.
	- Thus if it is asked to release/downgrade, it must write the dirty data to disk before complying. Downgrade = retain cache entry; Release = invalidate
- Locks are sticky; they generally stick with a client until another client needs it.
- All locks operate on a **lease**. When a client first contacts the lock service, it obtains a lease with an expiration time of $30$ seconds after its creation or its last renewal. 

> Frangipani designers mentioned they decided against having the lock-acquired-server send the data to the requester because Frangipani servers do not communicate with each other (they do not need to). When a server crashes, they only need to process the log used by that server. A crash log of forwarded data can be messy.

Some operations require atomically updating several on-disk data structures covered by different locks. They avoid deadlock by globally ordering these locks and acquiring them in two phases.
1. As server needs to determine what lock it needs. It may involve acquiring/releasing some locks to look up names in a directory.
2. It sorts the locks by inode address and acquires each lock in turn. 

## Lock Service 
The **lock service** is a set of mutually cooperating lock servers, and a clerk module linked into each Frangipani server. The lock service organizes locks into *tables* with 64-bit integer names for locks. Each file system has an associated table. 

Here is how the clerk and the LS use the table:
1. Frangipani file system is mounted.
2. Server calls into clerk, which opens a lock table associated for that file system 
3. A *lease identifier* is given, used in all subsequent communication between them.
4. When the FS is unmounted, the clerk closes the lock table. 

Clerks and LSes use asynchronous messages: `request`, `grant`, `revoke`, and `release`. 

How do the LSes detect failures/network partitions/etc? 
>[!info] Heartbeats
> Timely exchange of heartbeats and a majority consensus is used to tolerate network partitions. 

# Scalability 
How to add a server:
- configure which Petal virtual disk it is using 
- where the lock service is 
- contact the LS to obtain a lease, and determines which portion of the log space to use from the [[#Lock Service|lease identifier]] 
- other servers adapt to this new one automatically (recall they do not talk to one another!)
How to remove a server:
- shut the server off
- ideally, it should flush the data to disk and release the locks (but this is not needed, see [[#Logging and Recovery]])
Petal servers can be added/removed transparently. Lock servers are added and removed in a similar manner. 

