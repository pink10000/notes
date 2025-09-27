---
tags:
  - MATH_180B
---
Let $X,Y$ be independent RVs. Suppose that we know the distribution of the random variables. What is the distribution of $X + Y$?

# Discrete
Suppose $X,Y : \Omega \to \Z$ and are independent. We have:
$$
\begin{aligned}
f_{X + Y}(n) 
&= \P(X + Y = n) \\
&= \sum_{k \in \Z} P(X = k, Y = n - k) \\
&= \sum_{k \in \Z} P(X = k)\cdot P(Y = n - k) \\
&= \sum_{k \in \Z} P_{X}(k) \cdot P_{Y}(n - k) \\
&= P_{X} * P_Y(n)
\end{aligned}
$$
Indeed, 
$$
P_{X + Y} = P_{X} * P_{Y}
$$

# Continuous
Given $X,Y$ independent RVs and densities $f_{X}, f_{y}$ are given, then:
$$
\begin{aligned}
F_{X + Y}(t) 
&= \P(X + Y \leq t) \\
&= \int_{x + y \leq t} f_{X,Y}(x, y) \,dx dy \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{t - x} f_{X}(x)f_{Y}(y) \,dydx \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{t} f_{X}(x)f_{Y}(s - x) \,dsdx \\
&= \int_{-\infty}^{t} \int_{-\infty}^{\infty} f_{X}(x)f_{Y}(s - x) \,dsdx \\
\end{aligned}
$$
Then, 
$$
f_{X + Y}(s) = \int_{-\infty}^{\infty} f_{X}(x)f_{Y}(s - x) \, dx
$$
or, $f_{X} * f_{Y}(s)$

## Example 1
$X, Y \sim \Unif[0, 1]$ and independent. What is $f_{X + Y}$? Let $s = X + Y$. 

We have:
$$
f_{X}(x) = \begin{cases}
1 & 0 \leq x \leq 1 \\
0 & \text{otherwise} \\ 
\end{cases}
\quad\quad\quad
f_{Y}(s - x) = \begin{cases}
1 & 0 \leq s - x \leq 1 \\
0 & \text{otherwise} \\
\end{cases}
$$
Indeed, we have the case when $0 \leq x \leq 1$ and the case where 
$$
0 \leq s - x \leq 1 \iff s - 1 \leq x \leq 1
$$

We calculate the convolutions:
$$
\begin{aligned}
f_{X + Y}(s) 
&= \int_{0}^{s} f_{X}(x) f_{Y}(s - x) \,dx \\  
&= \int_{0}^{s} \frac{1}{1 - 0} \cdot \frac{1}{1 - 0} \, dx \\
&= \left[ x \right]_{0}^{s} \\ 
&= s
\end{aligned} \quad\quad\quad
\begin{aligned}
f_{X+Y}(s)
&= \int_{s - 1}^{1} 1 \cdot 1 \, dx \\
&= \left[x \right]_{s - 1}^{1} \\ 
&= 1 - (s - 1) \\
&= 2 - s
\end{aligned}
$$
such that
$$
f_{X + Y}(s) = \begin{cases}
s & 0 \leq s \leq 1 \\
2 - s & 1 \leq s \leq 2 \\
0 & \text{otherwise} \\
\end{cases}
$$

## Example 2 
Convolutions prove [[Normal#Sum of 2 Independent RVs]]. 