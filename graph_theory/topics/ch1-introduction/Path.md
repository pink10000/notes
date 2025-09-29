---
tags:
  - MATH_154
---
# Definition 
A **path** is a [[Graph]] where the edges have a certain length. 
- Denoted as $P_{n}$, a graph with path length $n$. 
- If vertices are $v_{1}, \dots, v_{n}$ then the edges are $(v_{1}, v_{2}), \dots (v_{n-1}, v_{n})$
- $|E| = n - 1$ 

```mermaid
graph LR
    A((A)) o--o B((B))
    B o--o C((C))
    C o--o D((D))
```
- A path is a [[Walk]] with no repeated vertices. 