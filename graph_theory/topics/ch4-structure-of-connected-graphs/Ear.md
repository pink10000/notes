---
tags:
  - MATH_154
---
# Definition (Ear)
Let $G \subset H$ be a [[Graph#Definition (Subgraph)|subgraph]]. An **ear** of $H$ is a [[Path]] in $G$ whose endpoints are in $H$ but no other points are. Example:
```tikz
\begin{document}
\begin{tikzpicture}
    % Style for the nodes
    \tikzstyle{vtx}=[draw, circle, fill=black!20, minimum size=6mm]

    % Draw the initial subgraph H (a cycle)
    \node[vtx] (v1) at (135:1.5cm) {$v_1$};
    \node[vtx] (v2) at (45:1.5cm) {$v_2$};
    \node[vtx] (v3) at (-45:1.5cm) {$v_3$};
    \node[vtx] (v4) at (-135:1.5cm) {$v_4$};

    \draw[thick] (v1) -- (v2) -- (v3) -- (v4) -- (v1);

    % Draw the "ear" (a path) in red
    \node[vtx, fill=red!20] (x1) at (1, 2) {$x_1$};
    \node[vtx, fill=red!20] (x2) at (2, 1) {$x_2$};

    \draw[red, very thick] (v1) -- (x1) -- (x2) -- (v3);

    % Add labels
    \node at (-2.5, 0) {Subgraph $H$};
    \node[red] at (2.5, 0) {Ear $P$};

\end{tikzpicture}
\end{document}
```
# Theorem (Ears Do Not Add Cut Vertices)
If $H$ has no [[Cut|cut vertex]], and if $E$ is an ear for $H$, then $E + H$ has no cut vertex. 

Proof:

Consider subgraph $H$ and ear $E$ with endpoints $u,v \in V(H)$. I claim that we have no cut vertices in $H + E$. We have three cases:
1. If we removed some $x \in V(H) - \{u, v\}$ that is not an endpoint of ear $E$, then as $H$ has no cut vertex and $E$ is still connected, $E + H - \{x\}$ is still connected.
2. If we removed some $x \in \{u, v\}$, then $E$ is still connected through the other endpoint to $H$, which is connected. Thus the graph is still connected. 
3. If we removed some $x \in V(E) - \{u, v\}$, some "internal" point of $E$, then one half of $E$ is still connected by $u$ and the other by $v$, so the graph is still connected. 

Since $E + H - \{x\}$ is still connected for any $x$, then $E + H$ has no cut vertices. 

# Theorem (Ear Decomposition)
A block $B$ is either equal to [[Complete Graph]] $K_{2}$ xor a [[Cycle]] with ears. 

Proof:

Let $B$ be a block. We know from [[Block Graph#Lemma (Blocks are $K_{2}$ xor Contain a Cycle)]] that $B$ is $K_{2}$ xor a cycle. If $B = K_{2}$ we are done. Let $B$ contain a [[Cycle]] $C$. We want to show that we can iteratively add ears to form $B$.

Let $H_{0} = C$ be our initial subgraph of $B$. Assume we have some subgraph $H_{i}$ of $B$ after adding $i$ ears. If $H_{i}= B$ we are done. Let $H_{i}\neq B$. Since $B$ is connected,  $\exists$ edge $e = (u, v)$ where $u \in V(H_{i})$ and $v \not\in V(H_{i})$.
> If all edges of $H_{i}$ connected to only vertices of $H_{i}$ then $H_{i}$ is a disconnected component, which is impossible since $B$ is connected.

Consider $B - \{u\}$. This is a [[Block Graph#Definition (Block)|block]] and so it has no cut vertices, and is connected. This gives some path $P'$ in $B - \{u\}$ from $v$ to some other vertex in $H_{i} - \{u\}$. This gives us path $P$ where 
$$
E = (u, v, \dots, w)
$$
where $w$ is the first vertex in in $H_{i}$ formed by the path $P$, which gives us ear $E$. The internal vertices of $E$ are not in $H_{i}$. 

We can repeat this, so that $H_{i+1} = H_{i} + E$. Since $B$ is finite, we can repeat this until we have some $k$ where $H_{k} = B$.

## Example 1
See [[#Definition (Ear)]] to see a graph. Although in class we called it a **Theta Graph**, here you can just imagine we moved $x_{1}, x_{2}$ inside the $v_{i}$ square, rotate it slightly and we have some "theta-looking" graph. 

Here the graph has $2$ vertices with $3$ disjoint paths between them. This is an example of starting with a cycle and adding an ear. 