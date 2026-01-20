---
tags:
  - MATH_114
aliases:
  - MC Integration
---
- How do we evaluate high-dimensional integrals numerically?
- E.g. consider $N$ particles $\unl{x}_{1}, \unl{x}_{2}, \dots, \unl{x}_{N} \in \R^{3}$. The [[Joint Distribution|Joint PDF]] is $f : \R^{3N} \to [0, \infty)$.
- If we want to find the average properties among all particles, we'd have to do 
$$
\int_{\R^{3N}} g(x) f(x) d\unl{x}
$$

# Problem 1 (Importance Sampling)
Consider 
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
Any integral on $D$ has the above form 
$$
\int_{D} h(x) dx = \int_{D} \frac{h(x)}{f(x)} f(x)dx = \mathbb{E}_{f}(g(X)) 
$$
for $g(x) = h(x)/f(x)$. This trick is called **Importance Sampling**. One simple choice we can do is 
$$
f(x) = \frac{1}{\text{vol}(D)}
$$
on $D$. For example, if we plug this is in, 
$$
g(x) = \frac{h(x)}{f(x)} = \frac{h(x)}{1/\text{vol}(D)} = \text{vol}(D) \cdot h(x)
$$
such that 
$$
I = \E{\text{vol}(D) \cdot h(X)} = \text{vol}(D) \cdot \E{h(X)}
$$
which is precisely what we want. 

# Algorithm (Monte Carlo Integration)
The goal is to evaluate
$$
I = \int_{D} g(x) f(x) dx 
$$
1. Generate $X_{1}, \dots, X_{N} \sim f$ which are iid. 
2. Set 
   $$
   I_{N} = \frac{1}{N} \sum_{i=1}^{N} g(X_{i}) \approx I
   $$
   where $I_{N}$ is a **MC estimator** of $I$ or a crude MC (**CMC Estimator**) of $I$. 

We want to know, 
1. Does $I_{N}$ converge? As $N \to \infty, I_{N} \to I$? 
2. What is the error? As $N \to \infty$ what is $|I_{N} - I|$? 

The idea is to look at $\E{I_{N}}$ and $\var(I_{N})$. 
# Proposition (MC Estimators Mean & Variance)
Claim:
$$
\begin{aligned}
\E{I_{N}} &= I \\
\var(I_{N}) &= \frac{1}{N}\var(g(X)) \\
\end{aligned}
$$
or that 
1. $I_{N}$ is unbiased
2. $X \sim g$

Proof: 

First, 
$$
\begin{aligned}
\E{I_{N}} 
&= \frac{1}{N} \sum_{n=1}^{N} \E{g(X)} \\
&= \frac{1}{N} \cdot NI = I 
\end{aligned}
$$
by [[Expectation#Theorem (Linearity of Expectation)|linearity]] of $\mathbb{E}$. Second,
$$
\begin{aligned}
\var(I_{N}) 
&= \var\left( \frac{1}{N} \sum_{n=1}^{N}g(X_{n}) \right) \\
&= \frac{1}{N^{2}} \var\left( \sum_{n=1}^{N} g(X_{n}) \right) \\
&= \frac{1}{N^{2}} \sum_{n=1}^{N} \var(g(X_{n})) & \text{by independence} \\
&= \frac{1}{N^{2}} \cdot N \var(g(X)) & \text{by identically distributed}\\
&= \frac{1}{N} \var(g(X))
\end{aligned}
$$
as required. 

# Theorem (Strong Consistency of MC Estimators)
$$
\lim_{N \to \infty} I_{N} = I
$$
with probability $1$. 

Proof: This follows from the Strong [[Law of Large Numbers]]. 
> This theorem tells us that if we run the simulation "long enough" we are guaranteed to get the correct answer. In particular, $P\left(\lim_{N \to \infty} I_{N} = I\right) = 1$.
# Theorem (Asymptotic Normality of MC Estimators)
Let $\sigma^{2} = \var(g(X))$ where $X \sim f$. Then 
$$
\frac{I_{N} - I}{\sigma /\sqrt{N}} \to Z \sim N(0, 1)
$$
Proof: By [[Central Limit Theorem]]. 
> This theorem tells us that we can calculate exactly how much error/noise is in our estimate and build confidence intervals. 