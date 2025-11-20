---
tags:
  - MATH_154
---
# Definition (Edge Coloring)
An edge [[Coloring|coloring]] of a graph $G$ is an assignment of a color to each edge so that no two edges that share the same vertex share the same color. 

For example, if we want to color [[Complete Graph]] $K_{4}$, 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNCxbMSwxLCJcXGJ1bGxldCJdLFsxLDAsIlxcYnVsbGV0Il0sWzAsMiwiXFxidWxsZXQiXSxbMiwyLCJcXGJ1bGxldCJdLFszLDIsIiIsMCx7ImNvbG91ciI6WzMwLDYwLDYwXSwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsyLDAsIiIsMCx7ImNvbG91ciI6WzEyMCw2MCw2MF0sInN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCwzLCIiLDAseyJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDEsIiIsMCx7ImNvbG91ciI6WzEyMCw2MCw2MF0sInN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMSwyLCIiLDAseyJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDAsIiIsMSx7ImNvbG91ciI6WzMwLDYwLDYwXSwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dXQ==
\begin{tikzcd}
	& \bullet \\
	& \bullet \\
	\bullet && \bullet
	\arrow[color={rgb,255:red,214;green,153;blue,92}, no head, from=1-2, to=2-2]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, no head, from=1-2, to=3-1]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, no head, from=2-2, to=3-3]
	\arrow[color={rgb,255:red,92;green,214;blue,92}, no head, from=3-1, to=2-2]
	\arrow[color={rgb,255:red,92;green,214;blue,92}, no head, from=3-3, to=1-2]
	\arrow[color={rgb,255:red,214;green,153;blue,92}, no head, from=3-3, to=3-1]
\end{tikzcd}
\end{document}
```
with $\color{red}\texttt{red}, \color{green}\texttt{green},$ and $\color{orange}\texttt{orange}$. 
# Definition (Edge Chromatic Number)
We can find the **Edge Chromatic Number**,
$$
\chi'(G) := \text{minimum number of colors to find an edge coloring of } G
$$
> Related: [[Coloring#Definition (Chromatic Number)]]. 

It is not hard to see that 
$$
\chi'(G) = \chi(L(G))
$$
where $L(G)$ is the line graph of the graph $G$. 

# Edge Chromatic Number Bounds
From [[Clique#Corollary (Chromatic Number Lower Bound)|corollary]], we have 
$$
\chi(L(G)) \geq \omega(L(G))
$$
maximally, if $G$ is a starfish graph, it's line graph is a complete graph. This gives us another (albeit weaker) lower bound:
$$
\chi(L(G)) \geq \omega(L(G)) \geq \Delta(G)
$$
For an upper bound, from [[Coloring#Lemma (Chromatic Upper Bound by Big Delta)|lemma]], 
$$
\chi'(G) = \chi(L(G)) \leq \Delta(L(G)) + 1
$$
> What is the degree of some vertex in the line graph? 

Suppose we had some edge $e$ connecting two starfishes centered on $u,v$. Then 
$$
\deg_{L(G)}(e) 
= \deg_{G}(u) - 1 + \deg_{G}(v) - 1 
= \deg_{G}(u) + \deg_{G}(v) - 2
\leq 2\Delta(G) - 2 
$$
which gives us:
$$
\chi'(G) = \chi(L(G)) \leq \Delta(L(G)) + 1 \leq 2(\Delta(G) - 1)
$$
> See [[Vizing's Theorem]].