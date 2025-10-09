---
tags:
  - MATH_190A
aliases:
  - homeomorphism
---
This note is separate from [[Homeomorphisms]] from analysis. This note is primarily for MATH 190A, since we're going to use it differently. Largely, they are the same. 

# Definition (Topological Homeomorphism)
A **homeomorphism** $(X, \tau_{X}) \to (Y, \tau_{Y})$ is a map that is 
- continuous
- bijective
- its inverse is continuous

We say $X \cong Y$ to mean $X$ is homeomorphic to $Y$.

Equivalently, we say two spaces, $(X, \tau_{X})$ and $(Y, \tau_{Y})$ are **homeomorphic** if $\exists$ mutually inverse continuous maps. Precisely,
$$
(X, \tau_{X}) \xrightleftarrows{g}{f} (Y, \tau_{Y})
$$
where
$$
f \circ g = \id_{X} 
\quad\quad\quad
g \circ f = \id_{Y}
$$
## Example 1:
We have $(-1, 1)$ and $\R$ are homeomorphic. 

Proof:
We could use $f(x) = \tan( \pi x/ 2 )$, with inverse being $g(y) = 2\tan^{-1}(y)/\pi$. 

## Example 2:
$$
f(x) = \frac{x}{1 - x^{2}}
$$
is homeomorphic with inverse
$$
g(y) = \frac{2y}{1 + \sqrt{1 + 4y^{2}}}
$$
We assert both are continuous by [[Topological Continuity#Theorem (Continuity by Composition in a Topology)]]. 
## Example 3 (Non-example):
Consider 
$$
\begin{aligned}
f : [0, 1) &\to S = \{x^{2}+ y^{2} = 1\} \subset \R^{2} \\
x &\mapsto (\cos 2\pi x, \sin 2 \pi x)
\end{aligned}
$$
This map is a continuous bijection, but its inverse is not. In particular, the $f$ is not an *open map*. 
