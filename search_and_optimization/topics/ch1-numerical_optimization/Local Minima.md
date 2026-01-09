---
tags:
  - CSE_257
---
# Definition (Local Minima)
Let $f: \R^{n} \to \R$ be a real-valued function. The **weak local minima** is defined by the **weak** local minimizer
$$
(\exists \vepsi > 0)\bigg(y \in N_{\vepsi}(x) \implies f(x) \leq f(y) \bigg)
$$
for some $\vepsi$ [[Metric Space#Neighborhood|neighborhood]] around $x$. See [[Derivative#Definition (Local Maximum/Minimum)|here]] for a more rigorous definition. The **strong local minima** is defined by the **strict/strong** local minimizer:
$$
(\exists \vepsi > 0)\bigg( y \in N_{\vepsi}(x) \wedge x \neq y \implies f(x) < f(y) \bigg)
$$

