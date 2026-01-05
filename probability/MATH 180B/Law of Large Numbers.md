---
tags:
  - MATH_180B
aliases:
  - LLN
  - SLLN
  - Strong LLN
---
# Definition
The Strong Law of Large Numbers states that the sample mean of a sequence of independent and identically distributed (i.i.d.) random variables converges to the expected value (true mean) with probability $1$ as the sample size approaches infinity.
# Formal Statement
Let 1$X_1, X_2, \dots$ be a sequence of i.i.d. random variables with finite expected value 2$E[X_i] = \mu$.3 Let $\bar{X}_n$ be the sample mean of the first $n$ variables:
$$
\ovl{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

The Strong Law states:
$$
P\left( \lim_{n \to \infty} \ovl{X}_n = \mu \right) = 1
$$
# Interpretation
The event that the sample mean does _not_ converge to the true mean has a probability of exactly zero. In a long sequence of experiments, the average of the results is virtually certain to equal the expected value.