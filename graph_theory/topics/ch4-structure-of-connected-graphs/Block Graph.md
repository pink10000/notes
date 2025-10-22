---
tags:
  - MATH_154
  - MATH_154_Lecture
aliases:
  - block
---
# Definition (Block)
In a [[Connectivity|connected]] [[Graph]] $G$, a **block** is a maximal [[Graph#Definition (Subgraph)|subgraph]] with no [[Cut]] vertices.  In particular, maximal refers to $\max|V(G)|$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	a & b & c
	\arrow[no head, from=1-1, to=1-2]
	\arrow[no head, from=1-2, to=1-3]
\end{tikzcd}
\end{document}
```
Here, $b$ is the cut vertex and $a,c$ would be blocks. 

# Lemma (All Edges Exist in a Block)
Every edge $e$ in a [[Connectivity|connected]] graph is contained in the some block. 

Proof: If we just take a graph of just some edge $e$, it is a connected subgraph without a cut vertex. So it must be part of a maximal subgraph (i.e. a block.)

# Lemma (Block Intersection is Singleton or Empty)
Intersection of two blocks is always either empty or a single [[Cut#Definition (Cut Vertex)|cut vertex]]. Formally, if $B_{1}$ and $B_{2}$ are some blocks, then 
$$
|V(B_{1}) \cap V(B_{2})| \in \{0, 1\}
$$

Proof: 

**Claim A**: If we have two blocks $B_{1},B_{2}$, then if $V(B_{1}) \cap V(B_{2})$ contains $v,w$, then $V(B_{1}) \cup V(B_{2})$ has no cut vertices. 

WTS that any vertex we remove leaves $B_{1} \cup B_{2}$ connected. WLOG, if $B_{2}$ had a vertex removed, it would still be connected since it has no cut vertices. WLOG, suppose we removed $w$. Then $B_{1} - \{w\}$ is connected, and $B_{2} - \{w\}$ is connected. But then from any vertex in $B_{1}$, we can reach $v$ and then reach any vertex in $B_{2}$ and vice versa. 

Therefore $(V(B_{1}) \cup V(B_{2})) - \{w\}$ is connected. But then this is a contradiction because their union is a larger subgraph with no cut vertices. 

**Claim B**: We cannot have $V(B_{1}) \cap V(B_{2}) = \{v\}$ where $v$ is a non-cut vertex. 

If this is true, then removing $v$ does not disconnect the graph. Indeed, there is a [[Path]] $P: u \to w$ where $u \in V(B_{1})$ and $w \in V(B_{2})$. Now if we have $B_{1} \cup B_{2} \cup P$, then this is connected subgraph with no cut vertex. So where is the cut vertex?

Suppose we cut $v$. Then we can use $P$ to connect $B_{1}$ and $B_{2}$. WLOG if we cut some vertex $x \in B_{1}$, then the subgraph is still trivially connected. Suppose we cut some $x$ in the path $P$. But then without $x$, $B_{1}, B_{2}$ are still connected (by vertex $v$).  

> So this means we can decompose our connected graph into smaller block subgraphs that are connected by one vertex, which are our cut vertices.


# Definition (Block Graph)
Let $G$ be a finite connected graph. Then the **block graph** of $G$ is a new graph with 
$$
\begin{aligned}
V &= \{\text{blocks of } G \} \cup \{\text{cut vertices of } G\} \\
E &= \text{edge between } B, v \text{ if } v \in V(B) \\ 
\end{aligned}
$$
Essentially, we are condensing the blocks into their own "vertex" and keeping the edges of the cut vertices. 

## Lemma (Block Graphs are Bipartite)
If $G$ is a finite connected graph, then its block graph is a [[Bipartite Graph]]. Indeed, we have two types of vertices, we simply have one be colored white and the other be colored black. And by [[#Lemma (Block Intersection is Singleton or Empty)]], then we cannot have an edge connecting to blocks, as they would just be combined to a single block vertex. 

## Lemma (Block Graphs are Trees)
A block graph is always a [[Tree]]. 

Proof: We need to show two properties:
1. Block graphs are always connected. 
2.  fsd

For $(1)$, let $B_{1}, B_{2}$ be two arbitrary blocks. We can assume both vertices are blocks. The proof is the same otherwise. Since the original graph $G$ was connected, then we have some path $P$ in $G$, and follow it for any vertex $u \in B_{1}$ and $v \in B_{2}$. If there is an edge $(u, v)$ we are done. 

Suppose not. Then we can follow path; we will encounter other partitions and cut vertices.  
$$
P : B_{1} \to c_{1} \to B_{3} \to c_{3} \to \dots \to c_{2} \to B_{2}
$$
Since $u,v$ and $B_{1},B_{2}$ were arbitrary, then we are done. 

## Lemma (Block Graphs have No Cycles)
A block graph has no [[Cycle|cycles]]. 

Proof:
Assume by contradiction there is a cycle in the block graph. Then we have some cycle from $B_{1}$ to $B_{n}$. 

But if we take the union $B_{1} \cup B_{2} \cup \dots \cup B_{n}$, then we'd have no cut vertex. Suppose we removed some vertex $x \in B_{i}$. Each individual $B_{j}$ without $x$ is still connected. Indeed, we still share
$$
B_{1} \to B_{2} \to \dots \to B_{i}
$$
and 
$$
B_{n} \to B_{n-1} \to \dots \to B_{i}
$$
with $B_{1} \to B_{n}$. But then as it is still connected, then we have new block, which is the union. 