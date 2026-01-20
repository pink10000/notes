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

# Discrete Case
We can apply the same methods used of continuous RVs on discrete RVs. 

Let RV $X \in \{x_{1}, x_{2}, \dots\}$ with [[Probability Distribution Function|PMF]] $P(X = x_{i}) = p_{i}$ and [[Cumulative Distribution Function|CDF]] $F(n)$ defined below. Also $x_{i}$ is strictly increasing. 
```desmos-graph
left=-1; right=9;
bottom=-0.1; top=1.1;
---
P_1 = 0.3 | hidden
P_2 = 0.4 | hidden
x_1 = 2 | hidden
x_2 = 5 | hidden
x_3 = 8.5 | hidden

u = 0.5 | #c74440 | hidden
y = u | dashed | #c74440

y = 0 | 0 <= x < x_1 - 0.08 | black

y = P_1 | x_1 <= x < x_2 - 0.08 | black
(x_1, P_1) | black
(5, 0.3)| black | open

y = P_1 + P_2 | x_2 <= x < x_3 - 0.08 | black
(x_2, P_1 + P_2) | black
(8.5, 0.7) | black | open

(1, u + 0.04) | #c74440 | label: u | hidden

(x_1, 0) | black | label: x_1
(x_2, 0) | black | label: x_2
(x_3, 0) | black | label: x_3

x = x_1 | 0 < y < P_1 | dashed | blue
(x_1 - 0.3, P_1/2) | label: p_1 | hidden | black

x = x_2 | P_1 < y < P_1 + P_2 | dashed | blue
(x_2 - 0.3, P_1 + P_2/2) | label: p_2 | hidden | black

(7, 0.8) | black | label: F(x) | hidden
```
1. Sample $U \sim U[0, 1]$. 
2. Let $F^{-1}(u) = \min\{z \,|\, F(z) \geq u\} = x_{h}$ for $h = \min\{s \,|\, \sum_{i=1}^{s} p_{i} \geq u\}$. Basically let the inverse be the minimum $x$ value that has the minimum probability of occurring.
3. Set $X \leftarrow x_{h}$. 
