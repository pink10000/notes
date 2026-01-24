---
tags:
  - MATH_114
aliases:
  - Importance Sampling
---
# Importance Sampling
**Importance Sampling** is a way to compute an [[Expectation|expectation]]/integral more efficiently by sampling from a *different* distribution that puts more probability mass on the parts of the domain that matter the most, and then reweighing them to keep the estimator correct.
## Motivation: Monte Carlo Integration
For example, consider [[Monte-Carlo Integration|MC Integration]]: 
$$
I = \int_{D} g(x) f(x) d\unl{x} 
$$
where 
- $D \subseteq \R^{\ell}$ where $D$ is bounded, i.e. $D = [0, 1]^{\ell}$. 
- $g : D \to \R$ is bounded and integrable (continuous)
- $f : D \to \R$ is a [[Probability Distribution Function|PDF]] where $f \geq 0$ with $\int_{D} f(x) d\unl{x} = 1$. 

Note that $I = \mathbb{E}_{f}[g(x)] = \E{g(x)}$ and 
$$
\begin{aligned}
\sigma^{2} 
&:= \var(g(x)) \\ 
&= \E{g(x)^{2}} - \left[ \E{g(x)} \right]^{2} \\
&= \int_{D} g(x)^{2} f(x) dx - I^{2} \\ 
&= \int_{D}g(x)^{2}f(x) dx - 2I^{2} + I^{2} \\ 
&= \int_{D} g(x)^{2} f(x) dx - \int_{D} 2I g(x) f(x) dx + \int_{D} I^{2} f(x)dx\\
&= \int_{D} \left( g(x)^{2} - 2Ig(x) + I^{2} \right)f(x) dx \\
&= \int_{D} (g(x) - I)^{2} f(x) dx 
\end{aligned}
$$
## Special Case: CMC via a Uniform Choice
More generally, any integral on $D$ can be rewritten as an expectation by introducing a PDF $p$ on $D$:
$$
\int_{D} h(x) dx = \int_{D} \frac{h(x)}{p(x)} p(x)dx = \mathbb{E}_{p}\!\left[\frac{h(X)}{p(X)}\right].
$$
One simple choice is the [[Uniform]] density on $D$:
$$
p(x) = \frac{1}{\text{vol}(D)}
$$
If we plug this is in, 
$$
\frac{h(x)}{p(x)} = \frac{h(x)}{1/\text{vol}(D)} = \text{vol}(D) \cdot h(x),
$$
such that 
$$
\int_D h(x)\,dx = \E{\text{vol}(D) \cdot h(X)} = \text{vol}(D) \cdot \E{h(X)}.
$$
as desired. 

# Importance Sampling (Variance Reduction)
Instead of sampling from the "default" density, choose a proposal density $\phi$ on $D$ (with $\phi(x) > 0$ wherever $g(x)f(x)\neq 0$) and reweigh:
$$
I = \int_{D} g(x) f(x) \, dx = \int_{D} \frac{g(x)f(x)}{\phi(x)} \phi(x) \, dx
$$
This gives
$$
I = \mathbb{E}_{f}[g(X)] = \mathbb{E}_{\phi} \left[ \frac{g(Y) f(Y)}{\phi(Y)} \right]
$$
for $X \sim f$ and $Y \sim \phi$. Some remarks:
- $\phi$ is called the **importance function**
- $\frac{f(x)}{\phi(x)}$ is the **likelihood ratio**
## Algorithm
1. Generate $Y_{1}, \dots, Y_{N} \sim \phi$ iid.
2. Set
   $$
   J_{N} = \frac{1}{N} \sum_{i=1}^{N} \frac{g(Y_{i})f(Y_{i})}{\phi(Y_{i})}.
   $$
## Choosing $\phi$
Pick $\phi$ to satisfy:
- **Support**: $\phi(x) > 0$ anywhere $g(x)f(x) \neq 0$ (so the weight $f(x)/\phi(x)$ is well-defined).
- **Computable**: easy to sample from.
- **Low-variance weights**: avoid making $\phi(x)$ tiny where $|g(x)f(x)|$ is large (that creates huge weights and high variance).

[[Variance Reduction]] means choosing $\phi$ such that
$$
\int_{D} \frac{g(x)^{2}f(x)^{2}}{\phi(x)}\, dx
$$
is small. The idea is to make $\phi(x)$ larger when $(g(x)f(x))^{2}$ is large. Why do we want that integral small? This comes from the **variance** formula. Let
$$
W := \frac{g(Y)f(Y)}{\phi(Y)}, \quad Y \sim \phi.
$$
Then $J_N = \frac{1}{N}\sum_{i=1}^N W_i$ with $W_i$ i.i.d., so
$$
\var(J_N) = \frac{1}{N}\var(W).
$$
Using $\var(W)=\mathbb{E}[W^2]-\mathbb{E}[W]^2$:
$$
\mathbb{E}_{\phi}[W] = \int_D \frac{g(x)f(x)}{\phi(x)}\phi(x)\,dx = \int_D g(x)f(x)\,dx = I,
$$
and
$$
\mathbb{E}_{\phi}[W^2] = \int_D \left(\frac{g(x)f(x)}{\phi(x)}\right)^2 \phi(x)\,dx
= \int_D \frac{g(x)^2 f(x)^2}{\phi(x)}\,dx.
$$
Therefore
$$
\var(J_N) = \frac{1}{N}\left(\int_D \frac{g(x)^2 f(x)^2}{\phi(x)}\,dx - I^2\right).
$$
Since $I^2$ does not depend on $\phi$, making $\int_D \frac{g^2 f^2}{\phi}$ small makes the estimator variance small.
# Example 1
Consider $D = [0, 1] \subseteq \R, f(x) = 1$ on $D$ where $(f(x) = 0, x \not\in D)$ and $g(x) = 4\sqrt{1 - x^{2}}$ on $D$. 

By Crude MC,
$$
I_{N} = \frac{1}N \sum_{k=1}^{N} g(U_{k})
$$
the variance is
$$
\frac{1}{N}\left[ \int_{0}^{1} 16(1 - x^{2}) dx - I^{2}  \right] \approx \frac{0.797 \cdots}{N}.
$$
Note that 
$$
I = \int_{0}^{1} 4\sqrt{1 - x^{2}} dx = \pi. 
$$
# Example 2 (Using Variance Reduction)
Let's try
$$
\phi(x) = \frac{4}{3} - \frac{2}{3}x \quad\quad\quad x \in [0, 1].
$$
```desmos-graph
left=-0.1; right=1.1;
bottom=-0.1; top=4.1;
---
g(x) = 4\sqrt{1 - x^2} | 0<=x<=1 |blue
p(x) = 4/3 - (2x)/3 | 0<=x<=1| red
(0.8, 2.5)|blue|label: g(x)|hidden
(0.2, 1)|red|label: \phi(x)|hidden
```
This gives the estimator
$$
J_{N} = \frac{1}{N} \sum_{k=1}^{N} \frac{g(Y_{k})f(Y_{k})}{\phi(Y_{k})}
$$
for $Y_{1}, \dots, Y_{N} \sim \phi$ iid. So,
$$
J_N = \frac{1}N \sum_{k=1}^{N} \frac{6\sqrt{1 - Y_{k}^{2}}}{2 - Y_{k}}.
$$
Then
$$
\begin{aligned}
\var_{\phi}(J_{N}) 
&= \frac{1}{N} \left[ \int_{0}^{1} \frac{g(x)^{2}}{\phi(x)} \,dx - I^{2} \right] \\
&= \frac{1}{N} \left[ \int_{0}^{1} \frac{24(1 - x^{2})}{2 - x}\,dx - \pi^{2} \right] \\ 
&\approx \frac{0.224\cdots}{N}.
\end{aligned}
$$
by applying the variance formula for estimators above. What if we overdo it with a large $\phi$?
```desmos-graph
left=-0.1; right=1.1;
bottom=-0.1; top=4.1;
---
g(x) = 4\sqrt{1 - x^2} | 0<=x<=1 |blue
p(x) = 2 - (2x)/3 | 0<=x<=1| red
(0.8, 2.5)|blue|label: g(x)|hidden
(0.2, 2)|red|label: \psi(x)|hidden
```
Let's try $\psi(x) = 2 - 2x$ for $x \in [0, 1]$. $\psi$ being $0$ when $x = 1$ is not ideal. What does that look like?

The estimator
$$
K_{N} = \frac{1}{N}\sum_{k=1}^{N} \frac{g(Z_{k})f(Z_{k})}{\psi(Z_{k})}
$$
with $Z_{1}, \dots, Z_{N} \sim \psi$. Then 
$$
\var_{\psi}(K_{N}) 
:= \frac{1}{N} \left[ \int_{0}^{1} \frac{8(1 - x^{2})}{1 - x}\, dx - \pi^{2} \right]
\approx \frac{2.1\cdots}{N},
$$
which shows it's a bad estimator.
