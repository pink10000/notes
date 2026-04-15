---
tags:
  - CSE_223B
---
# Vector Timestamps (TreadMarks)
This is with respect to [[TreadMarks]]. We care about where the/a lock has been throughout the system, so it can figure out what it needs to update. Perfect [[Memory Coherence#Definition (Memory Consistency)|consistency]] relies on a universal "wall-clock time"[^1] which is prohibitvely expensive to maintain. Instead of global time, TM uses logical clocks to track only the specific events we care about. 

[^1]: Some kind of "all-knowing" time reference that is not practically achievable in a distributed system."

Logical time advances only during lock acquires `acq` and releases `rel`. Every lock has a timestamp, called the logical clock, which is a [[Monotonic#Monotonically Increasing|monotonically increasing]] natural number. A **vector timestamp** is an array containing the logical clock for each node. If there are $N$ nodes, vector timestamp $\mathbf{t}$ has length $N$. Each entry $\mathbf{t}[i]$ is the logical clock for node $i$, and on initialization, all entries are $0$.

## Time Stamp Comparison 
Because each node maintains its own vector timestamp, these vectors can be mathematically compared in a [[Partial Order|partial order]] to determine the relative ordering of events. Consider two vector timestamps $\mathbf{t}_1$ and $\mathbf{t}_2$. There are three cases:
1. $\mathbf{t}_1 \geq \mathbf{t}_2$: This implies $\forall i, \mathbf{t}_1[i] \geq \mathbf{t}_2[i]$. 
2. $\mathbf{t}_1 \leq \mathbf{t}_2$: This implies $\forall i, \mathbf{t}_1[i] \leq \mathbf{t}_2[i]$.
3. $\mathbf{t}_1$ and $\mathbf{t}_2$ are incomparable. The timestamps are mixed when neither is strongly greater than the other. 
	- If there is only one lock, this cannot happen. Otherwise, it would imply that the lock was acquired by two different nodes at the same time, which is impossible (race condition).
	- If there are multiple locks, it can happen, only during execution of two independent locks. This is expected and not a problem, providing a partial ordering of events.

# Example 1 
Consider two nodes $A, B$ and that there is only one lock.
```
Init: [0, 0]
A acq: [1, 0]
A rel: [2, 0]
B acq: [2, 1]
```
Now suppose $B$ performs multiple acquires and releases, and we get the following vector timestamp:
```
[2, 17]
```

# Example 2 
Consider four nodes $A, B, C$ and that there are multiple locks. Suppose $A$ and $C$ acquire (different) locks at the same time, and then $C$ needs to talk to the lock manager (LM). In the middle of $C$'s acquire, $A$ might have released. The vector timestamps might look like:
```
Initial: [0, 0, 0]
ABC: [0, 0, 0]
A,C acq -> A[1, 0, 0], B[0, 0, 0], C[0, 0, 1]
A rel -> A[2, 0, 0], B[0, 0, 0], C[0, 0, 1]
```
How can we compare $\mathbf{t}_A = [2, 0, 0]$ and $\mathbf{t}_C = [0, 0, 1]$? Here, $\mathbf{t}_A$ and $\mathbf{t}_C$ are incomparable because neither is strongly greater than the other. This **undefined behavior** of vector timestamps is actually a feature, as it lets LM know that $C$'s acquire happened during $A$'s acquire, and thus $C$ needs to update based on $A$'s acquire, allowing LM to delay the update until the acquire. 

> The ability of undefined behavior gives an optimization opportunity. It allows the system to make more informed decisions about when to update locks and when to wait. 