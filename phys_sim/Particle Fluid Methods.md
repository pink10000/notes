---
tags:
  - CSE_291G
---

# Particle in Cell Method
Particle in Cell (PIC) is a numerical method that moves away from the grid-based method into a hybrid of Lagrangian and Eulerian solvers. 
- Grids (Eulerian): Excellent for solving the global pressure projection constraint because the math sits on a rigid, predictable matrix. 
    - However, they are terrible at advection because interpolating data across the grid causes massive numerical diffusion (blurring).
- Particles (Lagrangian): Perfect for advection. Simply move the particle through space ($\frac{\partial \phi}{\partial t} = \mathbf{v}$). There is exactly zero numerical diffusion. 
    - However, calculating the global pressure constraint is a nightmare because particles are disorganized and require expensive nearest-neighbor searches to figure out who is pushing whom.

First, discretize the material space $M$ as particles $M = \{1, \dots, \text{\# particles}\}$. Each particle $p \in M$ has a mass $m_p$ that is invariant over time. The particle location is our flow  map $\phi : M \to W = \R^3$. Computing pressure projection is difficult using this particle method. 

Denote an Eulerian function and its Lagrangian twin:
$$
\begin{aligned}
f &: W \to \R \\ 
\hat{f} &: M \to \R
\end{aligned}
$$
where 
$$
\hat{f} = \phi^* f = f \circ \phi
$$
To do **advection**, we need to move the particles according to the fluid velocity field. This is done by doing it in the Lagrangian coordinate:
$$
\begin{aligned}
\frac{\del}{\del t} \hat{f} &= 0 \\
\frac{\del}{\del t} \phi &= \bu \circ \phi
\end{aligned}
$$
This is much easier as there is no diffusion term. This is unlike the Eulerian method where 
$$
\frac{\del}{\del t} f + \mathscr{L}_\bu f = 0
$$
which requires heavy interpolation when discretized. This causes numerical diffusion and blurring.

## Steps
At the beginning of each iteration, each particle $p \in M$ has a velocity $\bv_p$ and $\phi_p$. 
1. Advection step $\frac{\del}{\del t} \phi_p = \bv_p$ or $\bu = \texttt{P2G}(\bv)$ and $\frac{\del}{\del t} \phi = \bu \circ \phi$. 
2. Transfer particle data to grid $\bu = \texttt{P2G}(\bv)$.
3. Pressure projection on grid $\bu = \texttt{PressureSolve}(\bu)$. Recall we do this via [[#Applying FFT (Spectral Method)]].
4. Transfer grid data back to particles $\bv = \texttt{G2P}(\bu)$.
5. End iteration.

# Fluid Implicit Particle Solver (FLIP)
At the beginning of each iteration, each particle $p \in M$ has a velocity $\bv_p$ and $\phi_p$. 
1. Advection step $\frac{\del}{\del t} \phi_p = \bv_p$ or $\bu = \texttt{P2G}(\bv)$ and $\frac{\del}{\del t} \phi = \bu \circ \phi$. 
2. Transfer particle data to grid $\bu = \texttt{P2G}(\bv)$.
3. Pressure projection on grid $\bu' = \texttt{PressureSolve}(\bu)$. Recall we do this via [[#Applying FFT (Spectral Method)]].
4. Transfer the incremental effect of pressure back to particle. $\bv \leftarrow \bv + \texttt{G2P}(\bu' - \bu)$.
5. End iteration.

This works because the particle keeps its own original, perfectly advected velocity, and only *adds* the acceleration caused by the pressure gradient. 

# Particle-Grid Transfer
How do we calculate the transfer of data between continuous floating particles and a rigid, discrete grid? In particular, how do we calculate $\texttt{P2G}(\cdot)$ and $\texttt{G2P}(\cdot)$?

Before we can transfer data, we need a rule for how much a particle affects a grid cell. This is the basis function $N_i(\bx)$ for $i \in \texttt{Grid}$ and $\bx \in \R^3$. It has the following properties:
- Local: $N_i(\bx) = 0$ when $\bx$ is far away from the grid point $i$. 
- Partition of unity: $\sum_{i \in \texttt{Grid}} N_i(\bx) = 1$ for all $\bx$.
- Nonnegativity: $N_i(\bx) \geq 0$ for all $i, \bx$.

> [!idea] 
> Imagine a particle glowing like a lightbulb. $N_i(\bx)$ describes how bright that light is at grid cell $i$ when the particle is at position $\bx$. 
> - Local: The light fades to exactly $0$ if the particle is too far away.
> - Partition of unity: If you add up the light hitting all the surrounding grid cells, it must equal exactly $100\%$. You cannot artificially create or destroy mass/momentum during the transfer. 
>   - Usually, this is calculated using a [[B-spline]], which is just a mathematically smooth bell curve.

Thus, we can calculate Grid to Particle ($\texttt{G2P}(\cdot)$) as 
$$
\hat{f}_p \approx \sum_{i \in \texttt{Grid}} f_i N_i(\phi_p)
$$
To find the particle's new velocity, we look at the surround grid cells and multiply each grid velocity by the basis weight, and add them up (kind of like a 2D convolution!).

And for Particle to Grid ($\texttt{P2G}(\cdot)$):
$$
f_i \approx \frac{
    \sum_{p \in M} \hat{f}_p m_p N_i(\phi_p)
}{
    \sum_{p \in M} m_p N_i(\phi_p)
}
$$
This is just the weighted average of the particles, which causes the smoothing effect.

## Affine Particle-Grid Transfer
We can upgrade both $\texttt{G2P}(\cdot)$ and $\texttt{P2G}(\cdot)$ to be [[Affine]] and not just linear. The idea is that each particle stores more information than just velocity. 

Affine Grid to Particle ($\texttt{AffineG2P}(\cdot)$):
$$
\begin{aligned}
\hat{f}_p &\approx \sum_{i \in \texttt{Grid}} f_i N_i(\phi_p) \\
% 
\widehat{\nabla f_p} &\approx 
\argmin_{\bA} \sum_{i \in \texttt{Grid}} \left| \frac{
    \sum_{p \in M} (\hat{f}_p + \mathbf{A}[\![ \mathbf{x}_i - \phi_p ]\!]) m_p N_i(\phi_p)
}{
    \sum_{p \in M} m_p N_i(\phi_p)
} - f_i \right|^2
\end{aligned}
$$
Affine Particle to Grid ($\texttt{AffineP2G}(\cdot)$):
$$
f_i \approx 
\frac{
    \sum_{p \in M} (\hat{f}_p + \widehat{\nabla f_p}[\![ \bx_i - \phi_p ]\!]) m_p N_i(\phi_p)
}{
    \sum_{p \in M} m_p N_i(\phi_p)
}
$$
The primary difference here is that the numerator now includes a term for the gradient of the particle's properties. This is merely a first-order [[Taylor's Theorem|Taylor expansion]] of the particle's influence on the grid.

> [!idea] 
> Instead of a particle being a single point moving through space with velocity $\bv$, we can imagine the particle is a tiny, squishy rubber ball. It can also stretch, shear, and spin. We store this inside $\widehat{\nabla f_p}$.

So how do we calculate the optimization problem? The goal is to find a specific $\bA = \widehat{\nabla f_p}$ gradient matrix that captures how the particle's properties are changing in space. 
- Let $\br_i = (\bx_i - \phi_p)$ be the distance vector from the particle to grid node $i$. 
- Our approximation of the velocity at node $i$ is $\hat{f}_p + \bA \br_i$. The actual velocity at node $i$ is $f_i$. 
- We also only care about the nodes that are close to the particle.

Thus, we get an error function for a given $\bA$:
$$
E(\bA) = \sum_{i \in \texttt{Grid}} N_i(\phi_p) \left\| (\hat{f}_p + \bA \br_i) - f_i \right\|^2
$$
We want to minimize this error. So we need to take the derivative and set it to $0$ to find the [[Local Minima]]. 
$$
\frac{\partial E}{\partial \bA} = 2 \sum_{i \in \texttt{Grid}} N_i(\phi_p) \left( \hat{f}_p + \bA\br_i - f_i \right) \br_i^\top = 0
$$
With some rearranging, we get 
$$
\sum_{i} N_i(\phi_p) \bA \br_i \br_i^\top = \sum_{i} N_i(\phi_p) (f_i - \hat{f}_p) \br_i^\top
$$
For this specific particle, $\bA$ is a constant matrix, so we can pull it out of the summation.
$$
\bA \left[ \sum_{i} N_i(\phi_p) \br_i \br_i^\top \right] 
= 
\sum_{i} N_i f_i \br_i^\top - \hat{f}_p \left[ \sum_{i} N_i(\phi_p) \br_i^\top \right]
$$
The very last term is important. Because standard [[B-spline]] basis functions are [[B-spline#some theorem|perfectly symmetrical]], if you sum up all the distances to the surrounding grid nodes weighted by the spline, they perfectly balance out to exactly $0$. This causes $\hat{f}_{p}$ to completely vanish! We are left with 
$$
\bA \left[ \sum_{i} N_i(\phi_p) \br_i \br_i^\top \right] = \sum_{i} N_i(\phi_p) f_i \br_i^\top
$$
Now, define 
$$
\begin{aligned}
\bB &:= \sum_{i \in \texttt{Grid}} N_i(\phi_p) f_i (\mathbf{x}_i - \phi_p)^\top \\
\bD &:= \sum_{i \in \texttt{Grid}} N_i(\phi_p)(\mathbf{x}_i - \phi_p)(\mathbf{x}_i - \phi_p)^\top \\
\end{aligned}
$$
where $\bD$ is the "Inertia" tensor (note how $N_i$ is like a mass distribution and $\br_i \br_i^\top$ is like the moment of inertia) and $\bB$ is the "Angular Momentum" tensor (note how $N_i$ is like a mass distribution, $f_i$ is like the velocity, and $\br_i$ is like the distance from the center of mass).

Thus, $\bA \bD = \bB$ and $\widehat{\nabla f_p} = \mathbf{B}\mathbf{D}^{-1}$.

# Lattice Boltzmann Method (LBM)
Previously, we have been solving the Eulerian fluid equations by directly discretizing the PDEs. The Lattice Boltzmann Method (LBM) simulates a mesoscopic[^3] statistical view of the fluid. 

[^3]: Mesoscopic means it is between the microscopic particle level and the macroscopic fluid level.

1. [[Continuum Mechanics]] is only a **macro**scopic model where the fluid is a continuous blob. Every point in space has one single, averaged velocity $\bu$. 
2. Molecular dynamics simulates every single fluid molecule bouncing off each other. One $\text{mol}$ of water is $10^{23}$ particles (computationally expensive!)
3. **Meso**scopic (statistical) dynamics tracks the probability of particles moving in certain directions at a given point in space instead of tracking one average velocity or many. 

The state of the system is a [[Probability Measure]] $f(\bx, \bv, t)$ over the [[Dual Space#Definition (Tangent Bundle)|tangent bundle]] $TW$. In particular, $f(\bx, \bv, t)$ is the probability density of a particle being at position $\bx$ and velocity $\bv$ at time $t$. With this, we can calculate:
- **The mass density**: 
    $$
    \rho_{(\bx, t)} = \int_{v \in T_{\bx}M} f(\bx, \bv, t)
    $$
- **The momentum density**:
    $$
    (\rho \bu)_{(\bx, t)} = \int_{v \in T_{\bx}W} \bv f(\bx, \bv, t)
    $$
- **Internal energy**:
    $$
    e_{(\bx, t)} = \int_{v \in T_{\bx}M} \frac{1}{2} \|\bv - \bu\|^2 f(\bx, \bv, t)
    = \frac{3kT_{\bx, t}}{2}
    $$
    where $T$ is the temperature and $k$ is the Boltzmann constant. 
- **Stress-energy tensor**:
    $$
    \Sigma_{(\bx, t)} = \int_{v \in T_{\bx}M} (\bv - \bu)(\bv - \bu)^\top f(\bx, \bv, t)
    $$
    
## Boltzmann Equation
The Boltzmann equation describes how the probability density $f$ evolves over time.
$$
\underbrace{
    \frac{\partial}{\partial t} f(\bx, \bv, t)
    + \bv \cdot f(\bx, \bv, t) 
    + \bg^{\text{ext}} \cdot \frac{\partial}{\partial \bv} f(\bx, \bv, t)
}_{\text{advection}}
= Q(f)_{(\bx, \bv, t)}
$$
The probability distribution is advected by its own velocity and external forces $\bg^{\text{ext}}$. The right hand side "can be"[^4] a pointwise operator $Q$ modeling the internal collision that mutates the distribution (obeying some conservation law). 

[^4]: The reason why it is "can be" is because it depends on the kind of fluid. For example, we could have a dilute fluid (like upper atmosphere) where the particles are so far apart that they almost never collide. Since collisions are statistically negligible, we can set $Q = 0$. Dense fluids will have a more complicated $Q$ that models the collisions.

Instead of particles moving in any direction, they are only allowed to move in a handful of fixed directions. This dramatically simplifies the computation required. 
- $f$ becomes discrete 
- Advection becomes a simple shift of the probability distribution along the lattice directions.
- Local collision runs $Q(f)$ on each node. 

```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}

% --- Color Definitions ---
\definecolor{lightgrey}{RGB}{200,200,200}
\definecolor{orangeorig}{RGB}{255,140,0}
\definecolor{redvec}{RGB}{153, 0, 0}
\definecolor{bluevec}{RGB}{51, 51, 255}
\definecolor{greenvec}{RGB}{30, 150, 30}

% --- Left Diagram: D2Q9 (2D) ---
\begin{scope}[shift={(0,0)}]
    % -- Grid Background --
    \draw[lightgrey, thick] (-2,-2) rectangle (2,2);
    \draw[lightgrey, thin] (-2,0) -- (2,0);
    \draw[lightgrey, thin] (0,-2) -- (0,2);

    % -- Vectors --
    % Red (axial)
    \draw[redvec,->,thick] (0,0) -- (2,0) node[right] {$c_1$};
    \draw[redvec,->,thick] (0,0) -- (0,2) node[above] {$c_2$};
    \draw[redvec,->,thick] (0,0) -- (-2,0) node[left] {$c_3$};
    \draw[redvec,->,thick] (0,0) -- (0,-2) node[below] {$c_4$};
    
    % Blue (diagonal)
    \draw[bluevec,->,thick] (0,0) -- (2,2) node[above right] {$c_5$};
    \draw[bluevec,->,thick] (0,0) -- (-2,2) node[above left] {$c_6$};
    \draw[bluevec,->,thick] (0,0) -- (-2,-2) node[below left] {$c_7$};
    \draw[bluevec,->,thick] (0,0) -- (2,-2) node[below right] {$c_8$};

    % -- Center Node (Drawn last for Z-index) --
    \fill[orangeorig] (0,0) circle (0.15);
    \node[anchor=north west, font=\large] at (0,0) {$c_0$};
\end{scope}

% --- Right Diagram: D3Q27 (3D) ---
% Using native TikZ isometric projection via customized x, y, z coordinate vectors
\begin{scope}[shift={(6,0)}, x={(1cm,0cm)}, y={(0cm,1cm)}, z={(-0.5cm,-0.4cm)}]
    \def\sc{2} % Scale boundary of the lattice

    % -- Box Background (Wireframe) --
    % Back face
    \draw[lightgrey] (-\sc,-\sc,-\sc) rectangle (\sc,\sc,-\sc);
    % Front face
    \draw[lightgrey] (-\sc,-\sc,\sc) rectangle (\sc,\sc,\sc);
    % Connecting edges
    \draw[lightgrey] (-\sc,-\sc,-\sc) -- (-\sc,-\sc,\sc);
    \draw[lightgrey] (\sc,-\sc,-\sc) -- (\sc,-\sc,\sc);
    \draw[lightgrey] (\sc,\sc,-\sc) -- (\sc,\sc,\sc);
    \draw[lightgrey] (-\sc,\sc,-\sc) -- (-\sc,\sc,\sc);

    % Internal subdivision lines (Midplanes)
    % XY plane at z=0
    \draw[lightgrey] (-\sc,0,-\sc) -- (\sc,0,-\sc);
    \draw[lightgrey] (-\sc,0,\sc) -- (\sc,0,\sc);
    \draw[lightgrey] (-\sc,-\sc,0) -- (-\sc,\sc,0);
    \draw[lightgrey] (\sc,-\sc,0) -- (\sc,\sc,0);
    \draw[lightgrey] (0,-\sc,-\sc) -- (0,\sc,-\sc);
    \draw[lightgrey] (0,-\sc,\sc) -- (0,\sc,\sc);

    % -- Vectors --
    % Red (Axial - 6 directions)
    \draw[redvec,->,thick] (0,0,0) -- (\sc,0,0) node[right] {$c_1$};
    \draw[redvec,->,thick] (0,0,0) -- (-\sc,0,0) node[left] {$c_2$};
    \draw[redvec,->,thick] (0,0,0) -- (0,\sc,0) node[above] {$c_3$};
    \draw[redvec,->,thick] (0,0,0) -- (0,-\sc,0) node[below] {$c_4$};
    \draw[redvec,->,thick] (0,0,0) -- (0,0,\sc) node[below left] {$c_5$};
    \draw[redvec,->,thick] (0,0,0) -- (0,0,-\sc) node[above right] {$c_6$};

    % Blue (Planar Diagonals - 12 directions)
    % XY Plane
    \draw[bluevec,->,thick] (0,0,0) -- (\sc,\sc,0) node[above right] {$c_7$};
    \draw[bluevec,->,thick] (0,0,0) -- (-\sc,\sc,0) node[above left] {$c_8$};
    \draw[bluevec,->,thick] (0,0,0) -- (-\sc,-\sc,0) node[below left] {$c_9$};
    \draw[bluevec,->,thick] (0,0,0) -- (\sc,-\sc,0) node[below right] {$c_{10}$};
    % XZ Plane
    \draw[bluevec,->,thick] (0,0,0) -- (\sc,0,\sc) node[right] {$c_{11}$};
    \draw[bluevec,->,thick] (0,0,0) -- (-\sc,0,\sc) node[left] {$c_{12}$};
    \draw[bluevec,->,thick] (0,0,0) -- (-\sc,0,-\sc) node[left] {$c_{13}$};
    \draw[bluevec,->,thick] (0,0,0) -- (\sc,0,-\sc) node[right] {$c_{14}$};
    % YZ Plane
    \draw[bluevec,->,thick] (0,0,0) -- (0,\sc,\sc) node[above] {$c_{15}$};
    \draw[bluevec,->,thick] (0,0,0) -- (0,\sc,-\sc) node[above] {$c_{16}$};
    \draw[bluevec,->,thick] (0,0,0) -- (0,-\sc,-\sc) node[below] {$c_{17}$};
    \draw[bluevec,->,thick] (0,0,0) -- (0,-\sc,\sc) node[below] {$c_{18}$};

    % Green (Volume Corners - 8 directions)
    \draw[greenvec,->,thick] (0,0,0) -- (\sc,\sc,\sc) node[above right] {$c_{19}$};
    \draw[greenvec,->,thick] (0,0,0) -- (-\sc,\sc,\sc) node[above left] {$c_{20}$};
    \draw[greenvec,->,thick] (0,0,0) -- (-\sc,-\sc,\sc) node[below left] {$c_{21}$};
    \draw[greenvec,->,thick] (0,0,0) -- (\sc,-\sc,\sc) node[below right] {$c_{22}$};
    \draw[greenvec,->,thick] (0,0,0) -- (\sc,\sc,-\sc) node[right] {$c_{23}$};
    \draw[greenvec,->,thick] (0,0,0) -- (-\sc,\sc,-\sc) node[left] {$c_{24}$};
    \draw[greenvec,->,thick] (0,0,0) -- (-\sc,-\sc,-\sc) node[left] {$c_{25}$};
    \draw[greenvec,->,thick] (0,0,0) -- (\sc,-\sc,-\sc) node[right] {$c_{26}$};

    % -- Center Node (Drawn last for Z-index) --
    \fill[orangeorig] (0,0,0) circle (0.15);
    \node[anchor=north west, font=\large] at (0,0,0) {$c_0$};
\end{scope}

\end{tikzpicture}
\end{document}
```

# Other Methods
- Vorticity is curl of velocity. Vortex lines are curves parallel to vorticity. 
- Vortex lines are transported in the Euler equation.
- One can reconstruct divergence-free velocity from the vorticity field (on simply-connected domains). 
- Simulations of fluid using this principle are called **vortex methods**. 
- When velocity is treated as 1-form (covector), it is also known as "impulse". They are Lie-transported in Euler fluids.
- They correspond to covector methods/impulse methods. 