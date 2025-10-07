---
tags:
  - MATH_190A
---
# Definition (Zariski Topology)
In algebraic topology, we use the **Zariski Topology** where the [[Metric Space#Open & Closed|open sets]] are the *complements* of the zero-sets (sets where the polynomial vanishes) of the polynomial function. 

In particular, when $X = \R$, the open sets are just the complements of the finite subsets of $\R$. This is also called **cofinite** topology on $\R$. 

## Lemma (Arbitrary Unions/Intersections of Cofinite Sets)
Let $X$ be infinite, and $A, B$ be finite. Then $(X - A)$ and $(X - B)$ are cofinite. Then, 
$$
\begin{aligned}
(X - A) \cup (X - B) &= X - (A \cap B) \\
(X - A) \cap (B - B) &= X - (A \cup B)
\end{aligned}
$$
