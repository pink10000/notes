---
tags:
  - MATH_114
---
The goal is to construct a [[Markov Chains|Markov Chain]] $\{X_{k}\}$ with a [[Invariant Distribution#Definition (Stationary or Invariant Distribution)|stationary distribution]] $\pi$. 

# Metropolis Algorithm
First, we construct the proposal transition matrix $Q = [q(i, j)]$ where $Q$ is [[Symmetric Matrix|symmetric]]. Then, choose an initial state $X_{0} \in S$ randomly. Given $X_{k} = i \in S$, 
1. Sample $Y \in S$ from $q(i, -)$, i.e. $\P(Y = y \,|\, X_{k} = i) = q(i, y)$ for all $y \in S$. We assume $Y = j$ is observed.
2. Let 
   $$
   \alpha = \alpha_{ij} = \min\left(1, \frac{\pi(j)}{\pi(i)}  \right) \in [0, 1]
   $$
   and generate $U \sim \mathcal{U}[0, 1]$. 
3. If $U \leq \alpha$ then accept $Y$ and $X_{k+1} \leftarrow Y$. 
4. If $U > \alpha$ then reject $Y$ and $X_{k+1} \leftarrow X_{k}$. 

This means we accept $Y$ with probability $\alpha$. The output is a sequence $X_{0}, X_{1}, \dots$ 

## Remarks About Computation 
- $\{X_{n}\}_{n=0}^{\infty}$ is a [[Markov Chains|Markov Chain]] with $\lim_{n \to \infty} X_{n} \sim \pi$. 
- We can choose $Q$ to be simple, like uniform jumps, where $q(i, j) = 1/N$. 
- We only need to now the ratio $\pi(j)/\pi(i)$, so we don't need to know the [[Long-Run Markov Chains#Remarks (Markov Chain Computation)|normalization value]] $Z$. 
- $Y$ is a *proposal state*.
- In practice, $\alpha = \alpha_{ij}$ is easy to calculate.
- This algorithm works for non-symmetric $Q$ and 
  $$
  \alpha = \alpha_{ij} = \min \left( 1, \frac{\pi(j)q(j, i)}{\pi(i)q(i, j)} \right)
  $$

# Example 1 (1D Ising Model)
Recall the [[Ising Model]], where we have $m$ particles each with spin $+$ or $-$. So, 
$$
S 
= \{ \sigma = (\sigma_{1}, \dots, \sigma_{m}) \,|\, \sigma_{i} = \pm 1, 1 \leq i \leq m \}
= \{-1, +1\}^{m}
$$
or the set of length $m$ strings of alphabet $-1, +1$. Obviously $|S| = 2^{m}$. 

Let 
$$
H(\sigma) = 
-J \sum_{i=1}^{m-1} \sigma_{i} \sigma_{i+1} - h \sum_{i=1}^{m} \sigma_{i}
$$
where $h> 0$[^1]. $H(\sigma)$ represents the "energy" of state $\sigma$. 
[^1]: This is the [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics).

Our target distribution[^2] is 
$$
\pi_{\beta}(\sigma) = \frac{1}{Z_{\beta}} \exp \left( - \beta H(\sigma) \right)
\quad\quad\quad
\forall \sigma \in S
$$
where $\beta > 0$ is the inverse temperature $(\beta = 1/k_{\beta}T)$, and $Z_{\beta}$ is normalization (partition function). This is hard to compute. 
[^2]: This is the [Boltzmann Distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution). 

Note that a large $\pi_{\beta}(\sigma) \iff$ small $H(\sigma) \iff$ many $\sigma_{j} = +1$ and many 
$$
\sigma_{j}\sigma_{j+1} = \begin{cases}
> 0 & \text{if } J > 0 \\
< 0 & \text{if } J < 0 \\ 
\end{cases}
$$
Here, we can apply the [[#Metropolis Algorithm]]. Choose $Q$ given by the random spin flips. For example, if $m = 2$:
```tikz
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,calc}
\tikzset{curve/.style={settings={#1},to path={(\tikztostart) .. controls ($(\tikztostart)!\pv{pos}!(\tikztotarget)!\pv{height}!270:(\tikztotarget)$) and ($(\tikztostart)!1-\pv{pos}!(\tikztotarget)!\pv{height}!270:(\tikztotarget)$) .. (\tikztotarget)\tikztonodes}}, settings/.code={\tikzset{quiver/.cd,#1}\def\pv##1{\pgfkeysvalueof{/tikz/quiver/##1}}}, quiver/.cd,pos/.initial=0.35,height/.initial=0}
\begin{document}
% https://q.uiver.app/#q=WzAsNCxbMSwwLCIrKyJdLFsyLDEsIistIl0sWzEsMiwiLS0iXSxbMCwxLCItKyJdLFszLDAsIjEvMiIsMSx7ImN1cnZlIjoxfV0sWzAsMywiMS8yIiwyLHsiY3VydmUiOjF9XSxbMSwwLCIxLzIiLDEseyJjdXJ2ZSI6LTF9XSxbMCwxLCIxLzIiLDAseyJjdXJ2ZSI6LTF9XSxbMiwxLCIxLzIiLDEseyJjdXJ2ZSI6LTF9XSxbMSwyLCIxLzIiLDAseyJjdXJ2ZSI6LTF9XSxbMiwzLCIxLzIiLDEseyJjdXJ2ZSI6MX1dLFszLDIsIjEvMiIsMix7ImN1cnZlIjoxfV1d
\begin{tikzcd}
	& {++} \\
	{-+} && {+-} \\
	& {--}
	\arrow["{1/2}"', curve={height=6pt}, from=1-2, to=2-1]
	\arrow["{1/2}", curve={height=-6pt}, from=1-2, to=2-3]
	\arrow["{1/2}"{description}, curve={height=6pt}, from=2-1, to=1-2]
	\arrow["{1/2}"', curve={height=6pt}, from=2-1, to=3-2]
	\arrow["{1/2}"{description}, curve={height=-6pt}, from=2-3, to=1-2]
	\arrow["{1/2}", curve={height=-6pt}, from=2-3, to=3-2]
	\arrow["{1/2}"{description}, curve={height=6pt}, from=3-2, to=2-1]
	\arrow["{1/2}"{description}, curve={height=-6pt}, from=3-2, to=2-3]
\end{tikzcd}
\end{document}
```
we get the following. If $S = \{++, +- , -+, --\}$, then the transition matrix is:
$$
P = \begin{bmatrix}
0 & 1/2 & 1/2 & 0 \\
1/2 & 0 & 0 & 1/2 \\
1/2 & 0 & 0 & 1/2 \\
0 & 1/2 & 1/2 & 0 \\
\end{bmatrix}
$$
which is [[Symmetric Matrix|symmetric]]. Choose $X_{0} \in S$ given $X_{k} = (\sigma_{1}, \dots, \sigma_{m}) \in S$. Some notes, 
- $J$ represents the interaction strength between particles. It can be treated as a constant. 
- $h$ is the external magnetic field on the particles. We can treat it as a constant. 

Algorithm:
1. Choose a site $i$ for $1 \leq i \leq m$ uniformly at random among $1,2, \dots, m$. 
2. Flip the $i$th site $\sigma_{i} \to -\sigma_{i}$ to obtain the proposal state:
   $$
   \hat{\sigma} = (\sigma_{1}, \dots, \sigma_{i-1}, -\sigma_{i}, \sigma_{i+1}, \dots, \sigma_{m}) \in S
   $$
   Note that $q(\sigma, \hat\sigma) = q(\hat\sigma, \sigma) = 1/m$. This shows $Q$ is symmetric. 
3. Compute
   $$
   \begin{aligned}
   \frac{\pi(\hat\sigma)}{\pi(\sigma)} 
   &= \exp\left[ -\beta(H(\hat\sigma) - H(\sigma)) \right] \\
   &= \exp(- \beta \Delta H)
   \end{aligned}
   $$
   Recall that we do this to avoid the [[Long-Run Markov Chains#Remark (Discreteness)|partition function]].
4. Three cases for $\Delta H$:
	1. If $1 < i < m$, (we picked a particle in the middle of the chain) then 
	   $$
	   \begin{aligned}
	   H(\hat\sigma) - H(\sigma) 
	   &= -J(\sigma_{i-1}(-\sigma_{i}) - \sigma_{i}\sigma_{i+1}) + h\sigma_{i} 
	   -\left[ -J(\sigma_{i-1}\sigma_{i} + \sigma_{i}\sigma_{i+1}) - h\sigma_{i} \right] \\
	   &= 2J\sigma_{i}(\sigma_{i-1} + \sigma_{i+1}) + 2h\sigma_{i}
	   \end{aligned}
	   $$
	2. If $i = 1$ (the left boundary), then 
	   $$
	   \begin{aligned}
	   H(\hat\sigma) - H(\sigma) 
	   &= -J(-\sigma_{1})\sigma_{2} + h\sigma_{1} - \left[ -J\sigma_{1} \sigma_{2} - h\sigma_{1} \right] \\
	   &= 2J\sigma_{1} \sigma_{2} + 2h\sigma_{1} 
	   \end{aligned}
	   $$
	3. If $i = m$ (the right boundary), similarly 
	   $$
	   \begin{aligned}
	   H(\hat\sigma) - H(\sigma) = 2J \sigma_{m-1} \sigma_{m} + 2h\sigma_{m} 
	   \end{aligned}
	   $$
	   Thus, 
	   $$
	   \Delta H = H(\hat\sigma) - H(\sigma) = \begin{cases}
	   2 J \sigma_{i}(\sigma_{i-1} + \sigma_{i+1}) + 2h\sigma_{i} & 1 < i < m\\
	   2 J \sigma_{1} \sigma_{2} + 2h \sigma_{1} & i = 1 \\
	   2 J \sigma_{m-1} \sigma_{m} + 2h \sigma_{m} & i = m
	   \end{cases}
	   $$
	4. We can then accept $\hat\sigma$ with probability
	   $$
	   \alpha 
	   = \min \left( 1, \frac{\pi(\hat\sigma)}{\pi(\sigma)}  \right)
	   = \min \left( 1, e^{-\beta \Delta H} \right)
	   $$
	5. Thus, 
		1. If $\Delta H \leq 0$ then $\alpha = 1$ and set $X_{k+1} \leftarrow \hat\sigma$. (Here, the system lost energy, i.e. became more stable, so the second term is positive and thus greater than $1$. We will accept).
		2. If $\Delta H > 0$ then $\alpha = \exp(-\beta \Delta H)$. (This is the opposite of above.) 
			1. Generate $U \sim \mathcal{U}[0, 1]$. 
			2. If $U \leq \exp(-\beta\Delta H)$, accept $\hat\sigma$ and $X_{k+1} \leftarrow \hat\sigma$
			3. If $U > \exp(-\beta\Delta H)$, reject $\hat\sigma$ and $X_{k+1} \leftarrow \sigma$. 

Why does it work?
- In step 2, we do not calculate $H$ since it is computationally inefficient. However, we can calculate the change, $\Delta H$. Every term in $H(\sigma)$ cancels out **but the changed term**. This means we only need to find the sum of a few terms.
- The Ising model only involves interactions with the nearest neighbors. This is why we see changes in $\sigma_{i-1}$ and $\sigma_{i+1}$, reducing the computations needed from $O(m)$ to $O(1)$. 

# Theorem (Metropolis Satisfies Detailed Balance)
1. The transition matrix $P = [p(i, j)]$ of the Metropolis Chain is 
   $$
   p(i, j) = \begin{cases}
   q(i, j) \cdot \min\left(1, \frac{\pi(j)}{\pi(i)} \right) & i \neq j \\
   1 - \sum_{k \in S \setminus\{i\}} q(i, k)\cdot \min\left(1, \frac{\pi(j)}{\pi(i)} \right) & i = j
   \end{cases}
   $$
	1. The idea in case $1$ is that we propose moving from $i \to j$ with probability $q(i, j)$ in Metropolis, but we accept this movement $\alpha(i, j)$ times. This is just the probability of these two events happening together.
	2. In case $2$, accounts for the probability of rejection. Indeed, $p(i, i)$ is the sum of chances we tried to move but failed.
2. $\pi$ and $P$ satisfy [[Invariant Distribution#Definition (Detailed Balance)|detailed balance]]: 
   $$
   \pi(i) \cdot p(i, j) = \pi(j) \cdot p(j, i)
   $$
   for all $i,j \in S$. (Hence $\pi$ is a [[Invariant Distribution#Definition (Stationary or Invariant Distribution)|stationary distribution]].)
3. If $\forall i, j \in S, q(i, j) > 0$ and $\forall i \in S, p(i, i) > 0$, then $\pi$ is unique, and 
   $$
   \lim_{n \to \infty} \pi_{0} P^{n} = \pi
   $$
Proof: 

$(1)$: For $i \neq j,$ 
$$
\begin{aligned}
p(i, j) 
&= \P(\text{propose } j  \mid i) \cdot \P(\text{accept }j \mid \text{proposed } j) \\
&= q(i, j) \cdot \min\left( 1, \frac{\pi(j)}{\pi(i)}\right)
\end{aligned}
$$
Then since $P$ is a stochastic matrix, for any state $i$, the sum $\sum_{j \in S} p(i, j) = 1$ by law of total probability. This implies 
$$
\begin{aligned}
p(i, i) 
&= 1 - \sum_{\substack{k \in S \\ k \neq i}} p(i, k)  \\
&= 1 - \sum_{\substack{k \in S \\ k \neq i}} q(i, k) \cdot  \min\left( 1, \frac{\pi(k)}{\pi(i)}\right)
\end{aligned}
$$
which represents the "rejection probability". The chain stays at state $i$ if either
1. The proposal $q(i, i)$ suggests staying at $i$, 
2. or if the the proposal $j \neq i$ was made, but was rejected with probability $1 - \alpha(i, j)$.

$(2)$: We want to show that 
$$
\forall i, j \in S, 
\pi(i) \cdot p(i, j) = \pi(j)\cdot p(j, i)
$$
Trivially, this is true for $i = j$. Suppose $i \neq j$. Then 
$$
\begin{aligned}
\pi(i) \cdot p(i, j)
&= \pi(i) \cdot q(i, j) \cdot \min\left( 1, \frac{\pi(j)}{\pi(i)}\right) \\
&= q(i, j) \cdot \min(\pi(i), \pi(j)) \\
&= q(j, i) \cdot \min(\pi(j), \pi(i)) \\ 
&= \pi(j) \cdot q(j, i) \cdot \min\left( 1, \frac{\pi(i)}{\pi(j)}\right) \\
&= \pi(j) \cdot p(j, i)
\end{aligned}
$$
However, this is only true because we let $q(i, j) = q(j, i)$, i.e. the matrix $Q$ must be symmetric. Thus Metropolis satisfies detailed balance, and $\pi$ is stationary.  

$(3)$: The condition $q(i, j) > 0$ ensures the chain is [[Invariant Distribution#Definition (Reducible)|irreducible]] (any state can reach any other in one step). The condition $p(i, i) > 0$ ensures the chain is [[Invariant Distribution#Definition (Periodic)|aperiodic]]. An irreducible, aperiodic chain on a finite state space is [[Invariant Distribution#Definition (Regular Transition Matrices)|regular]]. By the [[Invariant Distribution#Fundamental Theorem of Markov Chains|FTMC]], a regular matrix has a unique stationary distribution $\pi$ and $\lim_{n \to \infty} \pi_0 P^n = \pi$.

# Remark (Metropolis on Ising Model)
Using Metropolis on the [[Ising Model]], we had 
$$
S = \{\sigma = (\sigma_{1}, \dots, \sigma_{m}), \sigma_{j} \in \{+1, -1\} \}
$$
where sign flips would give us 
$$
(\sigma_{1}, \dots, \sigma_{j}, \dots , \sigma_{m}) 
\mapsto 
(\sigma_{1}, \dots, -\sigma_{j}, \dots, \sigma_{m})
$$
which defines our proposal probability as 
$$
q(\sigma, \sigma') = \begin{cases}
1/m & \sigma \to \sigma' \text{ is 1 flip} \\
0 & \text{otherwise}
\end{cases}
$$
We can show that $q$ gives a regular Markov Chain. The idea is that any $2$ states in $S$ are at most $m$ flips apart. 

# Metropolis-Hastings Algorithm
We can run Metropolis with an asymmetric proposal matrix $Q$. The purpose of this is to relax the condition that $Q$ must be symmetric in [[#Theorem (Metropolis Satisfies Detailed Balance)]]. This allows us to correct the model over-sampling states frequently proposed by $Q$ regardless of the actual probability in the target distribution $\pi$.
1. Given $X_{k} \in S$, choose $Y$ from $q(X_{k}, \cdot)$. 
2. Accept $Y$ with probability
$$
\alpha = \min\left( 
1, 
\frac{\pi(Y)}{\pi(X_{k})} \cdot \frac{q(Y, X_{k})}{q(X_{k}, Y)}
\right)
$$
The output is a Markov Chain of $X_{0}, X_{1}, \dots \in S$. 

> Convergence is hard to prove. Heuristically, consider that $R(n) = \Cov(X_{n}, X_{0})$. So as $n \to \infty$, $R(n) \to 0$.