---
tags:
  - MATH_180A
aliases:
  - CDF
---
# Definition (CDF)
Let $X \in \R$ be a random variable RV. The **Cumulative Distribution Function** (CDF) of $X$ denoted as $F_{X}$ or $F$ is a function 
$$
F_{X} : \R \to [0, 1]
$$
is defined by 
$$
F_{X}(x) = P(X \leq x)
$$
This function is 
- non-decreasing
- $F_{X}(-\infty) = 0$, an $F_{X}(\infty) = 1$ 

Equivalently, 
$$
F_{X}(x) = \int_{-\infty}^{x} f(x) \, dx \quad\quad\quad x \in \R 
$$
the integral over the [[Probability Distribution Function|PDF]].