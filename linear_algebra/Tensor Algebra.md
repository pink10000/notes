---
tags:
  - MATH_100B
  - CSE_291G
---

# Definition (Tensor Product Space)
Given two [[Vector Space|vector spaces]] $U$ and $V$, we can construct a new vector space called their **tensor product space**, denoted $W = U \otimes V$.

## Corollary (Dimension of Tensor Product Space)
If $\{\vec{e}_1, \dots, \vec{e}_m\}$ is a basis for $U$ and $\{\vec{f}_1, \dots, \vec{f}_n\}$ is a basis for $V$, then $W = U \otimes V$ is defined as the span of the formal products:
$$
\vec{e}_i \otimes \vec{f}_j
$$
As a result, the dimension multiplies: $\dim(U \otimes V) = \dim(U) \dim(V)$.

The $\otimes$ symbol extends to a **bilinear map** $\otimes : U \times V \xrightarrow{\text{bilinear}} W$. For any vectors $\vec{u} = u^i \vec{e}_i$ and $\vec{v} = v^j \vec{f}_j$, their tensor product distributes linearly:
$$
\vec{u} \otimes \vec{v} = (u^i \vec{e}_i) \otimes (v^j \vec{f}_j) = u^i v^j (\vec{e}_i \otimes \vec{f}_j)
$$

## Definition (Decomposable Tensor)
In general, an element $\tau \in U \otimes V$ is a linear combination of the basis elements:
$$
\tau = \sum_{i=1}^m \sum_{j=1}^n \tau^{ij} (\vec{e}_i \otimes \vec{f}_j)
$$
Most tensors $\tau$ cannot be factored into a simple product of two vectors. However, if the components satisfy $\tau^{ij} = u^i v^j$, then $\tau = \vec{u} \otimes \vec{v}$. Such a tensor is called a **decomposable** (or rank-1) tensor.

# Theorem (Universal Property of Tensor Products)
The tensor product can be elegantly defined through its **universal property**. This property guarantees that the tensor product space $U \otimes V$ is the "most general" space that linearizes bilinear operations.

Formally, for any vector spaces $U, V,$ and $W$, and any bilinear map $B: U \times V \to W$, there exists a **unique linear map** $L: U \otimes V \to W$ such that:
$$
B(\vec{u}, \vec{v}) = L(\vec{u} \otimes \vec{v})
$$
for all $\vec{u} \in U$ and $\vec{v} \in V$.

This means any bilinear operation on pairs of vectors can be equivalently understood as a purely linear operation on their tensor product. This property fundamentally motivates why we study tensor products: they reduce complex *multilinear* algebraic problems into standard *linear* algebra.

# Definition (Tensor Product, as Dual Space)
A powerful and simpler way to define the tensor product is to interpret it as a space of linear transformations:
$$
(U \otimes V) := (U^* \xrightarrow{\text{linear}} V)
$$
where $U^*$ is the [[Dual Space|dual space]] of $U$.

## Lemma (Tensors as Maps)
To understand how tensor products are equivalent to spaces of linear maps, consider the tensor product of two vector spaces $V \otimes W$. A single decomposable (or simple) tensor is written as $\vec{v} \otimes \vec{w}$, where $\vec{v} \in V$ and $\vec{w} \in W$.

We can define how this tensor $\vec{v} \otimes \vec{w}$ acts as a linear function $T : V^{*} \to W$. When we feed a covector $\alpha \in V^{*}$ into this simple tensor, the operation is defined by evaluating the covector on the $V$ component:
$$
T(\alpha) = (\vec{v} \otimes \vec{w})(\alpha) = \alpha(\vec{v})\vec{w} = \langle \alpha | \vec{v} \rangle \vec{w}
$$
*(Note: $\langle \alpha | \vec{v} \rangle$ is the [[Dual Space#Dual pairing|dual pairing]], sometimes written simply as $\alpha(\vec{v})$).*

Analyzing this operation:
1. $\langle \alpha | \vec{v} \rangle$ is a scalar.
2. $\vec{w}$ is a vector in $W$.
3. Therefore, $\langle \alpha | \vec{v} \rangle \vec{w}$ is simply the vector $\vec{w}$ scaled by the number $\langle \alpha | \vec{v} \rangle$.

Because the dual pairing is linear, this produces a linear map from $V^* \to W$. Since any tensor in $V \otimes W$ is a linear combination of such simple pairs, $V \otimes W$ represents the space of all possible linear maps from $V^*$ to $W$.

### Applying this to $U^* \otimes V$
If we replace $V$ with a dual space $U^*$, we are looking at the tensor product $U^* \otimes V$. Following the exact same logic, an outer product $\alpha \otimes \vec{v}$ (where $\alpha \in U^*$ and $\vec{v} \in V$) acts as a linear map from $U \to V$. 

When it acts on an input vector $\vec{u} \in U$:
$$
(\alpha \otimes \vec{v})(\vec{u}) = \langle \alpha | \vec{u} \rangle \vec{v}
$$
The covector $\alpha$ "eats" $\vec{u}$ to produce a scalar, which then scales $\vec{v}$. We can do this because of the bilinearity property of tensor products.

This mechanism applies directly to familiar objects:
- **Endomorphisms ([[Square Matrices|Matrices]]):** The space of linear maps from $U$ to itself is 
   $$
   \text{End}(U) = \{A: U \xrightarrow{\text{linear}} U\} = U^* \otimes U
   $$
   Constructed from $\alpha \otimes \vec{u}$, it takes an input vector, produces a scalar via $\alpha$, and outputs a scaled vector in $U$.
- **Bilinear Forms:** A bilinear form taking two vectors and returning a scalar can be viewed as 
   $$
   \{B: U \xrightarrow{\text{linear}} U^*\} = \{B: U \times U \xrightarrow{\text{bilinear}} \mathbb{R}\} = U^* \otimes U^*
   $$
   A tensor $\alpha \otimes \beta$ (two covectors) waits to eat two vectors, $\vec{u}$ and $\vec{w}$, resulting in multiplied scalars: $\langle \alpha | \vec{u} \rangle \langle \beta | \vec{w} \rangle$.
- **Vector-valued $k$-linear forms:** Can be constructed by chaining dual spaces, e.g., 
   $$
   \underbrace{U^* \otimes \cdots \otimes U^*}_{k} \otimes U
   $$

## Theorem (Dual of Tensor Product Space)
The [[Dual Space|dual space]] of a tensor product distributes nicely
$$
(U \otimes V)^* \cong (U^* \otimes V^*)
$$
but for finite-dimensional vector spaces. 

## Definition (Dual Pairing of Tensors)
The dual pairing between a tensor $A \in U \otimes V$ and $B \in U^* \otimes V^*$ is given by the trace:
$$
\langle A | B \rangle := \text{tr}(A^* B)
$$

# Definition (Symmetric and Skew-Symmetric Products)
In practice, we often work with tensors that have inherent symmetries (e.g., a symmetric bilinear form where $B^* = B$). We can define subspaces of $U \otimes U$ that enforce these symmetries:
1. **Symmetric Subspace ($U \odot U \subset U \otimes U$):**
   Consists of symmetric tensors and is spanned by the symmetric product:
   $$
   \vec{e}_i \odot \vec{e}_j = \vec{e}_j \odot \vec{e}_i \quad \text{for } 1 \leq i \leq j \leq m
   $$
2. **Skew-Symmetric Subspace ($U \wedge U \subset U \otimes U$):**
   Consists of skew-symmetric (anti-symmetric) tensors and is spanned by the wedge product:
   $$
   \vec{e}_i \wedge \vec{e}_j = -\vec{e}_j \wedge \vec{e}_i \quad \text{for } 1 \leq i < j \leq m
   $$
   When expressed as a matrix (e.g., as a bilinear form or an endomorphism over a chosen basis), an element of this subspace corresponds directly to a [[Skew-Symmetric Matrix|skew-symmetric matrix]] where $\mathbf{A}^\top = -\mathbf{A}$. This skew-symmetric construction also forms the mathematical foundation for **differential forms**.
