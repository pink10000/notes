---
tags:
  - MATH_114
---
Assume [[Probability Distribution Function|PDF]] $f : \R \to [0, \infty)$ is our target PDF and that 
- $f = 0$ outside $[a, b]$
- $f(x) \leq c$, $\forall x \in [a, b]$ for some $c \in \R$[^2]
The goal is to sample the RV $Z \sim f$. 
- Here, $c$ is green and $[a, b]$ are the red vertical bars.[^1]

```desmos-graph
left=-10; right=10; top=0.25; bottom=-0.05
---
y = \frac{0.3}{2.0\sqrt{2\pi}}e^{-\frac{(x+2)^2}{2(2.0)^2}} + \frac{0.7}{1.5\sqrt{2\pi}}e^{-\frac{(x-3)^2}{2(1.5)^2}}|-8<=x<=9
y=0.2|-8<=x<=9|green
x=-8|0<=y<=0.2|red
x=9|0<=y<=0.2|red
```
[^1]: Ideally, $c$ is as tight as possible. The textbook denotes $c = \sup\{f(x) \, | \, x \in [a,b]\}$.
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
- This integral works because we are integrating over $y$, and the PDF is only defined between $0$ and $f(x)$. The joint PDF collapses to $1$, because it is the value of the accepted points during sampling.

[^1]: This is a more computational notation. From a more probabilistic perspective, this is equivalent to saying $Z = X|(Y\leq f(X))$, or $X$ conditioned on $Y \leq f(X)$.  
[^2]: In practice, you want $c$ as small as possible so that sampling can converge faster. 

# General Algorithm
We can write a more general A-R method. The goal now is to sample from a target [[Probability Distribution Function|PDF]]
$$
f : \R^{n} \to [0, \infty)
$$
For intuition sake, we can imagine $n = 1$. 
```desmos-graph
left=-1; right=7;
bottom=-1; top=5;
---
y = \max(0, 4 - 1.333\sqrt{(x-3)^2})
y = 2.8e^{-(x-2.5)^{2}} + 2e^{-(x-3.8)^{2}}
0 <= y <= 2.8e^{-(x-2.5)^{2}} + 2e^{-(x-3.8)^{2}}
2.8e^{-(x-2.5)^{2}} + 2e^{-(x-3.8)^{2}} <= y <= \max(0, 4 - 1.333\sqrt{(x-3)^2})
A = (3, 3.6)|label:A
B = (3, 1.5)|label:B
```
> The top part is $\alpha g$ and the purple part is $f$. 

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

# Acceptance-Rejection Algorithm
Given target [[Probability Distribution Function|PDF]] $f : \R^{n} \to [0, \infty)$, find *proposal* PDF $g$ and constant $\alpha$ such that $\alpha g(x) \geq f(x)$ for all $x \in \R^{n}$. 
1. Generate $X \sim g$ where $X \in \R^{n}$. 
2. Generate $Y \sim U[0, \alpha g(x)]$ where $Y \in \R$. 
3. If $y \leq f(x)$, then accept $x$ and set $z \leftarrow x$. Otherwise, we reject and go step 1. 

We want to measure the following *rates*:

## Efficiency 
The probability of acceptance is: $$ P\left( (X, Y) \text{ is accepted} \right) = \frac{ v(B) }{ v(A) } $$ Where $v(B)$ and $v(A)$ correspond to the volumes under the curves: 
$$
\begin{aligned} 
v(B) &= \int_{\R^{n}} f(x) \, dx = 1 \\ 
v(A) &= \int_{\R^{n}} \alpha g(x) \, dx = \alpha 
\end{aligned} 
$$
Thus, the expected acceptance rate is $\frac{1}{\alpha}$.
# Theorem (Uniformity on Region $A$)
Let the relevant geometric regions be defined as:
$$
\begin{aligned}
A &= \{ (x, y) \mid 0 \leq y \leq \alpha g(x) \} \\
B &= \{ (x, y) \mid 0 \leq y \leq f(x) \} \subseteq A
\end{aligned}
$$
The pair $(X, Y)$ obtained from Steps 1 & 2 is uniformly distributed on $A$.

Proof:
- Let $f_{X,Y} : \mathbb{R}^n \times \mathbb{R} \to [0, \infty)$ be the joint PDF of $(X, Y)$.
- Let $f_{Y|X}(y|x)$ be the conditional PDF of $Y$ given $X=x$.

Recall from [[Conditional Probability#Continuous (Density)|theorem]] that the joint PDF is equal to the conditional times marginal. Since $X \sim g$ (Step 1), we have:
$$
f_{X,Y}(x,y) = \begin{cases} 
g(x) f_{Y|X}(y|x) & (x,y) \in A \\
0 & \text{otherwise}
\end{cases}
$$
From Step 2, we generate $Y \sim U[0, \alpha g(x)]$. The PDF of a uniform distribution on $[0, k]$ is $1/k$, so:
$$
f_{Y|X}(y|x) = \begin{cases}
\frac{1}{\alpha g(x)} & y \in [0, \alpha g(x)] \\
0 & \text{otherwise}
\end{cases}
$$
Substituting this back into the joint PDF:
$$
(\star)
\quad\quad\quad
f_{X,Y}(x,y) = g(x) \cdot \frac{1}{\alpha g(x)} = \frac{1}{\alpha}
$$
Since the PDF is constant on the support $A$, $(X, Y)$ is uniformly distributed on $A$.

# Theorem (From Uniformity on $A$ to Target $f(x)$)
We established that the candidate points $(X, Y)$ are uniform on $A$.
$$
\implies f_{X,Y}(x,y) = \frac{1}{\alpha} \quad \forall (x,y) \in A
$$
How does $X \sim f$? 

Proof:

Let $(X^*, Y^*)$ be the first *accepted* point. Because $(X,Y) \sim U(A)$ and we strictly accept points within $B \subseteq A$, the accepted points are uniformly distributed on $B$:
$$
(X,Y) \sim U(A) \implies (X^*, Y^*) \sim U(B)
$$
$B$ is the area under the PDF $f$, so its total volume is $\int f(x)dx = 1$. The joint PDF of the accepted point $(X^*, Y^*)$ is therefore:
$$
f_{X^*, Y^*}(x,y) = \begin{cases}
1 & (x,y) \in B \\
0 & \text{otherwise}
\end{cases}
$$
To find the distribution of just the $x$-values, we take the marginal of $f_{X^*, Y^*}$:
$$
\begin{aligned}
f_{X^*}(x) &= \int_{-\infty}^{\infty} f_{X^*, Y^*}(x,y) \, dy \\
&= \int_{0}^{f(x)} 1 \, dy \\
&= f(x)
\end{aligned}
$$
Thus the accepted samples $X^*$ follow the target distribution $f(x)$.
# Theorem (A-R Generates $Z \sim f$)
This theorem explains why this works via geometric intuition.

Consider the graph of $\alpha g(x)$ enveloping $f(x)$.
```desmos-graph
left=-1; right=7;
bottom=-1; top=5;
---
g(x) = \max(0, 4 - 1.333\sqrt{(x-3)^2})
f(x) = \max(0, 3 - 1.333\sqrt{(x-3)^2}) 
(3.2, 3.73) | label: \alpha g(x) | black
(3.2, 2.8) | label: g(x) | black
0 <= y <= f(x) | green
```
* Step 1 ($X \sim g$): $X$ is more likely to fall where $g$ is big. This leads to a "mushing" (clustering) of points along the x-axis at the peaks.
* Step 2 ($Y \sim U$): Choosing $Y \sim U[0, \alpha g(x)]$ gives "more space" for $Y$ to be uniform where $g$ is large.

This vertical expansion compensates for the horizontal "mushing" of $X$. The high horizontal density (large $g$) $\times$ low vertical density (large range $\alpha g$) gives us a near 2D constant density in $A$. These effects cancel out perfectly, see $(\star)$ from [[#Theorem (Uniformity on Region A)]]. This allows us to cut out the shape of $f(x)$ or region $B$. The remaining points (accepted points) form $f$. 

In general, this is easy to visualize in $\R^{2}$, but this method provides justification for $\R^{n}$. 

# Modified A-R
Let $f$ be our target PDF and $g$ be our proposal PDF. Let $\alpha \in \R$ where $f \geq \alpha g$ for all $x \in \R$. 
1. Generate $X \sim g$
2. Generate $U \sim U[0, 1]$. 
3. If
   $$
   U \leq \frac{f(X)}{\alpha g(X)}
   $$
   then accept $X$. Set $Z \leftarrow  X$. Else, reject $X$ and go to Step 1.

## Example 1 (Sampling Standard Normal via A-R)
Let suppose we wanted to sample $N(0, 1)$, the [[Normal|standard normal]]. So, 
$$
f(x) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}2 x^{2} \right)
\quad\quad\quad
x \in \R
$$
and let
$$
g(x) = \frac{1}\alpha \exp(-|x|)
\quad\quad\quad
\text{on }\R
$$
Visually, 
```desmos-graph
left=-0.1; right=3;
bottom=-0.05; top=0.6;
---
f(x) = \frac{1}{\sqrt{2\pi}}e^{-0.5x^2} | 0 <= x | red
g(x) = 0.5e^{-\max(x, 0)} | dashed | 0 <= x | blue
(0.5, 0.4) | red | label: f(x)
(0.1, 0.5) | blue | label: g(x)
```
Note that $g$ is the [[Exponential|exponential distribution]] $\Exp(1)$ which has PDF $e^{-x}$ for $x \geq 0$ multiplied randomly $\pm 1$. 

To do Step 1 (generate $X \sim g$) we need to:
1. Generate $U_{1}, U_{2} \sim [0, 1]$ independently. Let $U_{1}$ be transformed by [[Inversion]] and $U_{2}$ be $\pm 1$. 
2. Set 
   $$
   X = \begin{cases}
   -\ln U_{2} & U_{1} \leq \frac{1}2 \\ 
   +\ln U_{2} & U_{1} \geq \frac{1}2
   \end{cases}
   $$
3. Now we find $\alpha \geq 1$ such that $\alpha g(x) \geq f(x)$ for all $x \in \R$. 

For our case, we can set 
$$
\alpha 
= \sup_{x \in \R} \frac{f(x)}{g(x)} 
= \sup_{x \geq 0} \sqrt{\frac{2}{\pi}} \exp \left( x - \frac{x^{2}}{2} \right)
= \sqrt{\frac{2e}{\pi}}
\approx 1.315
$$
This allows us to sample $N(0, 1)$ computationally. 