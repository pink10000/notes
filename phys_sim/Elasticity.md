---
tags:
  - CSE_291G
---
# Postulates
1. The position of the body is described by 
	1. a (time-dependent) map $\phi: M \to W$, 
	2. where $M$ has a time-independent mass density $\rho_M \in \Omega^n(M)$ and 
	3. $W$ has a time-independent metric $\flat_W \in \Gamma(T^*W \odot T^*W)$.
		1. It is a covariant symmetric 2-tensor, with 2 open covector slots. 
		2. Physically, it is just the dot product. 
2. The elastic potential energy for a map $\phi$ takes the form:
   $$
   \mathcal{U}(\phi) = \int_M U(\phi^* \flat_W)
   $$
   for some fiber-wise (nonlinear) mapping (depending on material) 
   $$
   U_p: T_p^*M \odot T_p^*M \xrightarrow{\text{nonlinear}} \bigwedge^n T_p^*M
   $$
   i.e. the potential is only a function of the induced metric encoding its notion of distances in the world. (**Frame-indifference**)

# Terminology
The **deformation gradient** is defined by the [[Dual Space#Definition (Pushforward Operator)|pushforward]] $F$:
$$
F := \phi_{*} = d\phi \in \Gamma(T^{*}M \otimes T_{\phi}W)
$$
In index notation, it is $F_{\alpha}^{i} = \del_{\alpha} \phi^{i}$. If $U \in T_{x}M$ (a material tangent vector) then $F(U) = \sum_{\alpha} F_{\alpha}^{i} U^{\alpha}$. We can think of $i$ as a row index and $\alpha$ as a column index, such that $F$ pushes it forward via matrix multiplication.

> [!idea] Idea
> $F$ is a linear map (since it lives in the bundle over a tensor algebra) that "eats" a material vector and spits out a world vector. 

Since we want a measurement tool for material space $M$ (to measure deformation without having to constantly reference the world space $W$), we need to pullback. Indeed, the [[Dual Space#Definition (Adjoint Linear Map)|adjoint]] $F^{*}$ is the pullback. 

The induced metric $\phi^* \flat_W$ can be understood by:
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
The induced metric $C := F^* \flat_W F \in \Gamma(T^*M \odot T^*M)$ is called the **(right)-Cauchy-Green tensor**. 

> [!info] Understanding the Diagram: How to Measure Deformed Length
> The diagram illustrates how the Cauchy-Green tensor $C$ operates by composing three separate maps:
> 1. **$F$ (Deformation Gradient):** We start with a small undeformed vector in the material tangent space $T_p M$. $F$ pushes this vector forward into the physical world $W$, telling us what the deformed vector looks like in the spatial tangent space $T_{\phi(p)} W$.
> 2. **$\flat_W$ (World Metric):** Once in the physical world, you use the standard metric $\flat_W$ to measure its length (or compute the dot product with another vector). This mathematically "lowers the index", mapping the spatial vector to a spatial covector in $T_{\phi(p)}^* W$.
> 3. **$F^*$ (Pullback):** Finally, the adjoint $F^*$ pulls that measurement result back to the material covector space $T_p^* M$.
> 
> By taking the direct dashed path $C = F^* \flat_W F$, we skip the intermediate steps. $C$ acts as an "induced metric" living entirely in the undeformed material space. If we feed $C$ two undeformed material vectors, it instantly outputs what their dot product *will be* after they are stretched and twisted into the physical world.

> [!info] Another Perspective
> Another way to think about this is, suppose we had $X,Y \in T_{p}M$, two infinitesimal material vectors. We want to build a machine (tesnor) that lives entirely in $M$, but want to measure the dot product of $X,Y$ after deformation in world space $W$.
> 
> Let us call this machine $C$, where $C(X, Y) = \text{deformed dot product}$. The dot product, represents the distance/length/angle of the two material vectors. 
> 
> First, we simulate deformation. Then we measure them. 
> $$
> \begin{aligned}
> C(X, Y) 
> &:= \flat_{W}(FX, FY) \\
> &= \flat_{W}(\phi_{*} X, \phi_{*} Y) \\
> &= \langle \flat_W (FX) \mid FY \rangle \\
> &= \langle F^* \flat_W (FX) \mid Y \rangle \\
> &= \langle F^* \flat_W F X \mid Y \rangle \\
> \implies& C = F^* \flat_W F
> \end{aligned}
> $$
> This giving us our operator.

In 3D Cartesian coordinates:
- Let $(X,Y,Z)$ denote the Cartesian coordinate for $M$ and $(x,y,z)$ the Cartesian coordinate for $W$.
- Flow map $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} \phi^1(X,Y,Z) \\ \phi^2(X,Y,Z) \\ \phi^3(X,Y,Z) \end{bmatrix}$
- Deformation gradient $\mathbf{F} = \begin{bmatrix} \frac{\partial \phi^1}{\partial X} & \frac{\partial \phi^1}{\partial Y} & \frac{\partial \phi^1}{\partial Z} \\ \frac{\partial \phi^2}{\partial X} & \frac{\partial \phi^2}{\partial Y} & \frac{\partial \phi^2}{\partial Z} \\ \frac{\partial \phi^3}{\partial X} & \frac{\partial \phi^3}{\partial Y} & \frac{\partial \phi^3}{\partial Z} \end{bmatrix}$
- Right Cauchy-Green tensor $\mathbf{C} = \mathbf{F}^{\top} \bI \mathbf{F} = \bF^{\top}\bF$. 
	- Obviously, the [[Dual Space#Backward Pass (Pullback)|adjoint is the transpose]], so $F^{*} = \bF^{\top}$.
	- $\flat_{W} = \bI$ because it takes the inner product (dot product) of the basis vectors. Since the basis vectors in $\R^{3}$ are orthogonal to each other, it forms the identity matrix. 

# Deriving Elastic Force
Back to our potential energy, given some pointwise nonlinear elastic model $U$: 
$$
U: \Gamma(T^*M \odot T^*M) \xrightarrow{\text{pointwise nonlinear}} \Gamma(\bigwedge^n T^*M)
$$
$$
\mathcal{U}(\phi) = \int_{M} U(C) = \int_{M} U(\phi^{*} \flat_{W})
$$
The elastic force is the negative gradient of the potential energy: $\mathbf{f} = -d\mathcal{U}_\phi$. The assumption of elasticity is that the total potential energy is only a function of the Cauchy-Green tesnor in the above form. 

In particular, $U_{p}$ at each $p \in M$ is a $n$-form-valued (measures energy density) function of a metric. 
$$
U_{p} : T_{p}^{*}M \odot T_{p}^{*}M \xrightarrow{\text{nonlinear}} \bigwedge^{n} T_{p}^{*} M
$$
To compute this derivative, we can view the energy functional as a sequence of mappings and apply the chain rule. In the context of fields, this is essentially **continuous backpropagation**.

## 1. The Global Sequence of Maps
First, we can express the entire energy functional $\mathcal{U}(\phi)$ as a sequence of macroscopic maps from the space of all possible flow maps $C^\infty(M; W)$ to the final scalar energy:
$$
\underset{\textstyle \phi}{C^\infty(M; W)} \xrightarrow{d} \underset{\textstyle F}{\Gamma(T^*M \otimes T_\phi W)} \xrightarrow{\mathcal{G}} \underset{\textstyle C = F^*\flat_W F}{\Gamma(T^*M \odot T^*M)} \xrightarrow{U} \underset{\textstyle U(C)}{\Gamma\left(\bigwedge^n T^*M\right)} \xrightarrow{\int_M} \underset{\textstyle \mathcal{U}(\phi)}{\R}
$$

## 2. The Tangent Space Forward Pass (Kinematics)
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

## 3. The Backward Pass (Forces and Stresses)
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

# Actual Model
Let $(\flat^{M})_{\alpha \beta}$ be a fixed reference metric. This is the geometry of the material in its undeformed, relaxed state (the rest length). Let $\hat{C}$ be the deformation tensor. In particular, 
$$
\hat{C}^{\alpha}_{\beta} 
= (\sharp_{M})^{\alpha\gamma} C_{\gamma\beta} 
= \left[ (\flat^{M})^{-1} C \right]_{\beta}^{\alpha}
$$
Recall that $C$ is the current deformed lengths of the material vectors. The $\sharp_{M}$ operator "divides by the resting length". So, $\hat{C} = \text{id} \iff \text{no deformation}$. 

We have some different ways to model [[Stress#Equation of Motion|strain]]:
$$
\begin{aligned}
E_{\text{StV}} &= \frac{1}{2}(\hat{C} - \text{id}) && \text{St Venant Strain} \\
E_{\text{Biot}} &= \sqrt{\hat{C}} - \text{id} \\
E_{\text{Hencky}} &= \frac{1}{2} \log \hat{C} \\
E_{\text{Almansi}} &= \frac{1}{2}(\text{id} - \hat{C}^{-1})
\end{aligned}
$$

Write $U(C) = \Phi(E) \rho_M$, where we separate the energy density into a function of the strain and the mass density. $\Phi(E)$ represents the *energy per unit mass*, or the specific internal energy.

## St Venant-Kirchhoff Model
See [here](https://cseweb.ucsd.edu/~alchern/teaching/cse291_sp26/9-1Elasiticity.pdf) for derivation of the StVK model.

# Terminology (Stress Tensors)
By defining names for the intermediate states of the pullback, we recover the classic stress tensors of continuum mechanics!

## 2nd Piola-Kirchhoff Stress
When the pullback reaches the space dual to the Cauchy-Green tensor $C$, we get the 
[[Stress#Alternative Stress Tensors|2nd Piola-Kirchhoff stress]]:
$$
S := 2 \frac{\del U}{\del C} \in \Gamma\left(TM \odot TM \otimes \bigwedge^n T^*M\right)
$$
- **Physical Meaning**: This stress lives entirely in the undeformed material space ($M$). It is the energetic conjugate to the metric $C$. If you change the deformed lengths of the material (change $C$), $S$ tells you how much work is done.

## 1st Piola-Kirchhoff Stress Tensor
Pulling back one step further to the space dual to the deformation gradient $F$, we get the 1st Piola-Kirchhoff stress:
$$
P := d\mathcal{G}|_F^* S = \frac{\del U}{\del F} \in \Gamma\left(\bigwedge^{n-1} T^*M \otimes T_\phi^* W\right)
$$
- **Physical Meaning**: This is a **two-point tensor**. It eats a material $(n-1)$-form (an area element in the undeformed state) and outputs the actual physical force vector in the world space $W$. This is the mathematical formalization of "Force per unit undeformed area".
- Notice its type: $\Omega^{n-1}(M; T_\phi^* W)$. It's an $(n-1)$-form valued in world covectors!

Finally, pulling back $P$ through the spatial divergence $(d^\nabla)^*$ yields the actual elastic force density $d\mathcal{U}_\phi$.

# Force Evaluation
The formal derivation of all the above physics is quite long. We distill the math into the following pipeline for simulation:

The input is $\phi$, or a map of the current node positions. 
1. Evaluate $F_{\alpha}^{i} = \del_{\alpha}\phi^{i}$
	1. The spatial derivative of the current node positions relative to the original rest positions.
2. $C = F^{\top}F$, the right Cauchy-Green stress tensor.
3. $E = \frac{1}{2}[\sharp_{M} C - I]$, the St Venant Strain. Since $\flat_{W} = \bI$ in our orthonormal frame, then $\sharp_{M} = \flat_{W}^{-1} = \bI^{-1} = \bI$. 
4. $S = \sharp_{M}\left[\lambda \operatorname{tr}(E) \bI + 2\mu E \right] \rho_{M}$, the [[#2nd Piola-Kirchhoff Stress]]-Strain relationship
5. $P = FS$, the [[#1st Piola-Kirchhoff Stress Tensor]], 
6. $f = \nabla \cdot P$, the force output that accelerates the nodes in the next step. 

# Finite Element Simulation 
We can discretize the deformable body by triangle mesh (2D) or tetrahedral mesh (3D), where $n = \dim(M)$. Each vertex $i$ stores a fixed **rest position** $\bX_i$ (material coordinate) and a variable **world position** $\bx_i$ (representing value of flow map, $\phi(\bX_i) = \bx_i)$. 
```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}

% --- Color Definitions ---
% Matched to the reference image for clarity
\definecolor{meshBlue}{RGB}{50, 100, 175}
\definecolor{meshPurple}{RGB}{135, 75, 175}

% =====================================================
% Left Mesh: Reference Configuration (\mathbf{X}_i)
% =====================================================
\begin{scope}[shift={(0,0)}]
    % -- Coordinate Mapping --
    \coordinate (X0) at (0, 0);       % Center
    \coordinate (X1) at (-1.3, 1.0);  % Top Left
    \coordinate (X2) at (0.2, 1.6);   % Top
    \coordinate (X3) at (1.5, 0.5);   % Right
    \coordinate (X4) at (1.4, -1.0);  % Bottom Right
    \coordinate (X5) at (-0.1, -1.7); % Bottom
    \coordinate (X6) at (-1.4, -0.7); % Bottom Left

    % -- Background: Edges --
    % Perimeter
    \draw[meshBlue, thick] (X1) -- (X2) -- (X3) -- (X4) -- (X5) -- (X6) -- cycle;
    % Internal Spokes
    \draw[meshBlue, thick] (X0) -- (X1);
    \draw[meshBlue, thick] (X0) -- (X2);
    \draw[meshBlue, thick] (X0) -- (X3);
    \draw[meshBlue, thick] (X0) -- (X4);
    \draw[meshBlue, thick] (X0) -- (X5);
    \draw[meshBlue, thick] (X0) -- (X6);

    % -- Foreground: Nodes --
    \fill[meshBlue] (X1) circle (0.12);
    \fill[meshBlue] (X2) circle (0.12);
    \fill[meshBlue] (X3) circle (0.12);
    \fill[meshBlue] (X4) circle (0.12);
    \fill[meshBlue] (X5) circle (0.12);
    \fill[meshBlue] (X6) circle (0.12);
    \fill[meshBlue] (X0) circle (0.12);

    % -- Label --
    \node[meshBlue, font=\Large] at (-0.3, 0.6) {$\mathbf{X}_i$};
\end{scope}

% =====================================================
% Right Mesh: Current/Deformed Configuration (\mathbf{x}_i)
% =====================================================
\begin{scope}[shift={(8,0)}] % Shifted to the right
    % -- Coordinate Mapping (Stretched/Deformed) --
    \coordinate (x0) at (0, 0);       % Center
    \coordinate (x1) at (-2.2, 0.9);  % Top Left
    \coordinate (x2) at (-0.2, 1.4);  % Top
    \coordinate (x3) at (1.8, 0.5);   % Right
    \coordinate (x4) at (1.5, -0.9);  % Bottom Right
    \coordinate (x5) at (-0.7, -1.5); % Bottom
    \coordinate (x6) at (-2.4, -0.6); % Bottom Left

    % -- Background: Edges --
    % Perimeter
    \draw[meshPurple, thick] (x1) -- (x2) -- (x3) -- (x4) -- (x5) -- (x6) -- cycle;
    % Internal Spokes
    \draw[meshPurple, thick] (x0) -- (x1);
    \draw[meshPurple, thick] (x0) -- (x2);
    \draw[meshPurple, thick] (x0) -- (x3);
    \draw[meshPurple, thick] (x0) -- (x4);
    \draw[meshPurple, thick] (x0) -- (x5);
    \draw[meshPurple, thick] (x0) -- (x6);

    % -- Foreground: Nodes --
    \fill[meshPurple] (x1) circle (0.12);
    \fill[meshPurple] (x2) circle (0.12);
    \fill[meshPurple] (x3) circle (0.12);
    \fill[meshPurple] (x4) circle (0.12);
    \fill[meshPurple] (x5) circle (0.12);
    \fill[meshPurple] (x6) circle (0.12);
    \fill[meshPurple] (x0) circle (0.12);

    % -- Label --
    \node[meshPurple, font=\Large] at (-0.3, 0.4) {$\mathbf{x}_i$};
\end{scope}

\end{tikzpicture}
\end{document}
```

The data on the vertices can be linearly interpolated into a piecewise linear deformation map
$$
\begin{bmatrix} | \\ \by \\ | \\ 1 \end{bmatrix}
=
\begin{bmatrix} 
| & | &   & | \\
\bx_0 & \bx_1 & \cdots & \bx_n \\
| & | &   & | \\
1 & 1 & \cdots & 1
\end{bmatrix}
\begin{bmatrix}
| & | &   & | \\
\bX_0 & \bX_1 & \cdots & \bX_n \\
| & | &   & | \\
1 & 1 & \cdots & 1
\end{bmatrix}^{-1}
\begin{bmatrix} | \\ \bY \\ | \\ 1 \end{bmatrix}
$$

```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}

% --- Color Definitions ---
% Reference Mesh (Left)
\definecolor{meshBlue}{RGB}{45, 95, 175}
\definecolor{pointBlue}{RGB}{135, 185, 255}

% Current Mesh (Right)
\definecolor{meshPurple}{RGB}{135, 65, 175}
\definecolor{pointPurple}{RGB}{200, 160, 220}

% =====================================================
% Left Mesh: Reference Configuration
% =====================================================
\begin{scope}[shift={(0,0)}]
    % -- Coordinate Mapping --
    \coordinate (X1)   at (0, 0);       % Center
    \coordinate (Xn)   at (-1.3, 1.0);  % Top Left
    \coordinate (X0)   at (-1.5, -0.6); % Bottom Left
    \coordinate (Xtop) at (0.2, 1.6);   % Top
    \coordinate (Xr)   at (1.5, 0.5);   % Right
    \coordinate (Xbr)  at (1.4, -1.0);  % Bottom Right
    \coordinate (Xbot) at (-0.1, -1.7); % Bottom
    \coordinate (Y)    at (-0.9, 0.1);  % Interior point

    % -- Background: Edges --
    \draw[meshBlue, thick] (Xn) -- (Xtop) -- (Xr) -- (Xbr) -- (Xbot) -- (X0) -- cycle;
    \draw[meshBlue, thick] (X1) -- (Xn);
    \draw[meshBlue, thick] (X1) -- (Xtop);
    \draw[meshBlue, thick] (X1) -- (Xr);
    \draw[meshBlue, thick] (X1) -- (Xbr);
    \draw[meshBlue, thick] (X1) -- (Xbot);
    \draw[meshBlue, thick] (X1) -- (X0);

    % -- Foreground: Nodes --
    \fill[meshBlue] (Xn)   circle (0.12);
    \fill[meshBlue] (Xtop) circle (0.12);
    \fill[meshBlue] (Xr)   circle (0.12);
    \fill[meshBlue] (Xbr)  circle (0.12);
    \fill[meshBlue] (Xbot) circle (0.12);
    \fill[meshBlue] (X0)   circle (0.12);
    \fill[meshBlue] (X1)   circle (0.12);

    % -- Interior Point --
    \fill[pointBlue] (Y) circle (0.12);

    % -- Labels --
    \node[meshBlue, font=\Large, anchor=south east] at (-1.2, 1.1) {$\mathbf{X}_n$};
    \node[meshBlue, font=\Large, anchor=east]       at (-1.6, -0.5) {$\mathbf{X}_0$};
    \node[meshBlue, font=\Large, anchor=south east] at (-0.1, 0.1) {$\mathbf{X}_1$};
    \node[pointBlue, font=\Large, anchor=south]     at (-1.1, 0.1) {$\mathbf{Y}$};
\end{scope}

% =====================================================
% Right Mesh: Current Configuration
% =====================================================
\begin{scope}[shift={(8,0)}] 
    % -- Coordinate Mapping (Stretched/Deformed) --
    \coordinate (x1)   at (0, 0);       % Center
    \coordinate (xn)   at (-2.2, 0.9);  % Top Left
    \coordinate (x0)   at (-2.4, -0.6); % Bottom Left
    \coordinate (xtop) at (-0.2, 1.4);  % Top
    \coordinate (xr)   at (1.8, 0.5);   % Right
    \coordinate (xbr)  at (1.5, -0.9);  % Bottom Right
    \coordinate (xbot) at (-0.7, -1.5); % Bottom
    \coordinate (y)    at (-1.5, 0.1);  % Interior point

    % -- Background: Edges --
    \draw[meshPurple, thick] (xn) -- (xtop) -- (xr) -- (xbr) -- (xbot) -- (x0) -- cycle;
    \draw[meshPurple, thick] (x1) -- (xn);
    \draw[meshPurple, thick] (x1) -- (xtop);
    \draw[meshPurple, thick] (x1) -- (xr);
    \draw[meshPurple, thick] (x1) -- (xbr);
    \draw[meshPurple, thick] (x1) -- (xbot);
    \draw[meshPurple, thick] (x1) -- (x0);

    % -- Foreground: Nodes --
    \fill[meshPurple] (xn)   circle (0.12);
    \fill[meshPurple] (xtop) circle (0.12);
    \fill[meshPurple] (xr)   circle (0.12);
    \fill[meshPurple] (xbr)  circle (0.12);
    \fill[meshPurple] (xbot) circle (0.12);
    \fill[meshPurple] (x0)   circle (0.12);
    \fill[meshPurple] (x1)   circle (0.12);

    % -- Interior Point --
    \fill[pointPurple] (y) circle (0.12);

    % -- Labels --
    \node[meshPurple, font=\Large, anchor=south east]  at (-2.2, 1.0) {$\mathbf{x}_n$};
    \node[meshPurple, font=\Large, anchor=east]        at (-2.5, -0.5) {$\mathbf{x}_0$};
    \node[meshPurple, font=\Large, anchor=south east]  at (-0.1, 0.1) {$\mathbf{x}_1$};
    \node[pointPurple, font=\Large, anchor=west]       at (-1.35, 0.2) {$\mathbf{y}$};
\end{scope}

\end{tikzpicture}
\end{document}
```

Consider some point $\bY$ inside an undeformed triangle/tetrahedron. We can express $\bY$ as a linear combination (weighted sum) of the triangle's vertices $\bX_i$. These are called the **barycentric coordinates** of $\bY$. Two rules must be true:
1. $\bY = w_0 \bX_0 + w_1 \bX_1 + \cdots + w_n \bX_n$, such that the point is the weighted sum.
2. The weights must sum to 1: $w_0 + w_1 + \cdots + w_n = 1$. This ensures that the point is inside the triangle/tetrahedron.
$$
\begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_n \end{bmatrix}
= 
\begin{bmatrix}
\bX_0 & \bX_1 & \cdots & \bX_n \\
1 & 1 & \cdots & 1
\end{bmatrix}^{-1}
\begin{bmatrix} \bY \\ 1 \end{bmatrix}
$$
The interior points must also not change the weights during deformation, i.e they must stay at the same position relative to the other world space particles. Thus,
$$
\begin{bmatrix} \by \\ 1 \end{bmatrix}
= 
\begin{bmatrix}
\bx_0 & \bx_1 & \cdots & \bx_n \\
1 & 1 & \cdots & 1
\end{bmatrix}
\begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_n \end{bmatrix}
$$
By substitution, we get the above equation. 

## Deformation Gradient
The deformation gradient is a piecewise constant matrix
$$
\begin{bmatrix} 
&     &        & | \\
& \bF &        & \bt \\
&     &        & | \\
0     & \cdots & 0 & 1
\end{bmatrix}
= 
\begin{bmatrix}
| & | &   & | \\
\bx_0 & \bx_1 & \cdots & \bx_n \\
| & | &   & | \\
1 & 1 & \cdots & 1
\end{bmatrix}
\begin{bmatrix}
| & | &   & | \\
\bX_0 & \bX_1 & \cdots & \bX_n \\
| & | &   & | \\
1 & 1 & \cdots & 1
\end{bmatrix}^{-1}
$$
Let $A_j \bn_j$ is the area normal of the opposite face of $j$-th vertex and $V$ is the volume of the cell.
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}

% --- Color Definitions ---
% Reference Mesh
\definecolor{meshBlue}{RGB}{45, 95, 175}
\definecolor{highlightBlue}{RGB}{170, 205, 245} % Light blue for edge A1

% Current Mesh
\definecolor{meshPurple}{RGB}{135, 65, 175}

% =====================================================
% Left Mesh: Reference Configuration
% =====================================================
\begin{scope}[shift={(0,0)}]
    % -- Coordinate Mapping --
    \coordinate (X1)   at (0, 0);       % Center
    \coordinate (Xn)   at (-1.3, 1.0);  % Top Left
    \coordinate (X0)   at (-1.5, -0.6); % Bottom Left
    \coordinate (Xtop) at (0.2, 1.6);   % Top
    \coordinate (Xr)   at (1.5, 0.5);   % Right
    \coordinate (Xbr)  at (1.4, -1.0);  % Bottom Right
    \coordinate (Xbot) at (-0.1, -1.7); % Bottom

    % -- Background Highlight (Edge A1) --
    % Drawn first so the standard thin edge renders cleanly on top
    \draw[highlightBlue, line width=6pt] (Xn) -- (X0);

    % -- Background: Edges --
    \draw[meshBlue, thick] (Xn) -- (Xtop) -- (Xr) -- (Xbr) -- (Xbot) -- (X0) -- cycle;
    \draw[meshBlue, thick] (X1) -- (Xn);
    \draw[meshBlue, thick] (X1) -- (Xtop);
    \draw[meshBlue, thick] (X1) -- (Xr);
    \draw[meshBlue, thick] (X1) -- (Xbr);
    \draw[meshBlue, thick] (X1) -- (Xbot);
    \draw[meshBlue, thick] (X1) -- (X0);

    % -- Normal Vector (n1) --
    % Originating from the exact midpoint of X0 and Xn (-1.4, 0.2)
    \draw[meshBlue, thick, -{Stealth[scale=1.2]}] (-1.4, 0.2) -- (-2.0, 0.3);

    % -- Foreground: Nodes --
    \fill[meshBlue] (Xn)   circle (0.12);
    \fill[meshBlue] (Xtop) circle (0.12);
    \fill[meshBlue] (Xr)   circle (0.12);
    \fill[meshBlue] (Xbr)  circle (0.12);
    \fill[meshBlue] (Xbot) circle (0.12);
    \fill[meshBlue] (X0)   circle (0.12);
    \fill[meshBlue] (X1)   circle (0.12);

    % -- Labels --
    \node[meshBlue, font=\Large, anchor=south east]  at (-1.2, 1.1) {$\mathbf{X}_n$};
    \node[meshBlue, font=\Large, anchor=east]        at (-1.6, -0.5) {$\mathbf{X}_0$};
    \node[meshBlue, font=\Large, anchor=south east]  at (0.15, 0.3) {$\mathbf{X}_1$};
    
    % New geometric labels
    \node[highlightBlue, font=\Large, anchor=east]   at (-1.4, 0.7) {$A_1$};
    \node[meshBlue, font=\Large, anchor=east]        at (-2.1, 0.3) {$\mathbf{n}_1$};
    \node[meshBlue, font=\Large]                     at (-0.7, 0.1) {c};
\end{scope}

% =====================================================
% Right Mesh: Current Configuration
% =====================================================
\begin{scope}[shift={(8,0)}] 
    % -- Coordinate Mapping (Stretched/Deformed) --
    \coordinate (x1)   at (0, 0);       % Center
    \coordinate (xn)   at (-2.2, 0.9);  % Top Left
    \coordinate (x0)   at (-2.4, -0.6); % Bottom Left
    \coordinate (xtop) at (-0.2, 1.4);  % Top
    \coordinate (xr)   at (1.8, 0.5);   % Right
    \coordinate (xbr)  at (1.5, -0.9);  % Bottom Right
    \coordinate (xbot) at (-0.7, -1.5); % Bottom

    % -- Background: Edges --
    \draw[meshPurple, thick] (xn) -- (xtop) -- (xr) -- (xbr) -- (xbot) -- (x0) -- cycle;
    \draw[meshPurple, thick] (x1) -- (xn);
    \draw[meshPurple, thick] (x1) -- (xtop);
    \draw[meshPurple, thick] (x1) -- (xr);
    \draw[meshPurple, thick] (x1) -- (xbr);
    \draw[meshPurple, thick] (x1) -- (xbot);
    \draw[meshPurple, thick] (x1) -- (x0);

    % -- Foreground: Nodes --
    \fill[meshPurple] (xn)   circle (0.12);
    \fill[meshPurple] (xtop) circle (0.12);
    \fill[meshPurple] (xr)   circle (0.12);
    \fill[meshPurple] (xbr)  circle (0.12);
    \fill[meshPurple] (xbot) circle (0.12);
    \fill[meshPurple] (x0)   circle (0.12);
    \fill[meshPurple] (x1)   circle (0.12);

    % -- Labels --
    \node[meshPurple, font=\Large, anchor=south east]  at (-2.2, 1.0) {$\mathbf{x}_n$};
    \node[meshPurple, font=\Large, anchor=east]        at (-2.5, -0.5) {$\mathbf{x}_0$};
    \node[meshPurple, font=\Large, anchor=south east]  at (-0.1, 0.1) {$\mathbf{x}_1$};
\end{scope}

\end{tikzpicture}
\end{document}
```

Then the deformation for that cell is 
$$
\bF_{\text{c}} = -\frac{1}{nV_{\text{c}}}
\sum_{j=0}^{n}
\begin{bmatrix} | \\ \bx_j \\ | \end{bmatrix}
\begin{bmatrix} 
- \;\; A_{\text{c}, j} \bn_{\text{c}, j}^\top \;\; - \\
\end{bmatrix}
$$

Now, in each cell $\text{c}$ we have deformation gradient $\bF_{\text{c}}$. We
$$
\begin{aligned}
\text{Cauchy-Green Tensor} \quad \bC_{\text{c}} &= \bF_{\text{c}}^\top \bF_{\text{c}} \\
\text{St Venant Strain} \quad \bE_{\text{c}} &= \frac{1}{2}(\bC_{\text{c}} - \bI) \\
\text{2nd Piola-Kirchhoff Stress} \quad \bS_{\text{c}} &= \lambda \operatorname{tr}(\bE_{\text{c}}) \bI + 2\mu \bE_{\text{c}} \\
\text{1st Piola-Kirchhoff Stress} \quad \bP_{\text{c}} &= \bF_{\text{c}} \bS_{\text{c}} \\
\end{aligned}
$$
To compute the force on a vertex $i$, we take the adjoint of the gradient. The differential of $\bF$ with respect to $\bx_i$ is 
$$
\mathring{\bF}_{\text{c}} 
= -\frac{1}{nV_{\text{c}}}
\sum_{\text{v} \prec \text{c}} 
\begin{bmatrix} | \\ \mathring{\bx}_{\text{v}} \\ | \end{bmatrix}
\begin{bmatrix} 
- \;\; A_{\text{c}, \text{v}} \bn_{\text{c}, \text{v}}^\top \;\; - \\
\end{bmatrix}
$$
where $\text{v} \prec \text{c}$ are all the vertices of cell $\text{c}$. We get a tiny perturbation of a vertex as $\mathring{\bx}_{\text{v}}$. The resulting change is the change in the deformation gradient $\mathring{\bF}_{\text{c}}$. The adjoint of this gradient accumulates the traction force to the vertices:
$$
\begin{aligned}
\sum_{\text{c}} \operatorname{tr} \left(
    \bP_{\text{c}} \mathring{\bF}_{\text{c}}^\top
\right) V_{\text{c}}
&= \sum_{\text{v}} - \bf_{\text{v}}^\top \mathring{\bx}_{\text{v}} \\
% 
\bf_{\text{v}} 
&= \frac{1}{n} \sum_{\text{c} \succ \text{v}} \bP_{\text{c}} \bn_{\text{c}, \text{v}} A_{\text{c}, \text{v}} \\
% 
\bf_{\text{v}}
&= m_{\text{v}} \ddot{\bx}_{\text{v}}
\end{aligned}
$$
where $n$ is the dimension of the cell (3 for tetrahedra, 2 for triangles).

We also can calculate the total mass of each vertex by approximating the mass of each cell and distributing it to the vertices:
$$
m_{\text{v}} 
= \frac{1}{n} \sum_{\text{c} \succ \text{v}} \frac{1}{n+1} V_{\text{c}} 
$$
or the **lumped mass**.

## Time Integration
For external forces
$$
m_{\text{v}} \ddot{\bx}_{\text{v}} = \bf_{\text{v}} + \bf_{\text{v}}^{\text{ext}}
$$
We can use [[Numerical Methods#Runge-Kutta Method (RK4)|RK4]] or [[Incremental Potential and Dissipation#Symplectic & Backward Euler with Dissipation|symplectic Euler method]]. We just need to evaluate the force $(\bf_{\text{v}})_{\text{v}}$ given current positions $(\bx_{\text{v}})_{\text{v}}$ at each time step. The step size is $\Delta t = O(\text{edge length})$. 

Or [[Incremental Potential and Dissipation#Symplectic & Backward Euler with Dissipation|implicit Euler (with incremental potential)]]: 
$$
\bx^{(n+1)} = \argmin_{\bx \in \R^m} 
\sum_{\text{v}} \frac{m_{\text{v}}}{2\Delta t^2} \|\bx_{\text{v}} - \bx_{\text{v}}^{\text{pred}} \|^2 
+ \mathcal{U}(\bx)
$$
We can use [[Gradient#Naive Algorithm for Gradient Ascent/Descent|gradient descent]] or Newton's method. 
- Need evalulation of $\mathcal{U}(\bx) = \sum_{\text{c}} U(\bF^\top \bF) V_{\text{c}}$.
- Need evaluation of differential of potential (same as force evaluation)
- Need an (approximate) [[Hessian]] for the potential. 
    - The [[Laplacian]] can serve as one
      $$
      \bL = -\operatorname{div}
      \begin{bmatrix}
      V_{\text{c}} & &\\
      & &  \ddots \\
      \end{bmatrix}
      \operatorname{grad}
      $$
    - $\operatorname{grad}$ is the step to get $\bF_{\text{c}}$.