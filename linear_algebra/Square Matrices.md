---
tags:
  - MATH_100B
  - CSE_291G
---
# Square Matrices
These are matrices over some field $\mathbb{F}$ of size $n \times n$. There are exactly 2 types of square matrices: endomorphisms and bilinear forms.

## Remark (Connecting Vector and Dual Spaces to Matrices)
The conceptual leap in courses like Math 100B often comes down to moving between coordinate-free, abstract definitions and coordinate-dependent, concrete computations. Whether you are puzzling over these proofs in the library or mulling them over at a local spot in La Jolla, the trick to bridging this gap is always the same: you must explicitly introduce a basis.

Abstract linear maps, such as endomorphisms ($U \to U$) or bilinear forms ($U \to U^*$), are entirely coordinate-free until we give them a coordinate system. Once we do, these abstract maps perfectly collapse into standard square matrices.

Here is the exact mechanical breakdown of how that happens.

### 1. Set Up the Bases
Let $U$ be an $n$-dimensional vector space. To get a matrix, we first choose a basis for $U$:
$$
E = \{e_1, e_2, \dots, e_n\}
$$
Because we have a basis for $U$, we automatically get a strictly defined **dual basis** for the [[Dual Space|dual space]] $U^*$:
$$
E^* = \{e^1, e^2, \dots, e^n\}
$$
The defining rule of this dual basis is how it acts on the original basis vectors. It outputs $1$ if the indices match, and $0$ if they do not (the Kronecker delta):
$$
e^i(e_j) = \delta^i_j
$$

### 2. Map the Basis Vectors
We have two types of square matrices corresponding to our two maps. Let us see what they do to a single basis vector, $e_j$.

**For an Endomorphism ($A: U \to U$):**
The output $A(e_j)$ is a vector in $U$. Because $E$ is a basis for $U$, $A(e_j)$ can be written as a linear combination of the basis vectors. Let us call the scalar coefficients $A^i_j$:
$$
A(e_j) = \sum_{i=1}^n A^i_j e_i
$$

**For a Bilinear Form ($B: U \to U^*$):**
The output $B(e_j)$ is a covector in $U^*$. Because $E^*$ is a basis for $U^*$, $B(e_j)$ can be written as a linear combination of the dual basis vectors. Let us call the scalar coefficients $B_{ij}$:
$$
B(e_j) = \sum_{i=1}^n B_{ij} e^i
$$

By doing this for every basis vector $e_1$ through $e_n$, we generate an $n \times n$ grid of coefficients for both $A$ and $B$. That grid is your square matrix.

### 3. Evaluate the Map to Prove the Matrix
To see what those matrix entries actually mean, we evaluate the maps on a different basis vector, $e_i$.

**For Bilinear Forms:**
We take our covector $B(e_j)$ and evaluate it on $e_i$. Substituting the linear combination from Step 2:
$$
(B(e_j))(e_i) = \left( \sum_{k=1}^n B_{kj} e^k \right) (e_i)
$$
Because the evaluation of covectors is linear, we pull the sum and scalars out to the front:
$$
(B(e_j))(e_i) = \sum_{k=1}^n B_{kj} e^k(e_i)
$$
Applying the rule of the dual basis ($e^k(e_i) = \delta^k_i$), the sum collapses down to just one coefficient:
$$
(B(e_j))(e_i) = B_{ij}
$$

### 4. The Final Translation
For bilinear forms, evaluating the output of $B$ on a second vector is the definition of the bilinear form: $(B(e_j))(e_i)$ is identical to writing $B(e_i, e_j)$. Therefore:
$$
B_{ij} = B(e_i, e_j)
$$
This is the translation key. To build the square matrix $\mathbf{B}$ that represents $B: U \to U^*$, you evaluate the bilinear form on every possible pairing of your basis vectors. The scalar from $(e_1, e_2)$ goes into row 1, column 2, and so on.

If the tensor is symmetric ($B^* = B$), then $B(e_i, e_j) = B(e_j, e_i)$, which means $B_{ij} = B_{ji}$. The matrix equals its own transpose. This directly clarifies how the skew-symmetric case ($B^* = -B$) from [[Tensor Algebra]] alters the matrix structure: $B_{ij} = -B_{ji}$.

**For Endomorphisms and Matrix-Vector Multiplication:**
Endomorphisms are built using tensor products of the form $U^* \otimes U$. The endomorphism $A$ can be written as:
$$
A = \sum_{i=1}^n \sum_{j=1}^n A^i_j (e^j \otimes e_i)
$$
If you feed a column vector $\vec{v} = \sum_k v^k e_k$ into this tensor, the covector $e^j$ "eats" the vector components $v^k$ (since $e^j(e_k) = \delta^j_k$). The result collapses perfectly to:
$$
A(\vec{v}) = \sum_{i=1}^n \left( \sum_{j=1}^n A^i_j v^j \right) e_i
$$
This precisely recovers the standard **matrix-vector multiplication** formula, where the $n \times n$ matrix $A^i_j$ multiplies the column vector $\vec{v}$ to produce a new column vector in $U$.

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
B^{\top} \in \left(
  V^{**} \xrightarrow{\text{ linear}} V^*
\right)
$$
where $V^{**}$ is simply $V$. So, $B, B^{\top}$ are of the same type. 

# Definition (Symmetric Bilinear Forms)
A bilinear form $B$ is **symmetric** if $B = B^{\top}$. This is the same as $B(u)(v) = B(v)(u)$ or $B_{ij} = B_{ji}$.

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