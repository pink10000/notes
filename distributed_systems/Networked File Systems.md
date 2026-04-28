---
tags:
  - CSE_223B
aliases:
  - NFS
---

# Networked File Systems
**Networked File Systems**: a file system that is accessed over the network. It uses an RPC module to translate calls and send them to the kernel. It is built on top of Unix.

NFSes are not distributed file systems; there is no distribution of data, and they do not solve the problems of distributed systems. Instead, they are only a way to access files over the network. They still have the same problems. They are designed to only support one large server to store files, which is cheaper but has a single point of failure. We can try to fix this by adding more physical drives to the server (RAID), but this is not a good solution.

## Race Condition (Concurrent Access)
What happens when two applications try to write to a file at the same time? First, when a file is opened, it gets copied to the buffer cache in memory. Each application/process gets their own copy of the buffer cache in their section of memory. When an application calls "close", it writes to the buffer cache. If two applications are writing to the same file, the last one to close will overwrite the first one, leading to data inconsistency. The same thing happens when two clients are accessing a remote file system.

# Definition (High Availability)
A system is **highly available** if it can continue to operate even when some of its components fail. In the context of file systems, this means that the system can still serve client requests even if some of the servers or storage devices fail.

# Definition (External Consistency)
**External consistency** is a property of a distributed system that ensures that the results of operations are consistent with what the user/client expects, i.e. they follow the real-time order of operations. 