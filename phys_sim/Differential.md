---
tags:
  - CSE_291G
---
# Definition (Differential)
The **differential** of a function $f: \mathbb{R}^n \to \mathbb{R}^m$ at a point $x$ is a linear map that approximates the change in $f$ near $x$. For example, if $f$ is defined on $\R^2$ i.e. $f(\theta_1, \theta_2)$, then the differential is given by 
$$
df = \frac{\partial f}{\partial \theta_1} d\theta_1 + \frac{\partial f}{\partial \theta_2} d\theta_2
$$

## Differential vs Derivative
It is common misconception that the differential and derivative are the same thing. The derivative of a function $f$ at a point $x$ is a number that represents the rate of change of $f$ at that point. The differential, on the other hand, is a linear map that takes in a direction $\vec{v}$ and returns the directional derivative $df \llbracket \vec{v} \rrbracket$ that approximates the change in $f$ near $x$. It is **not** $\nabla f$. 
