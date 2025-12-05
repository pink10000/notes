---
tags:
  - MATH_154
---
# Turan's Theorem 
The [[Extremal Graph#Definition (Turan Numbers)|Turan number]] $\text{ex}(n, K_{r})$ is uniquely achieved by the [[Complete Graph|complete]] $(r - 1)$-partite graph with parts of size 
$$
\left\lfloor \frac{n}{r-1} \right\rfloor 
\text{ or } 
\left\lceil \frac{n}{r - 1} \right\rceil
$$
In particular, the extremal graph is denoted as $T_{n,r}$. 

Proof: 

First, we want to prove that 
$$
\text{ex}(n, K_{r}) = |E(T_{n,r})|
$$
by induction on $n$. 

**Base Case:** If $n = r - 1$ we are done since we have $K_{r -1}$, and clearly $K_{r}$ does not exist. 

**Inductive Step**: We WTS that if $G$ has no $K_{r}$, then $\delta(G) \leq n - \lceil n/(r-1) \rceil$. If such a vertex $v$ had this minimal degree, then by removing $v$, 
$$
\begin{aligned}
\text{ex}(n, K_{r})
&\leq n - \ceil{n/r-1} + \text{ex}(n - 1, K_{r}) \\
&= n - \ceil{n/r-1} + |E(T_{n-1, r})|  && \leftarrow \text{by IH}\\ 
&= |E(T_{n,r})|
\end{aligned}
$$
in the last step, we add back $v$. Since $\deg(v) = n - \ceil{n/(r-1)}$, then adding those edges back gives us $T_{n,r}$. Notice how the total number of vertices not in $v$'s partition is exactly the upper bound of $\delta(G)$.

Now assume for sake of contradiction that $\delta(G) > n - \ceil{n/(r-1)}$. The goal is to find $K_{r}$. So let's start with $n$ vertices and pick a vertex $v_{1}$ to be in $K_{r}$. Let's discard (or ignore) the non neighbors of $v_{1}$. In particular, we have not discarded many vertices. Since $\delta(G)$ is high, then we removed 
$$
\text{Removed} = n - \deg(v) < n - \left( n - \ceil{\frac{n}{r-1}} \right) = \frac{n}{r-1}
$$
Then we will pick a $v_{2} \in N(v_{1})$ and discard the non neighbors of $v_{2}$ and repeat. Each selected vertex must be adjacent to every previously selected vertex. At the end, we end up with a complete graph. 

The point is that on any round, the vertex selected and its non neighbors is going remove fewer than $n/(r-1)$ vertices. So after $k$ rounds, we have *strictly* more than 
$$
n - \frac{kn}{r-1}
$$
vertices left. After $r - 1$ rounds, there is *strictly* 
$$
n - \frac{(r - 1)n}{r-1} = n - n = 0  
$$
left. Indeed, $> 0 \iff \geq 1$, so this is at least one more vertex to select. But as each vertex selected is adjacent to every other vertex selected, we get $K_{r}$.

To prove $G$'s uniqueness, if $G$ is an extremal graph, then it must isomorphic to $T_{n,r}$. Suppose so. Then by the previous work, 
$$
|E(G)| = \text{ex}(n, K_{r}) = | E(T_{n,r} ) |
$$
We proceed by induction. I claim that 
$$
\delta(G) = n - \ceil{\frac{n}{r-1}}
%% \;\;\wedge\;\; 
%% \deg(v) = \delta(G) \implies |E(G - \{v\})| = |E(T_{n-1, r})| %%
$$
and that removing $v$ where $\deg(v) = \delta(G)$ gives us the Turan graph. From our previous work,
1. If $G$ has no $K_{r}$ then $\delta(G) \leq \delta(T_{n,r})$. 
2. $|E(T_{n,r})| = \delta(T_{n, r}) +  |E(T_{n-1,r})$
This gives us
$$
\begin{aligned}
\deg(v) + |E(G - v) | 
&= |E(G)|\\
&= |E(T_{n,r})\\
&= \delta(T_{n,r}) + | E(T_{n-1,r})|
\end{aligned}
$$
As $\deg(v) = \delta(G) \leq \delta(T_{n,r})$ and $|E(G - v)| \leq |E(T_{n-1,r})|$, then equality can only be achieved if pairwise, the terms are equal. Thus
$$
\delta(G) = \delta(T_{n,r}) = n - \ceil{\frac{n}{r-1}}
$$
Since $| E(G - v) | = | E(T_{n-1,r})|$ and that $G - v$ has no $K_{r}$, by the induction hypothesis on uniqueness, $G - v$ is uniquely isomorphic to $T_{n-1, r}$. 

Let $V_{1}, V_{2}, \dots, V_{r-1}$ be the partitions of the complete $(r-1)$-partite graph of $G - v$. The goal is to add back $v$, and show that doing so gives us $T_{n,r}$. In particular, 
1. $v$ cannot be adjacent to some vertex in every $V_{i}$. Otherwise, as these $r- 1$ vertices already connect to each other, then we have $K_{r-1} \subset G - v$. Thus, adding $v$ gives $K_{r}$, a contradiction.
2. So adding $v$ means we connect to every part *except* one partition. Since $\deg(v) = \delta(T_{n,r})$, then 
   $$
   \deg(v) \leq \left(\sum_{i \neq k} |V_{i}|\right) = (n - 1) - |V_{k}|
   $$
3. Since $v$ is minimal then it must be from the *largest* possible partition $V_{\text{max}}$. Thus, 
   $$
   \delta(T_{n,r}) = (n - 1) - |V_{\max}|
   $$
4. This gives us 
   $$
   \begin{aligned}
   \deg(v) &\leq (n - 1) - |V_{k}| \\
   (n - 1) - |V_{\max} | &\leq (n - 1) - |V_{k}| \\
   |V_{k}| &\leq |V_{\max}|
   \end{aligned}
   $$
   So, $v$ must be be connected to every vertex in every partition *but* $V_{k}$. 
5.  $V_{k} \cap N(v) = \varnothing$ means that we can add $v$ to $V_{k}$ while respecting the partition structure of $G$. Thus, $G$ is complete $(r - 1)$-partite graph with $V_{1}, \dots, V_{k}\cup \{v\}, \dots, V_{r-1}$. As $|E(G)| = \text{ex}(n, K_{r})$, $G$ is the unique extremal graph, and edge count is maximized when all sizes are as equal as possible. Thus $G \cong T_{n,r}$. 