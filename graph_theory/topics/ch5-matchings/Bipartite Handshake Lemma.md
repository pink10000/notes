---
tags:
  - MATH_154
---
# Bipartite Handshake Lemma
Let $G = (L, R, E)$ where $L \cup R$ are its vertex set. Then, 
$$
\sum_{v\in L} \deg(v) = \sum_{v \in R} \deg(v) = |E|
$$
Proof: 

We know that each edge in a bipartite graph connects a vertex in $L$ to $R$. Thus, for each edge it has one endpoint in $L$. But then as $\sum_{v \in L} \deg(v)$ counts the edges with endpoints in $L$, then
$$
\sum_{v \in L} \deg(v) = |E|
$$
Likewise, as each edge has an endpoint in $R$,
$$
\sum_{v \in R} \deg(v) = |E|
$$
and so
$$
|E| = \sum_{v \in L} \deg(v) = \sum_{v \in R} \deg(v)
$$
> Related: [[Handshake Lemma]], [[Face Handshake Lemma]].