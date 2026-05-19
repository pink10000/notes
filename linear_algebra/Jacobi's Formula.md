---
tags:
  - CSE_291G
---

# Lemma (Log-Determinant Identity)
The identity relates the determinant of an invertible matrix $A \in \mathbb{C}^{n \times n}$ to the trace of its matrix logarithm:
$$
\det A = e^{\text{tr}(\log A)}
$$

## Case 1: Diagonalizable Matrices
Assume $A$ is diagonalizable. Then there exists an invertible matrix $P$ and a diagonal matrix $D$ such that:
$$
A = PDP^{-1}
$$
where $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ contains the eigenvalues of $A$. The determinant of $A$ is the product of its eigenvalues:
$$
\det A = \det(PDP^{-1}) = \det P \cdot \det D \cdot \det(P^{-1}) = \det D = \prod_{i=1}^n \lambda_i
$$
The matrix logarithm of a diagonalizable matrix is defined by applying the scalar logarithm to its eigenvalues:
$$
\log A = P (\log D) P^{-1} = P \cdot \text{diag}(\log \lambda_1, \log \lambda_2, \dots, \log \lambda_n) \cdot P^{-1}
$$
Taking the trace of both sides and utilizing the cyclic property of the trace ($\text{tr}(BC)=\text{tr}(CB)$):
$$
\text{tr}(\log A) = \text{tr}\left(P (\log D) P^{-1}\right) = \text{tr}\left((\log D) P^{-1} P\right) = \text{tr}(\log D)
$$
The trace of a diagonal matrix is the sum of its diagonal entries:
$$
\text{tr}(\log D) = \sum_{i=1}^n \log \lambda_i
$$
The exponential of the trace:
$$
\begin{aligned}
e^{\text{tr}(\log A)} 
&= e^{\sum_{i=1}^n \log \lambda_i} \\
&= \prod_{i=1}^n e^{\log \lambda_i} \\
&= \prod_{i=1}^n \lambda_i
\end{aligned}
$$

Since both sides equal $\prod_{i=1}^n \lambda_i$, the identity holds for all diagonalizable matrices:

$$
\det A = e^{\text{tr}(\log A)}
$$

## Case 2: General Invertible Matrices (Continuity Argument)
If $A$ is invertible but not diagonalizable, we can use the property that diagonalizable matrices are dense in $\mathbb{C}^{n \times n}$. 

There exists a [[Sequences|sequence]] of diagonalizable matrices $\{A_k\}_{k=1}^{\infty}$ that converges to $A$:
$$
\lim_{k \to \infty} A_k = A
$$
Since the functions $\det(\cdot)$, $\log(\cdot)$, and $\text{tr}(\cdot)$ are [[Continuity|continuous]] on the domain of invertible matrices, we can take the limit of the identity:
$$
\det A = \det\left(\lim_{k \to \infty} A_k\right) = \lim_{k \to \infty} \det A_k = \lim_{k \to \infty} e^{\text{tr}(\log A_k)} = e^{\text{tr}\left(\log \left(\lim_{k \to \infty} A_k\right)\right)} = e^{\text{tr}(\log A)}
$$
This completes the proof for any invertible matrix $A$.

# Jacobi's Formula
The derivative of the determinant of a matrix $A$ (if $A$ is invertible) is given by:
$$
\frac{d}{dt} (\det A) = \det A \cdot \text{tr} \left( A^{-1} \frac{dA}{dt} \right)
$$

Proof:

First, we use the [[#Lemma (Log-Determinant Identity)|identity]]:
$$
\det A = e^{\text{tr}(\log A)}
$$
Differentiating both sides with respect to $t$:
$$
\frac{d}{dt} (\det A) = \frac{d}{dt} \left( e^{\text{tr}(\log A)} \right) = e^{\text{tr}(\log A)} \cdot \frac{d}{dt} \left( \text{tr}(\log A) \right) = \det A \cdot \text{tr} \left( \frac{d}{dt} \log A \right)
$$
To evaluate $\text{tr} \left( \frac{d}{dt} \log A \right)$, we recall the formula for the derivative of the matrix exponential. If $A = e^X$, then:
$$
\frac{dA}{dt} = \int_0^1 e^{sX} \frac{dX}{dt} e^{(1-s)X} \, ds
$$
Multiplying by $A^{-1} = e^{-X}$:
$$
A^{-1} \frac{dA}{dt} = e^{-X} \int_0^1 e^{sX} \frac{dX}{dt} e^{(1-s)X} \, ds = \int_0^1 e^{(s-1)X} \frac{dX}{dt} e^{(1-s)X} \, ds
$$
Taking the trace and using the cyclic property ($\text{tr}(BC) = \text{tr}(CB)$):
$$
\text{tr} \left( A^{-1} \frac{dA}{dt} \right) = \int_0^1 \text{tr} \left( e^{(s-1)X} \frac{dX}{dt} e^{(1-s)X} \right) \, ds = \int_0^1 \text{tr} \left( \frac{dX}{dt} \right) \, ds = \text{tr} \left( \frac{dX}{dt} \right)
$$
Since $X = \log A$, we have $\text{tr} \left( \frac{d}{dt} \log A \right) = \text{tr} \left( A^{-1} \frac{dA}{dt} \right)$. Substituting this back into our expression for the derivative of the determinant:
$$
\frac{d}{dt} (\det A) = \det A \cdot \text{tr} \left( A^{-1} \frac{dA}{dt} \right)
$$
Note: This derivation assumes $A$ is invertible so that $\log A$ is well-defined. The formula holds more generally (even if $A$ is singular) as $\frac{d}{dt} \det A = \text{tr}(\text{adj}(A) \dot{A})$.