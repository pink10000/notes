---
tags:
  - CSE_291G
---
# Lagrangian Mechanics
Lagrangian mechanics is the application of the [[Calculus of Variations|calculus of variations]] to classical mechanics. It derives the equations of motion for a system by finding the stationary point of a functional called the **action**.

# Least Action Principle
Let $y(t) : [0, T] \to \R^{3N}$ represent the position of $N$ particles. Call $v(t) := \dot{y}(t)$ the velocity of the particles. Suppose the dynamics of the particles is governed by Newton's law
$$
\frac{d}{dt} Mv(t) = f(y(t))
$$
for a mass matrix $M \in \R^{3N \times 3N}$ (stores the mass of every particle) and a force model $f: \R^{3N} \to \R^{3N}$. The kinetic energy is 
$$
K(y, v) = \frac{1}{2} v^{\top} M v
$$
The potential energy $U(y)$ is a function of positions $U : \R^{3N} \to \R$, so that 
$$
-\frac{\partial U}{\partial y}\bigg|_y = f(y)
$$
if the force is conservative (conservative vector field), i.e. the force pushing the particles is entirely determined by the "slope" of the energy landscape at their current position. 
# Definition (The Lagrangian)
We say that the Lagrangian of a system is the quantity $L$ defined as
$$
L(y, v) := K(y, v) - U(y)
$$
where 
- kinetic energy $K(y, v) = \frac{1}{2} v^{\top} M v$
- potential energy $U(y)$ such that $\left.-\frac{\partial U}{\partial y}\right|_y = f(y)$

## Theorem (Least Action Principle)
The Newton's law of of motion 
$$
\frac{d}{dt} Mv(t) = f(y(t))
$$
is the [[Calculus of Variations#Theorem (Euler-Lagrange Equation)|Euler-Lagrange equation]] for the *total action functional*
$$
\mathcal{S}(y) := \int_{t=0}^T L\left(y(t), \dot{y}(t)\right) dt
$$
Proof: We have that 
$$
\begin{aligned}
\frac{\del L}{\del y} - \frac{d}{dt} \left( \frac{\del L}{\del v} \right) &= 0 \\
\end{aligned}
$$
Since the kinetic energy $K$ does not depend on the position $y$, we have $\frac{\del K}{\del y} = 0$, and that potential energy $U$ only depends on $y$. Thus, we have
$$
\begin{aligned}
-\frac{\del U}{\del y} - \frac{d}{dt} \left( \frac{\del K}{\del v} \right) &= 0 \\
f(y) - \frac{d}{dt} \frac{1}{2} \nabla_v (v^{\top} Mv)  &= 0 \\
\frac{d}{dt} \frac{1}{2} (M + M^{\top})v &= f(y) \\
\frac{d}{dt} \frac{1}{2} (M + M)v &= f(y) \\
\frac{d}{dt} Mv &= f(y)
\end{aligned}
$$
> The second line deserves some explanation. See [here](https://www.cs.ubc.ca/~schmidtm/Courses/340-F16/linearQuadraticGradients.pdf) for a better proof. 

Then, as only $v$ depends on time, we can rewrite the above as
$$
f(y) = Ma
$$

> Symmetry is important here. Although $M$ is nicely diagonal where $M_{ii}$ is the mass of the $i$-th particle, and $M_{ij} = 0$ for $i \neq j$ (this is a consequence of the fact that we use a nice 3D Cartesian coordinate system to represent the positions of the particles), the real reason is that $M$ is symmetric $M_{ij} = M_{ji}$ to satisfy Newton's third law of motion.

## Applicability 
The least action principle (or stationary-action principle) works for any conservative system made of particles.
- Elastic body
- Fluid
- Rigid boy
There are systems with non-conservative (dissipative) forces, such as viscosity, heat, friction. 

# Why is this useful?
If LAP is equivalent to Newton's law that $f = ma$, what is the point?
- reduced order modeling (generalized coordinates)
  - A rigid object, like a bar-pendulum (a pendulum but the rod actually has mass) consists of a near-infinite number of particles. 
  - Accounting all forces acting on each other is impossible. 
  - It is not obvious how rigid body motions like torque and angular momentum should arise from Newton's laws. 
  - Knowing that macroscopically the rigid body system can only move in a few degrees of freedom, we can parameterize the location of each particle using smaller coordinates. 
  - It is easy to pullback the Lagrangian from particle system to the parameter space, and derive the equations of motion.
- derive structure-preserving discretizations (recall [[Numerical Methods#Forward Euler Method]])

## Example 1 (Compound Pendulum)
Consider a compound pendulum. The only mass of this system is the rod that connects the pivot.

Suppose we had $10^{23}$ particles ($1/6$ a $\text{mol}$). Computing the rotational dynamics of the rod in Newtonian mechanics requires $10^{23}$ ODEs for each of the positions, and another near infinite number of ODEs dictating that no two particles can move relative to one another. This gives us $\R^{\infty}$ space of postions and velocities of all particles in the body.

This is hard. On the other hand, no matter the number of atoms in the rigid bar, its position and orientation in 3D space can be completely described by 6 parameters
- $x,y,z$ for the position of the center of mass
- $\theta, \phi, \psi$ angles describing the rotation
Given that the Lagrangian $L = K - U$ only cares about the kinetic and potential energy of the system, we can pullback the Lagrangian from the particle system to the 6D parameter space, and derive the equations of motion for these 6 parameters. This is a much more tractable problem.

So, consider the position of the $\alpha$-th particle
$$
\begin{bmatrix}
x(\theta, \alpha) \\ y(\theta, \alpha)
\end{bmatrix}
= 
\begin{bmatrix}
\alpha \sin(\theta) \\ -\alpha \cos(\theta)
\end{bmatrix}
\quad\quad \alpha \in [0, \ell]
$$
where $\ell$ is the length of the rod and $\alpha$ is the distance of the particle from the pivot. It's velocity is 
$$
\frac{d}{dt} \begin{bmatrix}
x(\theta, \alpha) \\ y(\theta, \alpha)
\end{bmatrix}
= 
\begin{bmatrix}
\alpha \cos(\theta) \\ \alpha \sin(\theta)
\end{bmatrix} \dot{\theta}
$$
The mass of the particle is $\frac{m}{\ell} d\alpha$ where $m$ is the total mass of the rod. The total kinetic energy is then 
$$
K(\theta, \dot{\theta}) 
= \int_{\alpha=0}^{\ell} \frac{1}{2} \frac{m}{\ell} \left(\alpha \dot{\theta}\right)^2 d\alpha
= \frac{m\ell^2}{6} \dot{\theta}^2
$$
The total potential energy is 
$$
U(\theta) = \int_{\alpha=0}^{\ell} \frac{mg}{\ell} (-\alpha \cos \theta) d\alpha = -\frac{mg\ell}{2} \cos \theta
$$
> We use integrals here because we are summing over the kinetic and potential energy of all particles in the rod. Since the rod is continuous, we have infinitely many particles, and thus we need to use integrals instead of summations. 

Let's look at the Lagrangian.
$$
L(\theta, \dot{\theta}) = K(\theta, \dot{\theta}) - U(\theta) = \frac{m\ell^2}{6} \dot{\theta}^2 + \frac{mg\ell}{2} \cos \theta
$$
and the Euler-Lagrange equation
$$
\frac{\partial L}{\partial \theta}(\theta, \dot{\theta})
- \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}}(\theta, \dot{\theta}) \right) = 0
$$
Applying the equation, we get 
$$
\ddot{\theta} = -\frac{3}{2} \frac{g}{\ell} \sin \theta
$$

> Compare this to the simple pendulum where $\ddot{\theta} = -\frac{g}{\ell} \sin \theta$. The compound pendulum has an extra factor of $\frac{3}{2}$. This mathematically proves that a rigid rod swings *faster* than a point mass at the end of a massless rod of the same length. This is because the rod's mass is distributed evenly along its length (center of mass at $\ell/2$) making it easier to swing than a point mass.

# Noether's Theorem of Time Independence
Suppose the Lagrangian is time independent
$$
L(t, y, \dot{y}) = L(y, \dot{y})
$$
then the Euler-Lagrange ODE 
$$
\frac{\partial L}{\partial y}(y, \dot{y}) - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \right) = 0
$$
implies that 
$$
\left\langle \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \middle| \dot{y} \right\rangle - L(y, \dot{y}) 
$$
is time independent. 

Proof: We need to check that 
$$
\frac{d}{dt} \left(
\left\langle \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \middle| \dot{y} \right\rangle - L(y, \dot{y}) \right) = 0
$$
So, 
$$
\begin{aligned}
\frac{d}{dt} \left(
\left\langle \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \middle| \dot{y} \right\rangle - L(y, \dot{y}) \right) 
&=   
\left(
  \left\langle \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \right) \middle| \dot{y} \right\rangle +
  \left\langle \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \middle| \ddot{y} \right\rangle
\right)
- \frac{dL}{dt}
\\
&= 
\left(
  \left\langle \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \right) \middle| \dot{y} \right\rangle +
  \left\langle \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \middle| \ddot{y} \right\rangle
\right)
- \left\langle
\frac{\partial L}{\partial y} \middle| \dot{y} \right\rangle 
- \left\langle \frac{\partial L}{\partial \dot{y}} \middle| \ddot{y} 
\right\rangle
\\
&= \left\langle \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{y}}(y, \dot{y}) \right) \middle| \dot{y} \right\rangle
- \left\langle
\frac{\partial L}{\partial y} \middle| \dot{y} \right\rangle 
\\
&= 0
\end{aligned}
$$
where the last line is because of the Euler-Lagrange equation.  

For
$$
L = \frac{1}{2} \dot{y}^{\top} M \dot{y} - U(y)
$$
this time-independent quantity is the total energy of the system
$$
E = \frac{1}{2} \dot{y}^{\top} M \dot{y} + U(y)
$$
Time-independence of the Lagrangian implies the *Law of Conservation of Energy*.
