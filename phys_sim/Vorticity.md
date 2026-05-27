---
tags:
  - CSE_291G
---

# Definition (Vorticity Field)
A **vorticity field** is a continous distribution of of vorticity throughout the entire fluid domain. Because velocity varies from point to point in a fluid, the curl varies from point to point. Indeed, it defined as
$$
\bw := \nabla \times \bu = \text{curl } \bu
$$
In 2D, this is a scalar field, while in 3D, this is a vector field. 

Imagine we placed a small paddle wheel in the fluid. If the wheel spins, then there is vorticity at that point. In 3D, the vorticity field must be divergence-free. By [[Stokes Theorem]], the [[Kelvin's Circulation Theorem#Definition (Circulation)|circulation]] along some boundary $C$ is the integral of the vorticity over $\Sigma$. 
$$
\Gamma_{C} = \oint_{C} \bu \cdot d\ell = \iint_{\Sigma} \bw \cdot \bn \,dA
$$
By [[Kelvin's Circulation Theorem]], the [[Flux|flux]] of vorticity across a surface flowing with fluid is constant in time. 


# Definition (Vortex Line)
A **vortex line** is a curve tangential to the [[#Definition (Vorticity Field)|vorticity field]]. 
- We will see that a vorticity field can be viewed as infinitely many threads of infinitesimal vortex lines (these are the "atoms"). 
- The integral of vorticity through a surface is how many vortex lines pass through the surface. 
- Vorticity magnitude is the cross-sectional density of vortex lines. The more vortex lines per unit area, the stronger the vorticity.
- Vortex lines are passively advected by the flow. This means wrt a fluid particle, the vortex lines move with the particle.

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\begin{tikzpicture}

% --- Color Theme (Tweak RGB values here) ---
% Surface Gradient
\definecolor{surfTop}{RGB}{124, 125, 220}
\definecolor{surfBot}{RGB}{160, 90, 40}

% Vector Field Lines (Vibrant Blue for high visibility in dark/light modes)
\definecolor{vecColor}{RGB}{50, 120, 220}

% --- Surface (\Sigma) and Boundary (C) ---
% Drawn first as the background layer. 
% The decoration places the directional arrow exactly on the path.
\draw[thick, top color=surfTop, bottom color=surfBot,
      decoration={markings, mark=at position 0.68 with {\arrow[scale=1.5]{>}}},
      postaction={decorate}]
  plot [smooth cycle, tension=0.7] coordinates {
    (-4, 0)
    (-2, 1)
    (1, 0.5)
    (4, -0.5)
    (4.5, -2)
    (2, -3)
    (0, -2)
    (-2, -1.5)
  };

% --- Surface Label ---
\node[font=\Large] at (-2, -0.2) {$\Sigma$};

% --- Boundary Label ---
% Placed near the arrow mark
\node[font=\Large] at (0.5, -3) {$C$};

% --- Vector Field Lines (w) ---
% Drawn mid-ground, originating from inside the surface
\draw[->, >=stealth, very thick, color=vecColor] (-2.5, -0.2) to[out=80, in=210] (-1, 2.5);
\draw[->, >=stealth, very thick, color=vecColor] (-1, -0.5) to[out=80, in=210] (0.5, 2.8);
\draw[->, >=stealth, very thick, color=vecColor] (1, -1) to[out=75, in=210] (3, 2.2);
\draw[->, >=stealth, very thick, color=vecColor] (2.5, -1.8) to[out=75, in=210] (4.2, 0.8);

% --- Vector Label ---
\node[text=vecColor, font=\Large] at (1, 3.2) {$\mathbf{w}$};

\end{tikzpicture}
\end{document}
```

We can think of vortex lines as picking some arbitrary point in the fluid, and tracing out the curve that is always tangential to the vorticity field, by following the direction of the vorticity vector at each point. Tracing these points for infinitely many points gives us our curve.

# Preservation of Vortex Lines / Helmholtz's Theorem
If a curve or surface is tangential to the [[#Definition (Vorticity Field)|vorticity field]], and flows with the fluid, then the curve or surface remains tangential to the vorticity field over time.

**Intuition & Proof:**
* **The Surface Case:** Being tangential to the vorticity field means no [[#Definition (Vortex Line)|vortex lines]] cross or pierce the surface. Mathematically, this means the vorticity flux across the surface is exactly zero.
* **The Conservation:** By [[Kelvin's Circulation Theorem]], the vorticity flux across any material surface is constant over time. Since the flux starts at zero, it must remain zero forever. Therefore, the surface never crosses a vortex line and remains permanently tangential.
* **The Curve Case:** A single 1D vortex line (curve) can be defined locally as the geometric intersection of two 2D tangential surfaces. Because both surfaces perfectly follow the fluid motion without crossing vortex lines, their intersection is permanently glued to the fluid particles.

# Definition (Vortex Tube)
A **vortex tube** is taking a surface $S$ nowhere tangent to the vorticity field, and collecting all vortex lines extending from $S$. 

> [!idea] 
> If a single [[#Definition (Vortex Line)|vortex line]] is a thread, then a vortex tube is a bundle of threads (or a solid cable). We are essentially tracing infinitely many tubes.
>
> Also they really do look like tubes.

## Theorem (Circulation is Constant)
If $C_1, C_2$ are two closed curves encircling the tube, then $\Gamma_{C_1} = \Gamma_{C_2}$. In other words, the circulation around any closed curve encircling the tube is the same.

![[vortextube.jpg]]

Proof: Apply [[Divergence Theorem]] on vorticity field in $V$, the region enclosed. Note that vorticity has no divergence, so $\nabla \cdot \bw = 0$.
$$
\begin{aligned}
\iiint_V \nabla \cdot \bw \,dV &= \iint_{\partial V} \bw \cdot \bn \,dA \\
0 &= \iint_{S_1} \bw \cdot \bn \,dA - \iint_{S_2} \bw \cdot \bn \,dA + \iint_{S_3} \bw \cdot \bn \,dA \\
0 &= \iint_{S_1} \bw \cdot \bn \,dA - \iint_{S_2} \bw \cdot \bn \,dA + 0 \\
0 &= 0
\end{aligned}
$$
In $S_3$, the walls of the tube are tangential to the vorticity field, so no vortex lines cross $S_3$. Therefore, the flux of vorticity across $S_3$ is zero. The flux across $S_1$ and $S_2$ must be conserved, so they are equal. 

## Definition (Strength of a Vortex Tube)
Call this circulation the **strength** of the vortex tube. 

## Theorem (Vortex Strength is Constant)
As the [[#Definition (Vortex Tube)|vortex tube]] is flowing with the fluid, the vortex strength is constant over time. 

# Vortex Branches
In case the tube branches, the **strength** of from each branch adds up since vorticity cannot be created or destroyed out of nowhere (divergence-free). The circulation of the main trunk will always equal to the sum of the circulations of its branches. 

```tikz
\usepackage{tikz}
\usetikzlibrary{decorations.markings}

\begin{document}
\begin{tikzpicture}

% --- Color Theme ---
% Left Face (Surface S)
\definecolor{faceFill}{RGB}{60, 70, 85}
\definecolor{faceBorder}{RGB}{230, 230, 230}

% Vortex Lines & Point P
\definecolor{vortexLine}{RGB}{255, 140, 0}

% Loops (C1, C2)
\definecolor{loopColor}{RGB}{50, 180, 255}

% --- Left Cap (Surface S) ---
\fill[faceFill] (-4.5, 0) ellipse (0.4 and 1.5);
\draw[faceBorder, thick, dashed] (-4.5, 1.5) arc (90:-90:0.4 and 1.5);
\draw[faceBorder, thick, postaction={decorate, decoration={markings, mark=at position 0.5 with {\arrow[scale=1.5]{stealth}}}}] 
    (-4.5, 1.5) arc (90:270:0.4 and 1.5);

% --- Main Tube Outlines ---
% Top boundary
\draw[thick] plot [smooth, tension=0.7] coordinates {(-4.5, 1.5) (-1, 1.7) (4.5, 2.8)};
% Bottom boundary
\draw[thick] plot [smooth, tension=0.7] coordinates {(-4.5, -1.5) (-1, -1.7) (4.5, -2.8)};
% Inner split (Crotch of the bifurcation)
\draw[thick] plot [smooth, tension=0.8] coordinates {(4.5, 1.2) (2.5, 0.5) (0.8, 0) (2.5, -0.5) (4.5, -1.2)};

% --- Right Caps (Open ends of the split tubes) ---
% Top Branch Cap
\begin{scope}[shift={(4.5, 2.0)}, rotate=15]
    \draw[thick] (0,0) ellipse (0.3 and 0.85);
\end{scope}
% Bottom Branch Cap
\begin{scope}[shift={(4.5, -2.0)}, rotate=-15]
    \draw[thick] (0,0) ellipse (0.3 and 0.85);
\end{scope}

% --- Internal Vortex Lines ---
% Main trunk line ending at P (Branch lines removed)
\draw[vortexLine, thick] (-4.5, 0) -- (0.8,0);

% Point P (Zero of w)
\fill[vortexLine] (0.8,0) circle (0.08);

% --- Boundary Loops (C1, C2) ---
% Loop C1 
\draw[loopColor, thick, dashed, postaction={decorate, decoration={markings, mark=at position 0.5 with {\arrow[scale=1.5]{stealth}}}}] 
    (-2, 0.05) ellipse (0.5 and 1.6);

% Loop C2 Top (Re-centered to y=1.45 to fit inside branch boundaries)
\begin{scope}[shift={(2.5, 1.45)}, rotate=15]
    \draw[loopColor, thick, postaction={decorate, decoration={markings, mark=at position 0.5 with {\arrow[scale=1.5]{stealth}}}}] 
        (0,0) ellipse (0.2 and 0.75);
\end{scope}

% Loop C2 Bottom (Re-centered to y=-1.45 to fit inside branch boundaries)
\begin{scope}[shift={(2.5, -1.45)}, rotate=-15]
    \draw[loopColor, thick, postaction={decorate, decoration={markings, mark=at position 0.5 with {\arrow[scale=1.5]{stealth}}}}] 
        (0,0) ellipse (0.2 and 0.75);
\end{scope}

% --- Labels and Pointers ---
\node[font=\Large] at (-5.3, -0.5) {$S$};
\node[font=\Large] at (-5.1, 0.9) {$C$};
\node[font=\Large] at (-1.1, 0.6) {$C_1$};
\node[font=\Large] (c2label) at (1.5, 0) {$C_2$};

% Pointers for C2 adjusted to new loop centers
\draw[thin] (c2label.east) -- (2.3, 1.25);
\draw[thin] (c2label.east) -- (2.3, -1.25);

% Point P
\node[font=\Large] at (0.7, -0.3) {$P$};

% "a zero of w"
\node[font=\large] (zeroLabel) at (0.4, 2.6) {a zero of $\mathbf{w}$};
\draw[thin] (zeroLabel.south) -- (0.8, 0.15);

% "this vortex line ends at P"
\node[font=\large] (vLineLabel) at (-2, -2.5) {this vortex line ends at $P$};
\draw[thin] (vLineLabel.north) -- (-2, -0.1);

\end{tikzpicture}
\end{document}
```

Smoke rings (closed-loop vortex tubes) are a common example of vortex tubes. They are stable because an isolated vortex tube cannot just end; it must either 
- form a closed loop
- extend to the boundaries of the fluid domain
- branch infinitely



# Definition (Vortex Filaments/Sheets)
**Vortex filaments** are concentrated vortex tubes. It is the limit of a vortex tube as its cross-sectional area shrinks to zero with finite strength. We can think of it as squeezing vortex tubes until they become infinitely thin (1D curves) while keeping the [[#Definition (Strength of a Vortex Tube)|strength]] constant.

**Vortex Sheets** are vortex tubes that are squished completely flat into a 2D surface. It represents a severe, discontinuous jump in the fluid's velocity field. For example, if we have wind blowing the opposite direction over another gust of wind, the boundary between the two layers of air is a vortex sheet. 

# Vorticity Equation 
In 3D, the vorticity field is transported by the flow
$$
\bw_t = \bF_t \bw_0 
\quad\text{where } \bF_t = d\phi_t 
$$
One can show that 
$$
\underbrace{\frac{\del}{\del t} \bw + \nabla_\bu \bw}_{\text{advection}} 
= 
\underbrace{\nabla_\bw \cdot \bu}_{\substack{\text{vortex} \\ \text{stretching}}}
$$
The physical interpretation of the left side is that vorticity is being advected by the flow (carried by the flow)[^1]. The right side is the vortex stretching term, which is unique to 3D. It represents how the vorticity can be amplified by the flow. 

[^1]: Think of a literal water vortex in a fast moving river being carried downstream.

For example, imagine we have a thick vortex tube spinning in the fluid
> Going back to the literal water vortex analogy, we have a many vortex lines bundled together in a tube.

What happens when the velocity field of the fluid pulls the top and bottom of that tube, stretching it out?
> The literal vortex will grow because the movement of water is increasing the literal vortex size.

Because the fluid is incompressible, the cross-sectional area of the tube must shrink to keep the same strength, by [[#Theorem (Vortex Strength is Constant)]]. By conservation of angular momentum, the tube must spin faster to compensate for the smaller cross-sectional area. 
> Like an ice skater pulling in their arms to spin faster, the vortex tube must spin faster to maintain the same strength.

This deformation of the tube is expressed mathematically with $\bF_t$ (note the time $t$). It shows how a tiny, perfect cube of fluid gets squished, stretched, and tilted as it flows through space over time.

## 2D Case
In 2D, the vorticity field is a scalar function transported by the flow:
$$
\frac{\del}{\del t} w + \nabla_\bu w = 0
$$

# Reconstructing Velocity from Vorticity
If we decide to simulate a fluid by tracking its vorticity instead of its velocity, we encounter an obvious problem: we still need the velocity to actually move the fluid particles.

## Biot-Savart Law
In electromagnetism, the Biot-Savart law states that a wire carrying an electric current produces a magnetic field. In fluid dynamics, the Biot-Savart law states that a vortex tube produces a velocity field.

## Biot-Savart Integral
Let $\bw$ be the [[#Definition (Vorticity Field)|vorticity field]] in the fluid. If the fluid domain is the entire $\R^3$, then there is a unique divergence-free velocity field $\bu$ which decays to zero at infinity.
$$
\bu(\bx) = 
\frac{1}{4\pi} \int_{\text{supp}(\bw)} \frac{\bw(\by) \times (\bx - \by)}{|\bx - \by|^3} \,dV(\by)
$$
where 
- $\bu(\bx)$ is the velocity at point $\bx$ in the fluid
- $\bw(\by)$ is the vorticity at point $\by$ in the fluid
- The cross product $\times$ guarantees that the velocity field is always perpendicular to the vorticity field.
- The denominator $|\bx - \by|^3$ ensures that the influence of vorticity at $\by$ on the velocity at $\bx$ decays with distance, following the [[Inverse Square Law]] in 3D.
- The $\text{supp}(\bw)$ is the [[Support]] of the vorticity function $\bw$, the set of points in the domain where the function's value is not zero. It is the points in our domain where the fluid is actually swirling.

For 2D, the Biot-Savart law is
$$
\bu(\bx) = 
\frac{1}{2\pi} \int_{\text{supp}(w)} \frac{w(\by) R^{90^\circ} \times (\bx - \by)}{|\bx - \by|^2} \,dA_\by
$$
where $R^{90^\circ}$ is the 90 degree rotation matrix and $\text{supp}(\bw)$. 

When vorticity is concentrated into codimension-2[^2] geometry (vortex filament in 3D or point vortex in 2D), the Biot-Savart law simplifies significantly.

[^2]: In a 3D fluid simulation, codimension-2 means the vortex filament is a 1D curve ($3 - 1 = 2$). In a 2D fluid simulation, codimension-2 means the point vortex is a 0D point ($2 - 0 = 2$).

First, since the [[#Definition (Vortex Filaments/Sheets)|filament]] must be closed, with a fixed strength 
$$
\kappa = \oint_{\substack{\text{any loop} \\ \text{around } \Gamma}} \bu^{\flat}
$$
such that
$$
\bu(\bx) = 
\frac{\kappa}{4\pi} \int_{\Gamma} \frac{T(\by) \times (\bx - \by)}{|\bx - \by|^3} \, ds_\by
$$
where 
- $\Gamma$ is the curve representing the vortex filament, 
- $T(\by)$ is the unit tangent vector. Because the filament is infinitely thin, the complex 3D vorticity vector $\bw$ is perfectly replaced by just the direction the curve is pointing $\bT$ multiplied by the strength $\kappa$,
- $ds_\by$ is the line element along the curve $\Gamma$, which accounts for the length of the curve segment at $\by$.

> [!idea] 
> We now no longer need to simulate the fluid as a 3D field. Instead, we can just track the 1D curve of the vortex filament and its strength. This is a huge simplification that allows us to simulate fluids with less computational resources.

In 2D,
$$
\bu(\bx) = 
\sum_{i} \frac{\kappa_i}{2\pi} \frac{R^{90^\circ} (\bx - \by_i)}{|\bx - \by_i|^2}
$$
Because a 0D point has no length, we only need to sum over the discrete set of point vortices. 

### Biot-Savart Integral: Obstacle Treatment
The fatal flaw of the Biot-Savart integral is that it only works for infinite domains. It assumes the domain is infinitely large and completely empty. An obstacle (like a rock in a river) will calculate the velocity field that flows through the rock, which is (obviously) physically impossible.

Therefore we must modify the Biot-Savart field with a gradient field (i.e. a [[Grid-Based Fluid Methods#Pressure Projection|pressure projection]]). 
- Solve the Laplace problen in the outer domain with Neumann boundary condition
- Classically done with **boundary element method**
- Or by **Kelvin Transformation**. 

## Stream Function 
Instead of an $O(n^2)$ Biot-Savart integral, we can solve the PDE to find the velocity. Consider the followingn ansatz:
$$
\begin{aligned}
\bu &= \nabla \times \Psi && \text{in 3D} \\
\bu &= -R^{90^\circ} \nabla \psi && \text{in 2D}
\end{aligned}
$$
where $\Psi$ is the vector potential in 3D and $\psi$ is the scalar stream function in 2D. The first equation ensures the incompressibility condition $\nabla \cdot \bu = 0$ is automatically satisfied. We can plug this ansatz into the definition of vorticity $\bw = \nabla \times \bu$ to get
$$
\nabla \times (\nabla \times \Psi) = \bw
$$
and get (not sure how to derive this) 
$$
-\Delta \Psi = \bw
$$
In 2D, this is just $- \Delta \psi = w$ with $\psi = 0$ on the boundary. 

> Beware the result could be incorrect if there are multiple boundary components, or that the domain is non-simply-connected.
>
> [Paper](https://yhesper.github.io/fc23/Fluid_Cohomology_Final.pdf)

## Helmholtz-Hodge-Morrey-Friedrichs
In general, we have the following orthogonal decomposition 
$$
\begin{aligned}
\tilde{\bu} &= \nabla p + \nabla \times \Psi + \bh  && \text{in 3D} \\
\tilde{\bu} &= \nabla p -R^{90^\circ} \nabla \psi + \bh  && \text{in 2D} \\
\end{aligned}
$$
with $\Psi$ normal to the boundary and $\psi$ zero on the boundary. 
$$
\begin{cases}
\nabla \cdot \bh = 0 \\
\nabla \times \bh = 0 \\
\bh \cdot \bn = 0 & \text{on the boundary}
\end{cases}
$$

# Vortex Methods
We want to discretize the fluid by tracking its vorticity instead of its velocity. This is called the **vortex particle method**. In 3D, vorticity is done by measuring its vortex [[#Definition (Vortex Filaments/Sheets)|filaments]]
$$
\underbrace{\phi_t^*}_{\text{vec}} \bw_t = \bw_0
$$
and in 2D its point vortices
$$
w_t \circ \phi_t = w_0
$$
The vortex particle method makes little sense in 3D, because the vorticity must be divergence free, all [[#Definition (Vortex Line)|vortex lines]] must form a closed loop or extend infinitely to the boundaries of our fluid domain. Otherwise, we have fluid flowing from one place to another and stopping (creating a sink)[^3].  

[^3]: Apparently this is like the magnetic monopole problem in electromagnetism.

## 2D Vortex Particle Algorithm
We can turn the problem into a discrete $N-$body physics problem. Instead of a fluid, imagine we have a handful of active particles.

Each particle has a fixed vorticity strength $\kappa_p$ which can be positive or negative. The 2D position of each particle $\phi_p$ is described by  
$$
\frac{d}{dt} \phi_p 
= \sum_{
  \substack{q \in \texttt{VortexParticles} \\ q \neq p}
} 
\frac{\kappa_q}{2\pi} \frac{R^{90^\circ} (\phi_p - \phi_q)}{|\phi_p - \phi_q|^2}
$$

Then, we evaluate velocity for any **passively advected** smoke/dye by 
$$
\bv_\bx = \sum_{
  \substack{q \in \texttt{VortexParticles}}
}
\frac{\kappa_q}{2\pi} \frac{R^{90^\circ} (\bx - \phi_q)}{|\bx - \phi_q|^2}
$$
then solve the ODE by [[Numerical Methods#Runge-Kutta Method (RK4)|RK4]]. 

## 3D Vortex Filament Algorithm
This is extremely hard. Filaments stretch, twist, grow exponentially, need reconnection... 

Recall the continuous PDE for 3D vorticity:
$$
\frac{\del}{\del t} \bw + \nabla_\bu \bw = \nabla_\bw \bu
$$
Most papers solve this by splittng advection and stretching into two separate steps. This is unstable since the stretching step is calculated as an explicit addition, causing errors to accumulate. A better approach is to "do a semi-Lagrangian pullback for 2-form".

The original velocity-based semi-Lagrangian [[Grid-Based Fluid Methods|approaches]] $\dot\bu + \nabla_{\bu} \bu = 0$ typically did
$$
\bu_{t + \Delta t}(bx) = \bu_{t}(\psi_{\Delta t} (\bx))
$$
where $\psi_{\Delta x}(\bx) = \bx - \Delta t  \bu_{t}(\bx)$ is the traceback to find the old velocity at the past location $\bu_t$. This ignores deformation. 

Instead, we need to change what velocity physically represents. Instead of it being a vector ($0-$form), it needs to be a [[Dual Space#Definition (Covector)|covector]] ($1-$form), a measurement of flow along a line segment. That way, if the fluid deforms at some segment, the velocity measurement scale to conserve energy.
$$
\dot\bu + \nabla_{\bu} \bu = -(\nabla \bu)^\top \bu
$$
Then, we can do a semi-Lagrangian pullback for 1-form:
$$
\bu_{t + \Delta t}(bx) =  (d\psi_{\Delta t})^\top (\psi_{\Delta t} (\bx))
$$
Then velocity is transported as a covector. In particular, the [[Kelvin's Circulation Theorem]] holds. 

# Additional Conservation Laws
There are more invariants of the flow besides circulation.

## Theorem (Generalized Kelvin's Circulation Theorem)
We can generalize [[#Theorem (Kelvin's Circulation Theorem)]]. If $\bu$ is a velocity field and $\bv$ is any divergence-free vector field transported by the fluid, then 
$$
\int \langle\bu, \bv \rangle \,dV
$$
is constant. 

### Definition (Helicity)
$$
\mathcal{H} := \int \langle\bu, \bv \rangle \,dV
$$

### Theorem (Helicity is Constant)
Helicity is a constant of time.


## Theorem (Vortex Line Area Conservation)
In fluids, the total area of vortex lines is conserved. Vortex lines are twisted and bent curves. In $\R^3$, if we project them onto the $xz, yz, xy$ planes, we describe the **area vector**, $A = [A_{xz}, A_{yz}, A_{xy}]^\top$. The total area vector of all vortex lines is conserved. 

### Airplane Example
This theorem explains why airplanes can fly.