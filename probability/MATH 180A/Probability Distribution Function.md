---
tags:
  - MATH_180A
aliases:
  - PDF
  - PMF
---
# Definition (PDF)
Let $X \in \R$ be a random variable. The **Probability Distribution Function** (PDF) denoted as $f_{X}$ or $f$ is defined by 
$$
f_{X}(x) = F_{X}'(x)
$$
the [[Derivative|derivative]] of the [[Cumulative Distribution Function|CDF]] apart from a "few points". Some properties are that
- $f_{X} \geq 0$
- $\int_{-\infty}^{\infty} f_{X}(x) \, dx = 1$
- $P(a \leq X \leq b) = F_{X}(b) - F_{X}(a) = \int_{a}^{b} f(x)\, dx$ 
- $P(X = x) = F_{X}(x) - F_{X}(x^{-}) = F_{X}(x) - \lim_{y \to x} F_{X}(y)$.
	- This is particularly useful for discrete random variables. We call this a **Probability Mass Function**, or a PMF.

# Notation 
To denote that a RV $X$ has a particular distribution will be by 
$$
X \sim f \quad\quad\quad  X \sim F
$$
such that $X$ has PDF $f$ and [[Cumulative Distribution Function|CDF]] $F$. 