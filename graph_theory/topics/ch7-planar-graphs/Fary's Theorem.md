---
tags:
  - MATH_154
---
# Lemma (Pentagonal Center)
Given any [[Polyhedra|polygon]] $P$ in the plane with at most $5$ sides, there is a point $v$ inside of $P$ with straight line paths to each of $P$'s vertices. 

Proof: A triangle is trivial. We have $5$ cases:

**Case 1**: If we have no non-convex angles, then 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	& \bullet \\
	\bullet & v & \bullet \\
	\bullet && \bullet
	\arrow[no head, from=1-2, to=2-3]
	\arrow[no head, from=2-1, to=1-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-1, to=2-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-2, to=1-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-2, to=2-3]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-2, to=3-1]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-2, to=3-3]
	\arrow[no head, from=2-3, to=3-3]
	\arrow[no head, from=3-1, to=2-1]
	\arrow[no head, from=3-3, to=3-1]
\end{tikzcd}
\end{document}
```
any point on the interior works. 

**Case 2**: If we have $1$ non-convex angle, then 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	\bullet && \bullet \\
	& \bullet \\
	& v \\
	\bullet && \bullet
	\arrow[no head, from=1-1, to=2-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=1-1, to=3-2]
	\arrow[no head, from=1-3, to=4-3]
	\arrow[no head, from=2-2, to=1-3]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-2, to=1-3]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-2, to=2-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-2, to=4-1]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-2, to=4-3]
	\arrow[no head, from=4-1, to=1-1]
	\arrow[no head, from=4-3, to=4-1]
\end{tikzcd}
\end{document}
```
then we can place $v$ inside the non-convex angle. 

**Case 3**: If we have two adjacent non-convex angles,
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	&& \bullet \\
	&& v \\
	\\
	& \bullet && \bullet \\
	\bullet &&&& \bullet
	\arrow[no head, from=1-3, to=5-5]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-3, to=1-3]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-3, to=4-2]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-3, to=4-4]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=2-3, to=5-5]
	\arrow[no head, from=4-2, to=5-1]
	\arrow[no head, from=4-4, to=4-2]
	\arrow[no head, from=5-1, to=1-3]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=5-1, to=2-3]
	\arrow[no head, from=5-5, to=4-4]
\end{tikzcd}
\end{document}
```
then we can place near the opposite vertex. 

**Case 4**: If we have two non-adjacent non-convex angles,
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	&&&& \bullet \\
	&&&&& \bullet \\
	&&& \bullet & v \\
	\bullet &&&&&&&& \bullet
	\arrow[no head, from=1-5, to=2-6]
	\arrow[no head, from=2-6, to=4-9]
	\arrow[no head, from=3-4, to=1-5]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-4, to=3-5]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-5, to=1-5]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-5, to=2-6]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-5, to=4-1]
	\arrow[color={rgb,255:red,214;green,92;blue,214}, no head, from=3-5, to=4-9]
	\arrow[no head, from=4-1, to=3-4]
	\arrow[no head, from=4-9, to=4-1]
\end{tikzcd}
\end{document}
```
and we can place $v$ near the far wall so it can see all the vertices. 

**Case 5**: If we more than two non-convex angles, then this cannot happen. In particular, the sum of angles for an $n-$gon is $180(n - 2)$. 

## Corollary (Hexagonal Center)
No, this is not true for hexagons. Consider the following counter example:
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNixbMSwxLCJcXGJ1bGxldCJdLFswLDIsIlxcYnVsbGV0Il0sWzQsMSwiXFxidWxsZXQiXSxbMywxLCJcXGJ1bGxldCJdLFs1LDAsIlxcYnVsbGV0Il0sWzIsMSwiXFxidWxsZXQiXSxbMCw0LCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzQsMywiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDIsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMiwxLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzEsNSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs1LDAsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XV0=
\begin{tikzcd}
	&&&&& \bullet \\
	& \bullet & \bullet & \bullet & \bullet \\
	\bullet
	\arrow[no head, from=1-6, to=2-4]
	\arrow[no head, from=2-2, to=1-6]
	\arrow[no head, from=2-3, to=2-2]
	\arrow[no head, from=2-4, to=2-5]
	\arrow[no head, from=2-5, to=3-1]
	\arrow[no head, from=3-1, to=2-3]
\end{tikzcd}
\end{document}
```
which cannot have central vertex that keeps the graph planar. 

# Lemma (Triangulation Leads to Interior Vertex)
Let $G$ be a connected, planar graph. Let $|V| > 3$. If $G$ is constructed by [[Planar Graph#Lemma (Triangulations)|triangulation]], then any such $G$ will have an *interior* vertex $v$ of $\deg_{G}(v) \leq 5$. 

Proof: By the [[Handshake Lemma]], and [[Planar Graph#Theorem (Planar Graph Edge Bound)|theorem]],
$$
\sum_{v\in V} \deg(v) = 2|E| = 6|V| - 12
$$
Rearranging, we get 
$$
\sum_{v\in V} (6 - \deg(v)) = 12
$$
Since the graph is triangulated, the infinite face is a triangle, and thus bounded by $3$ boundary vertices. Then the [[Degree|degree]] of each is $2$, such that they can only contribute at most $4$, unless they do not connect anything else. Thus, some other vertex must have $6 - \deg(v) > 0$. 
# Fary's Theorem
Any finite simple [[Planar Graph|planar]] [[Graph|graph]] $G$ has a plane embedding where all of the edges are straight line segments.

Proof: 

We proceed with induction on $|V|$. For $|V| \leq 3$, this is trivial. Assume $G$ is connected (otherwise we can do this on each [[Connectivity|connected component]] separately). 

Assume we can draw any graph with $n$ vertices as planar. WTS this is true for $|V| + 1$. Suppose we [[Planar Graph#Lemma (Triangulations)|triangulated]] the graph $G$ to get $G'$. By [[#Lemma (Triangulation Leads to Interior Vertex)]], we have some interior vertex $v$ where $\deg_{G'}(v) \leq 5$. 

Consider graph $G'' = G' - \{v\}$. Then by the induction hypothesis, $G''$ is planar with straight lines. Since $\deg_{G'}(v) \leq 5$, then the face created in $G''$ is no more than a pentagon. By applying [[#Lemma (Pentagonal Center)]], we can reinsert $v$ that makes the graph still planar, but with straight lines. 