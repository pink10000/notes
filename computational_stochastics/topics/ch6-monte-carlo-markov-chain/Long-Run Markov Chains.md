---
tags:
  - MATH_114
---
# Example 1 (Stationary Distributions)
Consider a $2-$state [[Markov Chains|Markov Chain]] with $S = \{0, 1\}$.
$$
P = \begin{pmatrix}
3/4 & 1/4 \\ 1/6 & 5/6 \\
\end{pmatrix}
$$
and $\P(X_{1} = 0 \,|\, X_{0} = 0) = 3/4$ etc. Then 
$$
\lim_{n\to \infty} p^{n} = 
\begin{pmatrix}
0.4 & 0.6 \\ 0.4 & 0.6
\end{pmatrix}
= 
\begin{bmatrix}
\pi \\ \pi
\end{bmatrix}
$$
where $\pi = (0.4, 0.6)$ is the **stationary distribution**. 

Proof:

Let $\pi_{0} = (a_{0}, a_{1}) = (\P(X_{0} = 0), \P(X_{0} = 1))$. Note that $a_{0} + a_{1} = 1$. Then 
$$
\pi_{n} = [\P(X_{n} = 0), \P(X_{n} = 1)] = \pi_{0}p^{n}
$$
which implies that 
$$
\lim_{n\to \infty} \pi_{n} = \lim_{n \to \infty} \pi_{0} p^{n}
$$
from [[Markov Chains#Proposition (Stochastic Properties)]]. We get
$$
\lim_{n \to \infty} \pi_{0}p^{n}
= (a_{0}, a_{1}) \begin{pmatrix}
0.4 & 0.6 \\ 0.4 & 0.6 \\
\end{pmatrix}
= (0.4, 0.6)
= \pi 
$$
# Example 2 (Starting Distributions Don't Matter)
Suppose we have $3-$states and $S = \{0, 1, 2\}$ and 
$$
P = \begin{pmatrix}
3/4 & 1/4 & 0 \\ 1/8 & 2/3 & 5/24 \\ 0 & 5/6 & 1/6 \\
\end{pmatrix}
$$
With $\P$ being defined as usual. Then 
$$
\lim_{n\to\infty} p^{n} = \begin{pmatrix}
\pi \\ \pi \\ \pi
\end{pmatrix}
$$
where $\pi = (2/11, 4/11, 5/11)$. 

Set $\pi_{0} = (\P(X_{0} = i))$. Then $\pi_{n} = \pi_{0}p^{n}$ such that 
$$
\lim_{n\to \infty} \pi_{n} = \pi_{0} \cdot \begin{pmatrix}
\pi \\ \pi \\ \pi
\end{pmatrix}
= 
\left(
\pi(1) \cdot \sum_{i} \pi_{0}(i), \dots
\right)
= \pi 
$$
Because the sum of the starting distribution must equal $1$, it does not matter what distribution we start from. We will always return to stationary vector $\pi$. 

## Remark 
1. For any state $j$, the probability of a system being that state at time $n$ approaches a fixed value $\pi(j)$ as $n$ goes to infinity.
   $$
   \lim_{n\to \infty} \P(X_{n} = j) = \pi(j)
   $$
   Essentially, after enough time, the specific starting state is irrelevant. 
2. Once the distribution reaches the long-term state $\pi$, it stays there. The distribution is **invariant** under the transition matrix $P$.
   $$
   \begin{aligned}
   \pi = \lim_{n\to \infty} \pi_{n+1} 
   &= \lim_{n\to\infty} \pi_{0} p^{n+1} \\
   &= \lim_{n\to\infty} (\pi_{0} p^{n}) \cdot p \\
   &= \pi P
   \end{aligned}  
   $$
   So we get that $\pi$ is a row eigenvector of $P$. 
