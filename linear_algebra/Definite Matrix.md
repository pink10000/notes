---
tags:
  - CSE_257
  - CSE_291G
---
# Definition (Positive Definite Matrix)
A matrix $M \in \R^{n \times n}$ is called **positive definite** iff $\forall \vec{x}\in \R^{n}, \vec{x}^{T}M\vec{x} > 0$. We denote this property by $M \succ 0$. 

# Definition (Positive Semi-definite Matrix)
A matrix $M \in \R^{n \times n}$ is called **positive semi-definite** iff $\forall \vec{x}\in \R^{n}, \vec{x}^{T}M\vec{x} \geq 0$. We denote this property as $M \succeq 0$.

# Connection to Bilinear Forms
A symmetric bilinear form $B : V \times V \to \R$ is **positive definite** if its corresponding quadratic form $q(u) = B(u)(u)$ satisfies $q(u) > 0$ for all $u \neq 0$. In a given basis, this is equivalent to its matrix representation being positive definite.
