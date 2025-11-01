---
tags:
  - MATH_154
---
# Definition (Polyhedra)
A **Polyhedron** is  a $3$ dimensional figure bounded by finitely many flat faces. Examples are 
- Cube
- Various Prisms
- Various Pyramids
Faces meet at an edge and edges meet at vertices.
# Definition (Convex)
A polyhedron is **convex** if for any two points in the polyhedron, if the line segment connecting them is also contained in the polyhedron.  
# Lemma (Planar Graphs from Convex Polyhedra)
If we have a convex polyhedron, then we have a [[Planar Graph]] of its edges and vertices. We can essentially make a *wireframe* diagram of a polytope. For example, given a cube, we can draw
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsOCxbMSwxLCJcXGJ1bGxldCJdLFsyLDEsIlxcYnVsbGV0Il0sWzEsMiwiXFxidWxsZXQiXSxbMiwyLCJcXGJ1bGxldCJdLFszLDAsIlxcYnVsbGV0Il0sWzMsMywiXFxidWxsZXQiXSxbMCwzLCJcXGJ1bGxldCJdLFswLDAsIlxcYnVsbGV0Il0sWzcsMCwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs3LDQsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNCw1LCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzUsNiwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs2LDcsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMiw2LCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDQsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMSwzLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzMsNSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDIsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMiwwLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV1d
\begin{tikzcd}
	\bullet &&& \bullet \\
	& \bullet & \bullet \\
	& \bullet & \bullet \\
	\bullet &&& \bullet
	\arrow[no head, from=1-1, to=1-4]
	\arrow[no head, from=1-1, to=2-2]
	\arrow[no head, from=1-4, to=4-4]
	\arrow[no head, from=2-2, to=2-3]
	\arrow[no head, from=2-3, to=1-4]
	\arrow[no head, from=2-3, to=3-3]
	\arrow[no head, from=3-2, to=2-2]
	\arrow[no head, from=3-2, to=4-1]
	\arrow[no head, from=3-3, to=3-2]
	\arrow[no head, from=3-3, to=4-4]
	\arrow[no head, from=4-1, to=1-1]
	\arrow[no head, from=4-4, to=4-1]
\end{tikzcd}
\end{document}
```
which is obviously planar. Note that the polytope face "behind" the cube was "ripped open" to become the ambient space, which is our face. 

# Definition (Regular Polyhedra / Platonic Solid)
A **regular polyhedron** or **platonic solid** is a polyhedron where all
- the edges are the same length
- the faces are regular polygons
- all faces have the same number of sides
- the same number of faces at each vertex

## Lemma (Characterization of Platonic Solids)
What are the platonic solids? We can answer this by turning polytopes into planar graphs. 

Let's assume we have $s$ sides per face and we are $d-$regular (or $d$ edges at each vertex). Or equivalently, $d$ faces at each vertex. By [[Planar Graph#Euler's Formula|Euler's Formula]] we have 
$$
|F| - |E| + |V| = 2
$$
and by [[Handshake Lemma]], we have 
$$
|V| \cdot d = 2|E|
$$
In particular,
$$
|V| = \frac{2|E|}{d}
$$
So, by the [[Face Handshake Lemma]] where $|S|$ is the number of sides of a platonic solid, 
$$
\begin{aligned}
2 
&= |V| - |E| + |F|  \\
&= |E| \cdot \left(  \frac{2}{d} + \frac{2}{|S|} - 1 \right) \\
\end{aligned}
$$
and that for any polyhedron, each vertex has at least degree $3$, we have that 
- $d, |S| \geq 3$
- $2/d + 2/|S| > 1$
- $|E| = 2 \cdot (2/d + 2/|S| - 1)^{-1}$
- $|V| = 2|E|/d$
- $|F| = 2|E|/|S|$

giving us the following cases:
1. If $d = s = 3$, then  $|V| = 4, |E| = 6, |F| = 4$, a regular tetrahedron
2. If $d = 3, s = 4,$ then $|V| = 8, |E| = 12, |F| = 6$, a cube
3. If $d = 3, s = 5$, then $|V| = 20, |E| = 30, |F| = 12$, a regular dodecahedron
4. If $d = 3, s \geq 6$, then it does not work. We would get $3$ hexagons at a vertex. 
5. If $d = 4, s = 3$ then $|V| = 6, |E| = 12, |F| = 8$, a regular octahedron 
6. If $d = 4, s \geq 4$, this does not work. 
7. If $d = 5, s = 3$, then $|V| = 12, |E| = 30, |F| = 20$, a regular icosahedron
8. If $d = 5, s \geq 4$, this does not work. 
9. If $d \geq 6, s \geq 3$, then this does not work. 
We have only $5$ platonic solids. 

> See [Wikipedia](https://en.wikipedia.org/wiki/Platonic_solid) for images.

# Lemma (Faces Have At Least 3 Sides)
Every face has *at least* $3$ sides, such that $2|E| \geq 3|F|$. More generally, if $G$ only has faces with at least $k$ sides, then 
$$
|E| \geq \frac{k |F|}{2}
$$
# Lemma (Faces Have Maximum Edges)
If each face has at least $k$ sides, then the maximum number of edges is 

Proof: By [[Planar Graph#Euler's Formula|Euler's Formula]], 
$$
\begin{aligned}
2 &= |V| - |E| + |F| \\
&\leq |V| - |E| + \frac{2|E|}{k} \\
&= |V| - |E| \cdot \left( 1 - \frac{2}{k} \right) \\
\end{aligned}
$$
such that 
$$
|E| \leq \frac{|V| - 2}{1 - 2/k}
$$
and we are done.

# Corollary (Faces Have Maximum Sides)
Every polyhedron has a face with at most $5$ sides. This is from [[Planar Graph#Theorem (Planar Graphs have Bounded Minimum)]]. 