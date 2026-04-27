---
tags:
  - CSE_291G
---
# Dimensional Analysis
**Dimensional analysis** is a powerful tool for modeling and analysis of physical systems. It allows us to find the dimensionless quantities that govern the behavior of a system, reduce the number of parameters in a problem, and perform an equivalent system in a scaled model. 

# Definition (Dimension, Physics)
In physics, a **dimension** is a collection of measurements of one type of physical quantity. For example, length, mass, speed, acceleration, and force are all different dimensions. 

A dimension is a one-dimensional [[Vector Space|vector space]] over the field of real numbers. 

# Definition (Unit, Physics)
A **unit** for a dimension is a basis for the 1D vector space. A unit is a way to assign a numerical value to a physical quantity. Given any two elements of the same dimension $x, y \in \mathsf{D}$ and $y \neq 0$, there exists a unique scalar $s \in \R$ so that $x = s y$. 

# Multiplication of Dimensions
Dimensions can be added together and multiplied by scalars, but cannot be added/subtracted from each other. We can however multiply dimensions together to get new dimensions. For example, speed is the product of length and inverse time.

A dimension is denoted by sans serif font $\mathsf{D}$. Each element $x \in \mathsf{D}$ is a measurement. The *dimensionless dimension* $\R$ has a standard unit $1$. The bracket of a measurement in the dimension it is in is denoted by 
$$
\mathsf{D} = [x]
$$
For example, $[\text{kg}] = [5 \text{ kg}] = [\text{lb}] = \mathsf{M}$. An example of a product is 
$$
[x][y] = [xy]
$$
We can consider a collection of all dimensions that can be involved 
$$
\mathscr{D} = \{\R, \mathsf{D}_1, \mathsf{D}_2, \ldots\}
$$
which should be closed under multiplication, forming an [[Group#Definition (Abelian Group)|abelian group]]. 

# Physical Dimensions 
In physics, the space of dimensions is a finitely generated [[Group#Definition (Free Group)|free]] [[Group#Definition (Abelian Group)|abelian group]] by $7$ standard base dimensions. 

| Primary dimension |       Symbol        | SI Unit       |
| :---------------- | :-----------------: | :------------ |
| Mass              |   $\mathsf{M}$    | kg (kilogram) |
| Length            |   $\mathsf{L}$    | m (meter)     |
| Time              |   $\mathsf{T}$    | s (second)    |
| Temperature       | $\mathsf{\Theta}$ | K (Kelvin)    |
| Electric current  |   $\mathsf{I}$    | A (Ampere)    |
| Amount of light   |   $\mathsf{C}$    | cd (candela)  |
| Amount of matter  |   $\mathsf{N}$    | mol (mole)    |

Every physical dimension takes the form of 
$$
\mathsf{M}^{n_1} \mathsf{L}^{n_2} \mathsf{T}^{n_3} \mathsf{\Theta}^{n_4} \mathsf{I}^{n_5} \mathsf{C}^{n_6} \mathsf{N}^{n_7}
$$
represented as a 7D vector of integers $(n_1, n_2, n_3, n_4, n_5, n_6, n_7) \in \Z^7$. Multiplication between dimensions corresponds to addition of the corresponding vectors. For example, consider the dimension of force. 
$$
[\text{force}] = \mathsf{M} \mathsf{L} \mathsf{T}^{-2}
\quad\quad\quad
(1, 1, -2, 0, 0, 0, 0)^{\top}
$$
The 7D vector representation of the dimension of a dimensionless number is the zero vector.

# Dimension Homogeneity
In an equation of inequality, every additive term must have the same dimension. 

## Example 1 (Bernoulli's Equation)
Bernoulli's equation states that for an incompressible fluid, the following holds:
$$
\frac{1}{2} \rho v^2 + P + \rho g h = \text{constant}
$$
where 
- $\rho$ is the density of the fluid, with dimension $\mathsf{M} \mathsf{L}^{-3}$,
- $v$ is the speed of the fluid, with dimension $\mathsf{L} \mathsf{T}^{-1}$,
- $P$ is the pressure of the fluid, with dimension $\mathsf{M} \mathsf{L}^{-1} \mathsf{T}^{-2}$,
- $g$ is the acceleration due to gravity, with dimension $\mathsf{L} \mathsf{T}^{-2}$,
- $h$ is the height of the fluid, with dimension $\mathsf{L}$.

Thus, the dimension of each term (and consequently, the constant) is $\mathsf{M} \mathsf{L}^{-1} \mathsf{T}^{-2}$. 

# Dimensionless Equations
The idea is to rescale the physical variables so that they are all dimensionless. The equation is then a relationship between dimensionless variables, leaving us as few parameters as possible. We obtain the same result when the dimensionless parameters matches, even if the original problem is **at vastly different scale**.

## Example 2 (Parabolic Free Fall)
We can let height of an object in free fall be $z(t)$, as a function of time $t$. The equation of motion is
$$
z(t) = z_0 + v_0 t - \frac{1}{2} g t^2
$$
where $z_0$ is the initial height, $v_0$ is the initial velocity, and $g$ is the acceleration due to gravity. It's the solution to 
$$
\ddot{z}(t) = -g 
\quad\quad\quad
z(0) = z_0
\quad\quad\quad
\dot{z}(0) = v_0
$$
There are 3 parameters ($z_0$, $v_0$, $g$), but we can reduce them into 1 parameter. Let $z^*$ be the dimensionless height and $t^*$ be the dimensionless time. We can choose the following scaling:
$$
z^* = \frac{z}{z_0}
\quad\quad\quad
t^* = \frac{tv_0}{z_0}
$$
Substituting these dimensionless variables back into the original equation consolidates the parameters into a single dimensionless parameter called the Froude number:
$$
\text{Fr} = \frac{v_0}{\sqrt{g z_0}}
$$
The rescaled equation now depends entirely on the Froude number:
$$
z^* = 1 + t^* - \frac{1}{2\text{Fr}^2} (t^{*})^2
$$
The result is that the maximum peak height is calculated as 
$$
z^*_{\max} = 1 + \frac{\text{Fr}^2}{2}
$$
The significance of this is that if we have two different free fall problems with the same Froude number, they will have the same maximum peak height in terms of their respective initial heights, regardless of the actual values of $z_0$, $v_0$, and $g$.

# Example 3 (Navier-Stokes Equation)
The Navier-Stokes equation for an incompressible fluid is given by
$$
\frac{\del u}{\del t} + (u \cdot \nabla u) 
= -\frac{\nabla p}{\rho} + \frac{\mu}{\rho} \nabla \cdot \nabla u
$$
where
We assume density and viscosity are constant.
- Time and time derivative: $[t] = \mathsf{T}$ and $\left[ \frac{\del}{\del t} \right] = \mathsf{T}^{-1}$
- Space and spatial derivatives: $[x] = \mathsf{L}, [\nabla] = \mathsf{L}^{-1}, [\nabla \cdot \nabla] = \mathsf{L}^{-2}$
- Velocity: $[u] = \mathsf{L} \mathsf{T}^{-1}$,
- Density: $[\rho] = \mathsf{M} \mathsf{L}^{-3}$
- Pressure: $[p] = \mathsf{M} \mathsf{L}^{-1} \mathsf{T}^{-2}$,
- Viscosity (stress per speed gradient): $[\mu] = \mathsf{M} \mathsf{L}^{-1} \mathsf{T}^{-1}$

To create a dimensionless equation, the physical variables are rescaled using a characteristic length $L$ and a characteristic speed $U$. For example, in flow past an object, $L$ could be the diameter of the object and $U$ could be the background fluid speed. 
- $x^* = \frac{x}{L}$
- $t^* = \frac{tU}{L}$
- $u^* = \frac{u}{U}$
- $p^* = \frac{p}{\rho U^2}$

Thus, 
$$
\frac{\del u}{\del t} + (u \cdot \nabla u) 
= -\frac{\nabla p}{\rho} + \frac{\mu}{\rho} \nabla \cdot \nabla u
\iff 
\frac{\del u^*}{\del t^*} + (u^* \cdot \nabla^* u^*)
= -\nabla^* p^* + \frac{1}{\text{Re}} \nabla^* \cdot \nabla^* u^*
$$
where $\text{Re} = \frac{\rho U L}{\mu}$ is the **Reynolds number**. The Reynolds number is a dimensionless parameter that characterizes the physical behavior of the fluid. At *low* Reynolds numbers, viscous forces dominate, resulting in smooth, orderly flow. At *high* Reynolds numbers, inertial forces dominate, leading to turbulent/chaotic flow.

![[reynolds_num_comparison.png]]
