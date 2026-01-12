---
tags:
  - MATH_114
---

# Theorem (Inversion)
Let $U \sim U[0, 1]$ be on the [[Uniform|Uniform Distribution]] and let $F$ be the target [[Cumulative Distribution Function|CDF]]. Let $C = F^{-1}(U)$ where $X$ is a s? RV. Then $X \sim F$. 
```desmos-graph
bottom=-0.1; top=1; left=-0.5; right=2.2;
---
a=0.7
b=1.4
c=2
y=e^{(2x-3)}|x<=a
y=e^{(2a-3)}|a<=x<=b
y=x-1.2|b<=x<=c
y=0.5*\sqrt{x-c}+(c-1.2)|b<=x
```
Consider the following CDF of $F$. 

What exactly is $F^{-1}$? First, $F$ is an increasing function to $1$ (or asymptotically to $1$). If we take some point $u_{1}$ with the corresponding domain $F^{-1}(u_{1})$, then apart from the flat portion, it is clear what the value should be. 

Now for the range of $F$ where the value is neither increasing nor decreasing (the red portion in the graph), then we define 
$$
F^{-1} = \inf\{z \in \R \,|\, F(z)\}
$$
or the [[Infimum]]. In particular, 
$$
\begin{aligned}
P(X \leq x) 
&= P(F^{-1}(U) \leq x) \\ 
&= P(U \leq F(X)) \\ 
&= F_{U}(F(X)) \\ 
&= F(X)
\end{aligned}
$$
which is sort of a "baby sampling algorithm". 
## Inversion Algorithm
This gives us the following algorithm, 
1. Input: CDF $F$ (target)
2. Output Sample $X \sim F$
3. Step 1: Generate $U \sim U[0, 1]$
4. Step 2: Assign $X \leftarrow F^{-1}(U)$

## Example 1
Suppose we sampled the following RV with the [[Probability Distribution Function|PDF]]
$$
f(x) = \begin{cases}
0 & x < 0 \\
\lambda e^{-\lambda x} &x \geq 0  
\end{cases}
$$
or the [[Exponential]] distribution with parameter $\lambda$. 

Solution: We know that the CDF is 
$$
\int_{-\infty}^{x} \lambda e^{-\lambda s} \, ds 
= 
\begin{cases}
0 & x < 0 \\
1 - e^{-\lambda x} & x \geq 0
\end{cases}
$$
Then we finish by 
$$
\begin{aligned}
F(X) &= U \\ 
1 - e^{-\lambda X} = U \\ 
X = -\frac{1}{\lambda} \ln(1 - U)
\end{aligned}
$$
So, if $U \sim U[0, 1]$, then
$$
X = -\frac{1}{\lambda} \ln(1 - U) \sim f
$$

---
More generally, we want to know more about the [[Transformation of Random Variables]]. 