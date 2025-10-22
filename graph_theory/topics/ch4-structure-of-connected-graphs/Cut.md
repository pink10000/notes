---
tags:
  - MATH_154
aliases:
  - cut
---
# Definition (Cut Vertex)
A **cut vertex** of $G$ is a vertex $v$ of $G$ such that removing will make it [[Connectivity#Definition (Reachability)|disconnected]]. 

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
Here, if $b$ is removed, then $a$ and $c$ are not reachable from each other. 

