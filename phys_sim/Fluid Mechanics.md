---
tags:
  - CSE_291G
---
# Recall
Recall from [[Continuum Mechanics#Postulate 1]] that we have 
- $M$: a material space, equipped with the $\rho_{M}$ mass measure 
- $W$: a world space, equipped with the [[Metric Space#Definition (Metric)|metric]] $\langle \cdot, \cdot \rangle_{W}$ 
- $\phi(t) : M \to W$, the "flow map" to show how the particles are embedded in the world space $W$.
- $\bu \in \Gamma(TW)$ defined by $\dot{\phi} = \bu \circ \phi$, the [[Continuum Mechanics#Definition (Velocity Field)|velocity field]]

We also have the [[Continuum Mechanics#Continuity Equations|Continuity Equation]] for **mass conservation**. If $q_{W}$ denotes the mass density, then 
$$
\dot{q}_{W} + \bu \cdot \nabla q_{W} + (\nabla \cdot \bu)q_{W} = 0
$$
or 
$$
\dot{q}_W + \nabla \cdot (q_W \bu) = 0
$$

# Derivation of Fluid Momentum Equation
We will derive the fluid momentum equation by examining the forces on the system. Recall that
$$
\frac{D}{Dt} \bu = \frac{\partial \bu}{\partial t} + \bu \cdot \nabla \bu
$$
is the world-space acceleration of a flowing particle. The $D/Dt$ operator is the [[Continuum Mechanics#Definition (Material Derivative)|material derivative]] of the velocity field $\bu$ (so obviously, this gives us the acceleration of a particle). By Newton's second law, we have
$$
q_W \frac{D}{Dt} \bu =: \text{(force density)}
$$
Force density is the amount of force per unit volume. 
```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3, line join=round, line cap=round]

% --- Solid Cube Faces (Drawn first so they sit in the background) ---
% Front face
\draw[thick, fill=white] (-1, -1) rectangle (1, 1);
% Top face
\draw[thick, fill=white] (-1, 1) -- (-0.3, 1.6) -- (1.7, 1.6) -- (1, 1) -- cycle;
% Right face
\draw[thick, fill=white] (1, -1) -- (1.7, -0.4) -- (1.7, 1.6) -- (1, 1) -- cycle;

% --- Hidden Edges (Drawn on top of the white fill so they are visible) ---
\draw[dashed, thick] (-1, -1) -- (-0.3, -0.4);
\draw[dashed, thick] (-0.3, -0.4) -- (1.7, -0.4);
\draw[dashed, thick] (-0.3, -0.4) -- (-0.3, 1.6);

% --- Dimension Labels ---
% Delta x (width)
\node[below, yshift=-2pt] at (-0.8, -1) {\Large $\Delta x$};
% Delta z (height)
\node[left, xshift=-2pt] at (-1, -0.5) {\Large $\Delta z$};
% Delta y (depth)
\node[below right, xshift=-4pt, yshift=4pt] at (1.35, -0.7) {\Large $\Delta y$};

% --- Pressure Arrows ---
% Top Arrow (pointing down to the top face)
\draw[very thick, fill=white] 
    (0.1, 2.4) -- (0.6, 2.4) -- (0.6, 1.8) -- (0.85, 1.8) -- 
    (0.35, 1.3) -- (-0.15, 1.8) -- (0.1, 1.8) -- cycle;

% Bottom Arrow (pointing up to the bottom edge)
\draw[very thick, fill=white] 
    (-0.25, -2.1) -- (0.25, -2.1) -- (0.25, -1.5) -- (0.5, -1.5) -- 
    (0.0, -1.0) -- (-0.5, -1.5) -- (-0.25, -1.5) -- cycle;

% Left Arrow (pointing right to the left edge)
\draw[very thick, fill=white] 
    (-2.1, 0.55) -- (-1.5, 0.55) -- (-1.5, 0.8) -- (-1.0, 0.3) -- 
    (-1.5, -0.2) -- (-1.5, 0.05) -- (-2.1, 0.05) -- cycle;

% Right Arrow (pointing left to the right face)
\draw[very thick, fill=white] 
    (2.4, 0.55) -- (1.8, 0.55) -- (1.8, 0.8) -- (1.35, 0.3) -- 
    (1.8, -0.2) -- (1.8, 0.05) -- (2.4, 0.05) -- cycle;

\end{tikzpicture}
\end{document}
```
The force is given by the pressure on the parcel of volume. Suppose $p : W \to \R$ is the scalar pressure field and the center of the cube is at $(x, y, z)$ with the above dimensions. Using Taylor expansion, the pressure at the right wall is $p(x, y, z) + \frac{\partial p}{\partial x} \frac{\Delta x}{2}$. Since forice is pressure times area, the force at the right wall pointing in the $\vec{e}_{x}$ direction is
$$
-\left[ \left( p(x, y, z) + \frac{\del p}{\del x} \frac{\Delta x}{2} \right) \Delta y \Delta z \right]
\cdot \vec{e}_x
$$
Similarly, at the hidden left wall, the force is
$$
+ \left[ \left( p(x, y, z) - \frac{\del P}{\del x} \frac{\Delta x}{2} \right) \Delta y \Delta z \right] \cdot \vec{e}_x
$$
The net force from all six sides is 
$$
\bF_{\text{net}} = 
-\; \underbrace{
  \left(
    \frac{\del p}{\del x} \vec{e}_x + \frac{\del p}{\del y} \vec{e}_y + \frac{\del p}{\del z} \vec{e}_z
  \right)
}_{\nabla p}
\cdot \Delta x \Delta y \Delta z
$$
And so the force density is $-\nabla p$. Therefore, the equations of motion for a (compressible) fluid are
$$
\left\{
\begin{aligned}
\dot{q}_W + \nabla \cdot (q_W \bu) &= 0 \\
q_W \left( \frac{D \bu}{Dt} \right) &= -\nabla p \\
\quad\boxed{\text{still need equation for $p$}}
\end{aligned}
\right.
\iff
\left\{
\begin{aligned}
\dot{q}_W + \nabla \cdot (q_W \bu) &= 0 \\
\frac{\del}{\del t} (q_W \bu) + \text{div}(q_W \bu \otimes \bu + p \bI_{3 \times 3}) &= 0 \\
&\vdots
\end{aligned}
\right.
$$
Here, $\text{div}(p \bI_{3 \times 3}) = \nabla p$. We can show equivalence of the second equation as follows. 
$$
\begin{aligned}
\frac{\partial}{\partial t}(q_w \mathbf{u}) + \text{div}(q_w \mathbf{u} \otimes \mathbf{u}) + \text{div}(p \bI_{3 \times 3})
&= \left(
  \mathbf{u} \frac{\partial q_w}{\partial t} + q_w \frac{\partial \mathbf{u}}{\partial t}
\right) \\
% 
  &\quad\quad\quad + \bigg( 
    \mathbf{u} (\nabla \cdot (q_w \mathbf{u})) + q_w (\mathbf{u} \cdot \nabla)\mathbf{u}
  \bigg) \\
  &\quad\quad\quad + \text{div}(p \bI_{3 \times 3}) \\
% 
0 &=
\mathbf{u} \underbrace{\left[ \frac{\partial q_w}{\partial t} + \nabla \cdot (q_w \mathbf{u}) \right]}_{\text{Mass Continuity}} + q_w \underbrace{\left[ \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} \right]}_{\text{Material Derivative}} + \underbrace{\text{div}(pI)}_{\nabla p} \\
0 &= q_w \frac{D \mathbf{u}}{Dt} + \nabla p \\
q_w \frac{D \mathbf{u}}{Dt} &= -\nabla p
\end{aligned}
$$
These equations are not complete. Our equations govern mass continuity and momentum conservation but we still have some unknowns. Indeed, we have three unknowns: $q_W$, $\bu$, and $p$. We need an additional constraint on the fluids. One can take some assumptions about the pressure of the fluid. For example,
> "$p$ is only a function of the spatial mass density $q_W$" (barotropic fluid)

to complete the equation. Or 
> "$p$ is a function of $q_W$ and a hidden variable $s$ with $\frac{D s}{D t} = 0$"  

Then $s$ is called the "entropy" of the fluid, and the fluid is called "isentropic".

## Barotropic Fluids
A **barotropic fluid** is a fluid whose density is a function of pressure only. Suppose $p := p(q)$ is very "stiff", i.e. the fluid is hard to compress. 
```tikz
\usepackage{amsmath}
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.5, line width=1pt]

% --- Axes ---
\draw[->] (-0.5, 0) -- (3.0, 0) node[right, font=\Large] {$q$};
\draw[->] (0, -0.5) -- (0, 3.0) node[left, font=\Large] {$p$};

% --- Steep Curve ---
\draw (0.9, 0.4) .. controls (1.1, 1.2) and (1.3, 2.2) .. (1.4, 3.2);

% --- Point on curve ---
\fill (1.17, 1.6) circle (2pt);

% --- Tick mark on q-axis ---
\draw (1.17, 0.1) -- (1.17, -0.1) node[below, font=\Large] {$q_0$};

% --- Label and arrow for "large slope" ---
\node[right, font=\large] at (1.8, 2.3) {large slope};
\draw[->, thick] (1.8, 2.4) to[out=150, in=-30] (1.33, 2.6);

\end{tikzpicture}
\end{document}
```
then the fluid would want to stay at the same density $q_0$ and the fluid is effectively incompressible. The slope $dp/dq$ means that we can try to exert extreme pressure to change the density, but the fluid will resist it.

In fluid mechanics, the slope $dp/dq$ is the square of the **speed of sound** in that fluid's material. The speed of sound is really how fast vibrations travel.

# Linearized Fluid Equation
Let $q = q_0$ (some base density) and $\bu = 0$ (the fluid is not moving) be static solutions. Let 
$$
q = q_0 + \vepsi \tilde{q}  
\quad\text{and}\quad
\bu = 0 + \vepsi \tilde{\bu} 
\;\text{with $\vepsi <\!\!< 1$} 
$$
to $O(\vepsi^2)$. Visually, this means we applied some perturbation to the system at the initial state $(q_0, 0)$ and we want to see how the system evolves. We ignore $O(\vepsi^2)$ terms because we are only interested in the first-order behavior of the system. 

Our mass continuity equation is
$$
\begin{aligned}
\frac{\del q}{\del t} + \nabla \cdot (q \bu) = 0
\longrightarrow\quad
\frac{\del}{\del t} (q_0 + \vepsi \tilde{q}) + \nabla \cdot \left( (q_0 + \vepsi \tilde{q})(\vepsi \tilde{\bu}) \right) &= 0 \\
0 + \vepsi \dot{\tilde{q}} + \nabla \cdot \left(  q_0 \vepsi \tilde{\bu} + \vepsi^2 \tilde{q} \tilde{\bu} \right) &= 0 \\
\vepsi \dot{\tilde{q}} + \nabla \cdot (q_0 \vepsi \tilde{\bu}) &= 0
\end{aligned}
$$
The momenentum equation is 
$$
q \frac{D \bu}{Dt} = -\nabla p
\longrightarrow
% 
(q_0 + \vepsi \tilde{q}) \left( \frac{\partial}{\partial t} (\vepsi \tilde{\bu}) + (\vepsi \tilde{\bu} \cdot \nabla)(\vepsi \tilde{\bu}) \right) 
= -\nabla p(q_0 + \vepsi \tilde{q})
$$
The $(\vepsi \tilde{\bu} \cdot \nabla)(\vepsi \tilde{\bu})$ term generates a $\vepsi^2$ term which we can ignore. Likewise, the $\vepsi \tilde{q}$ term in the left side generates a $\vepsi^2$ term. Therefore, we have $q_0 \vepsi \dot{\tilde{\bu}}$. Now, we can perform [[Taylor's Theorem|Taylor expansion]] of the pressure field:
$$
\begin{aligned}
-\nabla p(q_0 + \vepsi \tilde{q})
&\approx -\nabla \left[ p_0 + \left( \frac{dp}{dq}\bigg| _{q_0} \right) \vepsi \tilde{q} \right] \\
&= -\nabla \left[ p_0 + c^2 \vepsi \tilde{q} \right] \\
&= - c^2 \vepsi \nabla \tilde{q}
\end{aligned}
$$
where $c^2$ is the speed of sound. Therefore, the linearized fluid equations are
$$
\left\{
\begin{aligned}
\vepsi \dot{\tilde{q}} + \nabla \cdot \left(  \vepsi q_0 \tilde{\bu} \right) &= 0 \\
q_0 \vepsi \dot{\tilde{\bu}} &= - c^2 \vepsi \nabla \tilde{q}
\end{aligned}
\right.
$$
This implies 
$$
\ddot{\tilde{q}} = c^2 \underbrace{\nabla \cdot \nabla}_{\Delta (\text{Laplacian})} \tilde{q} 
$$
This is the **acoustic wave equation**. The acoustic wave equation describes how sound (or vibrations) propagate through a medium (fluid). The speed of sound $c$ determines how fast these waves travel. 

## Definition (Mach Number)
The **Mach number** is a [[Dimensional Analysis#Dimensionless Equations|dimensionless quantity]] defined as 
$$
\frac{|\bu|}{c}
$$
When the speed of sound $u \ll c$, then we may assume $q = q_0$ for constant $q_0$ and has some perturbation $\vepsi \tilde{\bu}, \vepsi \tilde{q}$ satisfying the linear acoustic wave equation, the fluid has a low Mach number and is called *quasi-static*. In other words, it is incompressible. When the speed of sound $u$ is comparable to $c$, then the fluid is compressible and we need to use the full nonlinear equations.

# Incompressible Fluids
An **incompressible fluid** is a fluid whose density $q$ is constant $q_0$ throughout the flow and the divergence of the velocity field $\bu$ is zero ($\nabla \cdot \bu = 0$). We have two definitions of incompressibility. 

The strong version is that the density $q$ is constant. The equations of motion are
$$
\left\{
\begin{aligned}
q &= q_{0} \\
\nabla \cdot \bu &= 0 \\
\end{aligned}
\right.
$$
The weak version only requires $\nabla \cdot \bu = 0$. This is an iff condition with $\dot{\bq} + \bu \cdot \nabla q = 0$. So $q$ can be nonconstant, just that the more desnse part is advected (move or transport by bulk motion) by the fluid. Indeed, it is also volume preserving over time. For $\Omega \subset M$[^1], 
$$
\dot{\bq} + \bu \cdot \nabla q = 0
\quad\iff\quad
\nabla \cdot \bu = 0 
\quad\iff\quad
\frac{d}{dt} \int_{\phi_{t}(\Omega)} \, dV = 0
$$

[^1]: See [[Continuum Mechanics#Postulate 2]] for an explanation for this notation. 

# Theorem (Hodge Decomposition)
Let $\chi$ be the [[Vector Space|space]] of vector fields $\Gamma(TW)$. 

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2, line join=round, line cap=round]

% --- Define 3D Box Coordinates ---
% Front Face
\coordinate (FBL) at (0,0);
\coordinate (FBR) at (4,0);
\coordinate (FTR) at (4,4);
\coordinate (FTL) at (0,4);

% Back Face (Shifted +1.5x, +1.5y for perspective)
\coordinate (BBL) at (1.5,1.5);
\coordinate (BBR) at (5.5,1.5);
\coordinate (BTR) at (5.5,5.5);
\coordinate (BTL) at (1.5,5.5);

% Middle Plane (Cross-section at height y=2 on the front face)
\coordinate (MFL) at (0,2);
\coordinate (MFR) at (4,2);
\coordinate (MBR) at (5.5,3.5);
\coordinate (MBL) at (1.5,3.5);

% --- Draw Hidden Edges ---
\draw[dashed, thick, gray!80] (FBL) -- (BBL);
\draw[dashed, thick, gray!80] (BBL) -- (BBR);
\draw[dashed, thick, gray!80] (BBL) -- (BTL);

% --- Draw Middle Plane ---
\filldraw[fill=blue!10, draw=blue!60!black, thick, fill opacity=0.6] 
    (MFL) -- (MFR) -- (MBR) -- (MBL) -- cycle;

% --- Draw Vertical Perpendicular Line ---
% Top point on the top plane, bottom point on the middle plane
\coordinate (PT) at (2.75, 4.75); 
\coordinate (PB) at (2.75, 2.75);

\draw[thick] (PT) -- (PB);
\fill (PB) circle (1.5pt); % Contact point

% Right-angle indicator
\draw[thick] (2.75, 2.95) -- (2.95, 2.95) -- (2.95, 2.75);

% --- Draw Visible Outer Edges ---
% Front Face
\draw[thick] (FBL) -- (FBR) -- (FTR) -- (FTL) -- cycle; 
% Top Face
\draw[thick] (FTL) -- (BTL) -- (BTR) -- (FTR);          
% Right Face
\draw[thick] (FBR) -- (BBR) -- (BTR);                   

% --- Equation Text and Arrow ---
\node[align=left, anchor=east] (eq) at (-0.5, 2.5) {
    {\Large Space of $\vec{u}$}
    \\[1.5ex]
    {\Large $\chi_{\mathrm{div}}$} 
};

% Space
\node[align=left, anchor=east] (sp) at (4, 0.5) {
    {\Large $\chi$} 
};

\node[align=left, anchor=east] (xperp) at (7, 5) {
    {\Large $\chi_{\mathrm{div}}^{\perp}$} 
};

% Pointing arrow from text to the midplane
\draw[->, thick, shorten >=2pt] (eq.east) to[out=0, in=150] (0.8, 2.5);

% Pointing arrow from Xdivperp to the vertical line
\draw[->, thick, shorten >=2pt] (xperp.north) to[out=120, in=90] (2.75, 5);

\end{tikzpicture}
\end{document}
```

Define 
$$
\chi_{\text{div}} = \bigg\{ 
    \bu \in \Gamma(TW) 
    \;\bigg|\; 
    \nabla \cdot \bu = 0 \wedge (\bu \cdot \bn)|_{\del W} = 0 
\bigg\}
$$
If $\chi$ is the space of all possible vector fields, then $\chi_{\mathrm{div}}$ is the space of all *physically valid* incompressible velocity fields. In other words
- $\nabla \cdot \bu = 0$. The fluid is divergence-free (perfectly incompressible).
- $(\bu \cdot \bn)|_{\del W} = 0$. The fluid velocity normal $\bn$ to the boundary $\del W$ is zero. It can slide along the walls, but it cannot flow *through* the walls. 

Define the inner product ([[Continuum Mechanics#Definition (Fluid Kinetic Energy)|fluid kinetic energy]]) on $\Gamma(TW)$ by 
$$
\| \bu \|^2 = \iiint_{W} q_0 \| \bu \|^2 \, dV
$$
What does it mean to be completely orthogonal to $\chi_{\mathrm{div}}$? Define
$$
\chi_{\text{div}}^{\perp} = 
\left\{
    \frac{\nabla p}{q} \;\bigg|\; p : W \to \R
\right\}
$$
The theorem states that the orthogonal complement $\chi_{\text{div}}^{\perp}$ is the space of all pressure gradients $\nabla p$. 

**Proof**: We need to show the two vector spaces are orthogonal. This is done by seelcting any arbitrary vector $\bu \in \chi_{\mathrm{div}}$ and an arbitrary vector from the second space $\nabla p / q$ always has in inner product of $0$. 
$$
\begin{aligned}
\int_W q \left( \frac{\nabla p}{q}  \right) \cdot \bu
&= \int_W (\nabla p \cdot \bu) \, dV\\ 
&= \oint_{\del W} p(\bu \cdot \bn) \, dS - \int_W p (\nabla \cdot \bu)\, dV \\
&= 0 - 0 \\ 
&= 0 \\
\iff& \nabla \cdot \bu = 0 \wedge \frac{\del \bu}{\del \bn} = 0
\end{aligned}
$$
The second equality is by [[Divergence Theorem]]. 

---
The corollary is that $p$ is uniquely determined by orthogonal projection. The pressure force becomes the Lagrange multipler for the $\nabla \cdot \bu = 0$ constraint. Because these two spaces are orthogonal, any arbitrary vector field $w$ can be uniquely sliced into two independent pieces
$$
\bw = \bu_{\text{incompressible}} + \nabla p
$$
