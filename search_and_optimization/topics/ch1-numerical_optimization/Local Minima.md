---
tags:
  - CSE_257
---
# Definition (Local Minima)
Let $f: \R^{n} \to \R$ be a real-valued function. The **weak local minima** is defined by the **weak** local minimizer
$$
(\exists \vepsi > 0)\bigg(y \in N_{\vepsi}(x) \implies f(x) \leq f(y) \bigg)
$$
for some $\vepsi$ [[Metric Space#Neighborhood|neighborhood]][^1] around $x$. See [[Derivative#Definition (Local Maximum/Minimum)|here]] for a more rigorous definition. The **strong local minima** is defined by the **strict/strong** local minimizer:
$$
(\exists \vepsi > 0)\bigg( y \in N_{\vepsi}(x) \wedge x \neq y \implies f(x) < f(y) \bigg)
$$
In a [[Level Set]], the local minima is one point (or a set of single points).

> In class, it is defined slightly differently but they are logically equivalent.  


---
[^1]: For the purposes of this class, a neighborhood is the set of points no more than $\vepsi$ distance from some chosen point $x$. Distance is measured by the Euclidean norm. Sometimes the notation $B(x, \vepsi)$ is used, but they mean the same thing. In $\R^{2}$, $B(x, \vepsi)$ is a filled circle. In $\R^{3}$, $B(x, \vepsi)$ is a solid sphere. 