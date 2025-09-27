---
tags:
  - MATH_180B
---
#Lecture
- January 6, 2025

# Terminology
- Discrete Time: $T = \mathbb{N}, \mathbb{Z}, \text{ fininite set}$
- Continuous Time: $T = [0, \infty), [0,1], \cdots$
- Discrete Space: $S := \text{ a finite set }, \mathbb{N}$
- Continuous Space: $S = \mathbb{R}, \mathbb{R}^{d}, \cdots$

# Review

[[Conditional Probability]]
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$
[[Law of Total Probability]]. If $\{A_{i}\}$ is a partition of space $B$, 
$$
P(B) = \sum_{j} P(B|A_{j})P(A_j)
$$
Bayes Rule
$$
P(A_{i}|B) = \frac{P(B|A_{i})P(A_{i})}{\sum_{j} P(B|A_{j})P(A_{j})}
$$
Independence of 2 events
$$
P(A \cap B) = P(A)P(B) \iff A,B\text{ are independent}
$$
Distribution Function: 
$$
F_{X}(x) = P(X \leq x)
$$
- Discrete RV: $P_{X}(k) = P(X = k)$
- Continuous RV: $f_{X}(x)$ where $P(X \in A) = \int_{A}f_{X}(x)dx$ 

Expectation
$$
E[x] = \sum_{i} x_{i}P_{X}(x_{i})
$$
$$
E[x] = \int xf_{X}(x) dx
$$
Variance and Covariance
$$
\text{Var}(X) = E[(X - E[X])^{2}] = E[X^{2}] = (E[X])^{2}
$$
$$
\begin{aligned}
\text{Cov(X, Y)} 
&:= E[(X - E[X])(Y - E[Y])] \\
&:= \E{XY} - \E{X}\E{Y} \\
\end{aligned}
$$
We say $X,Y$ are uncorrelated if $\text{Cov(X,Y)} = 0$. In particular
$$
X,Y \text{ independent} \implies \text{Cov}(X,Y) = 0
$$
other direction is not true in general.

# [[Stochastic Process]]
