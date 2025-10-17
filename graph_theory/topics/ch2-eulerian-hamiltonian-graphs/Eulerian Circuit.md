---
tags:
  - MATH_154
aliases:
  - Eulerian
  - Semi-Eulerian
---
# Bridges of Konisberg 
This is essentially the origins of graph theory. The map is decomposed to the following graph:
```tikz
\begin{document}
\begin{tikzpicture}
    % Define coordinates for the land masses
    \coordinate (A) at (0,1);
    \coordinate (B) at (0,0);
    \coordinate (C) at (0,-1);
    \coordinate (D) at (4,0);

    % Draw the land masses as filled circles
    \node[draw, circle] at (A) (L1) {A};
    \node[draw, circle] at (B) (L2) {B};
    \node[draw, circle] at (C) (L3) {C};
    \node[draw, circle] at (D) (L4) {D};

    % Draw the bridges
    % Bridge 1: A to B
    \draw[line width=1pt, bend right=20] (L1) to (L2);
    % Bridge 2: A to B (another one)
    \draw[line width=1pt, bend left=20] (L1) to (L2);
	
	% Bridge 3: A to D
	\draw[line width=1pt] (L1) to (L4);

    % Bridge 4: B to C (two bridges)
    \draw[line width=1pt, bend left=20] (L2) to (L3);
    \draw[line width=1pt, bend right=20] (L2) to (L3);

    % Bridge 5: B to D
    \draw[line width=1pt] (L2) -- (L4);

    % Bridge 6: C to D
    \draw[line width=1pt] (L3) -- (L4);
\end{tikzpicture}
\end{document}
```
Is there a [[Walk#Definition (Trail)|trail]] that visits each edge once? 

# Definition (Eulerian Graph)
A [[Graph]] $G$ is called **Eulerian** if it contains a [[Walk#Definition (Circuit)|circuit]] that visits each edge of $G$ once (and has the same start and end. That circuit is called an **Eulerian Circuit**. 

If we are talking about a trail, then the graph is called **Semi-Eulerian** and the trail is called an **Eulerian Trail**. 

Since a circuit is a trail, then 
$$
\text{Eulerian} \implies \text{Semi-Eulerian}
$$
## Observations On Eulerian Graphs
- We note that if $G$ is Eulerian/Semi-Eulerian, it must be [[Connectivity|connected]] since there is no way to move between two connected components.  
- In any circuit, if you enter a vertex, you must also leave it. For some vertex $v$, and edge that visits $v$ must have some edge that exits. In particular, each edge must come in *pairs*. Thus, if $G$ is Eulerian, then $\deg(v)$ must be even $\forall v \in V(G)$.
	- So, in the [[#Bridges of Konisberg]], we this graph cannot possibly be Eulerian, since $\deg(D)$ is odd. 

# Theorem (Eulerian Graphs have Even Degree)
A *finite* graph $G$ is Eulerian iff
1. $G$ is [[Connectivity|connected]] except for its isolated vertices and
2. all vertices of $G$ have even [[Degree|degree]].

Proof: Let $G$ be Eulerian.

**Claim A**: $G$ has a circuit, or it is empty. This is obvious.

**Claim B**: The edges of $G$ can be partitioned into circuits. 

We prove by strong induction. We only need to assume $(2)$, in that all vertices of $G$ have even degree. If $|E| = 0$, then we are done (base case). Otherwise, we have some [[Cycle]] $C$. 

If we repeatedly remove $E(C)$ from $E(G)$, then the degrees of the vertices are even. Indeed, each vertex in the cycle only has $2$ degrees, so we are only removing an even number of edges. Thus, $G \setminus C$ satisfies $(2)$. The vertices have $0$ or $2$ edges of $C$. 

By the inductive hypothesis, we can partition the edges into cycles, and we have proven **B**. 

> The reason we use strong induction here is because when we remove the first cycle $C$, we want to be able to reason that $G \setminus C$, of some $n - k$ edges also satisfies the inductive hypothesis (as opposed to weak induction only allowing us to reason the next number/iteration). 

**Claim C**: We can merge cycles together to form a circuit. Given two cycles, $C_{1},C_{2}$, have no common edges, but they have a common vertex. 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNixbMCwyLCJcXGJ1bGxldCJdLFsyLDIsIlxcYnVsbGV0Il0sWzMsMSwiXFxidWxsZXQiXSxbMSwxLCJcXGJ1bGxldCJdLFsyLDAsIlxcYnVsbGV0Il0sWzQsMiwiXFxidWxsZXQiXSxbMCwxLCIiLDAseyJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDIsIiIsMCx7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMywiQ18xICIsMix7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fSxbMCw2MCw2MCwxXV0sWzMsMiwiIiwyLHsiY29sb3VyIjpbMCw2MCw2MF0sInN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMyw0LCJDXzIgIiwwLHsiY29sb3VyIjpbMjQwLDYwLDYwXSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19LFsyNDAsNjAsNjAsMV1dLFs0LDIsIiIsMCx7ImNvbG91ciI6WzI0MCw2MCw2MF0sInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzMsMSwiIiwwLHsiY29sb3VyIjpbMjQwLDYwLDYwXSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMSw1LCIiLDAseyJjb2xvdXIiOlsyNDAsNjAsNjBdLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifSwiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsyLDUsIiIsMCx7ImNvbG91ciI6WzI0MCw2MCw2MF0sInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV1d
\begin{tikzcd}
	&& \bullet \\
	& v && \bullet \\
	\bullet && \bullet && \bullet
	\arrow[color={rgb,255:red,92;green,92;blue,214}, dashed, no head, from=1-3, to=2-4]
	\arrow["{C_2 }", color={rgb,255:red,92;green,92;blue,214}, dashed, no head, from=2-2, to=1-3]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, no head, from=2-2, to=2-4]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, dashed, no head, from=2-2, to=3-3]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, dashed, no head, from=2-4, to=3-5]
	\arrow["{C_1 }"', color={rgb,255:red,214;green,92;blue,92}, no head, from=3-1, to=2-2]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, no head, from=3-1, to=3-3]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, no head, from=3-3, to=2-4]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, dashed, no head, from=3-3, to=3-5]
\end{tikzcd}
\end{document}
```
where $\color{red}C_{1}$ is a circuit, and $\color{blue}C_{2}$ is another (ignore that the colors don't match). You can think of the circuits at loop that 
- $C_{1} : v \to v$
- $C_{2} : v \to v$
- $C_{1} + C_{2} : v \xrightarrow{C_{1}} v \xrightarrow{C_2} v$
We have created a single circuit $C_{1} + C_{2}$ that uses all of their edges. Thus, **C** is proven.

**Claim D**: If $G$ is connected and its edges are partitions into some circuits $C_{1}, C_{2}, \dots, C_{n}$, then $G$ is Eulerian. We prove this by induction on $n$. 

If $n = 1$, then we are done. 

Note that $C_{n}$ should share some vertex with $C_{i}$ with $1 \leq i \leq n$. If not, $G$ would be disconnected, a contradiction. Let $C'$ be this circuit using the edges of $C_{i}$ and $C_{n}$. So our path 
$$
E = C_{1} \cup \cdots \cup C_{i}' \cup \dots \cup C_{n-1}
$$
with our partition $E$ as our set of edges. Essentially, at each step we apply **C** and keep merging to a larger circuit until $E$ is just $E(G)$. By our inductive hypothesis, $G$ is Eulerian since we now have a Eulerian trail over the entire graph.  
# Theorem (Semi-Eulerian Can Have Odd Degrees)
A finite $G$ is Semi-Eulerian iff 
1. $G$ is connected except for isolated vertices
2. $G$ has **at most** $2$ vertices of odd [[Degree|degree]]. 

Proof: 

$(\implies)$ Suppose $G$ had an Eulerian trail that starts at $u$ and ends at $v$. If this is true, then if we add an edge $e = (u, v)$, our trail is now a circuit since the start and end are the same. 

If $G$ has  a $u-v$ Eulerian trail (and thus Semi-Eulerian), then $G \cup \{u, v\}$ is Eulerian. By [[#Theorem (Eulerian Graphs have Even Degree)]], $G$ is connected except for isolated vertices, proving $(1)$. If we call this graph $G'$, then $G'$ has even degrees. Upon removal of edge $(u, v)$, every vertex of $G$ except $u,v$ has an even degree, proving $(2)$. 

$(\impliedby)$ We have cases on the number of odd degree vertices. 
- If there are *zero*, then $G$ is Eulerian, and thus Semi-Eulerian by definition of a [[Walk#Definition (Circuit)|circuit]]. 
- If there is *one* odd degree vertex, then this is impossible by the [[Handshake Lemma]], since we would have an odd sum of edges. 
- If we have *two* odd degree vertices, $u, v$, let $G' = (E(G) \cup \{e\}, V(G))$ where $e = (u, v)$. $G'$ has all even degree and is connected. By [[#Theorem (Equivalent Eulerian)]], $G'$ is Eulerian. Then $G'$ has a circuit that ends at with edge $e$, then removing it gives us an Eulerian trail, and so $G$ is Semi-Eulerian. 
## Alternative, Constructive Proof of Theorem
We can try to build a trail as we go. $G$ has an Eulerian trail that starting at some vertex $u$ iff
- all the edges of $G$ connect to the vertex $u$,
- **at most** one vertex other than $u$ has an odd degree. 

Say we took some edge $e = (u, w)$ as the start of our trail for some graph $G$. Obviously, the next edge must be incident with $w$. In particular, we want to prove graph $G'$ ($G$ without $e$) should have an Eulerian trail starting at $w$. 

So, is true if 
1. at most one vertex other than $u$ has an odd degree in $G'$. 
2. $G'$ is connected to all edges in $G'$. 

> This should look similar to what we were proving initially.

Here, $(1)$ is automatic if the removal of $e$ caused $u,w$ to have degree decreased, and thus are now even (with the degrees of the other vertices are invariant. Otherwise, $G$ has odd degrees in $u$ and some other vertex $v$. After removal of $e$, then $G'$ has odd degree at $w$ and some other vertex $v$. Unless of course, $v = w$ and $(1)$ holds. 

For $(2)$, we cannot choose a [[Connectivity#Definition (Bridge)|bridge]] (unless $\deg(u) = 1$). However, if $\deg(u) > 1$ and there are at most one other odd degree vertex, then $u$ has a a non-bridge edge. 

Suppose by contradiction $u$ has only bridges,
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	& {C_1} \\
	{C_2} & u & {C_3}
	\arrow[no head, from=2-2, to=1-2]
	\arrow[no head, from=2-2, to=2-1]
	\arrow[no head, from=2-2, to=2-3]
\end{tikzcd}
\end{document}
```
where $C_{i}$ are other connected parts of the graph. Then picking any edge will disconnect the graph. Suppose $G_{i}$ is the subgraph $C_{i}$ with $u$ and its edge to it. Then $G_{i}$ has an *even* number of odd degree vertices by the [[Handshake Lemma]]. In particular, an even number of odd degree vertices ensures $G$ has an even $|E|$ and thus an even $\sum_{v\in V(G)_{i}}\deg(v)$. But then $u$ is an odd degree. 

But then this implies $C_{i}$ has some other odd degree vertex. But then $G_{i}$ has exactly *one* (an odd number!) vertex of odd degree, contradicting the [[Handshake Lemma]]. 

Thus there must exist at least one edge that is not a bridge. By always choosing this edge, the graph of the remaining edges stays connected, allowing us to traverse every edge and complete the Eulerian trail.