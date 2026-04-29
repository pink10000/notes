---
tags:
  - CSE_223B
---
# Definition (False Sharing)
Imagine two nodes $A,B$ (processor and/or machine) is trying to access some resource $r$ (page, file, etc.) from some caching mechanism (cache line, page). Suppose $A,B$ want data $a,b$ stored in resource $r$. If $B$ is always writing to $b$, to maintain [[Memory Coherence#Definition (Memory Coherence)|memory coherence]], some kind of atomic operation is done so that $B$ can write to $r$ without other nodes being able to read/write to it. However, if all $A$ wants to do is read, it has some extra overhead; it needs to wait for $B$ to finish writing. 

This scenario is called **false sharing**, where one node is not actually sharing data with another node, but rather the resource granularity has enveloped both pieces of data. 

# Mitigation Strategies
- Design the data schema so that variables accessed by different nodes are physically stored in different shards or pages.
- [[Memory Coherence#Definition (Locality of Reference)|Locality]]: move the computation to the data (or vice versa)
- Looser consistency models
- Padding (specifically for multiprocessor setups)