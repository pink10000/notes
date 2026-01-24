---
tags:
  - MATH_114
aliases:
  - Variance Reduction
  - Common Random Numbers
  - Antithetic Variates
---
# Variance Reduction via Coupling
Let $X \sim F, Y \sim G$ for [[Cumulative Distribution Function|CDFs]] $F,G$. Estimate $\E{X \pm Y} = \mu_{\pm}$. For [[Monte-Carlo Integration|MC Integration]], a typical situation is
$$
I = \int (g(u) + h(u))f(u) \, du.
$$
But what if we wanted to reduce the [[Variance]] of $I_{N}$?

Set an unbiased estimator $W_{\pm}$ for $\mu_{\pm} = \E{X \pm Y}$. The goal is to choose a relationship between $X,Y$ to reduce the variance:
$$
\begin{aligned}
\var(W_{\pm}) 
&= \var(X) + \var(Y) \pm 2\Cov(X, Y) \\
&= \var(X) + \var(Y) \pm 2\Cov(F^{-1}(U), G^{-1}(V)).
\end{aligned}
$$
If $U,V$ are independent then $\var(W_{\pm}) = \var(X) + \var(Y)$. But we can do better by correlating them and thus having a nonzero [[Covariance#Definition (Covariance)|covariance]].
> We care about $\pm$ because if we did only one, (i.e $+$) the covariance becomes negative, increasing variance. This requires us to care about both cases simultaneously. 
## Common Random Numbers (CRN)
Take $U = V$. This reduces $\var(W_{-})$ since
$$
\Cov(F^{-1}(U), G^{-1}(U)) \ge 0 \implies \var(W_{-}) \le \var(X) + \var(Y).
$$
## Antithetic Variates
Take $V = 1 - U$. This reduces $\var(W_{+})$ since
$$
\Cov(F^{-1}(U), G^{-1}(1 - U)) \le 0 \implies \var(W_{+}) \le \var(X) + \var(Y).
$$
# Lemma (monotone covariance sign)
Let $U \sim U[0, 1]$ and $\alpha, \beta : [0, 1] \to \R$. Then:
- $\Cov(\alpha(U), \beta(U)) \geq 0$ if $\alpha, \beta$ are increasing.
- $\Cov(\alpha(U), \beta(U)) \leq 0$ if $\alpha$ is increasing and $\beta$ is decreasing.
## Remark
$F^{-1}, G^{-1}$ are increasing. $G^{-1}(1 - U)$ is decreasing. Therefore the lemma applies to the antithetic construction.

Proof:

Let $U,V \sim \mathcal{U}[0, 1]$, iid. Assume $\alpha, \beta$ are increasing functions. Then 
$$
\begin{aligned}
0 
&\leq \left[ \alpha(U) - \alpha(V) \right] \cdot \left[ \beta(U) - \beta(V) \right] \\
&\leq \E{ (\alpha(U) - \alpha(V)) \cdot (\beta(U) - \beta(V)) } \\
&= 2\E{\alpha(U)\beta(U)} - 2\E{\alpha(V)}\E{\beta(V)} \\
&= 2\Cov(\alpha(U), \beta(U)).
\end{aligned}
$$
We can switch $\E{\alpha(V)}$ to $\E{\alpha(U)}$ by iid. The inequality reverses if $\alpha$ is increasing and $\beta$ is decreasing.


