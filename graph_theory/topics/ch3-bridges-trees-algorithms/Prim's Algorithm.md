---
tags:
  - MATH_154
---
# Definition (Prim's Algorithm)
This algorithm generates the [[Minimum Spanning Tree|MST]] for any [[Graph]] $G$. 

Pick some vertex $v$. Let $T$ be our [[Minimum Spanning Tree|MST]]. While $T$ does not connect, in [[Graph]] $G$, find the [[Weighted Graph|lightest]] edge that connects $v$ to the new vertex and add it to $G$.