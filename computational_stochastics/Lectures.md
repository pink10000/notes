---
tags:
  - MATH_114
---
# Lecture 1 (1/5)
- Key questions: distributions, sampling, features of a system
- [[Random Sampling]]
- [[Ising Model]]
- The main idea is that sampling [[Random Sampling#Example 1 (Monte Carlo Estimation of Pi)|allows integration]], [[Random Sampling#Example 2 (Multidimensional Hypercube Integral)|scales better than grids]], and solves [[Ising Model#Problem|impossible sums]].

# Lecture 2 (1/7)
## Example 1:
Let $x(t)$ be a particle with the following ODE
$$
\begin{aligned}
\frac{dx}{dt} = - \frac{du}{dx}
\end{aligned}
$$
Let $u(x) = \frac{1}{2}x^{2}$.  Then
$$
\begin{aligned}
u(x) &= \frac{1}{2}x^{2} \\
\frac{du}{dx} &= x \\
\end{aligned}
$$
such that
$$
\frac{dx}{dt} = -x
$$
Upon solving this ODE, we get
$$
x(t) = x(0) \cdot e^{-t}
$$
So, as $t \to \infty, x \to 0$.

## Example 2:
We could have a double well
$$
u(x) = \frac{1}{4} (x^{2} - 1)^{2}
$$
```desmos-graph
	left=-2; right=2;
	top=1; bottom=-0.1;
	---
    y=(1/4)(x^2 - 1)^2
```
In the SDE case, given
$$
dx = -u'(x)\,dt + b(t)\,dB_{t}
$$
In order, the terms are:
- $dx$ is the change $x$
- $u'(x)$ is the deterministic force
- $b(t)dB_{t}$ is some "random" force. In particular, $dB_{t}$ is the Brownian increment, or "white noise".

So when we calculate the position of the particle via $x(t)$, the $u'(t)$ term tells us how we move via the force, with some randomness via $b(t)dB_{t}$. This leads to
- new frequency in a system
> what does frequency mean?
- new types of resonance/transport effects.

# Lecture 3 (1/9)
Reference for this section is Rubinstein Ch.2
- [[Inversion]]
- [[Transformation of Random Variables]]

# Lecture 4 (1/12)
Reference: Rubinstein Ch. 2, 2.4, 2.3.4
- [[Box-Muller Method]]
- [[Acceptance-Rejection]]

# Lecture 5 (1/14)
- [[Acceptance-Rejection]]
- [[Acceptance-Rejection#Theorem (Uniformity on Region $A$)]]
- [[Acceptance-Rejection#Theorem (From Uniformity on $A$ to Target $f(x)$)]]
- [[Acceptance-Rejection#Theorem (A-R Generates $Z sim f$)]]

# Lecture 6 (1/16)
- [[Acceptance-Rejection#Efficiency]]
- [[Acceptance-Rejection#Modified A-R]]
- [[Acceptance-Rejection#Example 1 (Sampling Standard Normal via A-R)]]
- [[Inversion#Discrete Case]]

# Lecture 7 (1/21)
- [[Monte-Carlo Integration]]
- [[Variance Reduction]]

# Lecture 8 (1/23)
- [[Importance Sampling]]
- [[Importance Sampling#Example 1]]

# Lecture 9 (1/26)
- Review of previous $2$ lectures. 
- [[Markov Chains]]. For the purposes of this class we only consider Discrete Time/State Homogeneous Markov Chains
- [[Stochastic Process]]

# Lecture 10 (1/28)
- [[Markov Chains]]

# Lecture 11 (1/31)
- [[Long-Run Markov Chains]]
- [[Invariant Distribution]]

# Lecture 12 (2/2)
- [[Long-Run Markov Chains]]
- [[Metropolis Algorithm]]

# Lecture 13 (2/4)
- [[Metropolis Algorithm#Example 1 (1D Ising Model)]]
- [[Metropolis Algorithm#Theorem (Metropolis Satisfies Detailed Balance)]]

# Lecture 14 (2/6)
- Review on [[Metropolis Algorithm#Theorem (Metropolis Satisfies Detailed Balance)]]
- [[Gibbs Sampler]]

# Lecture 15 (2/9)
- Review for midterm