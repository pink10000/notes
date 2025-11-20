---
tags:
  - MATH_154
---
# Konig's Theorem
For a finite [[Bipartite Graph|bipartite]] [[Graph|graph]], the size of the maximum [[Matching|matching]] is *equal* to the size of the minimum [[Vertex Cover|vertex cover]]. 

Proof:

Let $M$ be the maximum matching and $S$ be the minimum vertex cover. From [[Vertex Cover#Lemma (Maximum Matching Bound)|lemma]], we have that $|M|\leq |S|$. We want to show that $|M| \geq k$ unless $\exists$ a vertex cover $S < k$. 

What if $k = |L|$? In this case, [[Hall's Theorem]] says there is a matching of size $k$, unless there is some $S \subset L$ such that $|S| > |N(S)|$. Suppose this happens. This gives us a nice vertex cover:
$$
T := (L - S) \cup N(S)
$$
Indeed, let $e = (u, v)$, where $u \in L, v \in R$ (since it is bipartite!). If $u \not \in S$ then $u \in L \setminus S \subseteq T$. If $u \in S$, then for $v \in N(S), v \in T$. Thus, 
$$
|T| = |L| - |S| + |N(S)| < |L| = k
$$
Since $|S| > |N(S)| \implies 0 > |N(S)| - |S|$. Let $U$ be the set of unmatched vertices in $S$. So,
$$
|S| = |U| + |N(S)| \implies |N(S)| = |S| - |U|
$$
where substituting, gives us
$$
|T| = |L| - |U|
$$
where RHS is simply $|M|$, the number of matched vertices. 

