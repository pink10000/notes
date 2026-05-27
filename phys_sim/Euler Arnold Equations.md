---
tags:
  - CSE_291G
---
# Background
There are structural similarities between the equations of motion for an incompressible fluid and [[Rigid Body Dynamics|rigid body]] rotation. By examining their state spaces, symmetries, and the [[Lagrangian Mechanics#Least Action Principle|Principle of Least Action]], we can derive the [[Calculus of Variations#Euler-Lagrange Equation|Euler equations]] for both systems using a unified geometric framework, or the **Euler-Arnold equations**.  

The core realization of the EA-equations are that equations governing [[Fluid Mechanics#Incompressible Fluids|incompressible fluids]] and [[Rigid Body Dynamics|rigid bodies]] are describing the exact same geometric phenomenon on different types of spaces.
$$
\begin{aligned}
  \left\{
    \begin{aligned}
    \dot{\bu} + \nabla_{\bu} \bu &= - \nabla p \\
    \nabla \cdot \bu &= 0 \\
    \end{aligned}
  \right.
  &\quad\quad\quad\quad\quad\quad
  \left\{
    \begin{aligned}
    \bI_{\text{body}} \dot{\Omega} + \Omega \times (\bI_{\text{body}} \Omega) &=0 \\
    \end{aligned}
  \right.
\end{aligned}
$$
where the [[Continuum Mechanics#Definition (Flow Velocity)|flow map]] is $\dot{\phi} = u \circ \phi$ and the rotational velocity is $\dot{\bR} = \bR[\Omega \times]$. The left describes how the spatial velocity field evolves over time, balanced by the pressure gradient. The right describes how the angular velocity evolves over time. 

The first equation is no different from $F = ma$. Note that since the fluid is incompressible, the density $\rho = 1$ everywhere. 
- The $\dot{\bu}$ represents the local acceleration, i.e. how the velocity changes at a fixed point in space. - The $\nabla_{\bu} \bu$ represents the **convective acceleration** (or $(\bu \cdot \nabla) \bu$) represents how the velocity changes as a fluid particle moves to a new a region of space where the overall velocity field is different.
- The pressure gradient $-\nabla p$ is the driving force in $F = ma$. Fluids naturally accelerate from areas of high pressure to areas of low pressure; the negative sign indicates that the acceleration is in the opposite direction of the pressure gradient.

Finally, $\nabla \cdot \bu = 0$ represents the [[Fluid Mechanics#Incompressible Fluids|conservation of mass]] for an incompressible fluid. The flow map $\phi$ maps the initial position of a fluid particle to its position at time $t$; this is similar to the rotation matrix $\bR$ mapping the initial orientation of a rigid body to its orientation at time $t$. 

> We'll keep fluids on the left, and rigid bodies on the right.

# Variables 
Fluids and rigid bodies operate on different state spaces. 
$$
\begin{aligned}
  \left\{
    \begin{aligned}
    \text{State:} \quad& \phi : M \to W \\
    \text{Constraint:} \quad& \frac{d}{dt} \left( \phi^* \mu \right) = 0
    \end{aligned}
  \right.
  &\quad\quad\quad\quad\quad\quad
  \left\{
    \begin{aligned}
    \text{State:} \quad& \bR : \R^{3}_{\text{body}} \xrightarrow{\text{linear}} \R^{3}_{\text{world}} \\
    \text{Constraint:} \quad& \bR^\top \bR = \bR \bR^\top = \bI
    \end{aligned}
  \right.
\end{aligned}
$$
where $\bR$ is an [[Special Orthogonal Group|orthogonal]] rotation matrix. The fluid motion constraint formally defines the incompressiblility of the fluid. Indeed, $\mu$ is annotated as $dV$, some standard unit of volume in the world space. The [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] $\phi^{*}$ pulls $dV$ back to $M$, where the $0$ time derivative ensures that the volume of any arbitrary chunk of fluid is constant.

# Representation of Velocity 
We have already discussed this; but once again, 
$$
\begin{aligned}
  \dot{\phi} = \bu \circ \phi
  &\quad\quad\quad\quad\quad\quad
  \dot{\bR} = \bR[\Omega \times]
\end{aligned}
$$
where $\bu$ is a div-free vector field on $W$ and $[\Omega \times]$ is a [[Skew-Symmetric Matrix]]. 

# Kinetic Energy
$$
\begin{aligned}
  \left\{
    \begin{aligned}
    K(\phi, \dot{\phi}) 
      &= \frac{1}{2} \int_{M} \| \dot{\phi} \|^2 \rho_M \\
      &= \frac{1}{2} \int_{W} \| \bu \|^2 dV
    \end{aligned}
  \right.
  &\quad\quad\quad\quad\quad\quad
  \left\{
    \begin{aligned}
    K(\bR, \dot{\bR}) 
      &= \frac{1}{2} \int_{\ba \in M} \| \bR \ba \|^2 dm_{\ba} \\
      &= \frac{1}{2} \Omega^\top \bI_{\text{body}} \Omega
    \end{aligned}
  \right.
\end{aligned}
$$
The kinetic energy of a fluid is **right-invariant**. Let $\psi = \phi \circ \tilde{\phi}$. for some pertubation $\tilde{\phi} : M \to M$.
$$
K(\psi, \dot{\psi}) = K(\phi, \dot{\phi}) = K(u)
$$
We can think of $\tilde{\phi}$ as some "relabeling" of the fluid particles. If we paused the system, relabeled the particles, and then unpaused, the kinetic energy would be the same.

The kinetic energy of a rigid body is **left-invariant**. Let $\bQ$ be some rotation matrix.
$$
K(\bQ\bR, \dot{\bQ\bR}) = K(\bR, \dot{\bR}) = K(\Omega)
$$
for any $\bQ \in \SO(3)$. 

Here is a structured, scannable way to format these concepts for your notes. This layout uses a side-by-side comparative approach to emphasize the mathematical symmetry your professor is teaching.

# Preparation for Variation: Euler-Poincaré Method
To apply the [[Lagrangian Mechanics#Least Action Principle|principle of least action]], we must find how the physical velocity of a system changes when its path is subjected to an infinitesimal virtual variation.

Definitions:
- **Physical Velocity ($\cdot$):** The actual derivative with respect to time $t$.
  $$
  \dot{\phi} = \bu \circ \phi \quad\quad\quad \dot{\bR} = \bR[\Omega_\times]
  $$
- **Virtual Velocity ($\circ$):** The derivative with respect to an arbitrary variation parameter $\epsilon$.
  $$
  \mathring{\phi} = \bv \circ \phi \quad\quad\quad \mathring{\bR} = \bR[V_\times]
  $$

- **Commutativity:** Because time and the variation parameter are independent variables, their mixed partial derivatives commute.
  $$
  \frac{\partial}{\partial t}\left(\frac{\partial}{\partial \epsilon}\right) 
  = \frac{\partial}{\partial \epsilon}\left(\frac{\partial}{\partial t}\right)
  $$
  Commutativity allows us to show that 
  $$
  \dot{\mathring{\phi}} = \mathring{\dot{\phi}}
  \quad\quad\quad
  \dot{\mathring{R}} = \mathring{\dot{R}}
  $$
  which is the key step in deriving the Euler-Poincaré equations.


We can immediately use commutativity to express the variation.
$$
\begin{aligned}
  \dot{\mathring{\phi}} &= \dot{\bv} \circ \phi + (\nabla \bv)(\bu \circ \phi) \\
  \mathring{\dot{\phi}} &= \mathring{\bu} \circ \phi + (\nabla \bu)(\bv \circ \phi) \\
  \implies & \dot{\bu} = \dot{\bv} + 
    \underbrace{\nabla_{\bu} \bv - \nabla_{\bv} \bu}_{[\bu, \bv]}
\end{aligned}
$$
where $[\bu, \bv]$ is the Lie bracket of the two vector fields. Likewise, with rigid bodies,
$$
\begin{aligned}
  \dot{\mathring{R}} &= \bR[\dot{V}_\times] + \bR[\Omega_\times][V_\times] \\
  \mathring{\dot{R}} &= \bR[\mathring{\Omega}_\times] + \bR[V_\times][\Omega_\times] \\
  \implies & \mathring{\Omega} = \dot{V} + \Omega \times V
\end{aligned}
$$
via matrix commutator properties.

## Applying the Principle of Least Action
The principle of least action states that the actual path taken by a system between two states is the one that minimizes the action, which is the integral of the Lagrangian (kinetic energy minus potential energy) over time. 

### Rigid Bodies
For rigid bodies, we have 
$$
\begin{aligned}
S &= \int_0^T \frac{1}{2} \Omega^T \bI \Omega \, dt \\
\mathring{S} &= \int_0^T \Omega^T \bI \mathring{\Omega} \, dt = 0 \\
0 &= \int_0^T \Omega^\top \bI (\dot{V} + \Omega \times V) \, dt \\
0 &= \int_0^T (\bI\Omega)^\top \dot{V} \, dt + \int_0^T (\bI\Omega)^\top (\Omega \times V) \, dt \\
% 
& \\
\int_0^T (\bI\Omega)^\top \dot{V} \, dt 
  &= \left[ (\bI\Omega)^\top V \right]_0^T - \int_0^T (\bI\dot{\Omega})^\top V \, dt \\
  &= -\int_0^T (\bI\dot{\Omega})^\top V \, dt \quad \text{(since  $V(0)=V(T)=0$)} \\
% 
& \\
(\bI\Omega)^\top (\Omega \times V) &= (\bI\Omega) \cdot (\Omega \times V) \\
  &= ((\bI\Omega) \times \Omega) \cdot V \\
  &= -(\Omega \times (\bI\Omega)) \cdot V \\
  &= -(\Omega \times (\bI\Omega))^\top V \\
% 
& \\
0 &= -\int_0^T (\bI\dot{\Omega})^\top V \, dt - \int_0^T (\Omega \times (\bI\Omega))^\top V \, dt \\
0 &= -\int_0^T \left( \bI\dot{\Omega} + \Omega \times (\bI\Omega) \right)^\top V \, dt \\
\implies \quad \bI\dot{\Omega} + \Omega \times (\bI\Omega) &= 0
\end{aligned}
$$
The goal here was to remove the time derivative on $V$ via integration by parts over time.

### Incompressible Fluids
For incompressible fluids, we have 
$$
\begin{aligned}
S &= \int_0^T \left( \int_W \frac{1}{2} \langle \bu, \bu \rangle \, dV - \int_W \varphi (\nabla \cdot \bu) \, dV \right) dt \\
\mathring{S} &= \int_0^T \int_W \left( \langle \bu, \mathring{\bu} \rangle - \varphi (\nabla \cdot \mathring{\bu}) \right) dV \, dt = 0 \\
0 &= \int_0^T \int_W \langle \bu + \nabla \varphi, \mathring{\bu} \rangle \, dV \, dt \quad \text{(Integration by parts on divergence)} \\
0 &= \int_0^T \int_W \langle \bu + \nabla \varphi, \dot{\bv} + \nabla_{\bu} \bv - \nabla_{\bv} \bu \rangle \, dV \, dt \\
% 
& \\
\langle \bu + \nabla \varphi, \dot{\bv} \rangle &\xrightarrow{\text{IBP } t} \langle -\dot{\bu} - \nabla \dot{\varphi}, \bv \rangle \\
\langle \bu + \nabla \varphi, \nabla_{\bu} \bv \rangle &\xrightarrow{\text{IBP } x} \langle -\nabla_{\bu}\bu - \nabla_{\bu}\nabla \varphi, \bv \rangle \\
\langle \bu + \nabla \varphi, -\nabla_{\bv} \bu \rangle &= \langle -(\nabla \bu)^\top (\bu + \nabla \varphi), \bv \rangle \\
% 
& \\
0 &= \int_0^T \int_W \left\langle -\dot{\bu} - \nabla \dot{\varphi} - \nabla_{\bu} \bu - \nabla_{\bu} \nabla \varphi - (\nabla \bu)^\top \bu - (\nabla \bu)^\top \nabla \varphi, \bv \right\rangle dV \, dt \\
\implies 0 &= \dot{\bu} + \nabla_{\bu} \bu + (\nabla \bu)^\top \bu + \nabla \dot{\varphi} + \nabla_{\bu} \nabla \varphi + (\nabla \bu)^\top \nabla \varphi \\
% 
& \\
(\nabla \bu)^\top \bu &= \frac{1}{2} \nabla |\bu|^2 \\
\nabla \tilde{p} &= \nabla (\dot{\varphi} + \nabla_{\bu} \varphi) = \nabla \dot{\varphi} + \nabla_{\bu} \nabla \varphi + (\nabla \bu)^\top \nabla \varphi \\
0 &= \dot{\bu} + \nabla_{\bu} \bu + \frac{1}{2} \nabla |\bu|^2 + \nabla \tilde{p} \\
\dot{\bu} + \nabla_{\bu} \bu &= -\nabla \left( \tilde{p} + \frac{1}{2} |\bu|^2 \right) = -\nabla p
\end{aligned}
$$
where $\varphi$ is the incompressible fluid constrait Lagrange multiplier. The final Euler equation 
$$
\dot{\bu} + \nabla_{\bu} \bu = - \nabla p
$$
is our result from [[#Background]]. 

## Conservation of Angular Momentum
Recall from [[Rigid Body Dynamics#Theorem (Angular Momentum is Conserved in World Coordinate)]] that angular moment is conserved. In particular, 
$$
\bl := \bR\bI_{\text{body}} \Omega
$$
This theorem (or really, law) says that 
$$
\dot \bl = 0
$$
And so the total angular momentum relative to the fixed world space never changes. 


## Theorem (Kelvin's Circulation Theorem)
For incompressible fluids, we can define the **circulation** of the fluid. Imagine drawing a closed loop $\Gamma \in M$ in the fluid and connecting a specific set of fluid particles $\phi(\Gamma)$. As the fluid flows, those specific particles move and deform into a new loop, denoted by the flow map $\phi_t(\Gamma)$ where $t$ is time. The circulation is the line integral of velocity field $\bu$ around that moving loop. 

Kelvin's Circulation theorem states that if you follow a closed loop of fluid particles as they flow, the circulation around that specific loop will remain perfectly constant over time.
$$
\frac{d}{dt} \oint_{\phi_t(\Gamma)} \bu \cdot dl = 0
$$
But we can also further abstract this. Indeed, we can convert the velocity vector field into a covector field via $\bu \cdot dl = \bu^\flat$. Then, we can take [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] on the domain and get
$$
\frac{d}{dt} \oint_{\phi_t(\Gamma)} \bu \cdot dl 
= 
\frac{d}{dt} \oint_{\phi_t(\Gamma)} \bu^\flat 
=
\frac{d}{dt} \oint_{\Gamma} \left( \phi_t^* \bu^\flat \right) 
= 
\oint_{\Gamma} \frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
= 0
$$
for all closed curves $\Gamma$.

**Proof**:

We compute the integrand. 
$$
\begin{aligned}
  \frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
  &= \frac{d}{dt} \left[ (d\phi)^\top \bu  \right] \\ 
  &= \underbrace{(d\dot{\phi})}_{d(u \circ \phi)} \,\bu + (d\phi)^\top \dot\bu \\
  &= \left[ (\nabla \bu) d\phi \right]^\top \bu - (d \phi)^\top \left( \nabla_\bu \bu + \nabla p \right) \\
  &= (d\phi)^\top \left[ (\nabla \bu)^\top \bu - \nabla_\bu \bu + \nabla p  \right] \\
\end{aligned}
$$
via 
1. product rule
2. substitution with the flow map and the [[#Background|Euler Equation]].
3. factorization and simplification 

Then, let 
$$
-\nabla \tilde{p} = (\nabla \bu)^\top \bu - \nabla_\bu \bu - \nabla p
$$
be a new spatial gradient to absorb those inner terms. Thus, 
$$
\frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
= 
(d\phi)^\top [ -\nabla \tilde{p} ]
=
-\phi_t^* (d\tilde{p})
$$
Therefore 
$$
\begin{aligned}
\frac{d}{dt} \oint_{\phi_t(\Gamma)} \bu \cdot dl 
&= \oint_{\Gamma} \frac{d}{dt} \left( \phi_t^* \bu^\flat \right)  \\
&= \oint_{\Gamma} -\phi_t^* (d\tilde{p}) \\
&= \oint_{\phi_t (\Gamma)} d\tilde{p}  \\
&= 0
\end{aligned}
$$
where the last line is via [[Stokes Theorem]], since the curl of vector field is $0$. 