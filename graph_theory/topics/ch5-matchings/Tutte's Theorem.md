---
tags:
  - MATH_154
---
# Lemma (Tutte's: Parity of V)
Suppose that $\forall S \subset V, |S| \geq \Omega(G - S)$[^1]. We know $|V|$ must be even. This is because we can have $S = \varnothing$ such that 
$$
0 = |S| \geq \Omega(G - S) = \Omega(G) \geq 0
$$
implying that all connected components $C$ are even. Indeed, 
$$
|V| = \sum_{\text{CCs}} \deg(C)
$$
where a sum of even components is even. 

[^1]: See [[Connectivity#Definition (Odd Connected Components)]] for $\Omega(G - S)$, the number of connected components with an odd number of vertices.
# Lemma (Parity of Cut and Components)
For any $S \subset V, |S| - \Omega(G - S)$ is even.

Proof: Since $|V|$ must be even, then 
$$
|V| = |S| + \sum_{\substack{\text{CCs } C \\ \text{of } G - S}} |C|
$$
Using modular arithmetic, if $|C|$ is even then $|C| \equiv 0 \bmod 2$ and if $|C|$ is even, $|C| \equiv 1 \bmod 2$. Indeed, 
$$
\sum |C| \equiv \Omega(G - S) \bmod 2
$$
and as $|V| \equiv 0 \bmod 2$, 
$$
\begin{aligned}
|V| &= |S| + \sum_{\substack{\text{CCs } C \\ \text{of } G - S}} |C| \\
0 &\equiv [|S| + \Omega(G - S)] \bmod 2
\end{aligned}
$$
Implying that $|S|$ and $\Omega(G - S)$ have the same parity. Indeed, 
$$
|S| - \Omega(G - S) \equiv 0 \bmod 2
$$
which completes the lemma proof. 

## Corollary (Tutte Condition)
If $|S| > \Omega(G - S)$, then $|S| \geq \Omega(G - S) + 2$, which comes from the lemma. 

# Tutte's Theorem
The [[Bipartite Graph]] $G = (V, E)$ has a perfect [[Matching|matching]] $\iff \forall S \subset V, |S| \geq \Omega(G - S)$[^1].

Proof:

$(\implies)$
Let $G$ have a perfect matching. If by contradiction that $\exists S \subset V$ where $|S| < \Omega(G - S)$, then if $C$ is an odd connected component of $G - S$, then $C$ has no internal perfect matching because at least one vertex will be unpaired. 

Let this be $v \in C$. Then $v$ must match to some $w \in (G - S) - C$. As $C$ is a connected component of $C - S$, $C$ cannot bridge to another connected component, and thus must bridge to $S$ in $G$. Indeed, $w \in S$. 

This is true for all odd connected components. Thus, there are at least $\Omega(G - S)$ total $w \in S$, such that 
$$
|S| \geq \Omega(G - S)
$$
which is a contradiction. 

$(\impliedby)$
Suppose $\forall S \subset V, |S| \geq \Omega(G - S)$. From [[#Lemma (Tutte's Parity of V)]], $|V|$ must be even. 

We proceed with strong induction. If $|V| = 2$, then this is trivial. Assume for any graph with strictly less than $m$ vertices, the theorem holds. We want to show that for graph $G$ with $m$ vertices, it has a perfect matching. 

**Case 1**: Suppose that for all nonempty subsets $S \subseteq V$ the *strict* inequality $|S| > \Omega(G - S)$ holds. From [[#Corollary (Tutte Condition)]], then $|S| \geq \Omega(G - S) + 2$. 

We can pick an arbitrary edge $e = (u, v)$ and consider $G' = G - \{u, v\}$. We need to show it satisfies the Tutte Condition to apply IH. Suppose it does not, such that $\exists S \subseteq V(G')$ such that 
$$
|S| < \Omega(G' - S).
$$
Take $S' = S \cup \{u, v\}$ in $G$. This tells us that 
$$
|S'| = |S| + 2
$$
Indeed, $G - S'$ is isomorphic to $G' - S$ (we remove the same vertices) such that
$$
\Omega(G - S') = \Omega(G' - S)
$$
By substitution, 
$$
\begin{aligned}
|S| &< \Omega(G' - S) \\ 
|S'| - 2 &<  \Omega(G - S') \\
|S'| &< \Omega(G - S') + 2
\end{aligned}
$$
which contradicts the [[#Corollary (Strict Tutte Condition)|corollary]]. Thus no such subset exists and, by IH, $G'$ has as a perfect matching $M'$. Then $M = M \cup \{e\}$ is a perfect matching for $M$. 

**Case 2**: Suppose we took a maximal $S$ such that $|S| = \Omega(G - S)$. Let $|S| = k$ such that there are $k$ total odd connected components in $G - S$. Let $C_{1}, C_{2}, \dots, C_{k}$ be these connected components. Let $U$ be the union of the vertices in the even components (if any).

To construct a perfect matching for $G$, 
1. the even components in $G - S$ must have a perfect matching (there are actually none)
2. some vertex in the odd components and $S$ must have a perfect matching
3. the remaining vertices in $S$ need a perfect matching
In particular, we can match each distinct vertex in $S$ to a distinct off component $C_{i}$, and the remaining vertices in each $C_{i}$ can be perfectly matched amongst themselves. 

For point $1$, if $C$ were an even component of $G - S$, then we can pick some vertex $v \in C$ and let $S' = S \cup \{v\}$. I claim that $|S'| = \Omega(G - S')$. So,
$$
|S'| = |S| + 1 = \Omega(G - S) + 1
$$
Since $C - \{v\}$ has an odd number of vertices, when partitioned, at least one connected component must be odd. Thus, 
$$
\Omega(G - S') \geq \Omega(G - S) + 1
$$
From our global assumption, we know $|S'| \geq \Omega(G - S')$. Thus, 
$$
|S'| - \Omega(G- S') \leq (|S| + 1) - (\Omega(G - S) + 1) = 0
$$
where $|S| = \Omega(G - S)$ comes from our case premise. In particular, this means that $|S'| = \Omega(G - S')$. But then this is a contradiction on the maximality of $S$, since $S \subsetneq S'$ and $S'$ satisfies the equality.

For point $3$, if $C$ is an odd connected component of $G - S$, then for some $v \in C, C- \{v\}$ has a perfect matching. Assume for the sake of contradiction that $C' = C - \{v\}$ does not have a perfect matching. By the IH, then $\exists T \subset C'$ such that $|T| < \Omega(C' - T)$. 

By [[#Lemma (Tutte's Parity of V)]], $\Omega(C' - T) - |T|$ is even, and by [[#Corollary (Tutte Condition)]],
$$
|T| \leq \Omega(C' - T)  - 2
$$
Let $S' = S \cup \{v\} \cup T$. So,
$$
|S'| = |S| + |T| + 1
$$
When we remove $\{v\} \cup T$ from $C$, we get some odd components. Indeed, we have $\Omega(C' - T)$ total components. So, 
$$
\Omega(G - S') =  \Omega(G - S) - 1 + \Omega(C' - T)
$$
Where the $1$ compensates for $C'$, which is now even. We have that
$$
\begin{aligned}
\Omega(G - S') 
&= \Omega(G - S) - 1 + \Omega(C' - T) \\ 
&= |S| - 1 + \Omega(C' - T) \\
&\geq |S| - 1 + |T| + 2 \\
&= |S| + |T| + 1 \\
&= |S'|
\end{aligned}
$$
but here, we assumed $S$ was maximal. But here, $S'$ is a larger set that also holds, which is a contradiction on the maximality of $S$. 

Now we need to show point $2$. We need to show that there is a perfect matching between the odd connected components of $G - S$ and $S$ itself. In particular, we apply [[Hall's Theorem]]. There is a perfect matching *unless* there $\exists T \subset S$ such that 
$$
|N(T)| < |T|
$$
Where $|N(T)|$ is the number of all connected components of $G - S$ adjacent to some vertex in $T$. Let $S' = S - T$. We have that
$$
|S'| = |S| - |T|
$$
and 
$$
\Omega(S') \geq \Omega(S) - |N(T)|
$$
where $T$ "steals" away the connected components of $S$ from $S'$. By algebra, 
$$
\begin{aligned}
\Omega(S') &\geq \Omega(S) - |N(T)| \\
&= |S| - |N(T)| \\
&> |S| - |T| \\
&= |S'|
\end{aligned}
$$
which is a contradiction of the original assumption of Tutte's Theorem.

Thus the proof is done. 
# Peterson's Theorem 
Any [[Connectivity#Definition (Bridge)|bridgeless]] $3-$[[Degree#Definition $d-$regular|regular]] graph has a perfect [[Matching|matching]]. 

We first prove the following lemma:

## Lemma (Peterson: Odd Outbound Edges)
If $C \subseteq V$ is an odd-sized set of vertices, then the number of edges from $C$ to $V \setminus C$ is odd.

Proof: Let $\del(C)$ be the set of edges with one endpoint in $C$ to another in $V \setminus C$. So, 
$$
\sum_{v \in C} \deg(v) = 3|C|
$$
By [[Handshake Lemma]], 
$$
\sum_{v\in C} \deg(V) = 2|E(C)| + |\del(C)|
$$
such that 
$$
\begin{aligned}
3|C| &= 2|E(C)| + |\del(C)| \\
|\del(C)| &= 3|C| - 2|E(C)| \\
|\del(C)| &\equiv (3|C| - 2|E(C)|) \bmod 2 \\
&\equiv 3|C| \bmod 2 \\
&\equiv |C| \bmod 2 \\
&\equiv 1 \bmod 2 \\
\end{aligned}
$$
where as $3|C|$ is odd, $|\del(C)|$ is odd.
## Corollary (Peterson: Minimum Outbound Edges)
For odd $C \subseteq V, |\del(C)| \geq 3$. In particular, $|\del(C)|$ must  be odd, so it cannot be $2$. But $G$ is bridgeless, so it cannot be $1$. Thus it must be at least $3$.

## Peterson's Theorem Proof:
We can now apply [[#Tutte's Theorem]]. 

Assume for sake of contradiction that there was no perfect matching. Then $\exists S$ where $|S| < \Omega(G - S)$. Each of the vertices in $S$ to the odd components $C_{1}, \dots, C_{k}$ have degree at most $3$. 

For each $C_{i}$, it must have at least $3$ edges leaving the component. We get a sort of bipartite graph between $S$ and $C_{i}$. By the [[Bipartite Handshake Lemma]], 
$$
\begin{aligned}
3\Omega(G - S) \leq \sum_{v \in C_{i}} \deg(v) &= \sum_{v \in S} \deg(v) \leq 3|S| \\
\Omega(G - S) &\leq |S|
\end{aligned}
$$
which is a contradiction. Therefore there must be a perfect match. 

