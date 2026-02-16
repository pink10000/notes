---
tags:
  - MATH_114
---
# Example 1 (Glauber Dynamics for Ising Model)
Related: [[Ising Model]]

States: 
$$
S = \{ \unl{\sigma} = (\sigma_1, \dots, \sigma_{m}) \quad \sigma_j = +1, -1 \}
$$
Target: 
$$
\pi, \quad \pi(\underline{\sigma}) = \frac{b(\underline{\sigma})}{Z} > 0 \quad \forall \underline{\sigma} \in S
$$
Notation:
$$
\begin{aligned}
\underline{\sigma}^{j, +1} &= (\sigma_1, \dots, \sigma_{j-1}, +1, \sigma_{j+1}, \dots, \sigma_m) \\
\underline{\sigma}^{j, -1} &= (\sigma_1, \dots, \sigma_{j-1}, -1, \sigma_{j+1}, \dots, \sigma_m)
\end{aligned}
$$
Here we have a high dimensional state space. The goal is to sample from a distribution $\pi$ proportional to the weight function $b$. The constant $Z$, of course, is the [[Long-Run Markov Chains#Remark (Discreteness)|partition function]], which is often impossible to compute. We use the following notation to represent updates to the entire system. 

# Glauber dynamics (Random-scan Gibbs sampler)
- Given $X_n \in S$
- Assume $X_n = \underline{\sigma} \in S$

1. Choose $J$ uniformly at random from $\{1, 2, \dots, m\}$. (i.e. we pick a random spin)
2. Set 
   $$
   \alpha_+ = \frac{\pi(\underline{\sigma}^{J, +1})}{\pi(\underline{\sigma}^{J, -1}) + \pi(\underline{\sigma}^{J, +1})}
   $$
   Set $$
   \alpha_- = \frac{\pi(\underline{\sigma}^{J, -1})}{\pi(\underline{\sigma}^{J, -1}) + \pi(\underline{\sigma}^{J, +1})}
   $$
   (Note: $\alpha_+ + \alpha_- = 1$). This is the relative probability of that specific spin being $+1$ or $-1$ conditioned on the fact that all the other spins are fixed. The partition function $Z$ cancels out in these fractions. 

3. Set $X_{n+1} \leftarrow \underline{\sigma}^{J, +1}$ with prob. $\alpha_+$
4. Set $X_{n+1} \leftarrow \underline{\sigma}^{J, -1}$ with prob. $\alpha_-$

## Remarks
Each "spin" is in $\{-1, +1\}$. Set $J$th spin conditional on the value of every other spin. For example, let $m = 2$, such that 
$$
\pi(-1, -1) = \frac{1}{Z},
\quad
\pi(+1, -1) = \frac{2}Z,
\quad
\pi(-1, +1) = \frac{3}Z,
\quad
\pi(+1, +1) = \frac{5}{Z}
$$
Suppose $X_{k} = (-1, -1)$ and $J = 2$. Then 
$$
\begin{aligned}
\unl{\sigma}^{J, +1} &= (-1, +1) \\
\unl{\sigma}^{J, -1} &= (-1, -1) \\
\end{aligned}
$$
such that 
$$
\begin{aligned}
\alpha_{+} &= \frac{3}{1 + 3} = \frac{3}{4} \\
\alpha_{-} &= \frac{1}{1 + 3} = \frac{1}{4} \\
\end{aligned}
$$
We can see that $\alpha_{+} + \alpha_{-} = 1$. Then, 
$$
\P(X_{k+1} = (-1, +1) \mid X_{k} = (-1, -1)) = \frac{1}{2} \cdot \frac{3}{4} = \frac{3}{8}
$$
where the first product term is the probability of selecting particle $2$, or $1/J$, and the second is $\alpha_{+}$. 

# General Case of the Gibbs Sampler
The goal of this algorithm is to sample from complex, high-dimensional probability distributions that are difficult to compute directly. 

| Ising model | $\rightsquigarrow$ | General case                                                    |
| :------------------------------------ | :----------------: | :------------------------------------ |
| $\underline{\sigma} = (\sigma_1, \dots, \sigma_m)$ | $\rightsquigarrow$ | $\underline{x} = (x_1, \dots, x_m)$ |
| $\sigma_j \in \{-1, +1\}$ | $\rightsquigarrow$ | $x_j \in \mathbb{R}$                                            |
| $\pi(\underline{\sigma}) = \pi(\sigma_1, \dots, \sigma_m)$       | $\rightsquigarrow$ | $f(\underline{x}) = f(x_1, \dots, x_m)$ (unknown normalization) |
| $\pi(\sigma_j \mid \sigma_1, \dots, \sigma_{j-1}, \sigma_{j+1}, \dots, \sigma_m)$ | $\rightsquigarrow$ | $f(x_j \mid x_1, \dots, x_{j-1}, x_{j+1}, \dots, x_m)$          |
| PMF on $\sigma_j \in \{-1, +1\}$                                                  | $\rightsquigarrow$ | PDF on $x_j \in \mathbb{R}$                                     |

The conditional distribution does not require normalization. 