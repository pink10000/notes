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
- Flow map $\phi : M \times \mathbb{R} \to W$: Describes the state of the body at time $t$ via $\phi(X, t) = x$.

The visualization is that we have some space $M$ (the reference configuration) mapped by $\phi$ to how the particles are placed in the world space $W \cong \mathbb{R}^3$.

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
    \draw[ultra thick, color=blue!70!black, fill=blue!5] plot [smooth cycle, tension=0.7] coordinates {
        (0.2, 0.5)
        (0.5, 1.8)
        (2.0, 1.4)
        (2.8, 0.2)
        (2.2, -1.0)
        (1.0, -1.2)
        (0.1, -0.3)
    };
    % Label M
    \node[scale=1.5, color=blue!70!black] at (1.0, -0.6) {$M$};
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
    \draw[ultra thick, color=black!80, fill=gray!5] (F_TL) -- (B_TL) -- (B_TR) -- (F_TR) -- cycle;
    % Right face
    \draw[ultra thick, color=black!80, fill=gray!10] (F_BR) -- (B_BR) -- (B_TR) -- (F_TR) -- cycle;
    % Front face
    \draw[ultra thick, color=black!80, fill=white] (F_BL) rectangle (F_TR);

    % Label W
    \node[scale=1.5] at (4.2, 4.7) {$W$};

    % --- Embedded Manifold phi(M) ---
    % Deformed version of M living inside the front face of W
    \draw[ultra thick, color=blue!70!black, fill=blue!5] plot [smooth cycle, tension=0.7] coordinates {
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
  where $q_M$ is the material **mass density** and $dV_M$ is the **volume element**. Note that while $\rho_M$ is fixed for a piece of material, its representation in world space (density and volume) changes as it deforms.
  
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
\draw[thick, fill=blue!3] plot [smooth cycle, tension=0.8] coordinates {
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
\draw[thick, fill=blue!3] plot [smooth cycle, tension=0.7] coordinates {
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

To solve the transport equation[^1]:

[^1]: A transport equation is an equation that describes the transport of some quantity. 
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

Let $q_W(t) : W \to \R$ be the spatial mass density on $W$, meaning
$$
q_M(t) = q_W(t) \circ \phi(t)
$$
The material desnity $q_M$ is **not** conserved over time as a simple scalar function. If the material's volume changes, its density must change to compensate. Instead, it is the total mass measure $\rho_M$ that is conserved. We can express this conservation as:
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

Suppose $\alpha_{M}$ is some field[^2] of type `[TYPE]`. Let $\phi^{*}_{\texttt{[TYPE]}}$ denote the [[Dual Space#Definition (Pullback Operator for Functions)|pullback operator]] for `[TYPE]`. Let $\alpha_{W}$ be the corresponding field on $W$ such that 

[^2]: This is not a field in the sense of an algrebraic field, but rather a "field" in the physics sense, meaning a function that assigns a value to every point in space. A scalar field is a $0-$tensor field (assigns a scalar to each point), a vector field is a $1-$tensor field (assigns a vector to each point), and so on.
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

If you substitute these specific Lie derivatives back into our main formula:

$$\frac{\partial}{\partial t} \alpha_{M} = \phi^* \left( \frac{\partial}{\partial t} \alpha_{W} + \mathcal{L}_{\mathbf{u}} \alpha_{W} \right)$$

We find that:
* For a **Function**, it produces the standard material derivative: $\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T = 0$.
* For a **Measure**, it produces the mass continuity equation: $\frac{\partial q}{\partial t} + \nabla \cdot (q \mathbf{u}) = 0$.
* For a **Vector**, it produces the transport equations for embedded vector quantities (like the induction equation in magnetohydrodynamics).