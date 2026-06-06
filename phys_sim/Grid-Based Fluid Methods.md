---
tags:
  - CSE_291G
---
# Marker-and-Cell (MAC) Grid
We want to be able to simulate [[Continuum Mechanics]], and more specifically [[Fluid Mechanics]].

A crude and naive way to do is to split the world into a 3D grid of cells, labeled whether it is an obstacle, fluid, or empty space. The fluid velocity is defined on the cell wall. 
```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[scale=0.8, every node/.style={scale=1.0}]

% Grid lines
\draw (0,0) grid (8,8);

% Native TikZ mix colors (safest for Obsidian's dark mode SVG inversion)
\colorlet{lightgraycell}{black!35}
\colorlet{darkgraycell}{black!70}

% --- Shading and Text for Cells ---

% Row 1 (top, y=7 to y=8)
\foreach \x in {0,...,7} {
    \fill[white] (\x,7) rectangle (\x+1,8);
    \node at (\x+0.5,7.5) [font=\huge] {E};
}

% Row 2 (y=6 to y=7)
\fill[white] (0,6) rectangle (1,7); \node at (0.5,6.5) [font=\huge] {E};
\fill[lightgraycell] (1,6) rectangle (2,7); \node at (1.5,6.5) [font=\huge\bfseries] {F};
\foreach \x in {2,...,7} {
    \fill[white] (\x,6) rectangle (\x+1,7);
    \node at (\x+0.5,6.5) [font=\huge] {E};
}

% Row 3 (y=5 to y=6)
\fill[darkgraycell] (0,5) rectangle (1,6); \node at (0.5,5.5) [font=\huge, text=white] {S};
\fill[white] (1,5) rectangle (2,6); \node at (1.5,5.5) [font=\huge] {E};
\fill[white] (2,5) rectangle (3,6); \node at (2.5,5.5) [font=\huge] {E};
\fill[lightgraycell] (3,5) rectangle (4,6); \node at (3.5,5.5) [font=\huge\bfseries] {F};
\fill[lightgraycell] (4,5) rectangle (5,6); \node at (4.5,5.5) [font=\huge\bfseries] {F};
\fill[white] (5,5) rectangle (6,6); \node at (5.5,5.5) [font=\huge] {E};
\fill[white] (6,5) rectangle (7,6); \node at (6.5,5.5) [font=\huge] {E};
\fill[darkgraycell] (7,5) rectangle (8,6); \node at (7.5,5.5) [font=\huge, text=white] {S};

% Row 4 (y=4 to y=5)
\fill[darkgraycell] (0,4) rectangle (1,5); \node at (0.5,4.5) [font=\huge, text=white] {S};
\fill[white] (1,4) rectangle (2,5); \node at (1.5,4.5) [font=\huge] {E};
\fill[white] (2,4) rectangle (3,5); \node at (2.5,4.5) [font=\huge] {E};
\fill[white] (3,4) rectangle (4,5); \node at (3.5,4.5) [font=\huge] {E};
\fill[lightgraycell] (4,4) rectangle (5,5); \node at (4.5,4.5) [font=\huge\bfseries] {F};
\fill[lightgraycell] (5,4) rectangle (6,5); \node at (5.5,4.5) [font=\huge\bfseries] {F};
\fill[lightgraycell] (6,4) rectangle (7,5); \node at (6.5,4.5) [font=\huge\bfseries] {F};
\fill[darkgraycell] (7,4) rectangle (8,5); \node at (7.5,4.5) [font=\huge, text=white] {S};

% Row 5 (y=3 to y=4)
\fill[darkgraycell] (0,3) rectangle (1,4); \node at (0.5,3.5) [font=\huge, text=white] {S};
\fill[white] (1,3) rectangle (2,4); \node at (1.5,3.5) [font=\huge] {E};
\foreach \x in {2,...,6} {
    \fill[lightgraycell] (\x,3) rectangle (\x+1,4);
    \node at (\x+0.5,3.5) [font=\huge\bfseries] {F};
}
\fill[darkgraycell] (7,3) rectangle (8,4); \node at (7.5,3.5) [font=\huge, text=white] {S};

% Row 6 (y=2 to y=3)
\fill[darkgraycell] (0,2) rectangle (1,3); \node at (0.5,2.5) [font=\huge, text=white] {S};
\foreach \x in {1,...,5} {
    \fill[lightgraycell] (\x,2) rectangle (\x+1,3);
    \node at (\x+0.5,2.5) [font=\huge\bfseries] {F};
}
\fill[darkgraycell] (6,2) rectangle (7,3); \node at (6.5,2.5) [font=\huge, text=white] {S};
\fill[darkgraycell] (7,2) rectangle (8,3); \node at (7.5,2.5) [font=\huge, text=white] {S};

% Row 7 (y=1 to y=2)
\fill[darkgraycell] (0,1) rectangle (1,2); \node at (0.5,1.5) [font=\huge, text=white] {S};
\foreach \x in {1,...,3} {
    \fill[lightgraycell] (\x,1) rectangle (\x+1,2);
    \node at (\x+0.5,1.5) [font=\huge\bfseries] {F};
}
\foreach \x in {4,...,7} {
    \fill[darkgraycell] (\x,1) rectangle (\x+1,2);
    \node at (\x+0.5,1.5) [font=\huge, text=white] {S};
}

% Row 8 (bottom, y=0 to y=1)
\foreach \x in {0,...,7} {
    \fill[darkgraycell] (\x,0) rectangle (\x+1,1);
    \node at (\x+0.5,0.5) [font=\huge, text=white] {S};
}

% Draw border around the entire grid last for clean look
\draw[ultra thick] (0,0) rectangle (8,8);

\end{tikzpicture}
\end{document}
```

The fluid velocity has 3 components 
$$
\bu = (u^1, u^2, u^3)
$$
like 3 scalar fields, with $u^1$ defined on the faces normal to the $x-$direction (and similarly with the other two). Velocity on a wall next to a solid cell must be $0$. 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, line join=round, line cap=round, 
                    x={(1.3cm,0cm)}, y={(0cm,1.3cm)}, z={(0.6cm,0.45cm)}]

% --- Define Custom Colors Matching the Image ---
\definecolor{myblue}{RGB}{35, 75, 165}
\definecolor{fillblue}{RGB}{145, 175, 215}

\definecolor{myorange}{RGB}{200, 60, 15}
\definecolor{fillorange}{RGB}{240, 155, 115}

\definecolor{myteal}{RGB}{40, 145, 130}
\definecolor{fillteal}{RGB}{160, 215, 200}

% =========================================================
% BACKGROUND GRIDS (Solid Lines)
% =========================================================

% Top Face Grid
\foreach \x in {0,...,4} {
    \draw[thick] (\x, 4, 0) -- (\x, 4, 3);
}
\foreach \z in {0,...,3} {
    \draw[thick] (0, 4, \z) -- (4, 4, \z);
}

% Right Face Grid
\foreach \y in {0,...,4} {
    \draw[thick] (4, \y, 0) -- (4, \y, 3);
}
\foreach \z in {0,...,3} {
    \draw[thick] (4, 0, \z) -- (4, 4, \z);
}

% =========================================================
% INTERNAL GRIDS (Dashed Lines)
% =========================================================

% Internal Dashed Grid at z=1 (Back of the first cell layer)
\foreach \x in {1,...,3} {
    \draw[thick, dashed] (\x, 0, 1) -- (\x, 4, 1);
}
\foreach \y in {1,...,3} {
    \draw[thick, dashed] (0, \y, 1) -- (4, \y, 1);
}

% Depth Dashed Lines (z=0 to z=1)
% Interior depth lines
\foreach \x in {1,...,3} {
    \foreach \y in {1,...,3} {
        \draw[thick, dashed] (\x, \y, 0) -- (\x, \y, 1);
    }
}
% Left edge depth lines
\foreach \y in {1,...,3} {
    \draw[thick, dashed] (0, \y, 0) -- (0, \y, 1);
}
% Bottom edge depth lines
\foreach \x in {1,...,3} {
    \draw[thick, dashed] (\x, 0, 0) -- (\x, 0, 1);
}

% =========================================================
% STAGGERED GRID FACES (Colored Fills)
% =========================================================

% u3 (Blue) - Front face (y=2..3, x=0..1, z=0)
\fill[fillblue, fill opacity=0.8] (0,2,0) -- (1,2,0) -- (1,3,0) -- (0,3,0) -- cycle;

% u1 (Orange) - Right side face (y=2..3, x=2, z=0..1)
\fill[fillorange, fill opacity=0.8] (2,2,0) -- (2,3,0) -- (2,3,1) -- (2,2,1) -- cycle;

% u2 (Teal) - Top side face (y=2, x=2..3, z=0..1)
\fill[fillteal, fill opacity=0.8] (2,2,0) -- (3,2,0) -- (3,2,1) -- (2,2,1) -- cycle;

% =========================================================
% FRONT GRID (Solid Lines)
% =========================================================

\foreach \x in {0,...,4} {
    \draw[thick] (\x, 0, 0) -- (\x, 4, 0);
}
\foreach \y in {0,...,4} {
    \draw[thick] (0, \y, 0) -- (4, \y, 0);
}

% =========================================================
% COLORED BORDERS (Drawn over front grid for visibility)
% =========================================================

\draw[myblue, dashed, very thick] (0,2,0) -- (1,2,0) -- (1,3,0) -- (0,3,0) -- cycle;
\draw[myorange, dashed, very thick] (2,2,0) -- (2,3,0) -- (2,3,1) -- (2,2,1) -- cycle;
\draw[myteal, dashed, very thick] (2,2,0) -- (3,2,0) -- (3,2,1) -- (2,2,1) -- cycle;

% =========================================================
% CELL CENTERS (Black Dots)
% =========================================================

\foreach \x in {0.5, 1.5, 2.5, 3.5} {
    \foreach \y in {0.5, 1.5, 2.5, 3.5} {
        \fill (\x, \y, 0.5) circle (4pt);
    }
}

% =========================================================
% LABELS
% =========================================================

\node[font=\Huge, text=myblue] at (-0.4, 2.5, 0) {$u^3$};
\node[font=\Huge, text=myorange] at (1.8, 4.3, 0) {$u^1$};
\node[font=\Huge, text=myteal] at (3.5, 2.3, 0.5) {$u^2$};

\end{tikzpicture}
\end{document}
```

- Let $\mathcal{F}$ denote the set of faces incident to both fluid cells.
- Let $\mathcal{C}$ denote the set of fluid cells. 
- Velocity field is a data $\bu \in \R^\mathcal{F}$.
- Scalar quantities like pressure and density are stored at cell center. 

The divergence of the velocity field is defined on fluid cells
$$
q = \text{div } \bu \in \R^\mathcal{C}
$$
where $\text{div} : \R^{\mathcal{F}} \to \R^{\mathcal{C}}$ (a $|\mathcal{C}| \times |\mathcal{F}|$ sparse matrix) is defined by aggregating the total flux from each cell wall. 

## Pressure Projection 
Given non divergence free $\tilde{\bu} \in \R^{\mathcal{F}}$, (some velocity field generated without respect to pressure), we need to try and project it to $\text{ker}(\text{div}) \subset \R^{\mathcal{F}}$. The idea here is that $\text{ker}(\text{div})$ consists of all velocity fields with exactly zero divergence. The goal of the algorithm is to find the closest valid vector in this subspace to our invalid input vector $\tilde \bu$. 

> [!faq] Idea
> This is mathematically the least-squares projection problem. Again, treat $\text{div}$ as a linear operator (matrix). 

We want to solve for pressure $p \in \R^{\mathcal{C}}$ where 
$$
\bu = \tilde\bu - \text{div}^\top p
$$
and $\text{div } \bu = 0$ (to satisfy incompressibility). Mathematically this means we need to find a $p$ where 
$$
\begin{aligned}
\bu &= \tilde\bu - \text{div}^\top p \\ 
\text{div } \bu &= \text{div}(\tilde\bu - \text{div}^\top p) \\
0 &= \text{div } \tilde\bu - \text{div}\text{div}^\top p \\ 
\text{div}\text{div}^\top p &= \text{div }\tilde\bu
\end{aligned}
$$
Note that $\text{div}^\top : \R^{\mathcal{C}} \to \R^{\mathcal{F}}$ is a discrete (negative) gradient operator. So, solving this system is the same as finding $Ax = b$ where 
$$
\underbrace{\text{div}\text{div}^\top}_{A} \,p = \underbrace{\text{div } \tilde\bu}_{b}
$$
and $x := p$. We can also see that the matrix $\text{div}\text{div}^\top \in \R^{|\mathcal{C}| \times |\mathcal{C}|}$ is a discrete [[Laplacian Matrix|Laplacian]]. Fortunately, this means we can solve this by any linear algebra routine such as *conjugate gradient*. 

## Applying FFT (Spectral Method)
If the domain has a **simple periodic boundary condition**, then we can use the Fast [[Fourier Series|Fourier]] Transform (FFT) to turn this system into a diagonalized equation with direct solution.

For a fluid to have a simple periodic boundary condition, it means a fluid flows out one side of some volume (like a cube) and flows in seamlessly on the left[^1].

[^1]: Like in PacMan!

Let $(L_1, L_2, L_3)$ be the tuple that describes the "size" of the periodic domain. The goal is to solve the Poisson problem $\Delta \bu = f$[^2] such that 
$$
\frac{\del^2 \bu}{\del x^2} + \frac{\del^2 \bu}{\del y^2} + \frac{\del^2 \bu}{\del z^2} = f
$$

[^2] $\Delta$ is actually the Laplacian operator, the continuous equivalent of the discrete $\text{div}\text{div}^\top$ matrix!

We will discretize both $\bu$ and $f$ on a regular grid with resolution $(N_1, N_2, N_3)$. Then apply FFT:
$$
\begin{aligned}
u(j_1, j_2, j_3) &= \frac{1}{N_1 N_2 N_3} \sum_{k_1 = 0}^{N_1 - 1} \sum_{k_2 = 0}^{N_2 - 1} \sum_{k_3 = 0}^{N_3 - 1} 
    \hat{u}(k_1, k_2, k_3) \exp\left(
        2\pi i \left( \frac{j_1 k_1}{N_1} + \frac{j_2 k_2}{N_2} + \frac{j_3 k_3}{N_3} \right)
    \right) \\
    % 
\hat{u}(k_1, k_2, k_3) &= \sum_{j_1 = 0}^{N_1 - 1} \sum_{j_2 = 0}^{N_2 - 1} \sum_{j_3 = 0}^{N_3 - 1} 
    u(j_1, j_2, j_3) \exp\left(
        -2\pi i \left( \frac{j_1 k_1}{N_1} + \frac{j_2 k_2}{N_2} + \frac{j_3 k_3}{N_3} \right)
    \right)
\end{aligned}
$$
where $j_1, j_2, j_3$ represent the individual grid cells and $k_1, k_2, k_3$ represent the individual frequencies. Recall that $\bu, f$ represent variables in the spatial domain and $\hat{\bu}, \hat{f}$ represent variables in the frequency domain.

This is fast because we can represent the pressure field as a linear combination of [[Fourier Series|Fourier]] basis functions. More simply, image $\bu$ is the sum of one wave, $\bu = e^{ikx}$ where $x$ is the position in space and $k$ is the frequency of the wave. The derivative of $\bu$ is $\frac{\del}{\del x} \bu = ik e^{ikx}$, making this operation on a computer much easier. 

Since the simulation exists on a discrete grid of fixed pixels, we need to prevent aliasing[^2] via the following definition of $p_1$:
$$
\widehat{\frac{\del}{\del x}\bu(k)} = p_1 \hat{\bu}(k), \quad 
p_1 = \begin{cases}
    2\pi i \frac{k_1}{L_1} & 0 \leq k_1 < N_1/2 \\
    0 & k_1 = N_1/2 \\
    2\pi i \frac{k_1 - N_1}{L_1} & N_1/2 < k_1 < N_1
\end{cases}
$$

[^2]: This is a term from computer graphics. It refers to the phenomenon where high-frequency signals are misinterpreted as low-frequency signals when sampled at a discrete rate.

There are two distinct subspaces that our final velocity field $\bu$ can exist in
1. The subspace of all possible velocity fields where the fluid is perfectly incompressible everywhere (i.e. $\text{div } \bu = 0$). 
2. The subspace of all possible velocity fields where the fluid inside and immediately on the boundary of the solid obstacle is completely stationary (i.e. $\bu = 0$).

The solver finds the intersection of both. The alternating projection (pressure project $\to$ set velocity to zero by enforcing obstacles) will converge to their intersection. 

### Obstacles
If we want to add obstacles, we can just do [[#Pressure Projection]] and set velocity in the obstacle to zero. 

## Time Splitting 
Consider the [[Euler Arnold Equations#Background|incompressible fluid Euler equation]]:
$$
\left\{
\begin{aligned}
\frac{\del \bu}{\del t} + \bu \cdot \nabla \bu &= -\nabla p \\
\nabla \cdot \bu &= 0
\end{aligned}
\right.
$$

### Projection Method (Chorin)
For each time step, we will 
1. solve the advection term (for half timestep):
    $$
    \frac{\del \bu}{\del t} + \nabla_{\bu} \bu = 0
    $$
2. pressure "reflect"
    $$
    \bu \leftarrow \bu - \nabla \Delta^{-1} \nabla \cdot \bu
    $$

Because we advected the fluid while ignoring pressure, the fluid followed the wrong trajectory for that entire $\Delta t$. Projecting it straight back down does not return it to where it would have been if pressure had been applied continuously.

### Reflection Method (Strang)
We can solve this by: for each time step, we will 
1. solve the advection term (for half timestep):
    $$
    \frac{\del \bu}{\del t} + \nabla_{\bu} \bu = 0
    $$
2. pressure "reflect"
    $$
    \begin{aligned}
    \bu^* &= \bu - \nabla \Delta^{-1} \nabla \cdot \bu \\
    \bu &\leftarrow 2\bu^* - \bu
    \end{aligned}
    $$
    This reflection across the div-free subspace allows you to push the fluid further along the correct trajectory (via the advection step) before projecting it back down to the div-free subspace.
3. solve the advection equation (for half timestep):
    $$
    \frac{\del \bu}{\del t} + \nabla_{\bu} \bu = 0
    $$
4. pressure project 

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]

% --- Define Custom Colors ---
\definecolor{myteal}{RGB}{85, 175, 155}
\definecolor{mypurple}{RGB}{125, 80, 165}

% =========================================================
% TOP SECTION (Standard Projection)
% =========================================================

% Horizontal Line (div-free subspace)
\draw[line width=1.8pt] (0, 4) -- (6.8, 4) node[right, font=\large, text=black] {div-free subspace};

% Teal Curved Arrow (Solve)
\draw[->, myteal, line width=1.5pt] (0.5, 4) to[out=45, in=190] (3.8, 5.8);

% Teal Text Label
\node[myteal, align=left, font=\large, anchor=west] at (-1.2, 5.0) {Solve\\[0.5ex] $\frac{\partial \mathbf{u}}{\partial t} + \nabla_{\mathbf{u}}\mathbf{u} = 0$};

% Purple Straight Arrow (Projection)
\draw[->, mypurple, line width=1.5pt] (3.8, 5.7) -- (3.8, 4.05);

% Purple Text Label
\node[mypurple, align=left, font=\large, anchor=west] at (4.0, 4.9) {Pressure\\[0.3ex] projection};


% =========================================================
% BOTTOM SECTION (Higher-order / Reflection)
% =========================================================

% Horizontal Line (div-free subspace)
\draw[line width=1.8pt] (0, 0) -- (6.8, 0) node[right, font=\large, text=black] {div-free subspace};

% 1. Teal Curved Arrow (Solve)
\draw[->, myteal, line width=1.5pt] (0.5, 0) to[out=45, in=190] (2.2, 1.5);

% Teal Text Label
\node[myteal, align=left, font=\large, anchor=west] at (-1.2, 1.0) {Solve\\[0.5ex] $\frac{\partial \mathbf{u}}{\partial t} + \nabla_{\mathbf{u}}\mathbf{u} = 0$};

% 2. Purple Straight Arrow (Reflection - crosses line)
\draw[->, mypurple, line width=1.5pt] (2.2, 1.4) -- (2.2, -1.5);

% Purple Text Label (Reflection)
\node[mypurple, align=left, font=\large, anchor=west] at (2.4, 0.8) {Pressure\\[0.3ex] reflection};

% 3. Teal Curved Arrow (Returning from below)
\draw[->, myteal, line width=1.5pt] (2.2, -1.4) to[out=40, in=190] (4.4, 0.6);

% 4. Purple Straight Arrow (Final Projection)
\draw[->, mypurple, line width=1.5pt] (4.4, 0.5) -- (4.4, 0.05);

% Purple Text Label (Projection)
\node[mypurple, align=left, font=\large, anchor=west] at (4.6, 0.6) {Pressure\\[0.3ex] projection};

\node[align=left, font=\large\bfseries, text=black, anchor=north west] at (4.8, -0.5) {Less splitting error\\[0.3ex] with little additional cost};

\end{tikzpicture}
\end{document}
```

## Advection
Let $\bv$ be a time-independent vector field over the world coordinate $W$. A time dependent scalar function $f$ is **advected** by $\bv$ if 
$$
\frac{\del}{\del t} f + \bv \cdot \nabla f = 0
\quad\text{ or }\quad
\frac{\del}{\del t} f + df \llbracket \bv \rrbracket = 0
\quad\text{ or }\quad
\frac{\del}{\del t} f + \mathscr{L}_\bv f = 0
$$
where $\mathscr{L}_\bv$ is the **Lie Derivative**. Equivalently, if $\varphi_t : W \to W$ is the flow map generated by $\bv$ ($\dot\varphi = \bv \circ \varphi$ and $\varphi_{0} = \text{id}_{W}$) and let $\psi_t := \varphi_t^{-1}$ (inverse flow map), then an advected function satisfies
$$
f_t (\varphi_t (X)) = f_0 (X)
\quad\text{ or }\quad
f_t (x) = f_0(\psi_t(x))
$$
In other words, tracing the flow with $\psi_{t}$ allows us to see where the fluid originally came from. We can convert this to the language of pullbacks.
$$
\begin{aligned}
f_t (\varphi_t (X)) = f_0 (X) & \longrightarrow f_0 = \varphi_t^* f_t \\ 
f_t (x) = f_0(\psi_t(x)) & \longrightarrow f_t = \psi_t^* f_0 \\
\end{aligned}
$$
In fact, 
$$
\varphi_t^* = \exp(t \mathscr{L}_\bv)
\quad\text{ and }\quad
\psi_t^* = \exp(-t \mathscr{L}_\bv)
$$
connecting continuous geometry (the pullback) to discrete numerical methods (the $t$). 

We have two numerical methods for advection.
1. **Eulerian method**: approximate the $\exp(\text{derivative})$ or the pullback operator
2. **Lagrangian method**: set quantites on particles (or other geometry) and let the particle move by $\bv$.

# 1D Advection of a Function
Suppose we have an advection equation with [[Continuum Mechanics#Definition (Flow Velocity)|flow velocity]] $a = a(x)$. 
$$
\frac{\del}{\del t} u(t, x) + a\frac{\del}{\del x} u(t, x) = 0
\quad\text{ or }\quad
\dot u + a u' = 0
$$
Let $u_i^n$ denote the approximate solution at the $i-$th gridpoint and $n-$th timestep. 

## Aside: Von Neumann Stability Analysis
We can analyze the stability of a numerical method by looking at how it amplifies or dampens perfect continuous sine waves $r^n \exp(ikx)$. The scaling factor is $r \in \C$. If $|r| > 1$, the wave amplifies and the method is unstable. If $|r| < 1$, the wave dampens and the method is stable. If $|r| = 1$, the wave is preserved and the method is neutrally stable.

## Central Difference Method
A straightforward approach is to look at the neighboring cells to find the slope. We then step forward in time by $\Delta t$ using the formula
$$
u_i^{n+1} = u_i^n - \frac{a \Delta t}{\Delta x} (u_{i+1}^n - u_{i-1}^n)
$$
We can apply [[#Aside Von Neumann Stability Analysis|Von Neumann Stability Analysis]]. Let $u_i^n = r^n \exp(\bi kx)$. Then we get that 
$$
r = 1 - \bi \frac{a \Delta t}{\Delta x} \sin(k)
$$
Because its magnitude is greater than 1, this method is **unconditionally unstable**, meaning no matter how small we make $\Delta t$, the method will always explode.

## Using [[Ordinary Differential Equation|ODE]] Solvers
We can rewrite the advection equation as an [[Ordinary Differential Equation|ODE]] by treating $x$ as a parameter.
$$
\frac{d}{dt} u_i = -\frac{a}{2\Delta x} (u_{i+1} - u_{i-1})
$$
This equation can still be stable using [[Ordinary Differential Equation|ODE]] solvers like [[#Runge-Kutta Method (RK4)]] or [[#Forward Euler Method]] or [[#Backward Euler Method]]. 

But this leaves us with some [[Taylor's Theorem|Taylor expansion]] errors since we will try to approximate a continuos function on discrete grid points. We must analyze the modified euquation to see what errors we are making. For example, the central difference method generates
$$
\dot u = -au' - \underbrace{\frac{\Delta x^2}{12} au'''}_{\substack{\text{numerical} \\ \text{dispersion}}}
$$
The numerical dispersion term means waves of different frequencies will travel at different speeds, and cause rippling near sharp corners (like in a square wave).

## Lax-Friedrichs Method
One quick fix to the central difference method is to stop using the current cell value, and instead take the average of its left and right neighbors. This gives us the following update rule:
$$
u_i^{n+1} = \frac{1}{2}\left(u_{i-1}^n + u_{i+1}^n\right) 
- \frac{a \Delta t}{2\Delta x} \left(u_{i+1}^n - u_{i-1}^n\right)
$$
Using Von Neumann Stability Analysis, we can find that
$$
r = \cos(k) - \bi \frac{a \Delta t}{\Delta x} \sin(k)
$$
It is stable iff 
$$
\bigg| \frac{a \Delta t}{\Delta x} \bigg| \leq 1
$$
and so it is conditionally stable. We get the modified equation:
$$
\dot u = -au' + \underbrace{\frac{\Delta x^2}{2} u''}_{\substack{\text{numerical} \\ \text{diffusion}}}
$$
The average injects an artificial diffusion term, which causes the solution to blur over time.

## Upwind Method
Recall the $\dot u + au' = 0$ equation. The **Upwind Method** examines how $a$, the transport coefficient, changes sign.
$$
u_i^{n+1} = 
\left\{
\begin{aligned}
u_i^n - \frac{a \Delta t}{\Delta x} (u_i^n - u_{i-1}^n) &\quad\quad a > 0 \\
u_i^n - \frac{a \Delta t}{\Delta x} (u_{i+1}^n - u_i^n) &\quad\quad a < 0 
\end{aligned}
\right.
$$
This is stable iff
$$
\bigg| \frac{a \Delta t}{\Delta x} \bigg| \leq 1
$$
It is conditionally stable. The modified equation is
$$
\dot u = -au' + \underbrace{\frac{\Delta x}{2} u''}_{\substack{\text{numerical} \\ \text{diffusion}}}
$$
The numerical diffusion is better than Lax-Friedrichs. 

## Courant-Friedrichs-Lewy (CFL) Condition
The CFL condition ensures [[#Lax-Friedrichs Method]] and [[#Upwind Method]] are *conditionally stable*. They only work if 
$$
\bigg| \frac{a \Delta t}{\Delta x} \bigg| \leq 1
$$
To understand this physically,
1. $a \Delta t$ is the actual physical distance the fluid travels in one time step.
2. $\Delta x$ is the physical width of one grid cell. 

The CFL condition is a strict speed limit: **the fluid cannot travel more than one grid cell per time step**.

## Semi-Lagrangian Scheme
Consider again the advection equation $\dot u + au' = 0$. Sometimes we want a larger time step. We can do this by tracing the flow backwards in time.
$$
u_i^{n+1} = u^{n}(x_i - a \Delta t)
$$
How it works:
1. Stand at the current grid cell center $x_i$.
2. Trace a trajectory backwards in time by $\Delta t$ seconds.
3. Arrive at the physical location $\psi_{\Delta t} (x_i) = x_i - a \Delta t$.
4. The starting location will almost certainly not land perfectly on a grid cell center, so interpolate the values of the surrounding grid cells to estimate the fluid data at that exact continuous coordinate. 
5. Copy that value into the current grid cell.

This method is **unconditionally stable**. The modified equation is the same as the [[#Upwind Method]]. 

# nD Advection of a Function
The advection equation is now 
$$
\dot f + \mathscr{L}_\bv f = 0
$$
We want to approximate
$$
f^{n+1} = \psi_{\Delta t}^* f^n
$$
The Semi-Lagrangian scheme is somewhat the same. For scalar functions, we use 
$$
f_i^{n+1} = \text{Interpolate}(f^n, x_i - \Delta t \bv_i)
$$
In 1D, interpolation is simple between two points. In 2D, we need interpolate the surronding 4 grid cells (pixels). In 3D, we need to interpolate the surrounding 8 grid cells (voxels).

Let us call **one semi-Lagrangian step** as $f^{n+1} - \mathscr{A}^{\text{sL}}_{\bv, \Delta t} (f^n)$. By combining multiple semi-Lagrangian steps, we can bootstrap a higher order method. 

## Back-and-Forth Error Correction and Compensation (BFECC)
How can we remove the blur caused by the $u''$ term if the grid fundamentally requires interpolation? The idea is to trick the grid into calculating its own error and then compensate (subtract) for it.
$$
\mathscr{A}^{\text{BFECC}}_{\bv, \Delta t} 
:= 
\underbrace{\mathscr{A}^{\text{sL}}_{\bv, \Delta t}}_{ f^* }
- \left( \mathscr{A}^{\text{sL}}_{\bv, \Delta t} \right) \frac{1}{2} 
    \left( 
        \underbrace{\mathscr{A}_{-\bv, \Delta t}^{\text{sL}} \circ \mathscr{A}^{\text{sL}}_{\bv, \Delta t}}_{
            f^{**}
        }
        - 1
    \right)
$$
Here, we are calculating the forward step via $f^*$, and then finding the backward step by applying the opposite velocity $-\bv$ to $f^*$ giving us $f^{**}$. The remaining term is the error, which we take the semi-Lagrangian step of and subtract from $f^*$. Indeed, 
$$
f^{\text{final}} = f^* - \mathscr{A}^{\text{sL}}_{\bv, \Delta t} 
\;
    \underbrace{
        \left( 
        \frac{f^{**} - f}{2}
        \right)
    }_{\text{error}}
$$
The tradeoff is that we remove numerical dissipation (blurring) but we get some numerical dispersion (spatial oscillation). We can detect and cutoff overshoots using a **limiter**. 

> [!idea] Limiter
> If the value of the field after BFECC is lying outside some convex hull of the neighborhood values of stable semi-Lagrangian, blend with or use the stable semi-Lagrangian result. 

```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.1]

% =================================================
% LEFT PLOT: Numerical Dissipation
% =================================================
\begin{scope}[shift={(0,0)}]
    % Solid square wave
    \draw[thick] (0,1) -- (2.0,1) -- (2.0,4) -- (3.3,4) -- (3.3,1) -- (5.5,1);

    % Dashed smoothed wave (Dissipation)
    % Uses bezier curves centered perfectly on the jumps (x=2.0 and x=3.3)
    \draw[thick, dashed] (0,1) -- (1.6,1) 
        .. controls (2.0,1) and (2.0,4) .. (2.4,4) 
        -- (2.9,4) 
        .. controls (3.3,4) and (3.3,1) .. (3.7,1) 
        -- (5.5,1);

    % Label
    \node[font=\large] at (2.75, 0) {numerical dissipation};
\end{scope}

% =================================================
% RIGHT PLOT: Numerical Dispersion
% =================================================
\begin{scope}[shift={(6.5,0)}]
    % Solid square wave (drawn thin to match reference)
    \draw[thin] (0,1) -- (2.0,1) -- (2.0,4) -- (3.3,4) -- (3.3,1) -- (5.5,1);

    % Blue dispersed wave with dots (Ringing/Gibbs phenomenon)
    % Coordinates are hardcoded to safely bypass compiler loop issues while mimicking the oscillations
    \draw[blue, thick, mark=*, mark size=1.5pt] plot coordinates {
        (0,1) (0.15,1) (0.3,1) (0.45,1) (0.6,1) (0.75,1) (0.9,1) (1.05,1) (1.2,1) (1.35,1)
        (1.45, 0.98) (1.55, 1.05) (1.65, 0.9) (1.75, 1.2) (1.85, 0.6) (1.95, 1.5)
        (2.05, 3.5) (2.15, 3.9) (2.25, 4.05) (2.35, 3.9) (2.45, 4.1) (2.55, 3.85) 
        (2.65, 4.0) (2.75, 4.1) (2.85, 3.9) (2.95, 4.4) (3.05, 3.75) (3.15, 4.1) (3.25, 3.9)
        (3.35, 1.5) (3.45, 0.4) (3.55, 1.3) (3.65, 0.8) (3.75, 1.1) (3.85, 0.95) (3.95, 1.02)
        (4.05, 1) (4.2, 1) (4.35, 1) (4.5, 1) (4.65, 1) (4.8, 1) (4.95, 1) (5.1, 1) (5.25, 1) (5.4, 1) (5.5, 1)
    };

    % Label
    \node[font=\large] at (2.75, 0) {numerical dispersion};
\end{scope}

\end{tikzpicture}
\end{document}
```

