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
# Theorem (Weak Planar Coloring Bound)
If $G$ is a [[Planar Graph]], then $\chi(G) \leq 6$.

Proof:

By [[Planar Graph#Theorem (Planar Graphs have Bounded Minimum)]] we know $G$ has $\delta(G) \leq 5$. We apply greedy coloring but on low degree vertices last and proceed with induction on $|V|$. So, if $|V| = 1$, then we are done. 

Inductively, assume that if we have any planar graph on $n$ vertices, then $\chi(G) \leq 6$, then we want to show the same for $G$ with $n + 1$ vertices. 

Pick $v \in G$ where $\deg(v) \leq 5$, which will be the last vertex to color. In particular, we color $G - v$ then color $v$. Since $G$ is planar, $G - v$ is planar, and by the IH, we can color $G - v$. As $v$ has $\leq 5$ neighbors, then we must have some available color. Using that, we have a $6-$coloring of $G$. 

# Theorem (Strong Planar Coloring Bound)
If $G$ is a [[Planar Graph]], then $\chi(G) \leq 5$. 

Proof: We induct on $|V|$. If $|V| \leq 5$, we are done (assign each vertex a unique color). Assume all planar graphs with $k$ vertices have a  $5-$coloring, and we want to show this for a graph $G$ with $k + 1$ vertices. Pick $v \in V$ where $\deg(v) \leq 5$. Again, the goal is color $G - v$ (which we can by the IH), and then add back $v$ and color it.

**Case 1**: If $\deg(v) < 5$, then we have at least one color left for $v$, allowing us to color it. 

**Case 2**: Suppose $\deg(v) = 5$. In this case, we cannot greedily color. We get two sub-cases:

**Case 2A**: If $v$'s neighbors all use $4$ distinct colors, then at least one color is free. Select that and we are done. 

**Case 2B**: Suppose all of $v$'s neighbors all have distinct colors. 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsNixbMSwxLCJ2Il0sWzAsMCwiXFxjb2xvcntyZWR9dl8xIl0sWzIsMCwiXFxjb2xvcntibHVlfXZfMiJdLFszLDEsIlxcY29sb3J7Z3JlZW59dl8zIl0sWzIsMiwiXFxjb2xvcntwdXJwbGV9dl80Il0sWzAsMiwiXFxjb2xvcnticm93bn12XzUiXSxbMCwxLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsNSwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDIsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCw0LCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMywiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dXQ==
\begin{tikzcd}
	{\color{red}v_1} && {\color{blue}v_2} \\
	& v && {\color{green}v_3} \\
	{\color{orange}v_5} && {\color{purple}v_4}
	\arrow[no head, from=2-2, to=1-1]
	\arrow[no head, from=2-2, to=1-3]
	\arrow[no head, from=2-2, to=2-4]
	\arrow[no head, from=2-2, to=3-1]
	\arrow[no head, from=2-2, to=3-3]
\end{tikzcd}
\end{document}
```
The goal is to recolor one of $v$'s neighbors to free up a color for $v$. 

**Attempt 1**: Suppose we tried to free up $\color{red}\texttt{red}$ on $v_{1}$ by changing it to $\color{green}\texttt{green}$. We can only do this if $v_{1}$ has no $\color{green}\texttt{green}$ neighbors. But then to swap $w \in N(v_{1})$ to $\color{red}\texttt{red}$, none of $N(w)$ can be $\color{red}\texttt{red}$. We can abstract this by finding the [[Kempe Chain]] $K_{\color{red}\texttt{red},\color{green}\texttt{green}}$. It is the connected component containing $v_{1}$ that includes only $\color{red}\texttt{red}$ and $\color{green}\texttt{green}$ vertices. We get two cases:

**Case 2B.1.1**: If $v_{3} \not \in K_{\color{red}\texttt{red}, \color{green}\texttt{green}}$ then can safely swap all the colors from $\color{red}\texttt{red}$ to $\color{green}\texttt{green}$ and $\color{green}\texttt{green}$ to $\color{red}\texttt{red}$. This means $v_{1}$ is $\color{green}\texttt{green}$, and we can color $v$ $\color{red}\texttt{red}$. 

**Case 2B.1.2**: If $v_{3}\in K_{\color{red}\texttt{red},\color{green}\texttt{green}}$,
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsOCxbMSwyLCJ2Il0sWzAsMSwiXFxjb2xvcntyZWR9dl8xIl0sWzIsMSwiXFxjb2xvcntibHVlfXZfMiJdLFszLDIsIlxcY29sb3J7Z3JlZW59dl8zIl0sWzIsMywiXFxjb2xvcntwdXJwbGV9dl80Il0sWzAsMywiXFxjb2xvcnticm93bn12XzUiXSxbMSwwLCJcXGNvbG9ye2dyZWVufVxcYnVsbGV0Il0sWzMsMCwiXFxjb2xvcntyZWR9XFxidWxsZXQiXSxbMCwxLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsNSwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDIsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCw0LCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMywiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDZdLFs2LDddLFs3LDNdXQ==
\begin{tikzcd}
	& {\color{green}\bullet} && {\color{red}\bullet} \\
	{\color{red}v_1} && {\color{blue}v_2} \\
	& v && {\color{green}v_3} \\
	{\color{orange}v_5} && {\color{purple}v_4}
	\arrow[no head, from=1-2, to=1-4]
	\arrow[no head, from=1-4, to=3-4]
	\arrow[no head, from=2-1, to=1-2]
	\arrow[no head, from=3-2, to=2-1]
	\arrow[no head, from=3-2, to=2-3]
	\arrow[no head, from=3-2, to=3-4]
	\arrow[no head, from=3-2, to=4-1]
	\arrow[no head, from=3-2, to=4-3]
\end{tikzcd}
\end{document}
```
then we cannot swap to free up a color for $v$. 

**Attempt 2**: Suppose we tried to swap $\color{blue}\texttt{blue}$ and $\color{orange}\texttt{orange}$ for $v_{2}$ and $v_{5}$ respectively. We find [[Kempe Chain]] $K_{\color{blue}\texttt{blue},\color{orange}\texttt{orange}}$. This means that 

**Case 2B.2.1**: If $v_{4} \not\in K_{\color{blue}\texttt{blue},\color{orange}\texttt{orange}}$, then we can safely swap, and we are done. 

**Case 2B.2.2**: Otherwise, we have 
```tikz
\usepackage{tikz-cd}
\begin{document}
% https://q.uiver.app/#q=WzAsMTAsWzIsMiwidiJdLFsxLDEsIlxcY29sb3J7cmVkfXZfMSJdLFszLDEsIlxcY29sb3J7Ymx1ZX12XzIiXSxbNCwyLCJcXGNvbG9ye2dyZWVufXZfMyJdLFszLDMsIlxcY29sb3J7cHVycGxlfXZfNCJdLFsxLDMsIlxcY29sb3J7b3JhbmdlfXZfNSJdLFsyLDAsIlxcY29sb3J7Z3JlZW59XFxidWxsZXQiXSxbNCwwLCJcXGNvbG9ye3JlZH1cXGJ1bGxldCJdLFswLDIsIlxcY29sb3J7Ymx1ZX1cXGJ1bGxldCJdLFsxLDAsIlxcY29sb3J7b3JhbmdlfVxcYnVsbGV0Il0sWzAsMSwiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDUsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCwyLCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsNCwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDMsIiIsMix7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMSw2LCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzYsNywiIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs3LDMsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNSw4LCIiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzgsOSwiIiwyLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs5LDIsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XV0=
\begin{tikzcd}
	& {\color{orange}\bullet} & {\color{green}\bullet} && {\color{red}\bullet} \\
	& {\color{red}v_1} && {\color{blue}v_2} \\
	{\color{blue}\bullet} && v && {\color{green}v_3} \\
	& {\color{orange}v_5} && {\color{purple}v_4}
	\arrow[no head, from=1-2, to=2-4]
	\arrow[no head, from=1-3, to=1-5]
	\arrow[no head, from=1-5, to=3-5]
	\arrow[no head, from=2-2, to=1-3]
	\arrow[no head, from=3-1, to=1-2]
	\arrow[no head, from=3-3, to=2-2]
	\arrow[no head, from=3-3, to=2-4]
	\arrow[no head, from=3-3, to=3-5]
	\arrow[no head, from=3-3, to=4-2]
	\arrow[no head, from=3-3, to=4-4]
	\arrow[no head, from=4-2, to=3-1]
\end{tikzcd}
\end{document}
```
But then this means that **Case 2B.1.2** and **Case 2B.2.2** happened at the same time. In particular, both chains must be vertex disjoint since they use different colors, and since $K_{\color{red}\texttt{red},\color{green}\texttt{green}}$ surround $v_{2}$, the existence of $K_{\color{blue}\texttt{blue},\color{orange}\texttt{orange}}$ means that they must intersect. 

But this is a contradiction as $G$ must be planar. Therefore only a single case $2$ for both attempts must be true. The inductive step holds, and we are done.

> This is also known as the *Five Color Theorem*.

## Corollary (Four Color Theorem)
Actually, for planar $G$, $\chi(G) \leq 4$. 