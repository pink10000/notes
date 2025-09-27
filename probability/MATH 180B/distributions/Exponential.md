---
tags:
  - MATH_180B
---
The **exponential distribution** is a continuous probability distribution commonly used to model the time between events in a Poisson process. It is characterized by a single parameter $ \lambda > 0 $, known as the **rate parameter**.

---

## Probability Density Function (PDF)

The probability density function of the exponential distribution is:

$$
f_X(x) = \begin{cases} 
\lambda e^{-\lambda x}, & x \geq 0, \\
0, & x < 0.
\end{cases}
$$
- $ x $ represents the time or distance between events.
- $\lambda$ controls the rate of decay; higher $\lambda$ values result in a steeper decline.

---

## Cumulative Distribution Function (CDF)

The cumulative distribution function is the integral of the PDF:

$$
F_X(x) = \int_{0}^{x} \lambda e^{-\lambda t} \, dt = 
\begin{cases} 
1 - e^{-\lambda x}, & x \geq 0, \\
0, & x < 0.
\end{cases}
$$
The CDF represents the probability that $X \leq x$.

---

## Expectation (Mean)

The expected value of an exponential random variable $X$ is given by:

$$
E[X] = \frac{1}{\lambda}.
$$

This is the average time or distance between events.

---

## Variance

The variance of an exponential random variable $X$ is:
$$
\var(X) = \frac{1}{\lambda^2}
$$
The standard deviation is the square root of the variance, $\sigma_X = \frac{1}{\lambda}$.

---

## Key Properties

1. **Memorylessness**: The exponential distribution is the only continuous distribution with the property that:
$$
\Pr(X > x + t \mid X > t) = \Pr(X > x), \quad \forall x, t \geq 0.
$$
   This means that the distribution does not "remember" past events.

2. **Relationship with the Poisson Process**: If the time between events follows an exponential distribution with rate $\lambda$, the number of events in a time interval of length $t$ follows a Poisson distribution with mean $\lambda t$.