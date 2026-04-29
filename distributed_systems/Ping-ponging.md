---
tags:
  - CSE_223B
---
# Definition (Ping-ponging)
**Ping-ponging** describes a degenerate state in a distributed system where the system spends more time on transferring the data, rather than processing it. 

One particular example is a [[Memory Coherence#Definition (Shared Virtual Memory)|distributed shared memory]] where one node acquires a write lock on a page to update a value. Another node might then try to acquire the lock to change a different value *but in the same page*. The system must then serialize all the data and transfer it between the network. This can get looped repeatedly. 