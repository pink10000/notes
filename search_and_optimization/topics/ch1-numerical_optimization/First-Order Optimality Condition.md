---
tags:
  - CSE_257
---
# Theorem (Local Minima gives Zero Gradient)
If $x$ is a [[Local Minima]], then $\nabla f(x) = \vec{0}$. 

Proof: 

If by contradiction that $\nabla f(x) \neq \vec{0}$, then $\forall \vepsi > 0$, $\exists y \in N_{\vepsi}(x)$ such that $f(x) > f(y)$. Thus $x$ cannot be a local minima, a contradiction. 