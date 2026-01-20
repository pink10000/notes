---
tags:
  - MATH_180A
---
# Definition 
The **expectation** denoted as $\E{X}$ of some RV $X \sim f$ is defined as 
$$
\E{X} = \int_{-\infty}^{\infty} xf(x) \, dx 
$$
and for a particular $h$, 
$$
\E{h(X)} = \int_{-\infty}^{\infty} h(x)f(x) \, dx
$$
# Theorem (Linearity of Expectation)
The "Average of a Sum" is always equal to the "Sum of the Averages." This property allows you to break complex expected value problems into simpler, manageable pieces.

For any random variables $X$ and $Y$ (regardless of whether they are independent or dependent), and any constants $a$ and $b$:
1. Additivity:
    $$
    \mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]
    $$
2. Scaling (Homogeneity):
    $$
    \mathbb{E}[aX] = a \cdot \mathbb{E}[X]
    $$
3. Combined:
    $$
    \mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]
    $$