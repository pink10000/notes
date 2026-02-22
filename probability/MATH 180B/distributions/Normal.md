---
tags:
  - MATH_180B
---
# The Normal (Gaussian) Distribution
The normal distribution is a continuous probability distribution characterized by its symmetric, bell-shaped curve. It is the most important probability distribution in statistics because it accurately describes many natural phenomena and serves as the foundation for inferential statistics.
## Definition & Parameters
A random variable $X$ is normally distributed with mean $\mu$ and variance $\sigma^2$, denoted as:
$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$
* **Mean ($\mu$):** Determines the center of the distribution (where the peak is).
* **Standard Deviation ($\sigma$):** Determines the spread or width of the bell curve.
## Probability Density Function (PDF)
The PDF of a normal distribution is given by:
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}  \exp \left(-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}\right)
$$
# Theorem (Sum of Independent Normal RVs)
If $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ and $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$ are **independent** random variables, then their sum $Z = X + Y$ is also normally distributed:
$$
X + Y \sim \mathcal{N}(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)
$$
> [!important] Variance Summation
> Notice that we add the **variances** ($\sigma^2$), not the standard deviations ($\sigma$).

For any linear combination $aX + bY$ (where $a$ and $b$ are constants):
$$
aX + bY \sim \mathcal{N}(a\mu_X + b\mu_Y, a^2\sigma_X^2 + b^2\sigma_Y^2)
$$

# Theorem (Standardization)
Any normal random variable $X$ can be transformed into a **Standard Normal Distribution** ($\mathcal{N}(0, 1)$) using the $Z$-score formula:
$$
Z = \frac{X - \mu}{\sigma}
$$
# Central Limit Theorem (CLT)
The [[Central Limit Theorem]] states that for a sufficiently large sample size ($n \geq 30$), the distribution of the sample mean $\ovl{X}$ will be approximately normal, even if the underlying population is not:
$$
\ovl{X} \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
$$
