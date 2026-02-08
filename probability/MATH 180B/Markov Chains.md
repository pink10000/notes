---
tags:
  - MATH_180B
  - MATH_114
aliases:
  - Markov Chain
---
# Definition (Markov Process)
A [[Stochastic Process]] is a set $\{X_{n}\}_{n=0}^{\infty}$ is a **Markov Process** if 
$$
\P(
X_{n+1} = i_{n+1} \,|\, X_{0} = i_{0}, \dots, X_{n} = i_{n} 
)
=
\P(
X_{n+1} = i_{n+1} \,|\, X_{n} = i_{n}
)
$$
$\forall n \geq 0, \forall i_{0}, \dots i_{n+1} \in S$. In particular, it means if $(n+1)$th step only depends on the previous step. 

A Markov Process is *time homogeneous* if 
$$
\P(X_{n+1} = j \,|\, X_{n} = i)
=
\P(X_{1} = j \,|\, X_{0} = i)
$$
$\forall n \geq 0, \forall i_{j} \in S$. So the probability of going from state $i$ to $j$ does not depend on the time. 

# Definition (Transition Probability)
The **transition probability** of jumping between states is 
$$
p(i, j) = \P(X_{1} = j \,|\, X_{0} = i) = \P(i \to j)
$$
for all $i,j \in S$. This allows us to put these relationships into a matrix. 
$$
P = \begin{bmatrix}
p(i, j)
\end{bmatrix}
$$
for $i,j \in S$. Here, $i,j$ are states with row/column labels. 

# Definition (Joint Distribution for Markov Processes)
The [[Joint Distribution]] is for any $n \geq 1, i_{0}, \dots, i_{n} \in S$ we have 
$$
\begin{aligned}
\P(X_{0} = i_{0}, \dots, X_{n} = i_{n})
&=
\P(X_{0} = i_{0}) \prod_{k=1}^{n}\P(X_{k} = i_{k} \,|\,X_{0} = i_{0}, \dots, X_{k-1} = i_{k-1}) \\
&= 
\P(X_{0} = i_{0}) \prod_{k=1}^{n}\P(X_{k} = i_{k} \,|\, X_{k-1} = i_{k-1}) \\
&= P(X_{0} = i_{0}) \prod_{k=1}^{n} p(i_{k-1}, i_{k})
\end{aligned}
$$
by the chain rule, Markov Property, and time homogeneity in that order. Visually, this is a path through a graph. The probability of this path is the product of the edges crossed. 
# Example 1 (Transition Matrix)
Let $X_{0}, X_{1}, \dots X_{n} \in S$ be iid. Then $\{X_{n}\}_{n=0}^{\infty}$ is a time homogeneous Markov Chain. Let $S = \{1, 2, \dots, N\}$. Then $p(i, j) = \P(X_{1} = j \,|\, X_{0} = i) = \P(X_{1} = j) = p_{j}$. This means our **transition matrix** is 
$$
P = \begin{bmatrix}
p_{1} & p_{2} & \dots & p_{N} \\
p_{1} & p_{2} & \dots & p_{N} \\
\vdots & \vdots & \ddots & \vdots \\
p_{1} & p_{2} & \dots & p_{N} \\
\end{bmatrix}
,\quad\quad\quad \sum_{i=1}^{N} p_{i} = 1
$$
The sum of a column must be equal to $1$. This corresponds to every edge out of a node summing to $1$. 
# Example 3 (1D Random Walk)
Consider a random walk on a number line from $0 \to 1 \to 2 \to \dots \to N - 1 \to N$. Then 
$$
X_{n} \in S = \{0, 1, \dots, N\} 
$$
for $N = 0, 1, 2, \dots$ and $X_{n}$ at $i$ for $0 < i < N$. We jump right at probability $p$ and left with probability $1 - p$. We can model this with a Markov Chain where jumping from $i \to i + 1$ is probability $p$ and $i \to i - 1$ as $1 - p$. 

# Definition (Stochastic Matrix)
A square matrix $P = [p_{ij}]$ is a **stochastic matrix** if all $p_{ij} \geq 0$ and $\sum_{i} p_{ij} = 1$ for all $i$. All rows sum to $1$. For a discrete state time homogeneous Markov Chain, 
$$
X_{n} \in S = \{0, 1,\ \dots\}, n \geq 0 
$$
with transition matrix $P$, the **$n-$step transition probabilities** are 
$$
\begin{aligned}
p_{n} 
&= \P(X_{n+k} = j \,|\, X_{k} = i) \\
&= \P(X_{n} = j \,|\, X_{0} = i)
\end{aligned}
$$
and **$n$-step transition matrix** is 
$$
P_{n} = [p_{n}(i, j)]
$$
e.g. 
- $P_{0} = I, p_{0}(i, j) = \delta_{ij}$ 
- $P_{1} = p, p_{1}(i, j) = p(i, j)$
where $\delta_{ij}$ is the Kronecker Delta. 

# Definition (Distribution Vector)
The **distribution vector** $\pi_{n}$ for $X_{n}$ is 
$$
\vec{\pi}_{n} = \left[
\pi_{n}(0), \pi_{n}(1), \dots, 
\right]
$$
where $\pi_{n}(i) = \P(X_{n} = i)$ for $i \in S$. 

# Proposition (Stochastic Properties) 
Let $X_{n} \in S = \{0, 1, 2, \dots\}$ for $n \geq 0$ be a time homogeneous Markov Chain with transition matrix $P$. Then
1. $P$ is a [[#Definition (Stochastic Matrix)|Stochastic Matrix]]
2. $P\mathbb{1} = \mathbb{1}$ is an [[Eigenvector|Eigenvalue]] of $P$ with eigenvector $\mathbb{1}$. In particular,
   $$
   \mathbb{1} = \begin{pmatrix}
   1 \\ 1 \\ \vdots \\ 1
   \end{pmatrix}
   $$
3. $p_{m+n} = p_{m} \cdot p_{n}$ (Chapman-Kolmgorov Equality)
4. $\pi_{n} = \pi_{0} \cdot p_{n} = \pi_{0} p^{n}$ and $\pi_{n+1} = \pi_{n}\cdot p$ for all $n \geq 0$. 
