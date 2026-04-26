---
tags:
  - CSE_223B
---
# Definition (Replication)
**Replication** is the process of creating and maintaining multiple copies of data or services across different nodes in a distributed system. The main goal of replication is to improve [[Networked File Systems#Definition (High Availability)high availability]], fault tolerance, and performance by allowing multiple nodes to serve requests for the same data or service.

A node is called a **replica** if it holds a copy of the data or service. Replication can be done at different levels, such as file-level, block-level, or application-level. The replication process involves synchronizing the replicas to ensure [[Memory Coherence#Definition (Memory Consistency)|memory consistency]] and handling failures to maintain availability. 

Replication levels can vary. In general, 
$$
\text{more replicas} = \text{higher availability/robustness} = \text{more work/less efficiency}
$$