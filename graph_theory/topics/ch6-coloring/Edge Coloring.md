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