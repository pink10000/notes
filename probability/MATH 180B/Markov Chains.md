---
tags:
  - MATH_180B
  - MATH_114
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
&= P(X_{0} = i_{0}) \prod_{k=1}^{n} p(i_{0}, i_{1})
\end{aligned}
$$
by the chain rule, Markov Property, and time homogeneity in that order. Visually, this is a path through a graph. The probability of this path is the product of the edges crossed. 
# Example 1 
Let $X_{0}, X_{1}, \dots X_{n} \in S$ be iid. Then $\{X_{n}\}_{n=0}^{\infty}$ is a time homogeneous Markov Chain. Let $S = \{1, 2, \dots, N\}$. Then $p(i, j) = \P(X_{1} = j \,|\, X_{0} = i) = \P(X_{1} = j) = p_{j}$. This means our transition matrix is 
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
