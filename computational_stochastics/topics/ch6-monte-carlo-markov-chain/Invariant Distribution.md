---
tags:
  - MATH_114
---
- When do they exist?
- When are they unique?

See [[Markov Chains#Definition (Distribution Vector)]].
# Theorem (Distribution of a Markov Chain)
Let $X$ be a [[Markov Chains|Markov Chain]]. The distribution of $X$ at time $t$ is given by 
$$
\pi_{t} = \pi_{0} P^{t}
$$
where $\pi_{t}$ is the [[Markov Chains#Definition (Distribution Vector)|distribution vector]] at time $t = 0, 1, 2, \dots$. $P^{0}$ is the identity matrix. 

Proof: Use induction. 
# Definition (Stationary or Invariant Distribution)
Let $P = [p_{ij}]$ be the transition matrix for the [[Markov Chains|Markov Chain]] $\{X_{n}\}_{n=0}^{\infty}$ with $S = \{1, 2, \dots, N\}$. A probability vector $\pi \in \R^{N}$ is a **stationary** or **invariant** distribution for $X_{n}$ (or for $P$) if 
$$
\pi P = \pi
$$
## Remark (Conclusions from Examples 1,2)
The examples [[Long-Run Markov Chains#Example 1 (Stationary Distributions)|1]] and [[Long-Run Markov Chains#Example 2 (Starting Distributions Don't Matter)|2]] show that asymptotic distribution of $X_{n}$ is the [[#Definition (Stationary or Invariant Distribution)|invariant distribution]]. 

# Definition (Reducible)
If two states $i,j \in S$ are reachable from one another, then we say that can **communicate** with one another. This communicability forms an equivalence class (proof omitted). 

A [[Markov Chains|Markov Chain]] is **reducible** if there are two or more communication classes.

# Definition (Periodic)
A [[Markov Chains|Markov Chain]] is **periodic** if there is a state that is returned at regular intervals greater than $1$ step. 

# Theorem (Uniqueness of Invariant Distributions)
An invariant distribution for a [[Markov Chains|Markov Chain]] *unique* unless the MC is [[#Definition (Reducible)|reducible]] or [[#Definition (Periodic)|periodic]]. 

# Definition (Regular Transition Matrices)
A finite state time-homogeneous MC $X_{n} \;\; (n \geq 0)$ with transition matrix $P$ is **regular** if there exists an integer $k \geq 1$ such that $p^{k} > 0$ (i.e. all entries of $P^{k}$ are strictly positive). 
## Example 1 (Simple Regularity)
Consider 
$$
P = \begin{pmatrix}
3/4 & 1/4 \\
1/6 & 5/6 \\
\end{pmatrix}
$$
This MC is regular. Immediately, we see that if $k = 1$, the entries are positive. 

# Theorem (Regular MC Gives Unique Stationary Distributions)
Let $X_{n} \;\; (n \geq 0)$ be a [[#Definition (Regular Transition Matrices)|regular]] $N-$state [[Markov Chains|Markov Chain]] with transition matrix $P$. Then:
1. The chain $X_{n} \;\; (n \geq 0)$ has a unique [[#Definition (Stationary or Invariant Distribution)|stationary distribution]] $\pi$ with $\pi > 0$. 
2. The probabilities converge:
   $$
   \lim_{n\to \infty} P^{n} = \begin{pmatrix}
   \pi \\ \vdots \\ \pi
   \end{pmatrix}
   $$
   i.e. $\lim_{n \to \infty} p_{n}(i, j) = \pi(j)$ where $j$ represents the row of $P^{n}$. 
3. For any initial distribution $\pi_{0}$, 
   $$
   \lim_{n \to \infty} \pi_{0} P^{n} = \pi
   $$
   Or, $\lim_{n \to \infty} P(X_{n} = j) = \pi(j)$ for all states $j$. 

Proof: 

Let $\pi$ be the limit of the state distribution over time, such that $\pi = \lim_{n \to \infty} \pi_{n+1}$. Since $\pi_{n+1} = \pi_{0} P^{n+1}$ via [[#Theorem (Distribution of a Markov Chain)]], then $\pi_{n + 1} = (\pi_{0} P^{n}) \cdot P$. We apply the limit and get
$$
\lim_{n \to \infty} (\pi_{0} P^{n}) \cdot P = \pi P
$$
and that $\pi$ is a fixed point for $P$. This shows $\pi$ exists and is stationary. By $(2)$, since every row of matrix $P^{n}$ converges to the same $\pi$, then $\pi$ is unique, thus $(1)$. Then $(2) \implies (3)$ because the row-vector $\pi_{0} = (a_{0}, a_{1}, \dots, a_{N})$ has its entries sum to $1$. 

So,
$$
\lim_{n \to \infty} \pi_{0} \cdot P^{n}
=
\pi_{0} \cdot
\begin{pmatrix}
\pi \\ \vdots \\ \pi
\end{pmatrix}
$$
Consider the first component of the resulting vector:
$$
\big( (\pi_{0}(0) \cdot \pi(1)) + (\pi_{0}(1) \cdot \pi(1)) + \cdots \big)
$$
We can factor out the stationary probability $\pi(j)$ for each component and get 
$$
\pi(j) \cdot \sum_{i} \pi_{0}(i)
$$
which is precisely equal to $\pi(j) \cdot 1 = \pi(j)$. Thus it is independent. 
# Solving For Stationary Distributions
We can either:
1. Solve $\pi P = \pi$ or 
2. Diagonalize $P = U\Lambda U^{-1}$. 

So, 
$$
\begin{aligned}
\lim_{n \to \infty} P^{n} 
&= \lim_{n \to \infty} \left( U\Lambda U^{-1}  \right)^{n} \\
&= U \left( \lim_{n \to \infty} \Lambda^{n} \right) U^{-1} \\
&= \begin{pmatrix}
\pi \\ \vdots \\ \pi
\end{pmatrix}
\end{aligned}
$$
The last line is from the fact that the stationary matrix is from its eigenvalues. Also recall that diagonalization of a matrix $M$ gives $U$, it's matrix of [[Eigenvector|eigenvectors]] and $\Lambda$, a [[Diagonal]] matrix of eigenvalues. 

Note that $\lim_{n \to \infty} \Lambda^{n}$ collapses to 
$$
\begin{pmatrix}
1 & 0 & \dots & 0 \\
0 & 0 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & 0
\end{pmatrix}
$$
because one eigenvalue of a stochastic matrix will be $1$. The rest are $|\lambda| < 1$, and so $\lambda^{n} \to 0$ as $n \to \infty$. 

## Remark (Stationaries Have Equal Out/Inflow)
For a distribution to be stationary, the total *outflow* from a state $i$ must be exactly equal to the total *inflow* into that same state. 
$$
\sum_{j} \pi_{i} \cdot p(i, j) = \sum_{j} \pi_{j} \cdot p(j, i)
$$
# Definition (Detailed Balance)
A [[Markov Chains#Definition (Stochastic Matrix)|stochastic matrix]] $P$ and a probability vector $\lambda$ satisfy **detailed balance** if 
$$
\lambda_{i} \cdot p(i, j) = \lambda_{j} \cdot p(j, i)
$$
for all $i, j \in S$. 

## Proposition (Detailed Balance is Stationary)
If a stochastic matrix $P$ and a probability vector $\lambda$ satisfy detailed balance then $\lambda P = \lambda$, i.e. $\lambda$ is stationary with respect to $P$. 

Proof: 
$$
(\lambda P)_{j} = \sum_{i} \lambda_{i} \cdot p(i, j) = \sum_{i} \lambda_{j} p(j, i) = \lambda_{j}
$$
for row $j$. 