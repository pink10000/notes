---
tags:
  - MATH_114
---
Assume [[Probability Distribution Function|PDF]] $f : \R \to [0, \infty)$ is our target PDF and that 
- $f = 0$ outside $[a, b]$
- $f(x) \leq c$, $\forall x \in [a, b]$ for some $c \in \R$[^2]
The goal is to sample the RV $Z \sim f$. 
- Here, $c$ is green and $[a, b]$ are the red vertical bars. 
```desmos-graph
left=-10; right=10; top=0.25; bottom=-0.05
---
y = \frac{0.3}{2.0\sqrt{2\pi}}e^{-\frac{(x+2)^2}{2(2.0)^2}} + \frac{0.7}{1.5\sqrt{2\pi}}e^{-\frac{(x-3)^2}{2(1.5)^2}}|-8<=x<=9
y=0.2|-8<=x<=9|green
x=-8|0<=y<=0.2|red
x=9|0<=y<=0.2|red
```
# Naive Algorithm
1. Generate $X \sim U[a, b]$. For example, let $U \sim U[0, 1]$ and $X = a + (b - a)U$.
2. Generate $Y \sim U[0, 1]$ independent of $X$. 
3. If $Y \leq f(X)$, **accept** $X$ and set $Z \leftarrow X$.[^1]

Why does this work?
- $(X, Y)$ is [[Uniform|uniformly]] distributed in the box $[a, b] \times [0, 1]$. This means that the accepted pair $(X, Y)$ is uniformly distributed on 
$$
B = \left\{ (x, y) \, |\, a \leq x \leq b, 0 \leq y \leq f(x) \right\}
$$
- The area of $B$ is $1$, since the area of $f$ is $1$. 
- This implies that the marginal PDF for accepted $X$ is then 
$$
\int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy 
= \int_{0}^{f(x)} 1 \, dy
= f(x)
$$
- This tells us the distribution of accepted $X$ is $f(x)$. 
- This integral works because we are integrating over $y$, and the PDF is only defined between $0$ and $f(x)$. The joint PDF collapses to $1$, because it is the value of the accepted points during samplng.

[^1]: This is a more computational notation. From a more probabilistic perspective, this is equivalent to saying $Z = X|(Y\leq f(X))$, or $X$ conditioned on $Y \leq f(X)$.  
[^2]: In practice, you want $c$ as small as possible so that sampling can converge faster. 

# General Algorithm
We can write a more general A-R method. The goal now is to sample from a target [[Probability Distribution Function|PDF]]
$$
f : \R^{n} \to [0, \infty)
$$
For intuition sake, we can imagine $n = 1$. 

We want to find a PDF $g : \R^{n} \to [0, \infty)$ and $\alpha \geq 1$ such that 
- We know how to sample from $g$. $g$ is called the *proposed PDF*. It is close to $f$ and easy to sample from.
- $\alpha g(x) \geq f(x)$ for all $x \in \R^{n}$. $\alpha g(x)$ is called a *majorizing function* of $f$. 
	- Note that $\alpha \geq 1$ is required because $g$ is a PDF which integrates to $1$. 
$$
\alpha 
= \int_{\R^{n}} \alpha g(x) \, d\unl{x} 
\geq \int_{\R^{n}} f(x) \, d\unl{x} 
= 1
$$
- We want $\alpha$ to be as small as possible. 