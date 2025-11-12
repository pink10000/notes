---
tags:
  - MATH_154
aliases:
  - block
---
# Definition (Block)
In a [[Connectivity|connected]] [[Graph]] $G$, a **block** is a maximal [[Graph#Definition (Subgraph)|subgraph]] with no [[Cut]] vertices.  In particular, maximal refers to $\max|V(G)|$
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNSxbMSwxLCJhIl0sWzAsMCwiXFxidWxsZXQiXSxbMCwyLCJcXGJ1bGxldCJdLFsyLDAsIlxcYnVsbGV0Il0sWzIsMiwiXFxidWxsZXQiXSxbMCwyLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzIsMSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDAsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCw0LCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMywiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDQsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XV0=
\begin{tikzcd}
	\bullet && \bullet \\
	& a \\
	\bullet && \bullet
	\arrow[no head, from=1-1, to=2-2]
	\arrow[no head, from=1-3, to=3-3]
	\arrow[no head, from=2-2, to=1-3]
	\arrow[no head, from=2-2, to=3-1]
	\arrow[no head, from=2-2, to=3-3]
	\arrow[no head, from=3-1, to=1-1]
\end{tikzcd}
\end{document}
```
Here, $a$ is the cut vertex and the connected subgraphs formed by its removal on the left and right are blocks.

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
2. Block graphs have no cycle.

For $(1)$, let $B_{1}, B_{2}$ be two arbitrary blocks. We can assume both vertices are blocks. The proof is the same otherwise. Since the original graph $G$ was connected, then we have some path $P$ in $G$, and follow it for any vertex $u \in B_{1}$ and $v \in B_{2}$. If there is an edge $(u, v)$ we are done. 

Suppose not. Then we can follow path; we will encounter other partitions and cut vertices.  
$$
P : B_{1} \to c_{1} \to B_{3} \to c_{3} \to \dots \to c_{2} \to B_{2}
$$
Since $u,v$ and $B_{1},B_{2}$ were arbitrary, then we are done. 

For $(2)$, assume by contradiction there is a cycle in the block graph. Then we have some cycle from $B_{1}$ to $B_{n}$. 

But if we take the union $B_{1} \cup B_{2} \cup \dots \cup B_{n}$, then we'd have no cut vertex. Suppose we removed some vertex $x \in B_{i}$. Each individual $B_{j}$ without $x$ is still connected. Indeed, we still share
$$
B_{1} \to B_{2} \to \dots \to B_{i}
$$
and 
$$
B_{n} \to B_{n-1} \to \dots \to B_{i}
$$
with $B_{1} \to B_{n}$. But then as it is still connected, then we have new block, which is the union. 

# Theorem (Block Graph Leaves are Always Blocks)
Leaves in a block graph are always blocks. 

Proof: Every [[Cut|cut]] vertex is part of $\geq 2$ blocks, so they cannot be leaves. Then by [[#Lemma (Block Graphs are Trees)]], the block graph is a tree, and by [[Tree#Lemma (Minimum Leaves)]], the only vertices left are blocks, which must be leaves. 

# Lemma (Block-Cycle Characterization)
A block is either a $K_{2}$ *xor* contains a [[Cycle|cycle]]. 

Proof:
1. Block $B$ must always contain an edge since it must contain more than one vertex and by [[#Lemma (All Edges Exist in a Block)]], must have its edges (it's also connected).
2. If $B$ has no cycles, then it is a tree. Then by [[#Theorem (Block Graph Leaves are Always Blocks)]], any non-leaf is a cut vertex. Thus only the tree $K_{2}$ works since it has no cut vertices. If $B$ has a cycle, we are done. 

> $B$ is $K_{2} \iff$ its sole edge is a [[Connectivity#Definition (Bridge)|bridge]]. 

# Theorem (Edges & Vertices Share a Cycle in a Single Block)
For finite [[Connectivity|connected]] graph $G$ (that is not $K_{2}$), the following are equivalent:
1. $G$ is a single block.
2. Any two edges of $G$ share a cycle.
3. Any two vertices of $G$ share a cycle.

Proof:

Direction $(2) \implies (3)$ is trivial. For $(3) \implies (1)$, removing any vertex that is part of a cycle does not disconnect the graph, so there are no [[Cut#Definition (Cut Vertex)|cut vertices]], and $G$ is a single block. 

For $(1) \implies (2)$, we define a relation $\sim$  on $E(G)$ where $e \sim f$ if $e = f$ or $e,f$ are on a common cycle. This is trivially reflexive and symmetric. Transitivity is non-trivial. 

This partitions $E(G)$ into equivalence classes. The goal is to show that if $G$ is a block, there is only *one* equivalence class. By [[Ear#Theorem (Ear Decomposition)]], any block $G$ not $K_{2}$ can be constructed from cycle $C$ and adding ears. We prove by induction on the number of ears. 

Base Case: If we have $0$ ears, then $G = C$, such all edges of $G$ lie on a cycle, and so any two edges share a cycle. 

Inductive Hypothesis: Assume any block $H$ constructed from $k$ ears has only one edge equivalence class. 

Inductive Step: Let $G$ be a block constructed from $k + 1$ ears, such that $G = H + E$ where $H$ is a block constructed from $k$ ears and $E$ is a near ear. $E$ connects $u,v \in V(H)$. By the inductive hypothesis, $H$ is a singular equivalence class $\mathfrak{A}$. We form a new cycle $C' = P \cup E$ where $P$ is a path in $H$ whose endpoints are $u,v$ which correspond with $E$. Let $g$ be any edge of $E$, and $f$ be any edge on $P$, such that $g \sim f$. But then $g$ belongs in $\mathfrak{A}$. 

As $g$ arbitrary, all edges of $E$ belong in $\mathfrak{A}$. Thus $G$ is in the same equivalence class. Thus all edges are equivalent, and any two edges share a cycle.

> We did now show transitivity, so this proof is not complete. But the general idea is that since $G$ is connected and a single block, intersecting cycles allows you to construct a larger cycle that contains all edges $e,g$. 