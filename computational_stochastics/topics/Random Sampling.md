---
tags:
  - MATH_114
---
# Random Sampling
The goal of **random sampling** is to generalize *hard* random variables from *easy* RVs. This allows us to compute hard integrals by using sampling to solve deterministic problems.

# Example 1 (Monte Carlo Estimation of Pi)
Suppose we wanted to find the area of a unit circle in a plane. Let
$$
\begin{aligned}
U_{1} &\sim U(-1, +1) \\
U_{2} &\sim U(-1, +1) \\
\end{aligned}
$$
Let 
$$
X = \begin{cases}
0 & \text{if } (U_{1}, U_{2}) \text{ is outside the circle} \\
1 & \text{if } (U_{1}, U_{2}) \text{ is inside the circle} \\
\end{cases}
$$
Note that $U(-1, +1)$ is the [[Uniform|Uniform Distribution]]. Now, the area of th sample space, $U_{1} \times U_{2}$ is $4$. Thus,
$$
P(X = 1) = \frac{A}{4} \quad\quad\quad P(X = 0) = 1 - \frac{A}{4}
$$
where $A$ is the area of the unit circle. Since $X$ is a [[Bernoulli]] RV, then $\E{X} = A/4$. 

After $N$ trials, we have $X_{1}, X_{2}, \dots, X_N$ iid random variables.  Using the Strong [[Law of Large Numbers]], we see
$$
\lim_{N \to \infty} \frac{1}{N} \sum_{i=1}^{\infty} X_{i} \to \frac{A}{4} = \frac{\pi}{4}
$$
Effectively, we are counting the number of the dots that hit the circle with the summation, and finding the mean. 

# Example 2 (Multidimensional Hypercube Integral)
Compute the integral $I$ of a function $g : [0, 1]^{d} \to \R$ over a $d-$dimensional hypercube $[0, 1]^d$. Let 
$$
I = \int_{[0, 1]^{d}} g(x) \,dx
= \int_{0}^{1} \int_{0}^{1} \dots \int_{0}^{1} g(x_{1}, x_{2}, \dots, x_{d}) \, dx_{1} dx_{2} \cdots dx_{d}
$$
Numerically, integrating this is the same as doing this over a grid, dividing the domain into $N^{d}$ boxes of size $(1/N)^{d}$. Let the center of each box be $x^{(i)}$ be $g(x^{(i)})$. The sum is our integral, 
$$
I \approx \sum_{i=1}^{N^{d}} g(x^{(i)}) \left( \frac{1}{N} \right)^{d}
$$
The term $N^{d}$ means we need many points. Even with $d = 10$ and $N = 10$ total divisions, we need $10^{10}$ or $10$ billion points (which is computationally expensive!)

Instead, we can do **Monte Carlo Integration**. First, generate $N$ iid RVs $X_{1}, \dots, X_{N} \sim U(0, 1)$. Since the PDF of each RV is $p(x) = 1$, then 
$$
I 
= \int_{[0,1]^{d}} g(x) \, dx 
= \int_{[0,1]^{d}} g(x) \cdot 1 \, dx 
= \int_{[0,1]^{d}} g(x) \cdot p(x) \, dx \\
= \E{g(X)}
$$
Note that $X$ is the RV of any value of this distribution since they are identical. Then we can define an experiment with $N$ trials. Let 
$$
I_{N} = \frac{1}{N} \sum_{i=1}^{N} g(x_{i})
$$
Again, by [[Law of Large Numbers|Strong LLN]], as $N \to \infty$, then $I_{N} \to I$. We can create an [[Estimator]] for $I_{N}$ and get an error of $\approx 1/\sqrt{N}$. 

# Example 3 (Ising Model)
See [[Ising Model]]. 