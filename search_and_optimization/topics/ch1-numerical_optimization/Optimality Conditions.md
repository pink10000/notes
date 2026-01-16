---
tags:
  - CSE_257
---
# Theorem (First-Order Optimality Condition)
If $x$ is a [[Local Minima]], then $\nabla f(x) = \vec{0}$. 

Proof: 

If by contradiction that $\nabla f(x) \neq \vec{0}$, then $\forall \vepsi > 0$, $\exists y \in N_{\vepsi}(x)$ such that $f(x) > f(y)$. Thus $x$ cannot be a local minima, a contradiction. 

# Theorem (Second-Order Optimality Condition)
If $x$ is a [[Local Minima]], then $\nabla^{2}f(x) \succeq 0$. In particular, this means $\nabla^{2} f$ is [[Definite Matrix#Definition (Positive Semi-definite)|positive semidefinite]]. 

## Theorem (Second-Order Optimality Sufficiency)
The prior theorem only showed necessity. We can show the reverse direction (sufficient).

If $\nabla f = \vec{0}$ and $\nabla^{2} f(x) \succ 0$ (or that the Hessian is [[Definite Matrix#Definition (Positive Definite)|positive definite]]) then $x$ is a local minimum. In particular, note that it is not a necessary and sufficient condition because $\nabla^{2}f$ can be semidefinite. 