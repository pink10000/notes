| Distribution      | PDF/CDF                                           | Expectation $E[X]$ | Variance $\text{Var}(X)$  | Second Moment $E[X^2]$   |
|------------------|--------------------------------------------------|--------------------|--------------------|-------------------------|
| **Bernoulli(p)** | PDF: $p^x (1-p)^{1-x}, x \in \{0,1\}$  | $p$           | $p(1-p)$      | $p$                 |
| **Binomial(n, p)** | PDF: $\binom{n}{k} p^k (1-p)^{n-k}$        | $np$          | $np(1-p)$     | $np(1-p) + (np)^2$  |
| **Geometric(p)** | PDF: $(1-p)^{k-1} p, k \in \{1,2,\dots\}$ | $1/p$         | $(1-p)/p^2$   | $(2-p)/p^2$         |
| **Poisson(λ)**   | PDF: $\frac{\lambda^k e^{-\lambda}}{k!}, k \in \{0,1,2,\dots\}$ | $\lambda$    | $\lambda$     | $\lambda + \lambda^2$ |
| **Uniform(a, b)** | PDF: $\frac{1}{b-a}, a \leq x \leq b$  | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | $\frac{a^2 + ab + b^2}{3}$ |
| **Exponential(λ)** | PDF: $\lambda e^{-\lambda x}, x > 0$ | $1/\lambda$   | $1/\lambda^2$ | $2/\lambda^2$       |
| **Normal(μ, σ²)** | PDF: $\frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | $\mu^2 + \sigma^2$ |
| **Gamma(k, λ)** | PDF: $\frac{\lambda^k x^{k-1} e^{-\lambda x}}{\Gamma(k)}, x > 0$ | $k/\lambda$ | $k/\lambda^2$ | $(k+1)/\lambda^2$ |
