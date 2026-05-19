---
tags:
  - CSE_291G
---
# Background
**Continuum mechanics** is the study of deformable bodies, in contrast to [[Rigid Body Dynamics|rigid bodies]], which cannot deform. 

The following are examples of deformable bodies:
- jello
- two dimensional, like a cloth
- elastic rods
- hair
- food

# Definition (Shear)
**Shear** is a type of deformation that occurs when a force is applied parallel to the surface of a material. The material deforms by sliding layers of the material past each other.

# Definition (Fluid)
A **fluid** is a substance that can deform. The potential energy of a fluid is independent of the [[#Definition (Shear)|shearing]] mode of the deformation and is only a function of how the volume is changed. There is no restoration force for volume-preserving deformations (such as shearing). 

Air and water are two examples of fluids. They are both deformable, but they have different properties.

## Definition (Elastic Bodies)
An **elastic body** is a type of deformable body that can return to its original shape after being deformed. The potential energy of an elastic body depends on the deformation, and there is a restoration force that tries to return the body to its original shape.

For example, 
- rubber band
- a piece of cloth
- bread; if we squish it, it will return to its original shape after we release it. However, if we squish it too much, it will not return to its original shape and will be permanently deformed.

There is a notion of "elastoplasticity", which is the study of materials that can undergo both elastic and plastic deformation. Plastic deformation is a type of deformation that is permanent and does not return to the original shape after the force is removed.

## Definition (Viscoelastic Materials)
These are materials where the potential energy is a function of deformation and the rate of change of deformation. They have both elastic and viscous properties.

For example,
- slime
- [Oobleck](https://en.wikipedia.org/wiki/Non-Newtonian_fluid#Oobleck)

These are also known as non-Newtonian fluids.

## Definition (Ferrofluids)
**Ferrofluids** are fluids that become magnetized in the presence of a magnetic field. They are made of tiny magnetic particles suspended in a carrier fluid. When a magnetic field is applied, the particles align with the field, causing the fluid to become magnetized. 

## Definition (Plasma / Magnetohydrodynamics)
These fluids are made of electrically conducting material. They are affected by magnetic fields and can conduct electricity. Examples include:
- plasma, which is a state of matter where the gas is ionized and can conduct electricity
- liquid metals, which are metals that are in a liquid state at room temperature, such as mercury and gallium
- solar wind, which is a stream of charged particles emitted by the sun

--- 
The idea is that they are all deformable bodies, and we can use the same mathematical framework to describe their behavior. The differences between them come from the specific properties of the materials, such as their elasticity, viscosity, and conductivity.

# Postulate 1 
We assume that the setup is that we have a 
- [[Manifold]] $M$, or the **material space** (also known as the Lagrangian coordinate)
- $W$, or the **world space** (also known as the Eulerian coordinate)
- the state of the deformable body described by a map $\phi : M \to W$

The visualization is that we have some space $M$ (the index set of all the molecules) mapped by $\phi$ to how the molecules are placed in the space we view $W$. 
> Visualizing $W$ is done by visualizing in $\R^{3}$ and telling yourself it's $W$.

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

We kind of have this in rigid bodies; the index set to be the body coordinate, and $\phi$ maps via rotation and translation. Importantly, $M$ is independent of time, since the set of molecules does not change. 

> [!faq] What is a Postulate?
> A postulate is a statement that is assumed to be true without proof. It is kind of like an axiom but for physicists. 

# Postulate 2
The *first* part of this postulate is that $M$ is equipped with a time-independent mass measure 
$$
\rho_M := 
\underbrace{
  q_M (t)
}_{\substack{q_M : M \to \R \\ \text{mass density}}}
\cdot 
\underbrace{
  dV(t)
}_{\substack{\text{volume} \\ \text{element}}}
$$
Both could be dependent on time, since these measurements are done relative to the world space $W$. 

If $\Omega \subset M$, then we can measure the volume of $\Omega$ by integrating the volume element over $\Omega$:
$$
\text{Volume}(\phi_M(\Omega)) := \int_{\Omega} dV
$$
representing the volume of $\Omega$ occupied in the world space. Similarly, since we can determine some total mass of $\Omega$, we can have some mass that changes over time. 
$$
\text{Mass}(\Omega) := \int_{\Omega} \rho_M = \int_{\Omega} q_M dV
$$
The *second* part of this postulate equips $W$ with a time-independent inner-product structure denoted by $\flat_{W}$ or $\langle \cdot, \cdot \rangle_{W}$. 

> [!idea] 
> A good definition is that axiomatically, $\rho_M$ is given and is always time independent. We can define mass density as $q(t) = \rho_M / dV(t)$, which is time dependent.
>
> We do not give $M$ a [[Metric Space#Definition (Metric)|metric]], but only some mass measure. Most of the time, $W = \R^{3}$ in literature. 

---
With these two postulates, we can define things using objects introduced here. For example...

# Definition (Flow Velocity)
Write 
$$
\frac{d}{dt} \phi(t) = \dot{\phi}
$$
as the **flow velocity** of the deformation. The *type* of $\dot{\phi}$ is 
$$
\dot{\phi} : M \to TW
$$
or the [[Dual Space#Definition (Tangent Bundle)|tangent bundle]]. Indeed, $\dot{\phi}(p) \in T_{\phi(p)}W$. 
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
So we feed some point $p \in M$ into $\phi(t)$, and we get $\phi_{(t)}(p) \in W$. We can also feed other $q \in M$ and get velocity vectors at different points in $W$. This gives us a velocity field in $W$ denoted by $\vec{u} \in \Gamma(TW)$ where $\dot{\phi}(t) = \vec{u}(t) \circ \phi(t)$. Note that $\vec{u}$ is only defined only on the image of $\phi$.

$\vec{u}$ is called the **velocity field** in the Eulerian coordinate.

# Definition (Fluid Kinetic Energy)
The **kinetic energy** of the fluid is given by 
$$
K(\phi, \dot{\phi}) := \frac{1}{2} \int_{M} 
\left\langle \dot{\phi}, \dot{\phi}\right\rangle_{W} \, \rho_M
= 
\frac{1}{2} \int_{M} \| \dot{\phi}\|_{W}^{2} \rho_M
$$
In theory, we cannot define anything else other than kinetic energy (but this is good enough). We can also rewrite the second expression as
$$
K(\phi, \dot{\phi}) = \frac{1}{2} \int_{\phi(M) \subset W} \| \vec{u} \|^{2} q_W \, dV_W
$$

Suppose we have a function $f_M(t) : M \to \R$, a scalar field defined on $M$ (like temperature). Let $f_W(t) : W \to \R$ be defined such that $f_M = f_W \circ \phi$. 

So what is $\frac{\del}{\del t}f_M$? This means that we are "fixing the spatial degrees of freedom" in $M$ and asking the rate of change of $f_M$ at that point. Because $\phi$ is moving, this corresponds to some moving particle in $W$. So,
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

Where 
$$
(df_W)u = \sum_i u^{i} \frac{\del f_W}{\del x^{i}}
$$
the partial derivative with respect to the Eulerian coordinates. This is also called the **material derivative** of $f_W$.

# Definition (Material Derivative)
The **material derivative** of a scalar field is defined as
$$
\frac{D}{Dt} := \frac{\del}{\del t} + u \cdot \nabla
$$
To say the material derivative of $f$ is to multiply $f$ by the operator $\frac{D}{Dt}$. 

So, 
$$
\frac{\del}{\del t} (f \circ \phi) = \left( \frac{D}{Dt} f \right) \circ \phi
$$

# Lemma
If $\frac{Df}{Dt} = 0$, then $\frac{\del}{\del t} (f \circ \phi) = 0$ for scalar function $f$. In other words, if the material derivative of $f$ is zero, then the [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] by the flow map is constant over time. 

Proof: TODO

solve 
$$
\frac{\del}{\del t} f + u \cdot \nabla f = 0
$$
we build $\phi$ so that dotphi = u \circ \phi, and we get
$$
f(t, x) = f(0, \phi^{-1}_{t}(x))
$$
we follow the trajectory of the flow map back to the original point and evaluate it. This is also called the method of characteristic. it is called this because on the space and time diagram $x$ is x-axis, and $t$ is y-axis, (space is 1D to make it easier to draw), then the material derivative is represnted by some particle on a world line, where the time derivative points vertical, and the second term points horizontally, so together we get a directional derivative, or the corresponding speed of the world line of the particle.

this being 0 is saying we have level sets along these lines. by doing this we, are constructing phi in such a way that the material space is exactly time equal to 0?. 

these lines are called characteristic lines. if we can integrate this dotphi, we have exact solutions.

# Continuity Equations
What if $f$ was a vector field? Then we can no longer use the material derivative. This is the same as mass conservation. 

Let $q_W(t) : W \to \R$ be the mass density on $W$ where 
$$
q_M(t) = q_W(t) \circ \phi(t)
$$
So, $q_M$ is not conserved over time as a scalar fnction. if the volume is changing, the density is chaning. but we say that $\rho_M$ is conserved, 
$$
\rho_M = q_M(t) dV(t) = q_M(t) \det(d\phi) dX^1 dX^2 dX^3
$$ 

$$
\begin{aligned}
D &= \frac{\del}{\del t} \rho_M  \\
&= \left( \frac{\del}{\del t} q_M \right) dV + q_M \frac{\del}{\del t} dV \\
&= \left( \frac{\del}{\del t} + \vec{u} \cdot \nabla \right) q_W \circ \phi dV 
  + q_M \frac{\del}{\del t} \left( \det(d\phi) \right) dV \\
\end{aligned}
$$

## Lemma
$$
\dot{\left[ \det(A) \right]} = \det(A) \text{tr}(A^{-1} \dot{A}) 
$$

So, 
$$
\begin{aligned}
\text{So} \qquad \frac{\partial}{\partial t}(\det(d\phi)) &= \det(d\phi) \operatorname{tr}(d\phi^{-1} \dot{d\phi}) \\
&= \det(d\phi) \operatorname{tr}(d\phi^{-1} (\nabla \vec{u}) \cdot d\phi) \\
&= \det(d\phi) \operatorname{tr}(\nabla \mathbf{u}) \\
&= \det(d\phi) \underbrace{\operatorname{div} \vec{u}}_{\nabla \cdot \vec{u}} \\
\end{aligned}
$$
implies that
$$
\left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla \right) q_w + (\nabla \cdot \vec{u}) q_w = 0
$$
and equivalently 
$$
\underbrace{\frac{\partial}{\partial t} q_w}_{\text{mass density}} + \underbrace{\nabla \cdot \left( q_w \vec{u} \right)}_{\text{mass flux}} = 0
$$

Observe that 
- if $f_M$ is a conserved scalar function, we write
  $$
  \left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla \right) f_W = 0
  $$
- if $f_M$ is a conserved measure, we write
  $$
  \left( \frac{\partial}{\partial t} + \vec{u} \cdot \nabla + (\nabla \cdot \vec{u}) \right)q_W = 0
  $$