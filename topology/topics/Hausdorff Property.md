---
tags:
  - MATH_190A
---
# Definition (Hausdorff Property)
A space $(X, \tau)$ is **Hausdorff** if $\forall x \neq y$ in $X$, there exist open sets $U,V$ where $x \in U, y \in V$ which are disjoint.

We say $U,V$ are **"housed off"** from one another. 
# Theorem (Metric Spaces are Hausdorff)
Any [[Metric Space]] is Hausdorff. 

Proof:
For any $x \neq y \in X$, then $0 < d(x, y)$. But then we can define
$$
B_{d(x, y)/3}(x) 
\quad\quad\quad
B_{d(x, y)/3}(y)
$$
such that
$$
B_{d(x,y)/3}(x) \cap B_{d(x,y)/3}(y) = \varnothing
$$
If $\exists z$ is the intersection, the triangle inequality would be contradicted. 

# Theorem (Unique Limit in Hausdorff)
In a Hausdorff space, a [[Topological Sequence]] can have at most one limit. 

Proof. 
If $(x_{n}) \to x$ and $y$ where $x \neq y$, we can separate them by open $x \in U, y \in V$ such that $U \cap V = \varnothing$. We can then find $N,M$ such that 
$$
\forall n \geq N, x_{n}\in U
\quad\quad\quad
\forall m \geq M, x_{m}\in V
$$
which is a contradiction when $n > \max(N, M)$. 

