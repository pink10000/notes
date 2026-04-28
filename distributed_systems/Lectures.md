---
tags:
  - CSE_223B
---
This file collates the material taught during lecture in an organized, chronological manner. 

## Lecture 1 (3/31)
Distributed Systems involve cheating, we don't do anything natively/truly $\to$ we fake it somehow.

Why do we do Distributed Systems?
1. Increase performance and/or Capacity. Serve more demand than an individual machine can handle. (Scaling up): Basically because of Dennard Scaling (Moore's Law).
2. Fault Tolerance: If one machine fails, the system can continue to operate. (Scaling out), survive failure of individual components, "a Distributed System won't work if some part of the system you didn't know exists breaks". More Probability of failure due to more components.
3. Decrease latency somehow/access
4. Regulations + Policies (Different regulatory environments have different requirements and data)
5. Isolation/Security: Avoid doing our stuff locally $\to$ Cloud Service (renting resources).

# Lecture 2 (4/2)
- [[Memory Coherence#Definition (Memory Coherence)]]
- [[Memory Coherence#Definition (Strict Consistency Model)]]
- [[Memory Coherence#Definition (Shared Virtual Memory)]]
- [[Memory Coherence#Definition (Sequential Consistency)]]

# Lecture 3 (4/7)
- [[Ivy System]]
- [[Memory Coherence#Definition (Sequential Consistency)]]
- [[Memory Coherence#Definition (Locality of Reference)]]

# Lecture 4 (4/9)
Rust tutorial.

# Lecture 5 (4/14)
- [[TreadMarks]]
- [[TreadMarks#Lazy Release Consistency (LRC)]]
- [[Vector Timestamps]]
- [[Chord]]

# Lecture 6 (4/21)
- [[Networked File Systems]]
- [[HarpFS]]

# Lecture 7 (4/23)
- [[HarpFS]]
- [[Frangipani]]

# Lecture 8 (4/28)


---
Thanks to Samvrit for lending me his notes for the first few lectures. 