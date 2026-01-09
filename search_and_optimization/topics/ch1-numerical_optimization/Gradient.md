---
tags:
  - CSE_257
---
# Definition (Gradient)
Let $f: \R^{n} \to \R$ be sufficiently [[Derivative#Higher Derivatives|differentiable]]. The **Gradient** at $x \in \R^{n}$ is defined as 
$$
\nabla f(x) = \left[ \frac{\del f}{\del x_{1}}, \dots, \frac{\del f}{\del x_{n}} \right]^{T}
$$
for each component $x_{i}$ of $f$. 

# First-Order Taylor Expansion
Optimization algorithms use the following expansion to predict how the function value will change if we move a tiny amount in a certain direction (which is $\Delta x$). 
$$
f(x + \Delta x) = f(x) + \nabla f(x)^{T} \Delta(x) + O(||\Delta x||_{2}^{2})
$$
which is essentially linear approximation but in $\R^{n}$. 
> Recall how we do linear approximation for some simple curve in $\R^{2}$:
> $$
> f(x + \Delta x) = f(x) + \frac{d}{dx}[f(x)] \cdot \Delta x
> $$

The [[Taylor's Theorem|Taylor Expansion]] generalizes the tangent line into $n$ dimensions. The $O(||\Delta x ||_{2}^{2})$ term is essentially the remainder of the rest of the terms of the Taylor [[Series]]. As $\Delta x \to 0$, then the $O \to 0$. In **first-order optimization**, we assume $\Delta x$ is so small, that $\Delta x^{2}$ is essentially negligible. 

From the previous equation, by the Multivariate [[Derivative#Theorem (Lagrange Mean Value Theorem)|MVT]][^1] we get 
$$
\begin{aligned}
f(x + \Delta x) 
&= f(x) + \nabla f(x)^{T} \Delta(x) + O(||\Delta x||_{2}^{2}) \\
&= f(x) + \nabla f(x + t\Delta x)^{T} \Delta x  
\end{aligned}
$$
for some $t \in (0, 1)$. The last line needs some more justification. Let 
$$
g(t) = f(x + t\Delta x) \quad\quad\quad [0, 1] \to \R
$$
such that when $t = 0, g(0) = f(x)$ and $t = 1, g(1) = f(x + \Delta x)$. By applying MVT on this parameterized curve, 
$$
g(1) - g(0) = g'(t) \cdot (1 - 0)
$$
for some $t \in (0, 1)$. But $g'(t)$ is calculated via Chain Rule, it becomes the gradient of $f$ at that middle point.
$$
g'(t) = \nabla f(x + t\Delta x) \cdot \Delta x = \nabla f(x + t\Delta x)^{T} \Delta x
$$
and by substitution, 
$$
f(x + \Delta x) - f(x) = \nabla f(x + t\Delta x)^{T} \Delta x
$$
which is our desired result. 


[^1]: See these [notes](https://links.uwaterloo.ca/amath731docs/meanvalue.pdf) for more information about the Generalized Mean Value Theorem for multivariate real-valued functions. 