---
tags:
  - MATH_114
---
# Problem 
Suppose we had a sample space $S = \{-1, +1\}^{N}$. and $|S| = 2^{N}$[^1]. Let $\sigma \in S$ where 
$$
\sigma = (\sigma_{1},\sigma_{2}, \dots, \sigma_{N})
$$
a chain of $\sigma_{i} =\pm 1$. Clearly, $|S|$ grows exponentially large the more spins we have. The probability of finding a state $\sigma \in S$ is 
$$
p(\sigma) = \frac{1}{Z} f(\sigma)
$$
where $f$ is easy to compute, and 
$$
Z = \sum_{\sigma \in S} f(\sigma)
$$
the normalization factor. $Z$ is hard to compute. 
[^1]: This is a problem from statistical physics. The values are the spin states of electrons. 

> This sets the stage for **Markov Chain Monte Carlo (MCMC)**. Since we cannot calculate $Z$, we cannot compute $p(\sigma)$ directly.