---
tags:
  - MATH_180B
---
Given event $A$, we have some event $A^{c}$, the complement of it. In particular, 
$$
\begin{aligned}
P_{X}(x_{i})
&= P(X = x_{i}) \\
&= P(X = x_{i}, A) + P(X_{i}, A^{c}) \\
&= P_{X}(x_{i}\mid A) P(A) + P_{X}(x_{i}\mid A^{c})P(A^{c}) \\
\end{aligned}
$$
If we partition $\Omega$ into $\{A_{i}\}_{i\in I}$, then $\Omega\sqcup_{i\in I} A_{i}$. 

# Continuous Variables
Given event $A$ and a random variable $X$ in which $X$ partitions $A$, then 
$$
\P(A) = \int_{-\infty}^{\infty}\P(A \mid X = x) f_{X}(x) dx
$$
Intuitively, since $X$ partitions $A$ (where $A$ depends on the value of $X$),  it weights each of its own probabilities to $X$. 

# Joint Densities
Let $X,Y$ be two continuous random variables. Their [[Joint Distribution|joint density function]] is:
$$
f_{Y}(y)= \int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx
$$
where we sum up all possible values of $X$ to find $Y$. 

# Expected Values
Read more here: [[Conditional Expectation]].