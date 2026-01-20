---
tags:
  - CSE_257
---
If for some reason I take another linear algebra class, I'll move this file there. 
# Definition (Hessian Matrix)
Let $f : \R^{n} \to \R$. Recall that 
$$
\nabla = 
\begin{pmatrix}
\frac{\del}{\del x_{1}} \\ \frac{\del}{\del x_{2}} \\ \vdots \\ \frac{\del}{\del x_{n}}
\end{pmatrix}
$$
and that $\nabla f$ gives the [[Gradient]] of $f$. The **Hessian Matrix** denoted as $\mathbf{H}f$ is defined as $\nabla^{2}f$ or from a linear algebra perspective, $\nabla \nabla^{T}f$. In particular, 
$$
\mathbf{H}f
= \nabla \nabla^Tf
= \begin{pmatrix} 
\frac{\partial}{\partial x_1} \\ \vdots \\ \frac{\partial}{\partial x_N} \end{pmatrix} \begin{pmatrix} \frac{\partial f}{\partial x_1} & \ldots & \frac{\partial f}{\partial x_N} 
\end{pmatrix} 
= 
\begin{pmatrix} 
\frac{\partial^2 f}{\partial x_1^2} & \ldots & \frac{\partial^2 f}{\partial x_1 \partial x_N} \\ \vdots \\ \frac{\partial^2 f}{\partial x_N \partial x_1} & \ldots & \frac{\partial^2 f}{\partial x_N^2} \\ 
\end{pmatrix}
$$
describes the Hessian. In particular, we can describe $\mathbf{H}$ as a matrix in $\R^{n\times n}$. The Hessian describes the [second order mixed partials of a scalar field](https://math.stackexchange.com/a/3680709).

# Example 1 
Suppose $f :\R^{2} \to \R$. Then
$$
\nabla f = \left( f_{x}, f_{y} \right)^{T}
$$
and 
$$
\mathbf{H}f = 
\begin{bmatrix}
f_{xx} & f_{xy} \\
f_{yx} & f_{yx}
\end{bmatrix}
$$
Furthermore, $f_{xy}$ is equal to 
$$
\frac{\del^{2} f}{\del x \del y}
$$
and likewise with the other $3$ values. *Note the order*. 

# Hessian Intuitively
We can think of the Hessian operator as a *double-derivative* in the same way the [[Gradient]] or [[Jacobian]] is treated as a single derivative. Recall that the first derivative is no longer a scalar but rather a linear map (i.e. derivative of $f(x) = x^{2}$ is $2x$, a linear map). The second derivative is instead a *bilinear map*. 

Let $f : \R^{n} \to \R$ be a smooth function. The *first-derivative* 
$$
Df : \R^{n} \to L(\R^{n}, \R)
$$
is a smooth function from $\R^{n}$ to the set $L(\R^{n}, \R)$ of linear maps $\R^{n} \to \R$. From the example above, $2x$ is a map that is given from the derivative of $f$. We can do the same with Hessian 
$$
D^{2}f : \R^{n} \to L(\R^{n}, L(\R^{n}, \R))
$$
where the codomain is (trivially) isomorphic to the set of bilinear maps 
$$
\text{Bil}(\R^{n} \times \R^{n}, \R)
$$
But this is precisely what $H$ represents. It is a matrix operator in $\R^{n \times n}$. Similar to how double-derivatives model the concavity of a point on some curve/surface, $\mathbf{H}$ models the concavity of a hypersurface at a point.[^1] 

[^1]: See [this MSE post](https://math.stackexchange.com/a/3892335).