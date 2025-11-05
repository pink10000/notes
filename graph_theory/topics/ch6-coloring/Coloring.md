---
tags:
  - MATH_154
---
# Definition (Coloring)
A vertex **coloring** of a [[Graph|graph]] $G$ is an assignment of a color to each vertex of $G$ so that no two adjacent vertices have the same color. This is an $n-$coloring if only $n$ different colors are used. 

# Definition (Chromatic Number)
The **chromatic number** $\chi(G)$ of a graph $G$ is the smallest number $n$ so that $G$ has a graph coloring. 

## Lemma (Low Chromatic Numbers)
- $\chi(G) = 1 \iff |E(G)| = 0$ 
- $\chi(G) \leq 2 \iff G$ is [[Bipartite Graph#Formal|bipartite]].
- Determining $\chi(G)$ for more complicated graphs is difficult. For $2-$colorings, once you color a vertex, the is only one possible choice for its neighbors. For $3-$colorings, there are two. 