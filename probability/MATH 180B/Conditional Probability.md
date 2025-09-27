---
tags:
  - MATH_180B
---
# Discrete (Mass)
Let $X,Y$ be two discrete random variables taking values in 
$$
\begin{aligned}
\{x_{1}, x_{2}, \cdots\} \\
\{y_{1}, y_{2}, \cdots\}
\end{aligned}
$$
and let $A_{i} = \{Y = y_{i}\}$. The **conditional probability mass function of** $X$ given $Y$ is
$$
p_{X\mid Y}(x_{j}\mid y_{i}):= \P(X = x_{j} \mid Y = y_{i}) = \frac{\P_{X,Y}(x_{j},y_{i})}{\P_{Y}(y_{i})}
$$
Note that 
$$
\P_{X|Y}(x_{j},y_{i}) \equiv \P(X = x_{j} \cap Y = y_{i})
$$
From this conditional PMF, we can derive the marginal PMF for $X$ a **fixed** $Y = y$ by:
$$
\begin{aligned}
p_{X|Y}(x \mid y) &= \frac{p_{XY}(x, y)}{p_{Y(y)}}\\
p_{XY}(x, y) &= p_{X|Y}(x \mid y)p_{Y}(y) \\
\P(X = x) &= \sum_{y=0}^{\infty}p_{X|Y}(x \mid y)p_{Y}(y) \\
\end{aligned}
$$
which is given by the [[Law of Total Probability]]:

## Example 1 
- Let $m \in \N$, $p,q \in (0,1)$
- Let $N \sim \Binom(m, q)$ 
- Let $X \sim \Binom(N, p)$

1. What is the marginal distribution of $X$?
2. What is $\E{X}$?

We know that 
$$
P_{N}(k) = \binom{m}{k}q^{k}(1 - q)^{m-k}, \quad k \in \{0, 1, \cdots, m\}
$$
$$
P_{X|N}(j\mid k) = \binom{k}{j} p^{j}(1 - p)^{k - j}, \quad j \in \{0, 1, \cdots, k\}
$$
Where 
$$
P_{X}(j) = \sum_{k=j}^{m}P_{X|N}(j\mid k)\cdot P_N(k)
$$
which is equal to 
$$
\binom{m}{j}(pq)^{j}(1 - pq)^{m-j}
$$
and $X \sim \Binom(m, pq)$. Page 48 in PK. 



# Continuous (Density)
The **continuous conditional** $f$ of $X$ given $Y = y$ is
$$
f_{X\mid Y}(x\mid y) = \frac{f_{X, Y}(x,y)}{f_{Y}(y)}
$$
Using the probability measure:
$$
\P(X = x \mid Y = y) = \frac{\P(X = x \cap Y = y)}{\P(Y = y)}
$$
