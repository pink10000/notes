---
tags:
  - MATH_154
---
# Definition (Bipartite Graph)
A **bipartite graph** $V$ is a [[Graph]] that partitions a left $L$ and right $R$ side. Indeed, $V = L \cup R$. 
- $L \cap R = \varnothing$. 
- All edges connect a vertex in $L$ to a vertex in $R$. 
```mermaid
graph
    L1((L1)) o--o R2((R2))
    L1 o--o R3((R3))
    L2((L2)) o--o R1((R1))
    L2 o--o R2
    L2 o--o R3
    L3((L3)) o--o R1
    L3 o--o R2
    L3 o--o R3
```

## Formal
We want a way to define a bipartite graph without having to rearrange the vertices when drawing them. In particular, we want to (further) formalize the definition. 

A graph is **bipartite** if we can color vertices white and black such that each edge connects a white vertex to a black vertex. 

# Definition (Complete Bipartite Graph)
Denoted as $K_{a,b}$ a **complete bipartite graph** denotes a graph where $|L| = a$ and $|R| = b$. Every vertex on the left has an edge to the right side and vice versa.  
```mermaid
graph
    L1((L1)) o--o R1((R1))
    L1 o--o R2((R2))
    L1 o--o R3((R3))
    L1 o--o R4((R4))
    L1 o--o R5((R5))
    L2((L2)) o--o R1
    L2 o--o R2
    L2 o--o R3
    L2 o--o R4
    L2 o--o R5
```
The [[Degree]] of $K_{a,b}$ is equal to $ab$. 