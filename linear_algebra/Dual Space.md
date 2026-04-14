---
tags:
  - CSE_291G
---
# Definition (Linear Map)
Let $U,V$ be two [[Vector Space|vector spaces]]. A map $A: U \to V$ is **linear** if 
$$
A(\vec{u}_{1} + \vec{u}_{2}) = A(\vec{u}_{1}) + A(\vec{u}_{2})
\quad \text{and} \quad
A(c\vec{u}) = c A(\vec{u})
$$

## Theorem (Set of Linear Maps is a Vector Space)
The set $\left(U \xrightarrow{\text{linear}} V\right)$ of all linear maps from $U$ to $V$ is a vector space.

# Definition (Covector)
A **covector** on a [[Vector Space|vector space]] $V$ is a scalar-valued linear function 
$$
\alpha : V \xrightarrow{\text{linear}} \mathbb{R}
$$
A covector is a linear function that takes in a vector and outputs a scalar. Geometrically, it is best to visualize a covector as a set of equidistant, parallel hyperplanes. In 2D, these are parallel lines. In 3D, they are parallel planes. They are like "slabs". It is best to visualize them by its [[Level Set|level sets]]. 

# Definition (Dual Space)
The **dual space**
$$
V^* = \left\{ \alpha : V \xrightarrow{\text{linear}} \mathbb{R} \right\}
$$
of a [[Vector Space|vector space]] $V$ is the vector space of all covectors on $V$. The elements of $V^*$ are called **dual vectors** or [[#Definition (Covector)|covectors]]. The **dual pairing** is denoted by 
$$
\alpha(\vec{u}) = \langle \alpha | \vec{u} \rangle = \alpha \llbracket \vec{u} \rrbracket
$$
It is the act of "feeding" a vector $\vec{u}$ into a covector $\alpha$ to get a scalar value. Visually, evaluating the dual pairing means counting the number of times the vector's arrow pierces through the hyperplanes of the covector. If the arrow runs perfectly parallel to the covector's lines, it pierces $0$, and the pairing is $0$. If the arrow stretches across $3$ level-set lines, the pairing evaluates to $3$. 

## Theorem (Dimension of Dual Space)
The dimension of the dual space $V^*$ is equal to the dimension of the original vector space $V$. That is,
$$
\dim V^* = \dim V
$$
If $V$ is a finite-dimensional vector space, then $\dim V^{**} = \dim V$. 

# Theorem (Dual Basis)
Let $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n$ be a [[Vector Space#Theorem (Basis)|basis]] for a finite-dimensional vector space $V$. Then there is a unique **dual basis** $\beta^1, \beta^2, \ldots, \beta^n \in V^*$ so that 
$$
\langle \vec{e}_i | \beta^j \rangle 
= \delta_i^j
= \begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \neq j
\end{cases}
$$
where $\delta_i^j$ is the **Kronecker delta**. If we write 
$$
\vec{u} = \sum_{i=1}^{n} u^i \vec{e}_i
$$
using a basis, then we would write a covector $\alpha$ as
$$
\alpha = \sum_{j=1}^{n} \alpha_j \beta^j
$$
The dual pairing simply becomes 
$$
\langle \alpha | \vec{u} \rangle = \sum_{i=1}^{n} \alpha_i u^i
$$
Likewise to the visualization of the dual pairing, given some basis vector $\vec{e}_{1}\in V$, the corresponding $\beta^{1}$ dual vector means that the pairing evaluates to $1$, or that it crosses the covector slab exactly once. 

# Conventional Notation 
Vectors are conventionally columnar. Covectors are row vectors. The dual pairing is automatic
$$
\begin{bmatrix}
\alpha_1 & \cdots & \alpha_n 
\end{bmatrix}
% 
\begin{bmatrix}
u^1 \\ \vdots \\ u^n
\end{bmatrix}
= \sum_{i=1}^{n} \alpha_i u^i
$$
Vectors are labeled with an upper index $u^i$ and covectors are labeled with a lower index $\alpha_j$. We can also use the bra-ket notation, where the vector $\vec{u}$ is written as a "ket" $|\vec{u}\rangle$ and the covector $\alpha$ is written as a "bra" $\langle \alpha|$. The dual pairing is then written as $\langle \alpha | \vec{u} \rangle$. There is also Penrose graphical notation. 

# Definition (Adjoint Linear Map)
For each [[#Definition (Linear Map)|linear map]] $A: U \to V$, there is a linear map called its **adjoint** $A^T: V^* \to U^*$ defined by 
$$
\langle A^T \beta | \vec{u} \rangle = \langle \beta | A\vec{u} \rangle
$$ 
for all $\vec{u} \in U$ and $\beta \in V^*$. The adjoint map is also denoted as $A^*$. 