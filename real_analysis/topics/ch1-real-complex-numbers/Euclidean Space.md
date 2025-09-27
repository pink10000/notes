---
tags:
  - MATH_140A
  - real_analysis_ch1
---
Let $n \in \N$ and define 
$$
\R^{n} = \{(x_{1}, \cdots, x_{n} \mid x_{j}\in \R\}
$$
where $\vec{x}$ or $\mathbf{x}$ is denoted as an element in it. We have some properties:
- Addition is kept from $\R$ 
- Multiplication by scalar. For $a \in \R, \vec{x} \in \R^{n}$ we have $a\vec{x} = (ax_{1}, \cdots, ax_{n})$.
- We keep commutativity, associativity, distributive laws, etc. 

# Euclidean Space

## Vector Space
> **Note**: $(x) = (x_{1}, \dots, x_{k})$ is a vector.

An inner product $\langle \vec{x}, \vec{y} \rangle : \R^{k} \times \R^{k} \to \R$ for $\vec{x}, \vec{y} \in \R^{k}$ is defined as  
$$
\langle \vec{x}, \vec{y} \rangle = \vec{x} \cdot \vec{y}= x_{1}y_{1} + x_{2}y_{2} + \dots + x_{k}y_{k}  
$$

The **norm** (length) of a vector is $||\vec{x}|| = \sqrt{\langle \vec{x}, \vec{x}\rangle}$. For $\R^{k}$, we have:

1. $\langle \vec{x}, \vec{y} \rangle = \langle \vec{y}, \vec{x}\rangle$ 
2. $\langle a\vec{x} + b\vec{y}, \vec{z} \rangle = a\langle \vec{x}, \vec{z} \rangle + b\langle \vec{y}, \vec{z} \rangle$
3. [Cauchy-Schwarz Inequality](../ch1-real-complex-numbers/Complex%20Numbers.md#cauchy-schwarz-inequality): So, $|\vec{x}\vec{y}| \leq ||\vec{x}|| \cdots ||\vec{y}||$
4. [Triangle Inequality](../ch1-real-complex-numbers/Complex%20Numbers.md#triangle-inequality): $||\vec{x} + \vec{y}|| \leq ||\vec{x}|| + ||\vec{y}||$
5. $||\vec{x} - \vec{y}|| \geq | ||\vec{x}|| - ||\vec{y}|| |$

We see that $1,2$ is trivial and $3$ is just [Cauchy-Schwarz](../ch1-real-complex-numbers/Complex%20Numbers.md#cauchy-schwarz-inequality). Assume $4$. We prove $5$. We note that 
$$
x - y = (x - z) + (z - y)
$$
so, with $4$, we get
$$
\begin{aligned}
||x - y|| 
&\leq ||x - z|| + ||z - y|| \\
&= ||x - z|| + ||-(y - z)|| \\
&=_{2}||x - z|| + |-1|\cdot ||y - z|| \\
&= ||x - z|| + ||y - z|| \\
\end{aligned}
$$
Now, we prove $4$. Let $\vec{x} = (x_{1}, \cdots x_{n})$ and $\vec{y} = (y_{1}, \cdots y_{n})$.  Because both sides are positive, it suffices to show
$$
||\vec{x} + \vec{y}||^{2} \leq (||\vec{x}|| + ||\vec{y}||)^{2}
$$
Then
$$
\begin{aligned}
||x + y||^{2}
&= \sum_{i=1}^{n}(x_{i}+y_{i})^{2} \\
&= \sum_{i=1}^{n} \left(x_{i}^{2}+ 2x_{i}y_{i}+ y_{i}^{2}  \right) \\
&= \sum_{i=1}^{n} x_{i}^{2}+ \sum x_{i}y_{i} + \sum y_{i}^{2} \\
&= ||x||^{2}+ 2xy + ||y||^{2}
\end{aligned}
$$
Now, by [Cauchy-Schwarz](../ch1-real-complex-numbers/Complex%20Numbers.md#cauchy-schwarz-inequality), we have that $|xy| \leq ||x|| \cdot ||y||$, in which replacement of the middle term gives us:
$$
\begin{aligned}
&\leq ||x||^{2}+ 2||x|| \cdot ||y|| + ||y||^{2} \\
&= (||x|| + ||y||)^{2} \\
\end{aligned}
$$
And the proof is done. 