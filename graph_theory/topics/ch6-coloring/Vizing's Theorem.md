---
tags:
  - MATH_154
aliases:
  - vizing
---
# Vizing's Theorem 
For some finite simple graph $G$, 
$$
\chi'(G) \leq \Delta(G) + 1
$$
where its [[Edge Coloring#Definition (Edge Chromatic Number)|edge chromatic number]] is bounded by its [[Degree#Definition (Maximum Degree of a Graph)|maximum degree]] plus $1$. This is a [[Edge Coloring#Edge Chromatic Number Bounds|better upper bound]]. 

In particular, it is always *either* $\Delta(G)$ or $\Delta(G) + 1$. 

Proof Idea: We want to use induction on $|E|$, that if $\Delta(G) \leq k$, then $\chi'(G) \leq k + 1$. And [[Coloring#Greedy Coloring|greedy coloring]].

Proof:

Suppose $|E| = 0$, then $\chi'(G) = 0$, and we are done. Assume that the statement in the proof idea is true for $m - 1$ edges.. Consider graph $G$ with $m$ edges. If we remove edge $e \in E(G)$, then we have $m - 1$ edges. By the inductive hypothesis, we can color $G - e$ with $k + 1$ colors (assuming $\Delta(G) \leq k$).

Let $e = (u, v)$. In particular, $\deg(u) \leq \Delta(G) \leq k$, which means there is some color missing. If $v$ also does not have an incident edge of this color, we can color $e$ that color and we are done. 

For now, suppose $u$ is missing a blue edge and $v$ is not (denote this as $e_{b}$). For the same reason why we know there is some unused color, for $u$, $v$ must also have an unused color (denote this as red). If no other edge at $v$ is red, then we can color that particular edge as red, and color $e$ blue, and we are done. 

Consider that one red edge $e_{r} = (v, w)$. Again $w$ must have some unused color (denote this green). If $v$ has no green edge, then we can color $e_{r}$ green, color $e_{b}$ as red, and color $e$ as green. 

What if $v$ has a green edge $e_{g}$? Then we can repeat the process above. We can then exhaust these colorings. If we find a chain of recolorings we are done. 

However, we may have some *loop*, where the last color we need to swap is red. In general, we have some chain of edges before a loop. Suppose we removed the coloring on $e_{b}$. This allows us to recolor $e$ as blue. 

We can reframe the graph on this edge. 
```mermaid
graph LR;
	u((u')) o--o v((v))
```
where $v$ is new. We know $u'$ has no red incident edge, and $v$ has all the same properties as before. We know $v$ must be missing some other color also. Suppose it is missing orange.

This allows us to follow the recoloring edge and recolor $(u', v)$ as orange. This is fine unless there are orange edges on $u'$ and $w$ (the vertex on the edge where we started the recoloring chain). 

We now use a [[Kempe Chain]] on red-orange, allowing us to switch red to orange and vice versa. Consider the red-orange subgraph $G_{ro}$. We know $\Delta(G_{ro}) \leq 2$. In particular, this subgraph is only [[Path|paths]] and [[Cycle|cycles]]. To recolor, we recolor some [[Connectivity|connected component]] of paths and cycles. 

In particular, we only care about $u',v,w$. Each one of these vertices are an endpoint of some of these paths. As we deduced, 
- $w$ has no red, but orange 
- $v$ has red but no orange
- $u'$ has no red, but orange

Suppose we recolored one of these paths. Each path has $2$ ends, but we have $3$ vertices. It must be the case that one of these $3$ vertices where the other endpoint is not one of these $3$. We can then recolor that particular [[Kempe Chain]] (and potentially some minor recolorings) and we are done. 

> This proof write up is of very poor quality. You are better off watching a YouTube video on it (although the first video I watched was pretty bad).
# Theorem (Edge Coloring is Big Delta for Bipartite)
If $G$ is a finite [[Bipartite Graph]], then 
$$
\chi'(G) = \Delta(G)
$$
Proof: We induct on $\Delta(G)$. If $\Delta(G) = 0$, we are done. Otherwise, WTS there is a [[Matching]] $M$ that matches all the vertices of $\Delta(G)$.

Let's color all edges in $M$ the first color. Then we can induct on $G - M$. Since every maximum vertex in $G$ just lost $1$, vertex, then 
$$
\Delta(G - M) = \Delta(G) - 1
$$
By the inductive hypothesis, we can color the rest with $\Delta(G) - 1$ many colors. So, 