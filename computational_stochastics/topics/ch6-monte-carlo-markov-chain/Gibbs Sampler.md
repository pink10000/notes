---
tags:
  - MATH_114
---
# Example 1 (Glauber Dynamics for Ising Model)
Related: [[Ising Model]]

States: 
$$
S = \{ \underline{\sigma} = (\sigma_1, \dots, \sigma_{m}) \mid \sigma_j = +1, -1 \}
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

# Glauber Dynamics (Special Case of Gibbs Sampler)
The idea is to use conditional distributions to determine the probability of spin $\sigma_{j}$ or $V_{j}$ taking value $\tau$ where $\tau \in \{+1, -1\}$. For simplicity, let $\underline{\sigma} = \underline{V}$ and $\underline{V} \sim \pi$, so $\underline{V} = (V_{1}, \dots, V_{m}) \in S$. Consider the condition distribution of $V_{j}$ given by $V_{i}$ for $i \neq j$: 
$$
\begin{aligned}
\mathbb{P}(V_{j} = \tau \mid V_{1}, \dots V_{j-1}, V_{j+1}, \dots , V_{m}) 
&= \frac{\pi(V_{1}, \dots, V_{j-1}, \tau, V_{j+1}, \dots, V_{m})}{\pi(V_{1}, \dots, +1, \dots, V_{m}) + \pi(V_{1}, \dots, -1, \dots, V_{m})}
\end{aligned}
$$
where the $+1, -1$ in the denominator denotes the $j$th entry. This is only nonzero for $\tau = +1, -1$. Let 
$$
\begin{aligned}
\pi_{j}(\tau \mid \sigma_{1}, \dots, \sigma_{m-1})
&= \mathbb{P}(V_{j} = \tau \mid (V_{1}, \dots, V_{j-1}, V_{j+1}, \dots, V_{m}) = (\sigma_{1}, \dots, \sigma_{m-1}))
\end{aligned}
$$
for $\underline{V} \sim \pi$. Caution: Some conventions use $\pi(\cdot \mid \cdot)$ instead of $\pi_j(\cdot \mid \cdot)$.
# Glauber Dynamics (Random-scan Gibbs sampler)
Given $X_k = \underline{x}_k = (x_{k,1}, \dots, x_{k,m}) \in S$.

1. Choose $J$ uniformly at random from $\{1, 2, \dots, m\}$.
2. Sample $Y$ from the conditional distribution 
   $$
   \pi_J(\cdot \mid x_{k,1}, \dots, x_{k,J-1}, x_{k,J+1}, \dots, x_{k,m})
   $$
3. Set $X_{k+1} \leftarrow (x_{k,1}, \dots, x_{k,J-1}, Y, x_{k,J+1}, \dots, x_{k,m})$.

## Algorithmic Implementation (Discrete State Space)
For a discrete system like the [[Ising Model]] where $\sigma_j \in \{-1, +1\}$, Step 2 is implemented by calculating the explicit scalar probabilities for the two possible states of the $J$-th coordinate. 

Assume $X_k = \underline{\sigma} \in S$.

1. Set $\alpha_+$ as the probability of the $J$-th spin being $+1$:
$$
\alpha_+ = \pi_J(+1 \mid \sigma_{-J}) = \frac{\pi(\underline{\sigma}^{J, +1})}{\pi(\underline{\sigma}^{J, -1}) + \pi(\underline{\sigma}^{J, +1})}
$$
2. Set $\alpha_-$ as the probability of the $J$-th spin being $-1$:
$$
\alpha_- = \pi_J(-1 \mid \sigma_{-J}) = \frac{\pi(\underline{\sigma}^{J, -1})}{\pi(\underline{\sigma}^{J, -1}) + \pi(\underline{\sigma}^{J, +1})}
$$
Note $\alpha_+ + \alpha_- = 1$. The partition function $Z$ cancels out in these fractions.

3. Branch execution:
* Set $X_{k+1} \leftarrow \underline{\sigma}^{J, +1}$ with probability $\alpha_+$.
* Set $X_{k+1} \leftarrow \underline{\sigma}^{J, -1}$ with probability $\alpha_-$.

> Here, this requires a *discrete* state space, where $\sigma_{j} \in \{-1, +1\}$.

## Example 2
Each "spin" is in $\{-1, +1\}$. Set $J$th spin conditional on the value of every other spin. For example, let $m = 2$, such that 
$$
\pi(-1, -1) = \frac{1}{Z}, \quad 
\pi(+1, -1) = \frac{2}{Z}, \quad 
\pi(-1, +1) = \frac{3}{Z}, \quad 
\pi(+1, +1) = \frac{5}{Z}
$$
Suppose $X_{k} = (-1, -1)$ and $J = 2$. Then 
$$
\begin{aligned}
\underline{\sigma}^{J, +1} &= (-1, +1) \\
\underline{\sigma}^{J, -1} &= (-1, -1)
\end{aligned}
$$
such that 
$$
\begin{aligned}
\alpha_{+} &= \frac{3}{1 + 3} = \frac{3}{4} \\
\alpha_{-} &= \frac{1}{1 + 3} = \frac{1}{4}
\end{aligned}
$$
We can see that $\alpha_{+} + \alpha_{-} = 1$. Then, 
$$
\mathbb{P}(X_{k+1} = (-1, +1) \mid X_{k} = (-1, -1)) = \frac{1}{2} \cdot \frac{3}{4} = \frac{3}{8}
$$
where the first product term is the probability of selecting particle $2$, or $1/m$, and the second is $\alpha_{+}$. 

## Example 3
Assume we have the same setup as Example 2. Then the conditional distribution $\pi_{2}$ is 
$$
\begin{aligned}
\pi_{2}(-1 \mid +1) &= \mathbb{P}(\text{entry 2} = -1 \mid \text{entry 1} = +1) \\
&= \frac{\pi(+1, -1)}{\pi(+1, -1) + \pi(+1, +1)} \\
&= \frac{2}{7}
\end{aligned}
$$
Likewise, 
$$
\begin{aligned}
\pi_{2}(+1 \mid +1) 
&= \frac{\pi(+1, +1)}{\pi(+1, -1) + \pi(+1, +1)} \\
&= \frac{5}{7}
\end{aligned}
$$
Remarks:
- $\pi_{2}(\cdot \mid +1)$ is a [[Probability Distribution Function|PMF]] on $\{-1, +1\}$, just like $\pi_{1}(\cdot \mid -1), \pi_{1}(\cdot \mid +1), \pi_{2}(\cdot \mid -1)$ 
- Conditional distributions do not require knowledge on the normalization $Z$.
# General Case of the Gibbs Sampler
The goal of this algorithm is to sample from complex, high-dimensional probability distributions that are difficult to compute directly. 

| Ising model | $\rightsquigarrow$ | General case |
| :--- | :---: | :--- |
| $\underline{\sigma} = (\sigma_1, \dots, \sigma_m)$ | $\rightsquigarrow$ | $\underline{x} = (x_1, \dots, x_m)$ |
| $\sigma_j \in \{-1, +1\}$ | $\rightsquigarrow$ | $x_j \in \mathbb{R}$ |
| $\pi(\underline{\sigma}) = \pi(\sigma_1, \dots, \sigma_m)$ | $\rightsquigarrow$ | $f(\underline{x}) = f(x_1, \dots, x_m)$ (unknown normalization) |
| $\pi(\sigma_j \mid \sigma_1, \dots, \sigma_{j-1}, \sigma_{j+1}, \dots, \sigma_m)$ | $\rightsquigarrow$ | $f(x_j \mid x_1, \dots, x_{j-1}, x_{j+1}, \dots, x_m)$ |
| PMF on $\sigma_j \in \{-1, +1\}$ | $\rightsquigarrow$ | PDF on $x_j \in \mathbb{R}$ |

The conditional distribution does not require the global normalization constant. The continuous conditional distribution is computed as:
$$
f_{j}(y \mid x_{1}, \dots, x_{m-1}) = \frac{f(x_{1}, \dots, x_{j-1}, y, x_{j+1}, \dots, x_{m})}{\int_{\mathbb{R}} f(x_{1}, \dots, x_{j-1}, y, x_{j+1}, \dots, x_{m}) dy}
$$

So $f_j(\cdot \mid x_1, \dots, x_{m-1})$ is a PDF on $\mathbb{R}$. Note that the denominator is an integral, in the same way that in the [[#Algorithmic Implementation (Discrete State Space)|discrete space]], we sum the possibilities for that flip. This denotes the space of all possibilities that $x_{j}$ can become. In our case, we care about when $\P(x_{j} = y)$ specifically. 

# Example 4
Let 
$$
f(x, y) = c \exp\left( -(x^{2} + 1)(y^{2} + 1) \right), \quad\quad (x,y) \in \R^{2}
$$
$c$ is a normalization, so 
$$
\int_{\R^{2}} c \exp\left( -(x^{2} + 1)(y^{2} + 1) \right) \,dxdy = 1
$$
What are the conditional distributions? We see that 
$$
\begin{aligned}
f_{1}(x \mid y) 
&= \frac{
  c \exp\left( -(x^{2} + 1)(y^{2} + 1) \right)
}{
  \int_{\R} f(x, y) \, dx 
} \\
&= c_{1}(y) \exp\left( -(y^{2} + 1)x^{2}  \right)
\end{aligned}
$$
by treating $y$ as a constant and expanding out $f(x, y)$. Here, we apply the continuous conditional distribution from [[#General Case of the Gibbs Sampler]]. Then, $c_{1}(y)$ is such that 
$$
\int_{-\infty}^{\infty} c_{1}(y) \exp\left( -(y^{2} + 1)x^{2}  \right) \, dx = 1
$$
for all $y \in \R$. In other words, $c_{1}(y)$ is the normalization of the [[Probability Distribution Function|PDF]] 
$$
f_{1}(x \mid y) \propto \exp\left( -(y^{2} + 1)x^{2}  \right)
$$
Recall that $Z \sim N(0, \sigma^{2})$ has a PDF of 
$$
f_{Z}(z) \propto \exp\left( \frac{-1}{2\sigma^{2}} z^{2}  \right)
$$
This implies that $f_{1}(x \mid y)$ is the PDF of $N\left(0, \frac{1}{2(y^{2} + 1)} \right)$. Similarly, $f_{2}(y \mid x)$ is the PDF of $N\left(0, \frac{1}{2(x^{2} + 1)}\right)$.

# Algorithm (Random-Scan Gibbs Via Normal Distribution)
The previous examples gives the following insight: We can model the probabilities as part of the [[Normal]] distribution. 

Given $(X_{k}, Y_{k}) \in \R^{2}$. 
1. Choose $J$ uniformly at random from $\{1, 2\}$. Note that we are in $\R^{2}$. 
2. Generate $Z \sim N(0, 1)$. Recall [[Box-Muller Method]].
3. If $J = 1$, set 
   $$
   W = \frac{1}{\sqrt{2(Y_{k}^{2} + 1)}}Z \quad\quad (\text{i.e. } W \sim f_{1}(\cdot \mid Y_{k}))
   $$
   and set $(X_{k+1}, Y_{k+1}) \leftarrow (W, Y_{k})$.
4. If $J = 2$, set 
   $$
   W = \frac{1}{\sqrt{2(X_{k}^{2} + 1)}} Z \quad\quad (\text{i.e. } W \sim f_{2}(\cdot \mid X_{k}))
   $$
   and set $(X_{k+1}, Y_{k+1}) \leftarrow (X_{k}, W)$. 
# Algorithm (Systematic-Scan Gibbs Sampler)
Given $\underline{X}_{k} \in \mathbb{R}^{m}$:
1. Sample $Y_{1}$ from $f_{1}(\cdot \mid X_{k,2}, \dots, X_{k,m})$
2. For $i = 2$ to $m$:
Sample $Y_{i}$ from $f_{i}(\cdot \mid \underbrace{Y_{1}, \dots, Y_{i-1}, X_{k,i+1}, \dots, X_{k,m}}_{\in \R^{m-1}}  )$
3. Set $\underline{X}_{k+1} = (Y_{1}, \dots, Y_{m}) \in \mathbb{R}^{m}$

Output: $\underline{X}_{0}, \underline{X}_{1}, \dots \in \mathbb{R}^{m}$

Remarks:
- The Systematic-Scan chooses coordinates $j = 1, 2, \dots, m$ in strict order.
- The Random-Scan Gibbs Sampler is a special case of the Metropolis algorithm.

# Metropolis Algorithm (Random-Walk Sampler)
We can extend the [[Metropolis Algorithm#Metropolis Algorithm|Metropolis Algorithm]]. 
- Goal: Sample from target PDF $f(\unl{x})$ where $\unl{x} \in \R^{m}$. 
- Given $\unl{X}_{k} \in \R^{m}$,

1. Generate $\unl{Z} = (Z_{1}, \dots, Z_{m}) \in \R^{m}$ where $Z_{1}, \dots, Z_{m} \sim N(0, 1)$ iid. 
   > I.e., $\unl{Z} \sim N(\unl{0}, \Sigma)$ is [[Multivariate Normal]]. This is also our "noise", or a random directional perturbation.
2. Set proposal state $\unl{Y} = \unl{X}_{k} + \unl{Z}$. 
   > The proposal transition matrix $q(\unl{X}_{k}, \cdot)$ is a PDF of $N(\unl{X}_{k}, I_{m})$ 
3. Set
   $$
   \alpha = \min\left(1, \frac{f(\unl{Y})}{f(\unl{X}_{k})}  \right)
   $$
   and generate [[Uniform]] $U \sim \mathcal{U}[0, 1]$. 
   - Set $\unl{X}_{k+1} \leftarrow \unl{Y}$ if $U \leq \alpha$. 
   - Set $\unl{X}_{k+1} \leftarrow \unl{X}_{k}$ if $U < \alpha$.

Remarks:
- The output $\unl{X}_{0}, \unl{X}_{1}, \dots$ is a [[Markov Chains|Markov Chain]] on a continuous state space $\R^{m}$. 
- It is "sensitive" to the typical "jump" size $\unl{Z}$.
- What if happens if we take jumps $\ell Z$ and let $\ell \to 0$? We get SDEs! 
- $\ell$ is the spatial exploration rate of th random walk. 

# Remarks
1. We first define the [[Ising Model]] and use [[#Glauber Dynamics (Random-scan Gibbs sampler)|Glauber Dynamics]] algorithm to figure out how to sample from these difficult distributions. This is the most restricted class of MCMC: a discrete-space, single-coordinate update mechanism.
2. We generalize this via the [[Metropolis Algorithm]] to generalize transitions by permitting global state proposals via a transition matrix $Q$. At first, we let the transitions be symmetric, to show [[Invariant Distribution#Definition (Detailed Balance)|detailed balance]].
3. We further generalized this to show asymmetry via the [[Metropolis Algorithm#Metropolis-Hastings Algorithm|Metropolis Hastings Algorithm]] by having a ratio to penalize directional bias in the proposal distribution, forcing detailed balance.
4. We expand the problem domain from discrete states $\{-1, +1\}$ to the infinite continuous domain of $\R$. The target PMF $\pi(\unl{\sigma})$ becomes [[Probability Distribution Function|PDF]] $f(\unl{x})$. We generalize the discrete scalar fractions with continuous integrals to compute the conditional $f_{j}(y \mid x_{-j})$. The core mechanism is to update one dimension at a time while holding all others constant to bypass the global normalization integral.
5. We can generalize to multidimensional continuous transitions using additive noise in [[#Metropolis Algorithm (Random-Walk Sampler)]]. The proposal mechanism becomes a continuous Gaussian transition kernel.
6. Finally, we can further generalize this to continuous time steps by introducing the scaling factor $\ell$ to modify the variance of the Gaussian proposal jump to $\ell \unl{Z}$. By taking the limit $\ell \to 0$ and the discrete time step interval $\Delta t \to 0$ proportionally, the discrete [[Markov Chains|Markov Chain]] converges into a continuous-time mathematical model. This leads us to [[Stochastic Differential Equations]] (SDEs) over $t \in \R^{+}$. 
