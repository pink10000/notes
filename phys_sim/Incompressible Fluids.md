---
tags:
  - CSE_291G
---
# Background
There are structural similarities between the equations of motion for an incompressible fluid and [[Rigid Body Dynamics|rigid body]] rotation. By examining their state spaces, symmetries, and the [[Lagrangian Mechanics#Least Action Principle|Principle of Least Action]], we can derive the [[Calculus of Variations#Euler-Lagrange Equation|Euler equations]] for both systems using a unified geometric framework, or the **Euler-Arnold equations**.  

# Definition (Incompressible Fluid)
A fluid is **incompressible** if its density $\rho$ is constant (WLOG, let $\rho = 1$) throughout its motion. 

Suppose $u$ is its velocity. So we have 
$$
\left\{
  \begin{aligned}
    \dot{u} + \nabla_u u = -\nabla p \\ 
  \end{aligned}
\right.
$$