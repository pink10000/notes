---
tags:
  - MATH_180B
aliases:
  - Uniform Distribution
---
# Definition
A probability distribution where all values within a finite interval $[a, b]$ are equally likely. The density function is constant between the bounds. It is often denoted as $X \sim U(a, b)$.
# Probability Density Function (PDF)
The height of the density function is determined by the requirement that the total area under the curve must equal 1.
$$
f(x) = \begin{cases} \frac{1}{b - a} & \text{for } a \le x \le b \\ 0 & \text{otherwise} \end{cases}
$$
# Cumulative Distribution Function (CDF)
The CDF increases linearly from 0 to 1 over the interval $[a, b]$.
$$
F(x) = \begin{cases} 0 & \text{for } x < a \\ \frac{x - a}{b - a} & \text{for } a \le x \le b \\ 1 & \text{for } x > b \end{cases}
$$
# Key Statistics
Expectation (Mean):
$$
E[X] = \frac{a + b}{2}
$$
Variance:
$$
\text{Var}(X) = \frac{(b - a)^2}{12}
$$
Median:
$$
\text{Median} = \frac{a + b}{2}
$$
Moment Generating Function:
$$
M_X(t) = \begin{cases} \frac{e^{tb} - e^{ta}}{t(b - a)} & \text{for } t \ne 0 \\ 1 & \text{for } t = 0 \end{cases}
$$
# Standard Uniform Distribution
A special case where $a=0$ and $b=1$. 
$$
f(x) = 1 \quad \text{for } 0 \le x \le 1
$$
