---
tags:
  - MATH_154
---
# Kuratowski's Theorem
A finite [[Graph|graph]] $G$ is [[Planar Graph|planar]] $\iff$ it has no [[Graph Subdivision|subdivision]] of a [[Complete Graph]] $K_{5}$ or [[Bipartite Graph#Definition (Complete Bipartite Graph)|complete bipartite graph]] $K_{3,3}$ as a [[Graph#Definition (Subgraph)|subgraph]]. 

Proof: 

The reverse direction is trivial. We apply 
1. [[Planar Graph#Theorem ($K_{5}$ is Non-Planar)]]
2. [[Planar Graph#Theorem ($K_{3,3}$ is Non-Planar)]]
For the forward direction, we know $G$ is planar iff every [[Connectivity#Theorem (Connected Components)|connected component]] is planar, and that $G$ has $K_{5}$ or $K_{3,3}$ iff some component does. Then for each connected component, then $G$ is planar iff each block is planar. Then $G$ contains $K_{5}$ or $K_{3,3}$ iff some block does. 

$G$ has an [[Ear#Theorem (Ear Decomposition)|ear decomposition]]. We can now perform induction on ears. If the graph is just a [[Cycle|cycle]] $C$, then the theorem holds. Assume that Kuratowski's Theorem holds for $G'$, built from $k$ ears. 

So, WTS if $G = G' + P$ where $P$ is the $k$th ear is non-planar, then it must contain a $K_{5}$ or $K_{3,3}$ subdivision. So, we have two cases. 
1. If $G'$ is already non-planar, then we already have either subgraph as a subdivision in $G$.
2. Let $G'$ be planar, but $G$ is not. Let $u,v$ be $P$'s endpoints in cycle $C \subset G'$. Then as $G$ is non-planar, we cannot draw $P$ inside cycle $C$, nor can we draw it outside. This forms $K_{3,3}$. 

> The last part of this proof is not fleshed out.