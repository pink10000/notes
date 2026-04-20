---
tags:
  - CSE_291G
---
# Square Matrices
These are matrices over some field $\mathbb{F}$ of size $n \times n$. There are exactly 2 types of square matrices: endomorphisms and bilinear forms.

# Theorem (Operations on Square Matrices)
You can view [[Eigenvector|eigenvalues]], [[Trace|trace]], and the [[Determinant|determinant]]. 

# Definition (Endomorphisms)
[[Dual Space#Definition (Linear Map)|Linear Maps]] from $V$ to itself are called **endomorphisms**. 
$$
\text{End}(V) = \left\{f: V \xrightarrow{\text{ linear}} V\right\}
$$
Via index notation, we use $A_i^j$ to denote the matrix representation of an endomorphism.

# Definition (Bilinear Forms)
A **bilinear form** on $V$ are linear maps $B: V \to V^*$. A bilinear form works like 
$$
\underbrace{B(u)}_{\in V^*}(v)
$$
like a bilinear function on $V$. Via index notation, we use $B_{ij}$ to denote the matrix representation of a bilinear form.

# Remark (Endomorphisms vs Bilinear Forms)
Operations on matrices such as taking trace, determinant, and eigenvalues; or properties of being identity, etc. makes sense only for endomorphisms. 

Eigenvalues, trace, and determinants of $A_1 A_2 \dots A_k$ is invariant under cyclic permutations of the $A_i$'s. 
$$
\text{tr}(A_1 A_2 \dots A_k) = \text{tr}(A_k A_1 A_2 \dots A_{k-1}) = \cdots
$$

## Remark
Properties on matrices such as being symmetric (self-[[Dual Space#Definition (Adjoint Linear Map)|adjoint]]) makes sense only for bilinear forms.
$$
B \in \left(
  V \xrightarrow{\text{ linear}} V^*
\right)
\implies 
B^T \in \left(
  V^{**} \xrightarrow{\text{ linear}} V^*
\right)
$$
where $V^{**}$ is simply $V$. So, $B, B^T$ are of the same type. 

# Definition (Symmetric Bilinear Forms)
A bilinear form $B$ is **symmetric** if $B = B^T$. This is the same as $B(u)(v) = B(v)(u)$ or $B_{ij} = B_{ji}$.

## Theorem (Symmetric Bilinear Forms and Quadratic Forms)
There is a one-to-one correspondence between symmetric bilinear forms and quadratic forms. 
- From symmetric to quadratic: $q(u) = B(u)(u)$.
- From quadratic to symmetric: $q(u + v) = q(u) + q(v) + 2B(u)(v)$

# Definition (Positive Definite)
A symmetric bilinear form is [[Definite Matrix|positive definite]] if its quadratic form takes positive values $q(u) > 0$ for all $u \neq 0$.

# Definition (Inner Product Structure or Metric)
An **inner product structure** or [[Metric Space#Definition|metric]] on $V$ is a positive definite symmetric bilinear form. It is often denoted by $g_{ij}$ or $\flat_{ij}$, the flat operator.
$$
g(u, v) = \langle u, v \rangle = \langle \flat u | v \rangle
$$

There are infinitely many choices for a metric on $V$. That is, for a plain [[Vector Space|vector space]], there is no canonical choice of metric. The metric (as any bilinear form) is a map from vectors to covectors, so the flat operator is known as **index-lowering operator**. 
$$
(\flat u)_i = \flat_{ij} u^j
$$
- The flat operator is invertible (due to positive-definiteness). 
- The inverse of the flat operator is known as the **index-raising operator** or **sharp operator** $\sharp = \flat^{-1}$.
$$
\left(\sharp \alpha\right)^i = \sharp^{ij} \alpha_j
$$
Via index notation, the label is $g^{ij} = (g^{-1})^{ij}$.

In particular, an inner product structure $\flat : V \to V^*$ can turn vectors to covectors and vice versa with the inverse $\sharp : V^* \to V$. Geometrically, we can draw a quadratic surface with some vector $\vec{v}$. The covector is then the hyperplane $\vec{v}^{\flat}$ where $\flat(\vec{v})(\vec{v}) = 1$ denotes the unit sphere. The vectors are the tangent vectors to the surface. We construct the *polar* plane across the quadric surface. 