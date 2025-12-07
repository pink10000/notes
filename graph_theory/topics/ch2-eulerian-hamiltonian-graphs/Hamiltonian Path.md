---
tags:
  - MATH_154
aliases:
  - hamiltonian
  - Hamiltonian
  - Hamiltonian Cycle
  - hamiltonian cycle
---
We use $\delta(G)$ from [[Degree#Definition (Minimum Degree of a Graph)]].
# Definition (Hamiltonian)
A **Hamiltonian** [[Path]] or [[Cycle]] is a walk that visits each vertex, except the first and last vertex are the same (closed). A [[Graph]] is called a **Hamiltonian Graph** if it contains a Hamiltonian Cycle. 
# Theorem (Hamiltonian Implies Connected)
Graph $G$ is Hamiltonian only if it is [[Connectivity|connected]].
# Explore (Minimum Edges For Hamiltonian)
How many edges do we need to ensure that a graph is Hamiltonian? How big does [[Degree#Definition (Minimum Degree of a Graph)|the minimum degree of graph]] $G$, $\delta(G)$ need to be to ensure Hamiltonian? Suppose we had graph 
$$
K_{n/2} \circ K_{n/2}
$$
which is disconnected. We have that $\delta(G) = (n/2) - 1$. Here, the graph is *almost* Hamiltonian. Indeed, if we picked any size $K_{m},K_{n - m}$ then $\delta(G) = \min(m - 1, n - m - 1)$ to ensure $\delta(G)$ is maximized, it follows $m = n/2$. 
## Lemma (Minimum Degree for Connectivity)
If
$$
\delta(G) \geq \frac{n - 1}{2}
$$
then $G$ is [[Connectivity|connected]].

Proof:
If $u,v \in V$, then we need to prove there is a path $u \to v$. We have $n - 2$ other vertices. We have $2$ cases:
1. If there is an edge $(u, v)$, then we are done. 
2. If there is no edge, then we know $u,v$ connects to at least $\frac{n-1}{2}$ vertices each. Then, find vertex $w$ with $(u, w)$ and $(w, v)$. If so, we are done. 
   
   If there set of incident vertices from the edges of $v$ and $u$ are disjoint, then the total number of vertices is at least 
   $$
   \frac{n -1}{2} + \frac{n -1}{2} = n - 1
   $$
   which is a contradiction on $|V|  = n - 2$. And so both sets must overlap, and thus $w$ exists. 
## Lemma (Force a Cycle by Minimum Degree)
If $\delta(G) \geq n/2$ and if it has a path $P$ of length $k$, then if $k < n = |V|$, then we have a path of length $k + 1$ we can find. Otherwise, if $k = n$, then we have a cycle of length $n$. 

Intuitively: 
If you have a "long path", then we can use this to find a "longer path" by possibly finding a cycle in between. Then you can repeat this until you find all the vertices.

Proof:
Suppose we have a path $P$
$$
P: v_{1}, v_{2}, \dots, v_{m}
$$
I claim we can either *extend this path* or *turn it into a cycle*. 
- If there is some vertex $u$ or $w$ not in $P$ but $(u, v_{1})$ or $(v_{m}, w)$ exists, then we can extend $P$ unless $v_{1}, v_{m}$ only connect to other $v_{i}$ for $1 < i < m$. Then we are done. 
- Otherwise, we can turn $P$ to a cycle with the same vertices. If there is an edge $(v_{1}, v_{m})$, then we are done. If for some $i$, we have edges $(v_{1}, v_{i+1})$ and $(v_{i}, v_{m})$, we can create the following path which gives us a cycle:
  ```tikz
	\usepackage{tikz-cd}
	\begin{document}
	\begin{tikzcd}
		{v_1 } & {v_{i+1}} \\
		{v_i} & {v_m }
		\arrow["1", from=1-1, to=2-1]
		\arrow["4", from=1-2, to=1-1]
		\arrow["2", from=2-1, to=2-2]
		\arrow["3", from=2-2, to=1-2]
	\end{tikzcd}
	\end{document}
    ```
  Let $S$ be set of indices $i \in \{1, \dots, m - 1\}$ for which edge $(v_{i}, v_{m})$ exists. Let $T$ be the same for edge $(v_{1},v_{i+1})$. Since $P$ is assumed to be maximal length, all neighbors of its endpoints must lie within the path itself. Therefore the number of neighbors for each endpoint corresponds to
  $$
  |S| = \deg(v_{m}) \geq n/2 
  \quad\quad\quad
  |T| = \deg(v_{1}) \geq n/2
  $$
  We want to find an index $i$ that belongs to both $S$ and $T$, giving us the edges to form the cycle. Assume for the sake of contradiction that $S \cap T = \varnothing$. Then, 
  $$
  |S \cup T| = |S| + |T| \geq \frac{n}{2} + \frac{n}{2} = n
  $$
  But then as $S \cup T \subseteq \{1, 2, \dots, m - 1\}$, then 
  $$
  \begin{aligned}
  |S \cup T| 
  &\leq |\{1, 2, \dots, m- 1\}| = m - 1 \\
  n &\leq |S \cup T| \leq m - 1 \\ 
  n + 1 &\leq m
  \end{aligned}
  $$
  implying that the number of edges in our maximal length path $P$ is greater than the number of vertices in $G$, a contradiction.  
  > We are using the Pidgeonhole Principle here.
## Theorem (Hamiltonian: Minimum Vertex and Degree)
If $G = (V, E)$ and 
1. $|V| = n > 2$
2. $\delta(G) \geq n/2$
then $G$ is Hamiltonian. 

Proof: 

Assume by contradiction that $G$ is not Hamiltonian. Because $G$ is not Hamiltonian, there is no path of length $n - 1$. Let $P$ be a maximal path of length $m$. 

By [[#Lemma (Force a Cycle by Minimum Degree)]], and that $P$ is maximal, we must have a cycle $C$ containing all $k$ vertices of $P$. But then we have a cycle of length $k < n$, such that there must be a vertex $u$ in this graph not in the cycle. But as $\delta(G) \geq n/2$, then by [[#Lemma (Minimum Degree for Connectivity)]] $G$ is connected, such that there is a $v_{j}$ that connects to $u$. 

Consider this path $P'$, from $u \to v_{j}$ and then the entire cycle $C$. Then $P'$ has $k + 1$ vertices. But then this is a contradiction as we do not have a path of maximal length $k$. Thus $G$ must be Hamiltonian.