---
tags:
  - MATH_180A
---
# Probability Moments
Moments are a set of statistical parameters used to measure the characteristics of a distribution's shape. For a random variable $X$, the $n$-th moment is the expected value of the $n$-th power of $X$.
## Raw Moments (About the Origin)
Raw moments are calculated relative to zero. The $n$-th raw moment is denoted as $\mu'_n$:
$$
\mu'_{n} = E[X^{n}]
$$
The [[Expectation|mean]] ($\mu$), representing the "center of mass" of the distribution.

## Central Moments (About the Mean)
Central moments describe the shape of the distribution independent of its location. The $n$-th central moment is denoted as $\mu_n$:
$$
\mu_n = E[(X - \mu)^n]
$$

* **1st Central Moment:** Always equals $0$.
* **2nd Central Moment:** The [[Variance]] ($\sigma^2$), measuring the spread or scale.
* **3rd Central Moment:** Used to calculate **Skewness** (asymmetry).
* **4th Central Moment:** Used to calculate **Kurtosis** (thickness of tails).

## Standardized Moments
To compare different distributions regardless of scale, moments are normalized by the standard deviation $\sigma$:

$$\tilde{\mu}_n = \frac{\mu_n}{\sigma^n}$$

| Moment | Name | Interpretation |
| :--- | :--- | :--- |
| $\mu'_1$ | **Mean** | Central location. |
| $\mu_2$ | **Variance** | Width/Dispersion. |
| $\tilde{\mu}_3$ | **Skewness** | Direction and strength of the tail. |
| $\tilde{\mu}_4$ | **Kurtosis** | Frequency of outliers ("Peakedness"). |

## Moment Generating Function (MGF)
The MGF is a powerful tool that "encapsulates" all moments into a single function:
$$
M_X(t) = E[e^{tX}]
$$
To extract the $n$-th raw moment, differentiate the MGF $n$ times and evaluate at $t=0$:
$$
\mu'_n = \left. \frac{d^n}{dt^n} M_X(t) \right|_{t=0}
$$