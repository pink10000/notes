---
tags:
  - MATH_154
---
We use $\Delta(G)$ from [[Degree#Definition (Maximum Degree of a Graph)]].
# Definition (Coloring)
A vertex **coloring** of a [[Graph|graph]] $G$ is an assignment of a color to each vertex of $G$ so that no two adjacent vertices have the same color. This is an $n-$coloring if only $n$ different colors are used. 

# Definition (Chromatic Number)
The **chromatic number** $\chi(G)$ of a graph $G$ is the smallest number $n$ so that $G$ has a graph coloring. 

## Lemma (Low Chromatic Numbers)
- $\chi(G) = 1 \iff |E(G)| = 0$ 
- $\chi(G) \leq 2 \iff G$ is [[Bipartite Graph#Formal|bipartite]].
- Determining $\chi(G)$ for more complicated graphs is difficult. For $2-$colorings, once you color a vertex, the is only one possible choice for its neighbors. For $3-$colorings, there are two. 
## Lemma (Bipartite Chromatic Number)
Obviously, for any [[Bipartite Graph]], the chromatic number is $2$ (by definition!).
## Lemma (Path Chromatic Number)
For any [[Path]] $P_{n}, \chi(P_{n}) = 2$, since we can simply alternate. 
## Lemma (Cycle Chromatic Number)
For any [[Cycle]] $C_{n}, \chi(C_{n}) = 2$ if $n$ is even, but $3$ if $n$ is odd. 
## Lemma (Complete Chromatic Number)
For [[Complete Graph]] $K_{n}, \chi(K_{n}) = n$, since every vertex is connected to each other and thus must be different colors. 
# Lemma (Chromatic Upper Bound) 
For $G$ a graph on $n$ vertices, then $\chi(G) \leq n$. 

Proof: Give each vertex a different color. 

> The lower bound is given by [[Clique#Corollary (Chromatic Number Lower Bound)|corollary]].

# Greedy Coloring
We can try a greedy *coloring strategy* by coloring vertices one at a time and filling in the ones that do not conflict. If $v$ has $\deg(v)$ neighbors, then it is enough to have $\deg(v)+1$ colors to choose from.

## Lemma (Chromatic Upper Bound by Big Delta)
For any graph $G$, 
$$
\chi(G) \leq \Delta(G) + 1
$$
Proof: Use [[#Greedy Coloring]]. 
> This bound is far often from tight. For example, $\chi(K_{n,n}) =2$ but $\Delta(K_{n,n}) = n$. Note the same message in [[Clique#Corollary (Chromatic Number Lower Bound)|corollary]].

### Equality Special Cases
We have two cases where equality is achieved:
1. For $C_{n}$ with odd $n$, $\chi(C_{n}) = 3$ and $\Delta(G) = 2$. 
2. $K_{n}$ for $n > 1$, then $\chi(G) = n$ and $\Delta(G) = n - 1$.

### Brook's Theorem
If $G$ is a finite [[Connectivity|connected]] graph that is neither an odd cycle nor a complete graph, then 
$$
\chi(G) \leq \Delta(G)
$$
Proof: 

Let $G = (V, E)$. For the special cases, see [[#Equality Special Cases]]. For $\Delta(G) \leq 2$, see [[Degree#Lemma (Big Delta Less Than 3)]]. 

Suppose $G$ is not [[Degree#Definition $d-$regular|regular]]. Then there is some vertex $v \in V$ where $\deg(v) < \Delta(G)$. If we can color $G - \{v\}$, then we can try to greedily color $v$. But then 
$$
\forall w \in N(v) \subseteq V(G - \{v\}), \deg_{G - \{v\}}(w) = \deg_{G}(w) - 1
$$
guaranteeing there is at least one color. We can then repeat this for every vertex. 

Suppose $G$ is $k-$regular. We want to find vertex $v$ where $u,w \in N(v)$ have the same color.
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsMyxbMCwxLCJ2Il0sWzEsMCwiXFxjb2xvcntyZWR9dyJdLFsxLDIsIlxcY29sb3J7cmVkfXUiXSxbMCwxLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMiwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dXQ==
\begin{tikzcd}
	& {\color{red}w} \\
	v \\
	& {\color{red}u}
	\arrow[no head, from=2-1, to=1-2]
	\arrow[no head, from=2-1, to=3-2]
\end{tikzcd}
\end{document}
```
If $G$ is a complete graph, refer to [[#Equality Special Cases]]. So, since $G$ is not complete, $u,v$ are not adjacent. We can try to color $G - \{v\}$ with $u,w$ as the same color. 

If $\{u,w\}$ is *not* a [[Cut|cutset]], then we can recursively color the rest of the graph. If $\{u, w\}$ is a [[Cut|cutset]], then split $G$ into two parts. We color each half inductively and change colors so that $u,w$ match[^1]. 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNCxbMiwwLCJ1Il0sWzIsMiwidyJdLFswLDEsIihIXzEpIl0sWzQsMSwiKEhfMikgIl0sWzIsMCwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsyLDEsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCwzLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzMsMSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFszLDAsIiIsMSx7Im9mZnNldCI6LTMsInN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMiwxLCIiLDEseyJvZmZzZXQiOi0zLCJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzEsMywiIiwxLHsib2Zmc2V0IjotMywic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDIsIiIsMSx7Im9mZnNldCI6LTMsInN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XV0=
\begin{tikzcd}
	&& u \\
	{(H_1)} &&&& {(H_2) } \\
	&& w
	\arrow[shift left=3, no head, from=1-3, to=2-1]
	\arrow[no head, from=1-3, to=2-5]
	\arrow[no head, from=2-1, to=1-3]
	\arrow[no head, from=2-1, to=3-3]
	\arrow[shift left=3, no head, from=2-1, to=3-3]
	\arrow[shift left=3, no head, from=2-5, to=1-3]
	\arrow[no head, from=2-5, to=3-3]
	\arrow[shift left=3, no head, from=3-3, to=2-5]
\end{tikzcd}
\end{document}
```
[1]:Let $H_{1},H_{2}$ denote the halves split by $u, w$. You can imagine this is a graph contracted version of $G$.

We have two cases:

**Case 1**: If $v$ is a cut vertex, we can inductively color each connected component of $G - \{v\}$. We need arrange it so then two (non-adjacent) neighbors of $v$ are the same color. This gives the coloring for $v$.

**Case 2**: If we have $2$ cut vertices, then $\{u,w\}$ is our cutset. Let $H_{1}' = H_{1} \cup \{u,w\}$ and $H_{2}' = H_{2} \cup \{u,w\}$ be our two halves. We inductively find a $k-$coloring $c_{1},c_{2}$ for $H_{1}',H_{2}'$ respectively. However, we need to show that we can make $u,w$ match colors before combining two halves, which gives our coloring. 

**Case 2A**: Suppose we colored $H_{1}'$ such that $c_{1}(u) \neq c_{1}(w)$ by greedily coloring keeping $u,w$ be last. If 
$$
(\deg_{H_{1}}(u) < k - 1) \vee (\deg_{H_{1}}(u) < k - 1) 
$$
then we can ensure that there is at least one color to ensure the colors are different. 

**Case 2B**. Here, $c_{1}(u) = c_{1}(w)$, implying that
$$
\deg_{H_{1}}(u) = k - 1 \wedge \deg_{H_{1}}(w) = k - 1
$$
But since $G$ is $k-$regular, then 
$$
\begin{aligned}
\deg_{G}(u) &= \deg_{H_{1}}(u) + \deg_{H_{2}}(u) \\
k &= k - 1 + \deg_{H_{2}}(u) \\
1 &= \deg_{H_{2}}(u)
\end{aligned}
$$
and likewise for $w$. But then this means we can easily find a $k-$coloring $c_{2}$ for $H_{2}'$ where $c_{2}(u) = c_{2}(w)$. Then permute colors to ensure $c_{1}(u) = c_{2}(u)$ and $c_{1}(w) = c_{2}(w)$, allowing us to combine the halves, and giving us our coloring. 

# Coloring Planar Graphs
We extend the definition for [[Planar Graph|planar graphs]] by choosing to color faces and not vertices. 