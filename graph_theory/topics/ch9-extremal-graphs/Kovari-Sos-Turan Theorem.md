---
tags:
  - MATH_154
---
This theorem discusses [[Extremal Graph|extremal graphs]] for $\text{ex}(n, K_{r,s})$. In particular, we explore when $F$ is bipartite, as an extension of [[Extremal Graph#Bipartite Dichotomy]]. 
# Lemma (Discrete Jensen's Inequality)
Let $a_{1}, a_{2}, \dots, a_{n},r \in \Z_{+}$ and let 
$$
a = \frac{1}{n} \sum_{i=1}^{n} a_{i}
$$
If $a \geq r - 1$ then 
$$
n\binom{a}{r} \leq \sum_{i=1}^{n} \binom{a_{i}}{n}
$$

Proof: This is a special case of [Jensen's Inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality). Note that in Verstraete, the lemma is written wrong. Source: Kane.
# Kovari-Sos-Turan Theorem
The theorem states that 
$$
\text{ex}(n, K_{r,s}) \leq 
\left( \frac{s - 1}{2} \right)^{1/r} n^{2 - \frac{1}{r}} + \frac{(r - 1)n}{2}
$$
for [[Bipartite Graph#Definition (Complete Bipartite Graph)|complete bipartite graph]] $K_{r,s}$ and $r,s \in \Z_{+}$. As $n \to \infty$, then the left term will increase more than the right term. Then approximately it will be $n^{2- \frac{1}{r}}$. In particular, this is $<\!\!< n^{2}$. 

Proof: 

Let $G$ be an $n-$vertex graph not containing $K_{r,s}$. If $|E(G)| \leq (r - 1)n/2$ then we are done, so assume otherwise. For $n$ vertices, we have $\binom{n}{r}$ total $r-$tuples. If we named the vertices $\Z_{1\to n}$, and let $a_{v} = \deg(v)$, then there are exactly $\binom{a_{v}}{r}$ sets of size $r$ in $N(v)$. 

Thus, the total number of sets of size $r$ in the neighborhood of some vertex is
$$
\sum_{i=1}^{n} \binom{a_{v}}{r}
$$
In particular, we have counted up the total number of *star graphs* in $G$. We may have counted some sets of size $r$ more than once. However, no set of size $r$ could have been counted at least $s$ times. Otherwise, that particular set of size $r$ would be in the neighborhood of $s$ vertices in $V(G)$, and that would resolve $K_{r,s}$. Thus, 
$$
\sum_{i=1}^{n} \binom{a_{v}}{r} \leq (s - 1)\binom{n}{r}
$$
The RHS represents our "forbidden subgraph". By applying [[#Lemma (Discrete Jensen's Inequality)]], with 
$$
a = \frac{2|E(G)|}{n} \geq r - 1
$$
by [[Handshake Lemma]], we get 
$$
n\binom{a}{r} \leq (s - 1) \binom{n}{r}
$$
The goal now is to separate $a$ from the binomial, where $|E(G)|$ is trapped in. Unfortunate!

We use the fact that for $x \geq r$, 
$$
\frac{(x - r)^{r}}{r!} \geq \binom{x}{r} = \frac{ x(x - 1) \dots (x - r + 1) }{r!}
\geq \frac{(x - r + 1)^{r}}{r!}
$$
> In Verstraete, the inequalities are flipped, which I'm pretty sure is not correct. In particular, let $x = 5, r = 2$. 

and that 
$$
\binom{n}{r} \leq \frac{n^{r}}{r!}
$$
so that 
$$
n \frac{(a - r + 1)^{r}}{r!} \leq (s - 1)\frac{n^{r}}{r!}
$$
This tells us that 
$$
(an - (r - 1)n)^{r} \leq (s - 1)n^{2r - 1}
$$
and since $an = 2|E(G)|$, then 
$$
|E(G)| \leq
\left( \frac{s - 1}{2} \right)^{1/r} n^{2 - \frac{1}{r}} + \frac{(r - 1)n}{2}
$$
and the proof is complete. 