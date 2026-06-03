---
tags:
  - CSE_291G
---
# Background
**Continuum mechanics** is the study of the physics of continuous materials. Unlike [[Rigid Body Dynamics|rigid body dynamics]], where bodies are assumed to be undeformable, continuum mechanics models materials that can change shape, such as:
- **Solids:** Rubber, cloth, hair, elastic rods.
- **Fluids:** Air, water, honey.
- **Complex Materials:** Slime, Oobleck, plasma.

The mathematical framework allows us to treat these diverse materials uniformly by considering them as continuous mass distributions rather than discrete particles.

# Definition (Shear)
**Shear** is a mode of deformation where parallel layers of a material slide past one another. It typically occurs when a force is applied parallel to the surface of a material.

# Definition (Fluid)
A **fluid** is a substance that deforms continuously under any applied shear stress. In terms of energy:
- The potential energy of a fluid is independent of the [[#Definition (Shear)|shearing]] mode of deformation.
- It is primarily a function of volume changes (compression/expansion).
- There is no restorative force for volume-preserving (isochoric) deformations.

# Definition (Elastic Bodies)
An **elastic body** returns to its original shape after being deformed. Its potential energy depends on the deformation relative to a reference state, and it exerts a restorative force to minimize this energy.
- **Example:** A rubber band or a piece of cloth.
- **Elastoplasticity:** The study of materials that exhibit elastic behavior until a certain threshold (yield strength), after which they undergo permanent **plastic deformation**.

# Viscoelastic Materials
These materials exhibit both viscous (fluid-like) and elastic (solid-like) properties. Their internal forces depend on both the current deformation and the **rate** of deformation.
- **Example:** Slime or Oobleck (a non-Newtonian fluid).

# Ferrofluids
**Ferrofluids** are liquids containing nanoscale magnetic particles. They become strongly magnetized in the presence of an external magnetic field, allowing their shape and flow to be controlled magnetically.

# Plasma / Magnetohydrodynamics
These are electrically conducting fluids (e.g., ionized gases or liquid metals like mercury). Their behavior is governed by **Magnetohydrodynamics (MHD)**, which couples fluid dynamics with electromagnetic field equations.

--- 
While these materials have vastly different physical properties, they can all be described using a shared mathematical framework of deformable bodies. The differences emerge from specific constitutive laws (e.g., elasticity, viscosity, conductivity).

# Postulate 1 
We model a deformable body using two spaces and a mapping between them:
- [[Manifold]] $M$: The **material space** (or Lagrangian coordinates), representing the "index set" of all material particles. $M$ is time-independent.
- World space $W$: The **spatial space** (or Eulerian coordinates) where the particles reside.
- Flow map $\phi : M \times \R \to W$: Describes the state of the body at time $t$ via $\phi(X, t) = x$.

The visualization is that we have some space $M$ (the reference configuration) mapped by $\phi$ to how the particles are placed in the world space $W \cong \R^3$.

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]
% --- Left Space: Manifold M ---
\begin{scope}[shift={(0,0)}]
    % Organic blob shape for M
    \draw[ultra thick, color=blue!90!black, fill=blue!40] plot [smooth cycle, tension=0.7] coordinates {
        (0.2, 0.5)
        (0.5, 1.8)
        (2.0, 1.4)
        (2.8, 0.2)
        (2.2, -1.0)
        (1.0, -1.2)
        (0.1, -0.3)
    };
    % Label M
    \node[scale=1.5, color=blue!90!black] at (1.0, -0.6) {$M$};
\end{scope}

% --- Mapping Arrow ---
\draw[->, ultra thick] (3.2, 0.6) to[bend left=15] node[above, yshift=4pt, scale=1.4] {$\phi(t)$} (5.2, 0.3);

% --- Right Space: Target Space W ---
\begin{scope}[shift={(6.5, -0.5)}]
    
    % Define coordinates for the 3D Box (Space W)
    \coordinate (F_BL) at (0, -2.5);   % Front Bottom-Left
    \coordinate (F_BR) at (3.5, -2.5); % Front Bottom-Right
    \coordinate (F_TR) at (3.5, 3.5);  % Front Top-Right
    \coordinate (F_TL) at (0, 3.5);    % Front Top-Left

    % Back face coordinates (Shifted up and right for perspective)
    \coordinate (B_TR) at (4.5, 4.3);
    \coordinate (B_BR) at (4.5, -1.7);
    \coordinate (B_TL) at (1.0, 4.3);

    % Draw the Box W (back lines omitted for a solid block look)
    % Top face
    \draw[ultra thick, color=black] (F_TL) -- (B_TL) -- (B_TR) -- (F_TR) -- cycle;
    % Right face
    \draw[ultra thick, color=black] (F_BR) -- (B_BR) -- (B_TR) -- (F_TR) -- cycle;
    % Front face
    \draw[ultra thick, color=black] (F_BL) rectangle (F_TR);

    % Label W
    \node[scale=1.5] at (4.2, 4.7) {$W$};

    % --- Embedded Manifold phi(M) ---
    % Deformed version of M living inside the front face of W
    \draw[ultra thick, color=blue!70!black, fill=blue!40] plot [smooth cycle, tension=0.7] coordinates {
        (0.5, 0.8)
        (0.8, 2.4)
        (2.3, 1.8)
        (2.7, 0.2)
        (2.1, -1.3)
        (1.1, -1.6)
        (0.4, -0.2)
    };
\end{scope}

\end{tikzpicture}
\end{document}
```

Importantly, $M$ is independent of time, as the set of material points does not change. 

> [!idea] Intuition
> We want to observe a flowing material (like water in a river) like the following.
> 1. Lagrangian View ($M$): You are in a boat without an anchor, floating aloing the current. You track the exact same surrounding water particles for the entire journey. 
> 2. Eulerian View ($W$): You are standing on a bridge, staring down at one fixed location in the water. You can watch different water particles flow through in our fixed POV.

> [!faq] What is a Postulate?
> A postulate is a statement assumed to be true without proof, serving as a foundational axiom for a physical theory. 

# Postulate 2
This postulate defines the measure-theoretic and geometric structure of the spaces:

1. **Mass Measure:** $M$ is equipped with a time-independent mass measure $\rho_M$:
  $$
  \rho_M = q_M(X) \, dV_M(X)
  $$
  where $q_M$ is the **material mass density**[^1] and $dV_M$ is the **volume element**. Note that while $\rho_M$ is fixed for a piece of material, its representation in world space (density and volume) changes as it deforms.
  
  [^1]: Material mass density refers to the intrinsic allocation of mass to the material points. It is invariant to deformations and time.  
  
  For any subset $\Omega \subset M$, we can measure its volume as 
  $$
  \text{Volume}(\phi_M(\Omega)) := \int_{\Omega} dV
  $$
  Likewise, its mass is invariant (under the flow map):
  $$
  \text{Mass}(\Omega) = \int_{\Omega} \rho_M = \int_{\Omega} q_M \, dV_M
  $$
2.  **World Metric:** $W$ is equipped with a time-independent inner product $\langle \cdot, \cdot \rangle_W$ (denoted $\flat_W$ in some contexts). This allows us to measure lengths and velocities in the world space.

> [!idea] 
> Axiomatically, $\rho_M$ is given and time-independent. We can define the spatial mass density $q_w(x, t)$ such that mass is conserved. We do not typically give $M$ a [[Metric Space#Definition (Metric)|metric]], as its intrinsic geometry is secondary to its mass distribution.

---
With these two postulates, we can define things using objects introduced here. For example...

# Definition (Flow Velocity)

The **flow velocity** $\dot{\phi}$ is the time derivative of the flow map:
$$
\dot{\phi}(t) = \frac{\partial}{\partial t} \phi(t)
$$
The *type* of $\dot{\phi}$ is $\dot{\phi} : M \to TW$, where $TW$ is the [[Dual Space#Definition (Tangent Bundle)|tangent bundle]] of $W$. Indeed, $\dot{\phi}(p) \in T_{\phi(p)}W$. 

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]

% --- Define Colors ---
\definecolor{mypurple}{RGB}{145, 85, 210}

% ==========================================
% Left Side: Manifold M
% ==========================================

% Blob M
\draw[thick, fill=blue!40] plot [smooth cycle, tension=0.8] coordinates {
    (-0.5, 1.2) (0.5, 1.3) (1.2, 0.6) (1.4, -0.2) (0.8, -1.1) 
    (0.0, -1.3) (-1.0, -0.8) (-1.3, 0.0) (-1.1, 0.8)
};

% Point p
\fill (0, 0.2) circle (2pt) node[below=2pt, font=\Large] {$p$};

% Label M
\node[font=\Large] at (-0.3, -1.8) {$M$};


% ==========================================
% Middle: Mapping Arrow
% ==========================================

% Arrow phi(t)
\draw[->, thick] (1.7, 0.5) to[bend left=12] node[above, font=\Large] {$\phi(t)$} (3.7, 0.5);


% ==========================================
% Right Side: Space W
% ==========================================

% Hexagonal Boundary for Space W
\draw[thick] (4.5, -0.5) -- (4.5, 2.5) -- (6.0, 3.3) -- (7.3, 2.5) -- (7.5, -0.5) -- (6.0, -1.5) -- cycle;

% Internal Coordinate Axes
\coordinate (Origin) at (4.8, -0.7);
\draw[->, thick] (Origin) -- ++(0, 0.7);        % Y-axis
\draw[->, thick] (Origin) -- ++(0.6, -0.1);     % X-axis
\draw[->, thick] (Origin) -- ++(0.4, 0.3);      % Z-axis

% Label W
\node[font=\Large] at (4.5, -1.8) {$W$};

% Embedded Image Blob ( phi(M) )
\draw[thick, fill=blue!40] plot [smooth cycle, tension=0.7] coordinates {
    (5.4, 0.4) (5.8, 0.9) (6.6, 1.0) (7.0, 0.5) (6.6, -0.1) (6.0, -0.3) (5.2, -0.1)
};

% Point phi_t(p)
\coordinate (PhiP) at (6.2, 0.3);
\fill (PhiP) circle (2pt);

% Label and pointer for phi_t(p)
\node[font=\Large] (PhiP_label) at (8.0, -1.6) {$\phi_{(t)}(p)$};
\draw[->, thick] (PhiP_label) to[out=160, in=-70] (PhiP);

% Velocity Vector (Purple)
\coordinate (Vhead) at (6.7, 0.8);
\draw[->, thick, mypurple] (PhiP) -- (Vhead);

% Label and pointer for velocity vector
\node[font=\Large, mypurple] (Vlabel) at (8.5, -0.1) {$\dot{\phi}_{(t)}(p)$};
\draw[mypurple, thick] (Vlabel) to[out=180, in=-30] (6.5, 0.6);

\end{tikzpicture}
\end{document}
```

# Definition (Velocity Field)
If we feed a point $p \in M$ into $\phi(t)$, we get its position $\phi_{(t)}(p) \in W$. By tracking all points $q \in M$, we capture velocity vectors at different locations in $W$. This defines a velocity field in $W$, denoted by $\vec{u} \in \Gamma(TW)$ where $\dot{\phi}(t) = \vec{u}(t) \circ \phi(t)$. Note that $\vec{u}$ is only defined only on the image of $\phi$.

$\vec{u}$ is called the **velocity field** in the Eulerian coordinate.

# Definition (Fluid Kinetic Energy)
The **kinetic energy** of the fluid is given by 
$$
K(\phi, \dot{\phi}) := \frac{1}{2} \int_{M} 
\left\langle \dot{\phi}, \dot{\phi}\right\rangle_{W} \, \rho_M
= 
\frac{1}{2} \int_{M} \| \dot{\phi}\|_{W}^{2} \rho_M
$$
In theory, we cannot define anything else other than kinetic energy (but this is good enough). We can also rewrite the second expression in Eulerian space as
$$
K(\phi, \dot{\phi}) = \frac{1}{2} \int_{\phi(M) \subset W} \| \vec{u} \|^{2} q_W \, dV_W
$$

# Definition (Material Derivative)
Suppose we had a scalar field $f_M(t) : M \to \R$ defined on the material space $M$ (like temperature attached to specific particles). Let $f_W(t) : W \to \R$ be the corresponding spatial field such that $f_M = f_W \circ \phi$. 

If we fix the spatial degrees of freedom in $M$ and calculate the rate of change of $f_M$ (the time derivative), we are effectively tracking how the property changes for a moving particle in $W$. By applying the chain rule,
$$
\begin{aligned}
\frac{\del}{\del t}f_M 
&= \frac{\del}{\del t} (f_W \circ \phi) \\
&= \left( \frac{\del}{\del t} f_W \right) \circ \phi 
  + (d f_W) \underbrace{\dot{\phi}}_{u \circ \phi} \\
&= \left( \frac{\del}{\del t} f_W + (df_W) u \right) \circ \phi \\
&= \left( \frac{\del}{\del t} + u \cdot \nabla \right) f_W \circ \phi
\end{aligned}
$$

Where the spatial differential $df_W$ applied to the velocity field is the familiar directional derivative:
$$
(df_W)\vec{u} = \sum_i \vec{u}^{i} \frac{\del f_W}{\del x^{i}}
$$
The entire operator applied to $f_W$ is called the **material derivative**, formally defined as 
$$
\frac{D}{Dt} := \frac{\del}{\del t} + u \cdot \nabla
$$
Applying the material derivative to $f_W$ means passing it rhough this operator. Thus, we can compactly write 
$$
\frac{\del}{\del t} (f \circ \phi) = \left( \frac{D}{Dt} f \right) \circ \phi
$$
> [!idea] Intuition
> Suppose we wanted to measure the temperature of the river. 
> - Floating in the boat (Lagrangian $M$), $\frac{D}{Dt}$ tells us how the temperature of the water surroding the boat is changing as we drift downstream. 
> - Standing on the bridge (Eulerian $W$), $\frac{\del}{\del t}$ tells us how the temperature is changing right at that specific spot under the bridge.
> 
> We have two terms because the temperature can change for two different reasons.
> - The $\vec{u} \cdot \nabla$ is the temperature gradient, and so if we moved into a "shaded part" of the river, our temperature would change. 
> - The $\frac{\del}{\del t}$ term affects the entire river. For example, if the sun moved behind clouds at some time $t$, the entire river would have a lower temperature (it is independent of particle choice).
> 
> The material derivative combines both.
# Lemma (Conservation of Material Properties)
If $\frac{Df}{Dt} = 0$, then $\frac{\del}{\del t} (f \circ \phi) = 0$ for scalar function $f$. In other words, if the material derivative of $f$ is zero, then its [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] by the flow map is constant over time. 

**Proof Intuition** (Method of Characteristics):

To solve the transport equation[^2]:

[^2]: A transport equation is an equation that describes the transport of some quantity. 
$$
\frac{\del}{\del t} f + \vec{u} \cdot \nabla f = 0
$$
We construct the flow map $\phi$ such that $\dot{\phi} = u \circ \phi$. By tracking a particle back along the trajectory of this flow map, the function evaluates to:
$$
f(t, x) = f(0, \phi^{-1}_{t}(x))
$$
This is the **method of characteristics**. In a simple space-time (1D space on the $x-$axis, time on the $y-$axis), the material derivative corresponds to a directional derivative along a particle's "world line". Setting it to $0$ simply means the value of $f$ is constant along these characteristic lines; the function's [[Level Set|level sets]] align perfectly with the particle trajectories. If we can integrate along these lines, we can find exact solutions to the transport equation.

> [!idea] Intution
> If $\frac{Df}{Dt} = 0$, then $f$ is constant means that the material derivative of a property never changes. In our previous example, if we were sitting on the boat, our measurement of the water never changes. Even if the temperature is constantly fluctuating, the specific "patch of water" our boat is riding in maintains the exact same temperature. 
> 
> We are riding a "characteristic line", and this property is perfectly conserved for each specific particle as it travels through space and time. 

# Continuity Equations
What if $f$ is not a simple scalar field, but a measure representing density? This leads us to the principle of mass conservation.

Let $q_W(t) : W \to \R$ be the **spatial mass density**[^3] on $W$, meaning

[^3]: The spatial mass density lives in $W$. It is a dynamic, changing field[^4]. If a region of fluid expands (like air expanding to fill a vacuum), the same amount of mass occupies a larger spatial volume, so $q_{W}$ drops. If the fluid compresses, $q_{W}$ spikes.
$$
q_M(t) = q_W(t) \circ \phi(t)
$$
The material desnity $q_M$ is **not** conserved over time as a simple scalar function. If the material's volume changes, its density must change to compensate. Instead, it is the total mass measure $\rho_M$ that is conserved. We can express the conversion as:
$$
\rho_M = q_M(t) dV(t) = q_M(t) \det(d\phi) dX^1 dX^2 dX^3
$$ 
Taking the time derivative of the conserved measure:
$$
\begin{aligned}
0 &= \frac{\del}{\del t} \rho_M  \\
&= \left( \frac{\del}{\del t} q_M \right) dV + q_M \frac{\del}{\del t} dV \\
&= \left( \frac{\del}{\del t} + \vec{u} \cdot \nabla \right) q_W \circ \phi dV 
  + q_M \frac{\del}{\del t} \left( \det(d\phi) \right) dV \\
\end{aligned}
$$
Using [[Jacobi's Formula]], we can compute the time derivative of the determinant of the Jacobian:
$$
\begin{aligned}
\frac{\partial}{\partial t}(\det(d\phi)) &= \det(d\phi) \operatorname{tr}(d\phi^{-1} \dot{d\phi}) \\
&= \det(d\phi) \operatorname{tr}(d\phi^{-1} (\nabla \vec{u}) \cdot d\phi) \\
&= \det(d\phi) \operatorname{tr}(\nabla \mathbf{u}) \\
&= \det(d\phi) \underbrace{\operatorname{div} \vec{u}}_{\nabla \cdot \vec{u}} \\
\end{aligned}
$$
Substituting this back into our mass conservation equation, the $dV$ terms drop out, leaving us with 
$$
\left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla \right) q_w + (\nabla \cdot \vec{u}) q_w = 0
$$
and equivalently 
$$
\underbrace{\frac{\partial}{\partial t} q_w}_{\text{mass density}} + \nabla \cdot \underbrace{\left( q_w \vec{u} \right)}_{\text{mass flux}} = 0
$$

Observe that 
- if $f_M$ is a conserved scalar function (like temperature), we write
  $$
  \left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla \right) f_W = 0
  $$
- if $f_M$ is a conserved measure (like mass), we write
  $$
  \left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla + (\nabla \cdot \vec{u}) \right)q_W = 0
  $$
  This is the principle of **Mass Conservation**.
> [!idea] Intuition
> We cannot just say $\frac{D}{Dt}(q_{W})= 0$ for mass. This is because as the patch of water around our boat enters a narrow, fast-moving stream, our water could stretch out. The volume changes, so the spatial mass density *must* change, even though no mass was destroyed.
> 
> Instead, we return to the bridge (Eulerian View $W$) and draw an imaginary fixed box in the water. 
> - $\frac{\del q_{W}}{\del t}$ representes the rate at which mass is accumulating or depleting inside our fixed box. 
> - $\nabla \cdot (q_{W} \vec{u})$ is the "divergence of the mass flux". It measures the net difference between the mass flowing into the box and the mass flowing out. 
>   
>   The change in the amount of mass inside the box plus the net amount of mass that flowed out must equal exactly zero. Mass cannot be spawned from nothing, or deleted into nothing. 

# Definition (Lie Material Derivative)
We can generalize the [[#Definition (Material Derivative)|Material Derivative]] from scalar fields to more complex geometric objects like vectors, differential forms, or tensors. We particularly want this to measure more interesting fluids like [[#Viscoelastic Materials]], [[#Ferrofluids]], or [[#Plasma / Magnetohydrodynamics]]. Think magnetic fields or alignment of fibers in a piece of stretching cloth.

Suppose $\alpha_{M}$ is some field[^4] of type `[TYPE]`. Let $\phi^{*}_{\texttt{[TYPE]}}$ denote the [[Dual Space#Definition (Pullback Operator for Functions)|pullback operator]] for `[TYPE]`. Let $\alpha_{W}$ be the corresponding field on $W$ such that 

[^4]: This is not a field in the sense of an algrebraic field, but rather a "field" in the physics sense, meaning a function that assigns a value to every point in space. A scalar field is a $0-$tensor field (assigns a scalar to each point), a vector field is a $1-$tensor field (assigns a vector to each point), and so on.
$$
\alpha_{M} = \phi^{*}_{\texttt{[TYPE]}} \alpha_{W}
$$
Then 
$$
\begin{aligned}
\frac{\del}{\del t} \alpha_{M} 
&= \phi^{*}_{\texttt{[TYPE]}} \left( \frac{\del}{\del t} + \mathcal{L}_{\vec{u}} \right) \alpha_{W} \\
&= \phi^{*}_{\texttt{[TYPE]}} \left(
  {\frac{\del}{\del t} \alpha_{W} + {(\mathcal{L}_{\vec{u}})}_{\texttt{[TYPE]}} \alpha_{W}}
\right)
\end{aligned}
$$
where $(\mathcal{L}_{\vec{u}})_{\texttt{[TYPE]}}$ is a spatial derivative called the **Lie derivative** for `[TYPE]`.

Some explanation of the notation is helpful.
- $\alpha_{M}$: The property tracked on the fixed, undeformed material.
- $\frac{\partial}{\partial t} \alpha_{M}$: The true, intrinsic rate of change of this property for a specific particle over time.
- $\alpha_{W}$: The property as it appears floating in the deformed world space.
- $\frac{\partial}{\partial t} \alpha_{W}$: The local, fixed-point rate of change in world space (standing on the bridge).
- $\mathcal{L}_{\mathbf{u}} \alpha_{W}$: The convective rate of change that explicitly calculates how the flow $\mathbf{u}$ is dragging, rotating, and stretching $\alpha_{W}$.
- $\phi^{*}_{\texttt{[TYPE]}}$: The pullback. Because the term in the parentheses exists in the deformed world space $W$, we cannot directly equate it to something in the material space $M$. The pullback acts as a translator, mapping the spatial rates of change backward along the flow map to compare them correctly in the undeformed reference space.


Additionally, when we say `[TYPE]`, we mean 
- Scalar ($0-$tensor): The Lie derivative becomes the standard directional derivative $\mathcal{L}_{\vec{u}} f = \vec{u} \cdot \nabla f$.
- Vector ($1-$tensor): The Lie derivative accounts for the translation of the vector minus the distortion caused by the velocity field's gradients.
- Density/Measure: The Lie derivative accounts for translation plus the divergence of the flow.

## Examples 
Author note, to make my life slightly easier, $\bu$ is the exact same as $\vec{u}$, just different notation for the velocity field.

### 1. Functions (Scalar Fields)

This is the simplest case, where the field attached to the material is just a scalar value (like temperature or concentration).

**The Pullback:**

$$\phi^*_{\text{fcn}} f = f \circ \phi$$

Because a scalar is just a single number at a point, pulling it back from world space to material space requires no geometric transformation. You simply evaluate the world function $f$ at the current spatial position of the particle, $\phi(X, t)$. It is basic function composition.

**The Lie Derivative:**

$$\mathcal{L}_{\mathbf{u}, \text{fcn}} f = \mathbf{u} \cdot \nabla f$$

For a scalar function, the Lie derivative simplifies entirely to the standard directional derivative along the velocity field. It captures how the scalar field changes purely due to translation (advection) through space.

### 2. Measures (Mass Densities / Volumes)
This case describes tracking a physical quantity that depends on the local volume, such as a mass measure $\rho = q \, dV$.

**The Pullback:**

$$\phi^*_{\text{measure}} \rho = \phi^*_{\text{measure}} (q \, dV) = (q \circ \phi) \det(d\phi) \, dV_M$$

When pulling a measure back to the reference configuration, you cannot just compose the density function ($q \circ \phi$). You must also account for how the volume element stretches or compresses during the deformation. This scaling factor is precisely handled by the Jacobian determinant of the flow map, $\det(d\phi)$.

**The Lie Derivative:**

$$\mathcal{L}_{\mathbf{u}, \text{measure}} \rho = (\mathbf{u} \cdot \nabla + \nabla \cdot \mathbf{u}) q \, dV$$

When you take the Lie derivative of a measure, it acts via the product rule on both the density $q$ and the volume element $dV$.

* The first term, $\mathbf{u} \cdot \nabla q$, tracks the translation of the density.
* The second term, $(\nabla \cdot \mathbf{u}) q$, tracks how the changing volume of the fluid concentrates or dilutes that density via the velocity field's divergence.

Notice that this is exactly the spatial portion of the continuity equation we derived earlier.

### 3. Vector Fields
This case describes tracking a directional arrow embedded in the material (such as a magnetic field vector or a structural fiber direction).

**The Pullback:**

$$\phi^*_{\text{vec}} \mathbf{v} = d\phi^{-1}(\mathbf{v}) \circ \phi$$

Vectors live in the tangent space. If a vector $\mathbf{v}$ is floating in the deformed world space, pulling it back to the material reference space requires "un-deforming" it. We pass the spatial vector through the inverse differential of the flow map, $d\phi^{-1}$, to see what its original length and direction were before the material was stretched.

**The Lie Derivative:**

$$\mathcal{L}_{\mathbf{u}} \mathbf{v} = \mathbf{u} \cdot \nabla \mathbf{v} - \mathbf{v} \cdot \nabla \mathbf{u}$$

This is famously known as the **Lie Bracket** or commutator, often written as $[\mathbf{u}, \mathbf{v}]$. It reveals the dual nature of how a vector changes in a flow:

* **Translation ($\mathbf{u} \cdot \nabla \mathbf{v}$):** How the vector changes as it is carried downstream to a new position.
* **Deformation ($-\mathbf{v} \cdot \nabla \mathbf{u}$):** How the vector is physically stretched and rotated by the local spatial gradients of the velocity field. If the fluid particles ahead of the vector are moving faster than the particles behind it, the vector gets stretched out along that gradient.

---

### Connecting to the Lie Material Derivative
If we substitute these specific Lie derivatives back into our main formula:

$$\frac{\partial}{\partial t} \alpha_{M} = \phi^* \left( \frac{\partial}{\partial t} \alpha_{W} + \mathcal{L}_{\mathbf{u}} \alpha_{W} \right)$$

We find that:
* For a **Function**, it produces the standard material derivative: $\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T = 0$.
* For a **Measure**, it produces the mass continuity equation: $\frac{\partial q}{\partial t} + \nabla \cdot (q \mathbf{u}) = 0$.
* For a **Vector**, it produces the transport equations for embedded vector quantities (like the induction equation in magnetohydrodynamics).
---
# Tensors for Continuum Mechanics
Recall:
- [[Manifold]] $M$: **Material** coordinate, **Lagrangian** coordinate 
- [[Manifold]] $W$: **World** coordinate, **Eulerian** coordinate 
- A state of a deformable body is a map (called flow map) 
  $$
  \phi : M \to W
  $$
- The flow map assigns each material point its world position.
- For a dynamical system, the flow map is time-dependent 
  $$
  \phi : \R \times M \to W
  \quad\quad\quad
  \phi(t) : M \to W
  $$
To define inertia, we need a few more structures on Material and World. In particular, a time-independent $n$-[[Differential Forms#Definition (Differential Form)|form]] on $M$ describing mass density
$$
\rho_M \in \Omega^n(M)
$$
where the total mass of a some region $S$ inside $M$ is defined as $\int_S \rho_M$. A time independent metric on $W$ is 
$$
\flat_W \in \Gamma(T^*W \odot T^*W)
$$

> [!info] The Time-Independent World Metric
> A "time-independent metric" means that the background world (e.g. Euclidean space) is static. The intrinsic geometry of the physical space we are observing the material in does not stretch, contract, or change over time. 
>
> This metric is crucial because it provides a fixed way to measure distances and angles. It allows us to:
> 1. Compute the magnitude of the velocity vector $|\dot{\phi}|^2_{\flat_W}$ to define **kinetic energy** (inertia).
> 2. Measure the deformed lengths of the material by pulling this world metric back onto the material space, which induces the **right Cauchy-Green tensor** $C = \phi^* \flat_W$.

## Pullback Bundle
Consider a bundle over the world space $W$, say the tangent bundle $TW$. Suppose there is a map into $W$, say a flow map $\phi : M \to W$. Then we can construct a **pullback bundle** over $M$ called $\phi^* TW$ so that the fibers are given by
$$
(\phi^* TW)_x = T_{\phi(x)} W
$$
We will also use the following notation:
$$
T_\phi W = \phi^* TW
$$
and for some point $x \in W$:
$$
(T_\phi W)_x = T_{\phi(x)} W
$$
To summarize, with $\phi : M \to W$,
- $TM$ is a bundle over $M$
- $TW$ is a bundle over $W$
- $T_{\phi}W$ is a bundle over $M$ (because we pullback from $W$ to $M$).

```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}

% --- Color Theme Definitions ---
\definecolor{curveBlue}{RGB}{45, 110, 175}
\definecolor{fiberLine}{RGB}{140, 90, 180}
\definecolor{fiberFill}{RGB}{248, 240, 255}
\definecolor{planeFill}{RGB}{238, 230, 248}

% --- Macro: Foreground Fiber Bubble ---
% #1: x-shift, #2: y-shift, #3: rotation, #4: label text
\def\bubble#1#2#3#4{
  \begin{scope}[shift={(#1,#2)}, rotate=#3]
    \filldraw[draw=fiberLine, fill=fiberFill, thick, line join=round] 
      (0,0) -- (0.08,0.25) [rounded corners=4pt] -- (0.6,0.25) -- (0.6,1.4) -- (-0.6,1.4) -- (-0.6,0.25) [rounded corners=0pt] -- (-0.08,0.25) -- cycle;
    \node[font=\large, text=fiberLine] at (0, 0.8) {#4};
  \end{scope}
}

% --- Macro: Background Transparent Fiber Bubble ---
\def\bgbubble#1#2#3{
  \begin{scope}[shift={(#1,#2)}, rotate=#3, opacity=0.35]
    \filldraw[draw=fiberLine, fill=fiberFill, thick, line join=round] 
      (0,0) -- (0.08,0.25) [rounded corners=4pt] -- (0.6,0.25) -- (0.6,1.4) -- (-0.6,1.4) -- (-0.6,0.25) [rounded corners=0pt] -- (-0.08,0.25) -- cycle;
  \end{scope}
}

% ==========================================
% LEFT DIAGRAM: Pullback Bundle \phi^*TW
% ==========================================
\begin{scope}[shift={(-5, 0)}]
    
    % Label
    \node[text=fiberLine, font=\LARGE] at (-1.5, 2.2) {$\phi^*TW$};

    % Curve M
    \draw[curveBlue, very thick] (-3, -0.3) .. controls (0, 0.2) .. (3, -0.3);
    \node[text=curveBlue, font=\Large] at (-2.8, -0.8) {$M$};

    % Fibers (Drawn back-to-front for proper Z-indexing overlap)
    % Outer pair
    \bubble{-2.0}{-0.18}{12}{}
    \bubble{2.0}{-0.18}{-12}{}
    
    % Inner pair
    \bubble{-1.0}{0.02}{6}{}
    \bubble{1.0}{0.02}{-6}{}
    
    % Central foreground fiber
    \bubble{0}{0.12}{0}{$T_yW$}

    % Point x
    \fill[curveBlue] (0, 0.12) circle (0.1);
    \node[text=curveBlue, font=\Large] at (0, -0.3) {$x$};

\end{scope}

% ==========================================
% RIGHT DIAGRAM: Bundle TW over W
% ==========================================
\begin{scope}[shift={(4, 0)}]

    % 1. Background Plane (Manifold W)
    \filldraw[draw=fiberLine, fill=planeFill, thick] 
        (-4, -1.2) -- (4, -1.8) -- (4.5, 1.8) -- (-3.5, 2.4) -- cycle;
    \node[text=fiberLine, font=\LARGE] at (3.5, -1.2) {$W$};
    \node[text=fiberLine, font=\LARGE] at (3.0, 2.5) {$TW$};

    % 2. Background Fibers (Cluster)
    % Top row
    \bgbubble{-1.8}{1.3}{0}
    \bgbubble{-0.8}{1.6}{0}
    \bgbubble{0.2}{1.7}{0}
    \bgbubble{1.2}{1.5}{0}
    \bgbubble{2.0}{1.0}{0}
    
    % Middle row
    \bgbubble{-1.2}{0.5}{0}
    \bgbubble{-0.4}{0.8}{0}
    \bgbubble{0.6}{1.1}{0}
    \bgbubble{1.5}{0.6}{0}
    \bgbubble{2.5}{0.4}{0}

    % 3. Embedded Curve \phi(M)
    \draw[curveBlue, very thick] 
        (-2.5, -0.3) .. controls (-1.0, 1.0) and (1.0, -1.5) .. (3.2, 0.2);
    \node[text=curveBlue, font=\Large] at (-2.0, -0.8) {$\phi(M)$};

    % 4. Foreground Elements (Dots, Labels, and Solid Bubbles)
    
    % Point p
    \fill[fiberLine] (-0.8, -1.0) circle (0.08);
    \node[text=fiberLine, font=\large, right] at (-0.7, -1.2) {$p$};
    \bubble{-0.8}{-1.0}{0}{$T_pW$}

    % Point y = \phi(x)
    \fill[curveBlue] (1.6, -0.6) circle (0.08);
    \node[text=curveBlue, font=\large, below] at (1.8, -0.7) {$y = \phi(x)$};
    \bubble{1.6}{-0.6}{0}{$T_yW$}

\end{scope}

\end{tikzpicture}
\end{document}
```

## Time Derivative of Flow Map
For a time-dependent flow map $\phi(t): M \to W$:
$$
\dot{\phi} = \frac{\partial \phi}{\partial t} \in \Gamma(T_\phi W)
$$
It is a section of the pullback bundle, meaning at each point $x \in M$, the velocity is a vector in $T_{\phi(x)}W$.

## Differential (Jacobian) of Flow Map
Given a flow map $\phi: M \to W$, its differential at each point $p \in M$ is a linear map:
$$
d\phi|_p : T_p M \xrightarrow{\text{linear}} T_{\phi(p)} W
$$
The differential is of type "(world)vector-valued 1-form over $M$":
$$
\begin{aligned}
\phi_* = d\phi 
&\in \Gamma(T^{*}M \otimes T_{\phi} W) \\
&= \Omega^1(M; T_\phi W) \quad \text{for short}
\end{aligned}
$$
Because [[Tensor Algebra#Lemma (Tensors as Maps)|every linear map can be represented as a tensor product]], we are able to get this set. The $\Gamma$ is from [[Dual Space#Remark (Types in Differential Calculus)]], smoothly assigning (continuous field) at every point on the linear map.
> [!idea] Intuition
> Imagine drawing a line/curve connecting two points with a marker on some flexible rubber (think of it like a giant flat eraser) surface. You can see the above image for a visualization. 
> 
> If we stretch and twist the rubber, the line/curve will deform. Indeed, if $\phi$ maps how the line points moved in $W$, then the deformation gradient $d\phi$ tells us how that line moved. Feeding $d\phi$ the original undeformed vector spits out a new vector in $W$. By checking how $d\phi$ transforms these tiny vectors (via the differential!) we can describe how chunks of rubber stretched, compressed, rotatated, and sheared.  

## Two-point Tensor
In general, in continuum mechanics, **two-point tensors** are of type:
$$
\Gamma\left( \underbrace{T^*M \otimes \dots}_{p \text{ copies}} \otimes \underbrace{TM \otimes \dots}_{q \text{ copies}} \otimes \underbrace{T_\phi^*W \otimes \dots}_{\ell \text{ copies}} \otimes \underbrace{T_\phi W \otimes \dots}_{m \text{ copies}} \right)
$$
> (Term coined by Erickson 1960. See "Mathematical Foundation of Elasticity" by J. Marsden and T. Hughes 1983).

We use a special shorthand for an $E$-valued $k$-form:
$$
\Gamma\left( \underbrace{T^*M \wedge \dots \wedge T^*M}_{k \text{ copies}} \otimes E \right) = \Omega^k(M; E)
$$

> [!info] Why use this shorthand?
> This notation is useful because it captures the *operational signature* of the tensor. 
> 
> Recall that a standard $k$-form (which eats $k$ material vectors and produces a **scalar**) belongs to the space $\Omega^k(M)$. If we take those scalar-producing $k$-forms and tensor them with a new output space $E$ (like the spatial tangent space $T_\phi W$), we upgrade them into objects that spit out a full vector or tensor in $E$. 
> 
> Thus, whenever you see $\tau \in \Omega^k(M; E)$, we instantly know:
> 1. As a $k$-form, it takes exactly $k$ material vectors as inputs and satisfies skew-symmetry.
> 2. The result of that measurement is a "vector or tensor" of type $E$. 
> 
> For example, the deformation gradient $d\phi \in \Omega^1(M; T_\phi W)$ is essentially a 1-form ($k=1$) that eats one material vector and outputs a spatial vector in $T_\phi W$.

# Tensor Duality

## Dual Space of Tensor Product
The dual of a tensor product [[Tensor Algebra#Theorem (Dual of Tensor Product Space)|distributes]]:
$$
(U \otimes V)^* = U^* \otimes V^*
$$
With the pairing $\langle \alpha \otimes \beta | u \otimes v \rangle = \langle \alpha | u \rangle \langle \beta | v \rangle$. In a basis, this looks like the Frobenius inner product for matrices: $\mathbf{A} : \mathbf{B} = \text{tr}(\mathbf{A}^\top \mathbf{B}) = \sum_{i,j} A_{ij} B_{ij}$.

For tensor fields, the dual requires additionally tensoring an $n$-form:
$$
\Gamma(E)^* = \Gamma\left(E^* \otimes \bigwedge^{n} T^{*}M\right)
$$
With the pairing defined via integration:
$$
\langle\langle \tau | \sigma \rangle\rangle = \int_M \underbrace{\langle \tau | \sigma \rangle}_{n\text{-form}}
$$
The requirement to tensor with an $n$-form arises directly from the mathematical distinction between an algebraic dual space evaluated at a single point and a functional dual space evaluated over a [[Manifold]]. If $E$ is a tensor bundle over an $n-$dimensional manifold $M$, then at any specific point $p \in M$, $\tau_p \in E_p$ has a dual in $\sigma_p \in E_p^*$. The pointwise contraction yields $\langle \tau_p | \sigma_p \rangle \in \R$, a scalar. 

A tensor field is a smooth section of the bundle, denoted $\tau \in \Gamma(E)$. If the dual is simply a section of the dual bundle, $\sigma \in \Gamma(E^*)$, then the pointwise contraction generates a smooth scalar function over the manifold:
$$
f(x) = \langle \tau(x) | \sigma(x) \rangle
$$
To map a continuously varying scalar function $f(x)$ over a manifold to a single scalar, we must use an [[Differential Forms#Definition (Integration of k-form Field)|integral]]. But as integrals are only for differential $n$-forms, i.e. $\bigwedge^n T^{*}M$, the **result of the pointwise contraction must be an $n$-form to be integrable**. 

Indeed, this is why when we integrate, the $\tau, \sigma$ contract, yielding an $n$-form, which we can then integrate:
$$
\int_M \langle \tau | \sigma \rangle
$$

**Examples:**
- $\Omega^0(M)^* = \Omega^n(M)$
	- $\Omega(M)$ is the space of differential 0-forms, smooth scalar functions defined over the manifold $M$. Its dual are linear *functionals*, which take a function $f$ to return a scalar $\R$ over $M$. 
	- Again, since we cannot integrate $f$ without a volume measure, we need a second object to produce a valid $n$-form. Since $f$ is a 0-form, we merely need an $n$-form to multiply. But this is precisely $\Omega^{n}(M)$.
- $\Gamma(T^*M \otimes T_\phi W)^* = \Gamma(TM \otimes T_\phi^* W \otimes \bigwedge^n T^*M)$
	- Here, $E = T^{*}M \otimes T_{\phi}W$. Its dual is trivial to compute. 

## Vector Tensor n-form is a (n-1)-form
Let $V$ be any vector space. We have a canonical isomorphism:
$$
V \otimes \left(\bigwedge^{n} V^* \right) \cong \bigwedge^{n-1} V^*
$$
given by the mapping $\vec{v} \otimes \mu \mapsto i_{\vec{v}} \mu$. This mapping is linearly bijective.

More generally:
$$
\left(\bigwedge^k V \right) \otimes \left(\bigwedge^n V^*\right) \cong \bigwedge^{n-k} V^*
$$

**Example:**
$$
\begin{aligned}
\Omega^k(M)^* &= \Gamma\left(\bigwedge^k T^*M\right)^* \\
&= \Gamma\left(\left(\bigwedge^k TM\right) \otimes \left(\bigwedge^n T^*M\right)\right) \\
&= \Gamma\left(\bigwedge^{n-k} T^*M\right) \\
&= \Omega^{n-k}(M)
\end{aligned}
$$
With the pairing $\langle\langle \alpha_{k\text{-form}} | \beta_{(n-k)\text{-form}} \rangle\rangle = \int_M (\alpha \wedge \beta)_{n\text{-form}}$.

This is a "specialization"[^5] of the [[Exterior Algebra#Definition (Interior Product / Contraction)|interior product]].

[^5]: As the opposite of generalization.
## More Examples
What is the type of the deformation gradient $d\phi$, and what is its dual object?
$$
d\phi \in \Gamma(T^*M \otimes T_\phi W)
$$
$$
\begin{aligned}
\Gamma(T^*M \otimes T_\phi W)^* 
&= \Gamma\left(TM \otimes T_\phi^* W \otimes \bigwedge^n T^*M\right) \\
&= \Gamma\left(
  \underbrace{\bigwedge^{n-1} T^*M}_{\text{flux}}
  \otimes 
  \underbrace{T_\phi^* W}_{\text{momentum}}
\right)
\end{aligned}
$$
This dual object represents **momentum flux**, which is **stress**.

> [!idea] Intuition
> In a 3D world (which we care about), $n = 3$. Since the left side tensor is designed to be $(n-1)$-form integrated, it is no different from integrating over a surface, calculating the density in that area.
# Elasticity

## Postulates
1. The position of the body is described by 
	1. a (time-dependent) map $\phi: M \to W$, 
	2. where $M$ has a time-independent mass density $\rho_M \in \Omega^n(M)$ and 
	3. $W$ has a time-independent metric $\flat_W \in \Gamma(T^*W \odot T^*W)$.
2. The elastic potential energy for a map $\phi$ takes the form:
   $$
   \mathcal{U}(\phi) = \int_M U(\phi^* \flat_W)
   $$
   for some fiber-wise (nonlinear) mapping (depending on material) 
   $$
   U_p: T_p^*M \odot T_p^*M \xrightarrow{\text{nonlinear}} \bigwedge^n T_p^*M
   $$
   i.e. the potential is only a function of the induced metric encoding its notion of distances in the world. (**Frame-indifference**)

## Terminology
- We call $F = \phi_* = d\phi \in \Gamma(T^*M \otimes T_\phi W)$ the **deformation gradient**.
- The induced metric $\phi^* \flat_W$ can be understood by:
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}[>=stealth]

% --- Color Definitions ---
\definecolor{blueNode}{RGB}{45, 85, 165}
\definecolor{purpleNode}{RGB}{115, 55, 155}

% --- Core Nodes ---
\node (TL) at (0, 2) {\LARGE $\textcolor{blueNode}{T_pM}$};
\node (TR) at (4, 2) {\LARGE $\textcolor{purpleNode}{T_{\phi(p)}W}$};
\node (BR) at (4, 0) {\LARGE $\textcolor{purpleNode}{T_{\phi(p)}^*W}$};
\node (BL) at (0, 0) {\LARGE $\textcolor{blueNode}{T_p^*M}$};

% --- Left Equation Node ---
\node (EQ) at (-1.5, 1) {\LARGE $F^* \textcolor{purpleNode}{\flat_W} F = \phi^* \textcolor{purpleNode}{\flat_W}$};

% --- Arrows ---
% Top arrow (F)
\draw[->, very thick] (TL) -- (TR) node[midway, above, yshift=4pt] {\Large $F$};

% Right arrow (flat_W)
\draw[->, very thick] (TR) -- (BR) node[midway, right, xshift=4pt] {\Large $\textcolor{purpleNode}{\flat_W}$};

% Bottom arrow (F^*)
\draw[->, very thick] (BR) -- (BL) node[midway, above, yshift=4pt] {\Large $F^*$};

% Dashed curved arrow
% Bulges to the right using explicit departure and arrival angles
\draw[->, very thick, dashed] (TL) to[out=-40, in=40] (BL);

\end{tikzpicture}
\end{document}
```
- The induced metric $C := F^* \flat_W F \in \Gamma(T^*M \odot T^*M)$ is called the **(right)-Cauchy-Green tensor**. 

> [!info] Understanding the Diagram: How to Measure Deformed Length
> The diagram illustrates how the Cauchy-Green tensor $C$ operates by composing three separate maps:
> 1. **$F$ (Deformation Gradient):** We start with a small undeformed vector in the material tangent space $T_p M$. $F$ pushes this vector forward into the physical world $W$, telling us what the deformed vector looks like in the spatial tangent space $T_{\phi(p)} W$.
> 2. **$\flat_W$ (World Metric):** Once in the physical world, you use the standard metric $\flat_W$ to measure its length (or compute the dot product with another vector). This mathematically "lowers the index", mapping the spatial vector to a spatial covector in $T_{\phi(p)}^* W$.
> 3. **$F^*$ (Pullback):** Finally, the adjoint $F^*$ pulls that measurement result back to the material covector space $T_p^* M$.
> 
> By taking the direct dashed path $C = F^* \flat_W F$, we skip the intermediate steps. $C$ acts as an "induced metric" living entirely in the undeformed material space. If we feed $C$ two undeformed material vectors, it instantly outputs what their dot product *will be* after they are stretched and twisted into the physical world.

In 3D Cartesian coordinates:
- Let $(X,Y,Z)$ denote the Cartesian coordinate for $M$ and $(x,y,z)$ the Cartesian coordinate for $W$.
- Flow map $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} \phi^1(X,Y,Z) \\ \phi^2(X,Y,Z) \\ \phi^3(X,Y,Z) \end{bmatrix}$
- Deformation gradient $\mathbf{F} = \begin{bmatrix} \frac{\partial \phi^1}{\partial X} & \frac{\partial \phi^1}{\partial Y} & \frac{\partial \phi^1}{\partial Z} \\ \frac{\partial \phi^2}{\partial X} & \frac{\partial \phi^2}{\partial Y} & \frac{\partial \phi^2}{\partial Z} \\ \frac{\partial \phi^3}{\partial X} & \frac{\partial \phi^3}{\partial Y} & \frac{\partial \phi^3}{\partial Z} \end{bmatrix}$
- Right Cauchy-Green tensor $\mathbf{C} = \mathbf{F}^\top \mathbf{F}$

## Deriving Elastic Force
Back to our potential energy, given some pointwise nonlinear elastic model $U$: 
$$
U: \Gamma(T^*M \odot T^*M) \xrightarrow{\text{pointwise nonlinear}} \Gamma(\bigwedge^n T^*M)
$$
$$
\mathcal{U}(\phi) = \int_M U(\phi^* \flat_W) = \int_M U(C)
$$
The elastic force is the negative gradient of the potential energy: $\mathbf{f} = -d\mathcal{U}_\phi$. To compute this derivative, we can view the energy functional as a sequence of mappings and apply the chain rule. In the context of fields, this is essentially **continuous backpropagation**.

### 1. The Global Sequence of Maps
First, we can express the entire energy functional $\mathcal{U}(\phi)$ as a sequence of macroscopic maps from the space of all possible flow maps $C^\infty(M; W)$ to the final scalar energy:
$$
\underset{\textstyle \phi}{C^\infty(M; W)} \xrightarrow{d} \underset{\textstyle F}{\Gamma(T^*M \otimes T_\phi W)} \xrightarrow{\mathcal{G}} \underset{\textstyle C = F^*\flat_W F}{\Gamma(T^*M \odot T^*M)} \xrightarrow{U} \underset{\textstyle U(C)}{\Gamma(\bigwedge^n T^*M)} \xrightarrow{\int_M} \underset{\textstyle \mathcal{U}(\phi)}{\R}
$$

### 2. The Tangent Space Forward Pass (Kinematics)
Consider a small perturbation to the flow map $\phi$, which gives us a velocity field $\delta \phi \in \Gamma(T_\phi W)$. How does this velocity propagate through our quantities?
$$
\Gamma(T_\phi W) 
\xrightarrow{d^{\nabla^W}} \Gamma\left(T^*M \otimes T_\phi W\right) 
\xrightarrow{d\mathcal{G}|_F} \Gamma\left(T^*M \odot T^*M\right) 
\xrightarrow{dU|_C} \Gamma\left(\bigwedge^n T^*M\right) 
\xrightarrow{\int_M} \R
$$
- **$d^{\nabla^W}$**: Takes the velocity field and computes its spatial gradient (giving the perturbation to the deformation gradient $F$).
- **$d\mathcal{G}|_F$**: Maps the change in $F$ to the change in the Cauchy-Green tensor $C$ (where $\mathcal{G}(F) = F^* \flat_W F$).
- **$dU|_C$**: Maps the change in the metric/strain to a change in the local energy density (an $n$-form).
- **$\int_M$**: Integrates the energy density to get the total change in scalar energy $\delta \mathcal{U} \in \R$.

### 3. The Backward Pass (Forces and Stresses)
To find the force, we need the derivative $d\mathcal{U}_\phi$. We start from the scalar energy output (the number $1 \in \R^*$) and pull it backward through the adjoint/dual of each linear map:
$$
\begin{aligned}
\underset{\textstyle d\mathcal{U}_\phi}{\Gamma\left(\bigwedge^n T^*M \otimes T_\phi^* W\right)} 
\xleftarrow{(d^\nabla)^*} \underset{\textstyle \frac{\del U}{\del F}}{\Gamma\left(\bigwedge^{n-1} T^*M \otimes T_\phi^* W\right)} 
\\
\xleftarrow{d\mathcal{G}|_F^*} \underset{\textstyle \frac{\del U}{\del C}}{\Gamma\left(TM \odot TM \otimes \bigwedge^n T^*M\right)} 
\xleftarrow{dU|_C^*} \underset{\textstyle \mathbb{1}}{\Omega^0(M)} 
\xleftarrow{\mathbb{1}} \underset{\textstyle 1}{\R^*}
\end{aligned}
$$
As we pull back the scalar "$1$", it transforms into different physical stress quantities at each intermediate space. 

## Terminology (Stress Tensors)
By defining names for the intermediate states of the pullback, we recover the classic stress tensors of continuum mechanics!

### 2nd Piola-Kirchhoff Stress
When the pullback reaches the space dual to the Cauchy-Green tensor $C$, we get the 
[[Stress#Alternative Stress Tensors|2nd Piola-Kirchhoff stress]]:
$$
S := 2 \frac{\del U}{\del C} \in \Gamma\left(TM \odot TM \otimes \bigwedge^n T^*M\right)
$$
- **Physical Meaning**: This stress lives entirely in the undeformed material space ($M$). It is the energetic conjugate to the metric $C$. If you change the deformed lengths of the material (change $C$), $S$ tells you how much work is done.

### 1st Piola-Kirchhoff Stress Tensor
Pulling back one step further to the space dual to the deformation gradient $F$, we get the 1st Piola-Kirchhoff stress:
$$
P := d\mathcal{G}|_F^* S = \frac{\del U}{\del F} \in \Gamma\left(\bigwedge^{n-1} T^*M \otimes T_\phi^* W\right)
$$
- **Physical Meaning**: This is a **two-point tensor**. It eats a material $(n-1)$-form (an area element in the undeformed state) and outputs the actual physical force vector in the world space $W$. This is the mathematical formalization of "Force per unit undeformed area".
- Notice its type: $\Omega^{n-1}(M; T_\phi^* W)$. It's an $(n-1)$-form valued in world covectors!

Finally, pulling back $P$ through the spatial divergence $(d^\nabla)^*$ yields the actual elastic force density $d\mathcal{U}_\phi$.

