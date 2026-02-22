---
tags:
  - MATH_114
aliases:
  - SDE
  - SDEs
---
# Stochastic Processes
Read [[Stochastic Process]].

# Random Walk on the Reals
We want to generalize stochastic processes to continuous time and continuous state spaces. Consider the random walk on $\R$. 

Let $Z_{0}, \dots, Z_{n} \sim \mathcal{N}(0, 1)$ be [[Normal]] iid RVs and consider 
$$
X_{n+1} = X_{n} + \delta t^{\alpha} \cdot Z_{n}, 
\quad\quad\quad n = 0, 1, 2, \dots
$$
and $X_{0} = 0$. Recall this form from [[Non-Stochastic Processes#Continuum Limit of Difference Equations|the continuum limit]]. Expanding this sequence yields:
- $X_{1} = \delta t^{\alpha} Z_{1}$
- $X_{2} = \delta t^{\alpha} (Z_{1} + Z_{2})$
- $X_{n} = \sum_{i=0}^{n-1} \delta t^{\alpha} Z_{i}$
Because the [[Normal#Theorem (Sum of Independent Normal RVs)|sum of normally distributed RVs is normal]], $X_{n}$ is normally distributed. The [[Moments]] of this process are 
- $\E{X_{n}} = 0$
- $\var(X_{n}) = n \delta t^{2\alpha}$
This establishes the distribution 
$$
X_{n} \sim \mathcal{N}\left(0, n \delta t^{2 \alpha} \right)
$$
## Continuum Limit of the Random Walk 
To determine if there is a continuous limit $X(t)$ such that $X_{n} \to X(t)$ as $n \to \infty$, the observation time $t  =n \delta t$ must remain fixed. We can analyze the variance under this limit:
$$
\var(X_{n}) = n \delta t^{2\alpha} = t \cdot \delta t^{2\alpha - 1} \to 
\begin{cases}
0 & \alpha > \frac{1}2 \\
\infty & \alpha < \frac{1}{2}
\end{cases}
$$
as $\delta t \to 0$. In fact, the continuum limit only exists for $\alpha = 1/2$. 
> We look at the variance because the mean provides no information. 
### Brownian Motion and SDE Formulation
- The continuum limit $X(t)$ is called Brownian Motion or Wiener process.
- Discretized form for $X_{n} \in \R$:
  $$
  X_{n+1} = X_{n} + \sqrt{\delta t } \cdot Z_{n}
  $$
  for $Z_{0}, Z_{1}, \dots, \sim \mathcal{N}(0, 1)$ iid. 
- The SDE notation for $X(t) \in \R$ is written as 
  $$
  \underbrace{dx}_{\text{increment of $X$}} = 
  \underbrace{dB}_{\text{Brownian increment}}
  $$
- We can think of SDEs in terms of discrete equations with $\delta t \to 0$.