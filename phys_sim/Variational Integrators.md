---
tags:
  - CSE_291G
---
# Variational Integrators
Standard numerical methods for solving ODEs (e.g. [[Numerical Methods#Forward Euler Method|Forward Euler Method]], or [[Numerical Methods#Runge-Kutta Method (RK4)|RK4]]) look at $F = ma$ at a specific point in time and try to blindly guess the next geometric slope. A **variational integrator** is a numerical method that tries to preserve the underlying geometric structure of the system. It defines the total physical energy of the system across a span of time ("discrete action") and uses calculus to find the trajectory that minimizes this energy over time (least action paths). 

In particular, we see that in [[Numerical Methods#Example 1.2 (2nd Order Discretization)|this example]], when $\Delta t$ is larger (i.e. $0.9$), the system is stable in "asteroid belts". Although the system is a good approximation, as it never explodes, it is still only an approximation. We can improve the accuracy of the system by replacing the RHS of the example with 
$$
\frac{\theta_{i+1} - 2\theta_i + \theta_{i-1}}{\Delta t^2}
= 4 \arg \left(
  1 + \frac{\Delta t^2}{4} e^{-i\theta_i}
\right)
$$
where $\arg$ calculates the angle of a [[Complex Numbers|complex number]] in the complex plane. The result is that the system is stable for all $\Delta t$, and removes the "asteroid belts" that we see in the previous example. 

![[numerical_methods_comparison.png]]

