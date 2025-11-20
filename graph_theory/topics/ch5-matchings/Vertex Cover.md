---
tags:
  - MATH_154
---
# Definition (Vertex Cover)
For a graph $G$, a **vertex cover** is a set $S \subset V$ such that every edge in $G(E)$ is incident on some vertex in $S$. 


# Lemma (Maximum Matching Bound)
The size of the *maximum* [[Matching]] is at most the size of the *minimum* vertex cover. 

Proof: If we matching $M$ and a vertex cover $S$, then each edge $e \in M$ must be incident on some $v \in S$. On the other hand, each $e \in M$ must be incident on a distinct $v \in S$ (because it is a matching). Thus, for $e \in M$, we can pick a unique $v \in S$, giving us an injective map from $M \to S$, implying $|M| \leq |S|$.  