---
tags:
  - MATH_100B
  - CSE_291G
---

# Definition (Adjugate Matrix)
In linear algebra, the **adjugate matrix** (historically also called the **classical adjoint**) of a square matrix $A$ is the transpose of its cofactor matrix. It is an extremely important construction because it allows us to express the inverse of a matrix and the derivatives of determinants analytically without needing to perform division.

Before defining the adjugate, we must define the building blocks: **minors** and **cofactors**.
# Definition (Minors and Cofactors)
For any square matrix $A \in \mathbb{F}^{n \times n}$:

## 1. Submatrices and Minors
If we delete row $i$ and column $j$ from $A$, we obtain an $(n-1) \times (n-1)$ submatrix, denoted as $A_{\backslash i, \backslash j}$.
The **minor** $M_{ij}$ associated with the entry $A_{ij}$ is defined as the determinant of this submatrix:
$$
M_{ij} = \det(A_{\backslash i, \backslash j})
$$
Since $M_{ij}$ is the determinant of an $(n-1) \times (n-1)$ matrix, it measures the "volume scaling" of the subspace map ignoring the $i$-th input direction and $j$-th output direction.

## 2. Cofactors
The **cofactor** $C_{ij}$ associated with the entry $A_{ij}$ is the minor signed by its position in the checkerboard pattern:
$$
C_{ij} = (-1)^{i+j} M_{ij} = (-1)^{i+j} \det(A_{\backslash i, \backslash j})
$$
The sign factor $(-1)^{i+j}$ alternates in a checkerboard grid:
$$
\begin{bmatrix}
+ & - & + & \cdots \\
- & + & - & \cdots \\
+ & - & + & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$
The cofactor $C_{ij}$ represents the rate of change of the determinant with respect to the entry $A_{ij}$, i.e., $\frac{\partial \det(A)}{\partial A_{ij}} = C_{ij}$ (see [[Jacobi's Formula#Proof 3: Via Cofactor Expansion (General Case)|Jacobi's Formula]]).

# Definition (Adjugate Matrix Construction)
The **adjugate matrix** $\operatorname{adj}(A)$ is the transpose of the cofactor matrix $C$:
$$
\operatorname{adj}(A) = C^{\top}
$$
This means that the $(i, j)$-entry of $\operatorname{adj}(A)$ is the cofactor $C_{ji}$:
$$
\operatorname{adj}(A)_{ij} = C_{ji} = (-1)^{i+j} M_{ji} = (-1)^{i+j} \det(A_{\backslash j, \backslash i})
$$
## Theorem (Adjugate Entries are Determinants of Submatrix)
By definition, the cofactor $C_{ji}$ is $(-1)^{j+i} \det(A_{\backslash j, \backslash i})$. The term $\det(A_{\backslash j, \backslash i})$ is the determinant of the $(n-1) \times (n-1)$ submatrix formed by deleting the $j$-th row and $i$-th column of $A$. 

Because the entry at row $i$, column $j$ of the adjugate is exactly $C_{ji}$, every single element in $\operatorname{adj}(A)$ is a signed determinant of one of these $(n-1) \times (n-1)$ submatrices.

# Example (2x2 Adjugate Matrix)
Let $A$ be a general $2 \times 2$ matrix:
$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$
We compute the minors and cofactors for each entry:
- For $A_{11} = a$: Delete row 1, col 1 $\implies A_{\backslash 1, \backslash 1} = [d] \implies M_{11} = d$. Cofactor $C_{11} = (-1)^{1+1} d = d$.
- For $A_{12} = b$: Delete row 1, col 2 $\implies A_{\backslash 1, \backslash 2} = [c] \implies M_{12} = c$. Cofactor $C_{12} = (-1)^{1+2} c = -c$.
- For $A_{21} = c$: Delete row 2, col 1 $\implies A_{\backslash 2, \backslash 1} = [b] \implies M_{21} = b$. Cofactor $C_{21} = (-1)^{2+1} b = -b$.
- For $A_{22} = d$: Delete row 2, col 2 $\implies A_{\backslash 2, \backslash 2} = [a] \implies M_{22} = a$. Cofactor $C_{22} = (-1)^{2+2} a = a$.

The cofactor matrix is:
$$
C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix} = \begin{bmatrix} d & -c \\ -b & a \end{bmatrix}
$$
Taking the transpose of $C$ yields the adjugate matrix:
$$
\operatorname{adj}(A) = C^{\top} = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$
Observe how:
1. Every entry is the determinant of a $1 \times 1$ submatrix (a scalar).
2. For invertible $A$, $A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$, which perfectly matches the $2 \times 2$ inverse formula!
# Example (3x3 Adjugate Matrix)
Let $A$ be the $3 \times 3$ matrix:
$$
A = \begin{bmatrix} 1 & 0 & 2 \\ -1 & 3 & 0 \\ 0 & 2 & 1 \end{bmatrix}
$$
We compute the cofactors $C_{ij} = (-1)^{i+j} \det(A_{\backslash i, \backslash j})$:
* **Row 1:**
  - $C_{11} = + \det \begin{bmatrix} 3 & 0 \\ 2 & 1 \end{bmatrix} = +(3 \cdot 1 - 0) = 3$
  - $C_{12} = - \det \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} = -((-1) \cdot 1 - 0) = 1$
  - $C_{13} = + \det \begin{bmatrix} -1 & 3 \\ 0 & 2 \end{bmatrix} = +((-1) \cdot 2 - 0) = -2$
* **Row 2:**
  - $C_{21} = - \det \begin{bmatrix} 0 & 2 \\ 2 & 1 \end{bmatrix} = -(0 \cdot 1 - 4) = 4$
  - $C_{22} = + \det \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = +(1 \cdot 1 - 0) = 1$
  - $C_{23} = - \det \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} = -(1 \cdot 2 - 0) = -2$
* **Row 3:**
  - $C_{31} = + \det \begin{bmatrix} 0 & 2 \\ 3 & 0 \end{bmatrix} = +(0 \cdot 0 - 6) = -6$
  - $C_{32} = - \det \begin{bmatrix} 1 & 2 \\ -1 & 0 \end{bmatrix} = -(1 \cdot 0 - (-2)) = -2$
  - $C_{33} = + \det \begin{bmatrix} 1 & 0 \\ -1 & 3 \end{bmatrix} = +(1 \cdot 3 - 0) = 3$

The cofactor matrix is:
$$
C = \begin{bmatrix} 3 & 1 & -2 \\ 4 & 1 & -2 \\ -6 & -2 & 3 \end{bmatrix}
$$
Taking the transpose of $C$ yields the adjugate matrix:
$$
\operatorname{adj}(A) = C^{\top} = \begin{bmatrix} 3 & 4 & -6 \\ 1 & 1 & -2 \\ -2 & -2 & 3 \end{bmatrix}
$$
We can verify the identity $A \operatorname{adj}(A) = \det(A) I_3$. Cofactor expansion along the first row of $A$ gives:
$$
\det(A) = A_{11}C_{11} + A_{12}C_{12} + A_{13}C_{13} = 1(3) + 0(1) + 2(-2) = -1
$$
Computing the product:
$$
A \operatorname{adj}(A) = \begin{bmatrix} 1 & 0 & 2 \\ -1 & 3 & 0 \\ 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} 3 & 4 & -6 \\ 1 & 1 & -2 \\ -2 & -2 & 3 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix} = -1 \cdot \bI_{3\times 3}
$$
This perfectly holds!

# Theorem (The Adjugate Identity)
For any $n \times n$ matrix $A$, we have:
$$
A \operatorname{adj}(A) = \operatorname{adj}(A) A = \det(A) I_n
$$
where $I_n$ denotes the $n \times n$ **identity matrix** (the matrix with $1$s on the main diagonal and $0$s elsewhere).

## Proof
Let $B = A \operatorname{adj}(A)$. The $(i, j)$-entry of $B$ is given by matrix multiplication:
$$
B_{ij} = \sum_{k=1}^n A_{ik} \operatorname{adj}(A)_{kj} = \sum_{k=1}^n A_{ik} C_{jk}
$$
We analyze two cases:
1. **If $i = j$:**
   $$
   B_{ii} = \sum_{k=1}^n A_{ik} C_{ik}
   $$
   This is exactly the cofactor expansion of $\det(A)$ along row $i$. Thus, $B_{ii} = \det(A)$.
2. **If $i \neq j$:**
   $$
   B_{ij} = \sum_{k=1}^n A_{ik} C_{jk}
   $$
   This expression represents the cofactor expansion along row $j$ of a matrix $A'$ obtained by replacing row $j$ of $A$ with row $i$. Since $A'$ has two identical rows (row $i$ and row $j$), its determinant is zero. Thus, $B_{ij} = 0$ for $i \neq j$.

Therefore, $B = \det(A) I_n$. A completely symmetric argument for $\operatorname{adj}(A) A$ yields the same result.

---

# Corollary (Matrix Inverse Formula)
If $\det(A) \neq 0$, then $A$ is invertible and:
$$
A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A)
$$

## Proof
Divide the adjugate identity (Theorem 1) by the scalar $\det(A)$:
$$
A \left( \frac{1}{\det(A)} \operatorname{adj}(A) \right) = \bI_{3\times 3}
$$
By uniqueness of the matrix inverse, the formula holds.

---

# Theorem (Determinant of the Adjugate)
For any $n \times n$ matrix $A$:
$$
\det(\operatorname{adj}(A)) = \det(A)^{n-1}
$$

## Proof
Taking the determinant of both sides of the adjugate identity $A \operatorname{adj}(A) = \det(A) I_n$:
$$
\det(A) \det(\operatorname{adj}(A)) = \det(\det(A) I_n) = \det(A)^n \det(I_n) = \det(A)^n
$$
* **Case 1 ($\det(A) \neq 0$):** We can divide both sides by $\det(A)$ to get:
  $$
  \det(\operatorname{adj}(A)) = \det(A)^{n-1}
  $$
* **Case 2 ($\det(A) = 0$):** If $\det(A) = 0$, then $A \operatorname{adj}(A) = 0$. If $\operatorname{adj}(A)$ were invertible, we could multiply by its inverse to get $A = 0$, which would imply $\operatorname{adj}(A) = 0$ (for $n > 1$), a contradiction. Thus $\operatorname{adj}(A)$ must be singular, so $\det(\operatorname{adj}(A)) = 0$. Thus, $0 = 0^{n-1}$ holds (assuming $n > 1$).

---

# Theorem (Adjugate of a Product)
For any two $n \times n$ matrices $A$ and $B$:
$$
\operatorname{adj}(AB) = \operatorname{adj}(B) \operatorname{adj}(A)
$$

## Proof
* **If $A$ and $B$ are invertible:**
  $$
  \operatorname{adj}(AB) = \det(AB) (AB)^{-1} = \det(A)\det(B) B^{-1} A^{-1} = \left(\det(B) B^{-1}\right) \left(\det(A) A^{-1}\right) = \operatorname{adj}(B) \operatorname{adj}(A)
  $$
* **General Case:** Since invertible matrices are dense in the set of all matrices, the identity extends to all matrices by continuity.

---

# Application (Invariant Derivatives in Continuum Mechanics)

In [[phys_sim/Stress-Strain Relation|Stress-Strain Relation]], we differentiate the characteristic polynomial $P_{\mathbf{C}}(z) = \det(z\mathbf{I} - \mathbf{C})$ with respect to the right Cauchy-Green deformation tensor $\mathbf{C}$. 

Applying [[Jacobi's Formula]], we start with the matrix derivative:
$$
\frac{\partial \det(A)}{\partial A} = \det(A) A^{-\top}
$$
Setting $A = z\mathbf{I} - \mathbf{C}$, the chain rule gives:
$$
\frac{\partial P_{\mathbf{C}}(z)}{\partial \mathbf{C}} = \frac{\partial \det(z\mathbf{I} - \mathbf{C})}{\partial \mathbf{C}} = -\det(z\mathbf{I} - \mathbf{C}) (z\mathbf{I} - \mathbf{C})^{-\top}
$$
Using the inverse formula $\mathbf{A}^{-1} = \frac{\operatorname{adj}(\mathbf{A})}{\det(\mathbf{A})}$, we can rewrite the transpose-inverse term:
$$
(z\mathbf{I} - \mathbf{C})^{-\top} = \left( \frac{\operatorname{adj}(z\mathbf{I} - \mathbf{C})}{\det(z\mathbf{I} - \mathbf{C})} \right)^{\top}
$$
Substituting this back into the derivative:
$$
\begin{aligned}
\frac{\partial P_{\mathbf{C}}(z)}{\partial \mathbf{C}} &= -P_{\mathbf{C}}(z) \left( \frac{\operatorname{adj}(z\mathbf{I} - \mathbf{C})}{\det(z\mathbf{I} - \mathbf{C})} \right)^{\top} \\
&= -P_{\mathbf{C}}(z) \left( \frac{\operatorname{adj}(z\mathbf{I} - \mathbf{C})}{P_{\mathbf{C}}(z)} \right)^{\top} \\
&= -\operatorname{adj}(z\mathbf{I} - \mathbf{C})^{\top}
\end{aligned}
$$
The determinant terms cancel out completely. Since $\operatorname{adj}(z\mathbf{I} - \mathbf{C})$ is a matrix polynomial in $z$, we can equate powers of $z$ on both sides to compute the derivatives of individual invariants $\frac{\partial I_k}{\partial \mathbf{C}}$ without needing to perform division by singular determinants.
