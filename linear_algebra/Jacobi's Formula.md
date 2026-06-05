---
tags:
  - CSE_291G
---

# Theorem (Jacobi's Formula)

In matrix calculus, **Jacobi's formula** expresses the derivative of the determinant of a matrix $A$ in terms of its adjugate and the derivative of $A$. 

Formally, if $A: \mathbb{R} \to \mathbb{R}^{n \times n}$ is a differentiable matrix-valued function, the derivative of its determinant is:

$$
\frac{d}{dt} \det A(t) = \operatorname{tr}\left( \operatorname{adj}(A(t)) \frac{dA(t)}{dt} \right)
$$

where:
- $\operatorname{adj}(A(t))$ is the [[Adjugate Matrix|adjugate matrix]] (the transpose of the cofactor matrix) of $A(t)$, as discussed in [[Square Matrices]].
- $\operatorname{tr}(\cdot)$ denotes the [[Square Matrices#Remark (Endomorphisms vs Bilinear Forms)|trace]] operator.

### Invertible Case
If $A(t)$ is invertible (so $\det A(t) \neq 0$), we can use the identity $\operatorname{adj}(A(t)) = \det A(t) A(t)^{-1}$ to write the formula in the more common form:

$$
\frac{d}{dt} \det A(t) = \det A(t) \operatorname{tr}\left( A(t)^{-1} \frac{dA(t)}{dt} \right)
$$

### Matrix Derivative Form
In terms of matrix derivatives (often used in machine learning and optimization, see [[phys_sim/Stress-Strain Relation|Stress-Strain Relation]]), Jacobi's formula can be written as:

$$
\frac{\partial \det A}{\partial A} = \operatorname{adj}(A)^{\top}
$$

For invertible $A$, this simplifies to:

$$
\frac{\partial \det A}{\partial A} = \det(A) A^{-\top}
$$

where $A^{-\top} = (A^{-1})^{\top}$.

---

# Lemma (Log-Determinant Identity)
For any invertible matrix $A \in \mathbb{C}^{n \times n}$, we have the identity:
$$
\det A = e^{\operatorname{tr}(\log A)}
$$

## Case 1: Diagonalizable Matrices
Assume $A$ is diagonalizable. Then there exists an invertible matrix $P$ and a diagonal matrix $D$ such that:
$$
A = PDP^{-1}
$$
where $D = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ contains the eigenvalues of $A$. The determinant of $A$ is the product of its eigenvalues:
$$
\det A = \det(PDP^{-1}) = \det P \cdot \det D \cdot \det(P^{-1}) = \det D = \prod_{i=1}^n \lambda_i
$$
The matrix logarithm of a diagonalizable matrix is defined by applying the scalar logarithm to its eigenvalues:
$$
\log A = P (\log D) P^{-1} = P \cdot \operatorname{diag}(\log \lambda_1, \log \lambda_2, \dots, \log \lambda_n) \cdot P^{-1}
$$
Taking the trace of both sides and utilizing the cyclic property of the trace ($\operatorname{tr}(BC)=\operatorname{tr}(CB)$):
$$
\operatorname{tr}(\log A) = \operatorname{tr}\left(P (\log D) P^{-1}\right) = \operatorname{tr}\left((\log D) P^{-1} P\right) = \operatorname{tr}(\log D)
$$
The trace of a diagonal matrix is the sum of its diagonal entries:
$$
\operatorname{tr}(\log D) = \sum_{i=1}^n \log \lambda_i
$$
The exponential of the trace:
$$
e^{\operatorname{tr}(\log A)} = e^{\sum_{i=1}^n \log \lambda_i} = \prod_{i=1}^n e^{\log \lambda_i} = \prod_{i=1}^n \lambda_i
$$
Since both sides equal $\prod_{i=1}^n \lambda_i$, the identity holds for all diagonalizable matrices:
$$
\det A = e^{\operatorname{tr}(\log A)}
$$

## Case 2: General Invertible Matrices (Continuity Argument)
If $A$ is invertible but not diagonalizable, we can use the property that diagonalizable matrices are dense in $\mathbb{C}^{n \times n}$. There exists a sequence of diagonalizable matrices $\{A_k\}_{k=1}^{\infty}$ that converges to $A$:
$$
\lim_{k \to \infty} A_k = A
$$
Since the functions $\det(\cdot)$, $\log(\cdot)$, and $\operatorname{tr}(\cdot)$ are continuous on the domain of invertible matrices, we can take the limit of the identity:
$$
\det A = \det\left(\lim_{k \to \infty} A_k\right) = \lim_{k \to \infty} \det A_k = \lim_{k \to \infty} e^{\operatorname{tr}(\log A_k)} = e^{\operatorname{tr}\left(\log \left(\lim_{k \to \infty} A_k\right)\right)} = e^{\operatorname{tr}(\log A)}
$$
This completes the proof for any invertible matrix $A$.

---

# Proof (Jacobi's Formula)

Below are three different proofs of Jacobi's formula, each highlighting different mathematical techniques.

## Proof 1: Via the Log-Determinant Identity
We differentiate the log-determinant identity:
$$
\det A = e^{\operatorname{tr}(\log A)}
$$
Differentiating both sides with respect to $t$ using the chain rule:
$$
\frac{d}{dt} (\det A) = \frac{d}{dt} \left( e^{\operatorname{tr}(\log A)} \right) = e^{\operatorname{tr}(\log A)} \cdot \frac{d}{dt} \left( \operatorname{tr}(\log A) \right) = \det A \cdot \operatorname{tr} \left( \frac{d}{dt} \log A \right)
$$
To evaluate $\operatorname{tr} \left( \frac{d}{dt} \log A \right)$, we use the formula for the derivative of the matrix exponential. If $A = e^X$, then:
$$
\frac{dA}{dt} = \int_0^1 e^{sX} \frac{dX}{dt} e^{(1-s)X} \, ds
$$
Multiplying by $A^{-1} = e^{-X}$:
$$
A^{-1} \frac{dA}{dt} = e^{-X} \int_0^1 e^{sX} \frac{dX}{dt} e^{(1-s)X} \, ds = \int_0^1 e^{(s-1)X} \frac{dX}{dt} e^{(1-s)X} \, ds
$$
Taking the trace and using the cyclic property of trace:
$$
\operatorname{tr} \left( A^{-1} \frac{dA}{dt} \right) = \int_0^1 \operatorname{tr} \left( e^{(s-1)X} \frac{dX}{dt} e^{(1-s)X} \right) \, ds = \int_0^1 \operatorname{tr} \left( \frac{dX}{dt} \right) \, ds = \operatorname{tr} \left( \frac{dX}{dt} \right)
$$
Since $X = \log A$, we have $\operatorname{tr} \left( \frac{d}{dt} \log A \right) = \operatorname{tr} \left( A^{-1} \frac{dA}{dt} \right)$. Substituting this back gives:
$$
\frac{d}{dt} (\det A) = \det A \cdot \operatorname{tr} \left( A^{-1} \frac{dA}{dt} \right)
$$

## Proof 2: Via Differentiation at the Identity
We first establish the formula when $A(t) = I$ at a given point $t=t_0$. Let $B = \dot{A}(t_0)$. Using the Leibniz formula for the determinant:
$$
\det(I + \epsilon B) = 1 + \epsilon \operatorname{tr}(B) + O(\epsilon^2)
$$
This is because in the expansion of $\det(I + \epsilon B)$, the only term that does not contain any $\epsilon$ is $1$, and the terms linear in $\epsilon$ must come from the product of the diagonal elements $(1 + \epsilon B_{ii})$, which yields $\epsilon \sum_{i=1}^n B_{ii} = \epsilon \operatorname{tr}(B)$.
Therefore, the derivative of the determinant at the identity is:
$$
\left. \frac{d}{d\epsilon} \det(I + \epsilon B) \right|_{\epsilon=0} = \operatorname{tr}(B)
$$
For a general invertible matrix $A(t)$, we can factor out $A(t)$:
$$
\begin{aligned}
\frac{d}{dt} \det A(t) &= \lim_{\epsilon \to 0} \frac{\det A(t + \epsilon) - \det A(t)}{\epsilon} \\
&= \lim_{\epsilon \to 0} \frac{\det(A(t) + \epsilon \dot{A}(t) + O(\epsilon^2)) - \det A(t)}{\epsilon} \\
&= \det A(t) \lim_{\epsilon \to 0} \frac{\det(I + \epsilon A(t)^{-1}\dot{A}(t) + O(\epsilon^2)) - 1}{\epsilon} \\
&= \det A(t) \operatorname{tr}\left( A(t)^{-1} \dot{A}(t) \right)
\end{aligned}
$$

## Proof 3: Via Cofactor Expansion
Recall the cofactor expansion of the determinant along any row $i$:
$$
\det A = \sum_{j=1}^n A_{ij} C_{ij}
$$
where $C_{ij}$ is the cofactor of entry $A_{ij}$. Since $C_{ij}$ is the determinant of the submatrix obtained by deleting row $i$ and column $j$, it does not depend on any entry in row $i$. Thus:
$$
\frac{\partial \det A}{\partial A_{ij}} = C_{ij}
$$
By definition, the adjugate matrix $\operatorname{adj}(A)$ is the transpose of the cofactor matrix, meaning $\operatorname{adj}(A)_{ji} = C_{ij}$. Therefore:
$$
\frac{\partial \det A}{\partial A_{ij}} = \operatorname{adj}(A)_{ji}
$$
Using the multivariable chain rule, we compute the total derivative with respect to $t$:
$$
\frac{d}{dt} \det A(t) = \sum_{i=1}^n \sum_{j=1}^n \frac{\partial \det A}{\partial A_{ij}} \frac{dA_{ij}}{dt} = \sum_{i=1}^n \sum_{j=1}^n \operatorname{adj}(A)_{ji} \frac{dA_{ij}}{dt} = \operatorname{tr}\left( \operatorname{adj}(A) \frac{dA}{dt} \right)
$$
This proof is completely general and does not assume $A$ is invertible.

---

# Application (Ordinary Differential Equations and Continuum Mechanics)

## Theorem (Liouville's Formula)
Jacobi's formula is the key tool used to prove **Liouville's formula** (or Abel's identity) for linear systems of [[diffeq/Ordinary Differential Equation|Ordinary Differential Equations]]. 
Consider a homogeneous linear system:
$$
\dot{x}(t) = P(t)x(t)
$$
If $\Phi(t)$ is a fundamental matrix solution (so $\dot{\Phi}(t) = P(t)\Phi(t)$), then the derivative of its determinant (called the Wronskian $W(t) = \det \Phi(t)$) is given by:
$$
\frac{d}{dt} W(t) = W(t) \operatorname{tr}\left( \Phi(t)^{-1} \dot{\Phi}(t) \right) = W(t) \operatorname{tr}\left( \Phi(t)^{-1} P(t) \Phi(t) \right)
$$
Using the cyclic property of trace, $\operatorname{tr}(\Phi^{-1} P \Phi) = \operatorname{tr}(P \Phi \Phi^{-1}) = \operatorname{tr}(P(t))$. Therefore:
$$
\frac{d}{dt} W(t) = \operatorname{tr}(P(t)) W(t)
$$
Integrating this scalar ODE yields Liouville's formula:
$$
W(t) = W(t_0) \exp\left( \int_{t_0}^t \operatorname{tr}(P(s)) \, ds \right)
$$

## Theorem (Mass Conservation Equation)
In [[phys_sim/Continuum Mechanics|Continuum Mechanics]], Jacobi's formula relates the change in volume of a deforming body to the divergence of its velocity field. If $\phi(X, t)$ is the flow map and $F = d\phi$ is the deformation gradient, the local volume ratio is $J = \det F$. The rate of change of $J$ is:
$$
\dot{J} = J \operatorname{tr}(F^{-1} \dot{F})
$$
Since $\dot{F} F^{-1} = L$ is the spatial velocity gradient $\nabla \mathbf{u}$, we have:
$$
\dot{J} = J \operatorname{tr}(\nabla \mathbf{u}) = J (\nabla \cdot \mathbf{u}) = J \operatorname{div}(\mathbf{u})
$$
This identity is central to deriving the continuity equation for mass conservation.