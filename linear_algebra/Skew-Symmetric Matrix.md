---
tags:
  - CSE_291G
  - MATH_100B
---
# Skew-Symmetric Matrix
A square matrix $\mathbf{A}$ is **skew-symmetric** (or **antisymmetric**) if its transpose is its negative:
$$
\mathbf{A}^\top = -\mathbf{A}
$$
In terms of its entries $a_{ij}$, this means $a_{ji} = -a_{ij}$ for all $i, j$.

# Properties
- **Zero Diagonal**: The diagonal elements of a skew-symmetric matrix must be zero, as $a_{ii} = -a_{ii} \implies a_{ii} = 0$.
- **Quadratic Form**: For any vector $\mathbf{x}$, the quadratic form associated with a skew-symmetric matrix is zero:
  $$
  \mathbf{x}^\top \mathbf{A} \mathbf{x} = 0
  $$
- **Eigenvalues**: The eigenvalues of a real skew-symmetric matrix are either zero or purely imaginary.
- **Trace**: The trace of a skew-symmetric matrix is always zero.
- **Lie Algebra**: The set of all $n \times n$ skew-symmetric matrices forms the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group $O(n)$ and the special orthogonal group $\SO(n)$.

# 3D Case: The Hat Map
In 3D [[Euclidean Space]], there is a one-to-one correspondence between vectors in $\R^3$ and $3 \times 3$ skew-symmetric matrices. For a vector $\boldsymbol{\omega} = (\omega_1, \omega_2, \omega_3)^\top$, we define the **hat map** $[\cdot]_\times : \R^3 \to \SO(3)$ as:
$$
[\boldsymbol{\omega}]_\times = \hat{\boldsymbol{\omega}} = \begin{bmatrix}
0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{bmatrix}
$$
It can also be denoted as $[\mathbf{\omega} \times]$.
## Relation to Cross Product
The skew-symmetric matrix $[\boldsymbol{\omega}]_\times$ represents the cross product operation with $\boldsymbol{\omega}$. For any vector $\mathbf{v} \in \R^3$:
$$
[\boldsymbol{\omega}]_\times \mathbf{v} = \boldsymbol{\omega} \times \mathbf{v}
$$

# Application in Rigid Body Dynamics
In [[phys_sim/Rigid Body Dynamics|rigid body dynamics]], skew-symmetric matrices are used to represent angular velocity. If $\mathbf{R}(t)$ is a rotation matrix, then its derivative $\dot{\mathbf{R}}(t)$ satisfies:
$$
\dot{\mathbf{R}} = [\boldsymbol{\omega}_s]_\times \mathbf{R} = \mathbf{R} [\boldsymbol{\omega}_b]_\times
$$
where $\boldsymbol{\omega}_s$ is the spatial angular velocity and $\boldsymbol{\omega}_b$ is the body angular velocity. The matrix $\mathbf{R}^\top \dot{\mathbf{R}}$ is always skew-symmetric.

# Theorem (Skew-Symmetric Transpose Multiplication)
Let $a$ be a vector in $\R^3$ and $[a]_\times$ be the corresponding skew-symmetric matrix. Then:
$$
[a]_\times^\top [a]_\times = |a|^2 I - a a^\top
$$

Proof:

First, recall that $[a]_\times^\top = -[a]_\times$. Thus, $[a]_\times^\top [a]_\times = -[a]_\times^2$.

We compute $[a]_\times^2$ by direct matrix multiplication:
$$
\begin{aligned}
% 
[a]_\times^2 
&= \begin{bmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{bmatrix} \begin{bmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{bmatrix} \\
&= \begin{bmatrix} -(a_2^2 + a_3^2) & a_1 a_2 & a_1 a_3 \\ a_1 a_2 & -(a_1^2 + a_3^2) & a_2 a_3 \\ a_1 a_3 & a_2 a_3 & -(a_1^2 + a_2^2) \end{bmatrix}
\end{aligned}
$$
Note that $|a|^2 = a_1^2 + a_2^2 + a_3^2$. We can rewrite the diagonal elements as 
$$
-(a_2^2 + a_3^2) = a_1^2 - |a|^2
$$
and so on:
$$
\begin{aligned}
% 
[a]_\times^2 
&= \begin{bmatrix} a_1^2 - |a|^2 & a_1 a_2 & a_1 a_3 \\ a_1 a_2 & a_2^2 - |a|^2 & a_2 a_3 \\ a_1 a_3 & a_2 a_3 & a_3^2 - |a|^2 \end{bmatrix} \\
&= \begin{bmatrix} a_1^2 & a_1 a_2 & a_1 a_3 \\ a_1 a_2 & a_2^2 & a_2 a_3 \\ a_1 a_3 & a_2 a_3 & a_3^2 \end{bmatrix} - |a|^2 \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \\
&= a a^\top - |a|^2 I
\end{aligned}
$$
Therefore, $[a]_\times^\top [a]_\times = -[a]_\times^2 = |a|^2 I - a a^\top$.
