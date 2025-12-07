---
tags:
  - MATH_154
---
# Erdos-Gallai Theorem 
If we want the [[Extremal Graph]] number for [[Path]] $P_{k}$ (path with $k$ edges, or $k+1$ vertices), then it is at most $(k-1)n/2$. 

This bound is *almost* tight. It will be tight if $n$ is a multiple of $k$. We can have $G$ be a union of [[Complete Graph|complete graphs]] $K_{k}$. If that happens, the as all the [[Connectivity|connected components]] of size $k$, we will never have a connected subgraph with $k + 1$ vertices. Then by [[Handshake Lemma]] and that $G$ is $(k-1)$-regular, there are $(k-1)n/2$ edges.  

Also recall that the extremal graph need not be connected. We are simply trying to maximize the number of edges. 

Proof: 

Let $G$ be an $n-$vertex graph with at least $(k - 1)n/2$ edges. We prove by strong induction on $n + k$ that $G$ contains $P_{k}$ unless every component of $G$ is $K_{k}$. 

If $G$ is disconnected, then we can examine each piece individually. Suppose some component of $G$ contains a path of length $k$ or equals $K_{k}$. We remove it and get a graph with $n - k$ vertices with the following edges:
$$
\frac{(k - 1)n}{2} - \frac{k(k-1)}{2}
=
\frac{(k - 1)(n - k)}{2}
$$
edges. By induction, that graph is a union of $K_{k}$ or contains a path of length $k$, and we are done. 

Therefore we can assume $G$ is connected. If $k = 1$,  then a single edge forms $P_{1}$. If there are no edges, then every component is $K_{1}$. Let $k \geq 2$. If $G$ contains a vertex $v$ degree less than $k/2$, then $G' = G - \{v\}$ has at least 
$$
|E(G')| > 
\frac{(k - 1)n}{2} - \frac{k}{2} = 
\frac{(k - 1)(n - 1)}{2}
$$
edges remaining. Since $G'$ still has enough edges, by induction it must contain a path $P_{k}$ or be a union of $K_{k}$. Since $G' \subset G$, then the same holds for $G$. 

Thus, $\delta(G) \geq k/2$. By induction, $G$ contains a path $P$ of length $k - 1$. Let this be from $u \to w$. All $N(u), N(v) \subseteq P$, otherwise we could just extend the path $P$ and be done. By [[Hamiltonian Path#Lemma (Force a Cycle by Minimum Degree)|lemma]][^1], we have a cycle $C$ of length $k$ containing $P$. 
[^1]: This is also known as **Dirac's Theorem**.

If there is a vertex $x \not \in C$, and as $G$ is connected, there must be a path from $x \to C$, and in particular, adding edge $(w, x)$ with $w \in V(C)$, we get a path of length $k$ ending with $x$. Thus $V(C) = C(G)$ and so $|V(G)| = k$ and $G = K_{k}$ as required. 

> This proof is almost entirely copied verbatim from the Verstraete textbook. 

# Erdos-Gallai Conjecture 
If $T$ is any [[Tree]] with $k$ edges, then 
$$
\text{ex}(n, T) \leq \frac{(k - 1)n}{2}
$$
The above [[#Erdos-Gallai Theorem]] was used to prove this for paths specifically. 