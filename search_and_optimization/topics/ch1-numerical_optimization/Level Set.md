---
tags:
  - CSE_257
---
# Definition (Level Set)
Let $f: \R^{n} \to \R$ be sufficiently [[Derivative#Higher Derivatives|differentiable]]. The **Level Set** at some constant $c \in \R$, is defined as 
$$
L_{f}(c) = \{ x \in \text{dom}(f) \,|\, f(x) = c \}
$$
where $\text{dom}(f)$ is the domain of $f$. 

# Theorem (Level Sets are Orthogonal with Gradients)
Level sets are always orthogonal to [[Gradient|gradients]]. In particular, if $r(t)$ is a curve that lies entirely within the level set $L_{f}(c)$ for some $c \in \R$, then for any point $x = r(t)$ on that curve,
$$
\nabla f(x) \cdot r'(t) = \vec{0}
$$
where $r'(t)$ is the tangent direction along that level set. One important thing to note is that $\Delta f(x) \neq \vec{0}$.