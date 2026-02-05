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
which is [[Symmetric Matrix|symmetric]]. 