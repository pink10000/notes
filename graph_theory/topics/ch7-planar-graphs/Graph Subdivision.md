---
tags:
  - MATH_154
aliases:
  - subdivision
---
# Definition (Graph Subdivision)
A **subdivision** of [[Graph|graph]] $G$ is obtained by placing vertices in the middle of some of its edges. 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsMTMsWzAsMCwiXFxidWxsZXQiXSxbMCwyLCJcXGJ1bGxldCJdLFsyLDIsIlxcYnVsbGV0Il0sWzIsMCwiXFxidWxsZXQiXSxbMywxLCJcXGxvbmdyaWdodGFycm93Il0sWzQsMCwiXFxidWxsZXQiXSxbNCwyLCJcXGJ1bGxldCJdLFs2LDIsIlxcYnVsbGV0Il0sWzYsMCwiXFxidWxsZXQiXSxbNCwxLCJcXGJ1bGxldCJdLFs1LDAsIlxcYnVsbGV0Il0sWzYsMSwiXFxidWxsZXQiXSxbNSwxLCJcXGJ1bGxldCJdLFswLDEsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMSwyLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzIsMywiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDAsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCwyLCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzYsNywiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs1LDEyLCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzEyLDcsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNywxMSwiIiwxLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxMSw4LCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzgsMTAsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMTAsNSwiIiwxLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs1LDksIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbOSw2LCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV1d
\begin{tikzcd}
	\bullet && \bullet && \bullet & \bullet & \bullet \\
	&&& \longrightarrow & \bullet & \bullet & \bullet \\
	\bullet && \bullet && \bullet && \bullet
	\arrow[no head, from=1-1, to=3-1]
	\arrow[no head, from=1-1, to=3-3]
	\arrow[no head, from=1-3, to=1-1]
	\arrow[no head, from=1-5, to=2-5]
	\arrow[no head, from=1-5, to=2-6]
	\arrow[no head, from=1-6, to=1-5]
	\arrow[no head, from=1-7, to=1-6]
	\arrow[no head, from=2-5, to=3-5]
	\arrow[no head, from=2-6, to=3-7]
	\arrow[no head, from=2-7, to=1-7]
	\arrow[no head, from=3-1, to=3-3]
	\arrow[no head, from=3-3, to=1-3]
	\arrow[no head, from=3-5, to=3-7]
	\arrow[no head, from=3-7, to=2-7]
\end{tikzcd}
\end{document}
```
# Lemma (Subdivisions Preserve Planarity)
If $G'$ is a subdivision of $G$, then $G'$ is [[Planar Graph|planar]] $\iff$ $G$ is planar. 

Proof: Given a plane embedding of $G$ we can add vertices of in the middles of $E(G)$ to get the embedding of $G'$. Given the embedding of $G'$, we remove vertices and join edges to get the embedding of $G$.