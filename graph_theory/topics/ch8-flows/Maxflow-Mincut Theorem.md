---
tags:
  - MATH_154
---
# Maxflow-Mincut Theorem 
The maximum [[#Definition (Flow)|flow]] of a [[#Definition (Network)|network]] is **equal** to the size of the minimum [[#Definition (Network Cut)|cut]]. 

Proof: 

We have the easy $\leq$ direction from [[Network#Lemma (Maxflow is at Most the Mincut)]]. So, in the reverse direction, consider the maximum flow $F$, where it is impossible for us to create an [[Network#Definition (Augmenting Path)|augmenting path]] to apply [[Network#Lemma (Add Augmenting Path to Flow)|lemma]] to increase it. 

On the other hand, we can create a *partial* augmenting path. We start at the source, but we don't need to end at the sink. It's edges are in $G \setminus F$ or reverse edges in $F$. Let 
$$
\begin{aligned}
S &= \{ \text{endpoints of a partial augmenting path} \} \\
T &= V \setminus S
\end{aligned}
$$
Since there's no partial augmenting path that ends at the sink, then the sink must be in $T$. This allows us to define a cut $C = (S, T)$ with this partition. 

I claim that $\text{size}(C) = \text{size}(F)$. First, there is no edge from $S \to T$. Suppose by contradiction there was. But then this means there is a partial augmenting path with an endpoint in $T$, contradicting the definition of $S$. This implies the flow is equal to the capacity.

Likewise, we cannot have an edge from $T \to S$. Otherwise, the reverse of it would be $S \to T$, giving us a contradiction. 

This allows us to compute $\text{size}(F)$:
$$
\begin{aligned}
\text{size}(F) 
&= |\{\text{edges from $S \to T$}\}| - |\{\text{edges from $T \to S$}\}|\\
&= |\{\text{edges in $G$ from $S \to T$}\}| - 0\\ 
&= \text{size}(C)
\end{aligned}
$$
where the last equality is by definition. But this tell us, 
$$
\begin{aligned}
&(\forall F, C)(\text{size}(F) \leq \text{size}(C)) \\
&(\exists F_{0},C_{0})(\text{size}(F_{0}) = \text{size}(C_{0}))
\end{aligned}
$$
Indeed, for all flows $F$, 
$$
\text{size}(F) \leq \text{size}(C_{0}) = \text{size}(F_{0}) \implies \text{maxflow} = F_{0}
$$
and for all cuts $C$, 
$$
\text{size}(C) \geq \text{size}(F_{0}) = \text{size}(C_{0}) \implies \text{mincut} = C_{0}
$$
Therefore the maxflow and mincut are equal. 

## Applications
We can apply this to [[Konig's Theorem]] by turning it into a network graph where the directed edges are from $L \to R$, and that we can create an arbitrary source vertex connecting all of $L$, (i.e. $N(\text{source}) = L$) and an arbitrary sink vertex where $N(\text{sink}) = R$. This gives a correspondence from [[Matching|matchings]] in $G$, to [[Network#Definition (Flow)|flows]] in $N$. 

We can also apply this to [[Menger's Theorem]]. Replace each edge with two directed edges in the opposite direction to form a network. If we can remove edges to separate $S, T$, then it defines a cut $C$. Then $\text{size}(C)$ is at most the number of removed edges. But for a minimum cut, this is equal to the maxflow. Indeed, there exists a flow $F$ where $\text{size}(F) = \text{size}(C) = k$. 

If $F$ is a flow of size at least $k$, then it contains $k$ edge disjoint $S \to T$ paths. We can prove this by induction on $k$. For $k = 1$, we start at $S$ and create a path by adding new edges to $F$ until we get stuck (in particular, $T$). Suppose we stopped at some vertex $v$. For each ingoing edge to $v$, we take an outgoing edge, except for the last one such that we cannot get stuck. At $S$, the number of outgoing is ingoing plus $k$. So, we cannot get stuck here. Thus we can only stop at $T$. 

For the inductive step, consider a $S \to T$ path $P$. We induct on $F - P$, giving us $k - 1$ edge disjoint paths. The proof is trivial from here.

