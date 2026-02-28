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
\infty & \alpha < \frac{1}{2} \\
t & \alpha = \frac{1}2 \\
\end{cases}
$$
as $\delta t \to 0$. In fact, the continuum limit only exists for $\alpha = 1/2$, i.e. there exists a finite, non-zero $X(t)$ such that $X_{n} \to X(t)$ as $n \to \infty, \delta t \to 0$ with $n \cdot \delta t = t$ fixed.
> We look at the variance because the mean provides no information. The discussion above is also non-rigorous. The continuum limit $X(t)$ is called **Brownian motion**/**Wiener process**. 
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

# Definition (Brownian Motion, Wiener Process)
**Brownian Motion** (BM) is a time-homogeneous, continuous-time, continuous state [[Markov Chains#Definition (Markov Process)|Markov Process]]. At [[Stochastic Process]] $B(t) \in \R$ for $t \geq 0$ is a Brownian Motion if:
1. $B(0) = 0$ with probability $1$.
2. $B(t) - B(s) \sim N(0, t - s)$ for all $t \geq s \geq 0$. In particular, $B(t) \sim N(0, t)$. 
3. For any $0 = t_{0} \leq t_{1} \leq \cdots \leq t_{n}$, the RVs $B(t_{1}) - B(t_{0}), \dots, B(t_{n}) - B(t_{n-1})$ are independent. These are called independent increments
4. $B(t)$ is a continuous function for $t \geq 0$.

From $(2)$, $B(t + \delta t) - B(t) \sim N(0, \delta t)$ for $\delta t > 0$. This implies that 
$$
B(t + \delta t) - B(t) = \sqrt{\delta t} \cdot Z
$$
for $Z \sim \mathcal{N}(0, 1)$. See [[#Brownian Motion and SDE Formulation]]. 

BM is [[Continuity#Definition (Point)|continuous]] but nowhere [[Derivative#Theorem (Differentiable is Continuous)|differentiable]]. From above, we see that 
$$
\frac{B(t + \delta t) - B(t)}{\delta t} 
= \frac{\sqrt{\delta t} \cdot Z}{\delta t}
= \frac{1}{\sqrt{\delta t}} \cdot Z
$$
for $Z \sim \mathcal{N}(0, 1)$. 

## Properties of Brownian Motion
- Since $B(t)$ for $t \geq 0$ is a Markov process, then for $0 \leq t_{1}\leq \dots t_{n} \leq t$, we have that 
  $$
  \P(B(t) \leq b \mid B(t_{1}), \dots , B(t_{n}))
  = \P(B(t) \leq b \mid B(t_{n}) )
  $$
- From $(2)$, we can have $B(t) - B(0) \sim \mathcal{N}(0, t)$. This implies that $\E{B(t)} = 0$ and $\E{B(t)^{2}} = t$, i.e. the mean and variance. We can write $B(t) = \sqrt{t}Z$ for $Z \sim \mathcal{N}(0, 1)$.
- The following processes are BMs. It is sufficient to check $\tilde B(t)$ for all four properties above, if $B(t)$ is already a BM.
	- $\tilde B(t) = -B(t), t\geq 0$
	- $\tilde B(t) = B(t + t_{0})  - B(t_{0})$ for any $t_{0}> 0$
	- $\tilde B(t) = B(\lambda t)/\sqrt{\lambda}$ for any $\lambda > 0$
- The transition probability density is denoted as $p(y, t \mid x, s)$ for $s < t$, where 
  $$
  \begin{aligned}
  \int_{a}^{b} p(y, t \mid x , s) \, dy
  &= \P(a < B(t) < b \mid B(s) = x) \\
  &= \P(a - x < B(t) - B(s) < b - x) \\
  &= \P(a < \sqrt{t - s} \cdot Z + x < b) 
  \end{aligned}
  $$
  for $Z \sim \mathcal{N}(0, 1)$. This implies that $p(y, t \mid x, s)$ is a [[Probability Distribution Function|PDF]] of [[Normal]] $\mathcal{N}(x, t - s)$, or
  $$
  = \frac{1}{\sqrt{2\pi(t - s)}} \exp\left( - \frac{(y - x)^{2}}{2(t - s)}  \right)
  $$
- $B(t), B(s)$ are not independent. Indeed, their [[Covariance]] is as follows:
  $$
  \begin{aligned}
  \Cov(B(t), B(s))
  &= \E{ B(t) \cdot B(s) } - \E{B(t)} \cdot \E{B(s)} \\
  &= \E{ B(t) \cdot B(s) } - 0 \\
  &= \E{ [B(t) - B(s)] \cdot [B(s) - B(0)] + B(s)^{2}} \\
  &= \E{B(t) - B(s)} \cdot \E{B(s) - B(0)} + \E{B(s)^{2}} \\
  &= 0 + \E{B(s)^{2}} \\
  &= \var(B(s)) \\
  &= s
  \end{aligned}
  $$
  In particular, $\E{B(t) \cdot B(s)} = \min(s, t)$. 

## Example 1
We know $\E{B(3)} = 0$ and $\E{B(3)^{2}} = 3$. Then 
$$
\begin{aligned}
\P(B(8) \leq 4 \mid B(2) = 1)
&= \P(B(8) - B(2) \leq 3) \\
&= \P(\sqrt{6} Z \leq 3) \\
&= \P\left(Z \leq \sqrt{3/2}\right) \\
&= \frac{1}{\sqrt{2\pi } } \int_{0}^{\sqrt{3/2}} \exp \left(- \frac{1}{2}x^{2} \right) \, dx \\
&= \mathbf{\Phi}\left(\frac{3}{2}\right)
\end{aligned}
$$
relating how BM and the normal distribution. 

# Ornstein-Uhlenbeck Process (OU)
The Ornstein-Uhlenbeck (OU) process is defined by the stochastic differential equation:
$$
dX=-\alpha Xdt+\sqrt{2D}dB
$$
with initial condition $X(0)=x_{0}$.

## Euler's Method for OU Process
Algorithm for discrete simulation:
1. Set $\delta t>0$, $n\in\mathbb{Z}$, and $t_k=k\delta t$ for $k=0,1,2,\dots,n$.
2. Set $X_0=x_0$.
3. For $i=0$ to $n-1$:
	1. Generate $Z\sim\mathcal{N}(0,1)$.
	   $$
	   X_{i+1}=X_i-\alpha X_i\delta t+\sqrt{2D\delta t}Z
	   $$
4. The sequence $X_{i}$ approximates the true continuous solution $X(t_{i})$.

## Moments of the OU Process
Evaluate the first moment by applying the expectation operator to the SDE.
$$
dX=-\alpha Xdt+\sqrt{2D}dB
$$
Taking the expectation $\mathbb{E}$ yields:
$$
d\mathbb{E}[X]=-\alpha\mathbb{E}[X]dt
$$
This translates to an ordinary differential equation (ODE) for the expectation:
$$
\frac{d}{dt}\mathbb{E}[X]=-\alpha\mathbb{E}[X]
$$
To solve this ODE, let $y(t)=\mathbb{E}[X(t)]$. The differential equation becomes:
$$
\frac{dy}{dt}=-\alpha y
$$
Solving this linear ODE with the initial condition $y(0)=x_{0}$ yields:
$$
y=x_0e^{-\alpha t}
$$
Substituting the expectation back provides the exact first moment:
$$
\mathbb{E}[X]=x_0e^{-\alpha t}
$$
