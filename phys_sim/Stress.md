---
tags:
  - CSE_291G
---
What is the force experienced by each point? This is called **stress** inside the material. 

There are a couple types of stress:
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}

% --- Color Theme ---
\definecolor{frontColor}{RGB}{85, 136, 205}  
\definecolor{topColor}{RGB}{125, 175, 235}   
\definecolor{sideColor}{RGB}{65, 110, 175}   
\definecolor{transFill}{RGB}{200, 220, 240}  
\definecolor{transLine}{RGB}{120, 140, 160}  
\definecolor{arrowColor}{RGB}{230, 20, 20}   

% --- Global Styles ---
\tikzset{
    force/.style={-{Stealth[length=4mm, width=3.5mm]}, line width=2pt, arrowColor},
    trans/.style={transLine, dashed, fill=transFill, fill opacity=0.3, thick}
}

% -----------------------------------------------------
% 1. Tension
% -----------------------------------------------------
\begin{scope}[shift={(0,0)}]
    % Solid Block
    \filldraw[fill=frontColor, draw=black] (-0.35, -2.2) rectangle (0.35, 2.2);
    \filldraw[fill=topColor, draw=black] (-0.35, 2.2) -- (0.35, 2.2) -- (0.55, 2.4) -- (-0.15, 2.4) -- cycle;
    \filldraw[fill=sideColor, draw=black] (0.35, -2.2) -- (0.55, -2.0) -- (0.55, 2.4) -- (0.35, 2.2) -- cycle;

    % Transparent Over-Block (Original State)
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.8, -1.2) -- (-0.2, -1.2) -- cycle; 
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.5, 1.5) -- (-0.5, 1.5) -- cycle;   
    \draw[trans] (0.5, -1.5) -- (0.8, -1.2) -- (0.8, 1.8) -- (0.5, 1.5) -- cycle;     
    \draw[trans] (-0.5, 1.5) -- (0.5, 1.5) -- (0.8, 1.8) -- (-0.2, 1.8) -- cycle;     

    % Force Arrows
    \draw[force] (0.1, 2.4) -- (0.1, 3.4);
    \draw[force] (0.1, -2.2) -- (0.1, -3.2);

    % Label
    \node[font=\Large] at (0.1, -3.8) {tension};
\end{scope}

% -----------------------------------------------------
% 2. Compression
% -----------------------------------------------------
\begin{scope}[shift={(3.5,0)}]
    % Solid Block 
    \filldraw[fill=frontColor, draw=black] (-0.65, -1.0) rectangle (0.65, 1.0);
    \filldraw[fill=topColor, draw=black] (-0.65, 1.0) -- (0.65, 1.0) -- (1.05, 1.4) -- (-0.25, 1.4) -- cycle;
    \filldraw[fill=sideColor, draw=black] (0.65, -1.0) -- (1.05, -0.6) -- (1.05, 1.4) -- (0.65, 1.0) -- cycle;

    % Transparent Over-Block
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.8, -1.2) -- (-0.2, -1.2) -- cycle;
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.5, 1.5) -- (-0.5, 1.5) -- cycle;
    \draw[trans] (0.5, -1.5) -- (0.8, -1.2) -- (0.8, 1.8) -- (0.5, 1.5) -- cycle;
    \draw[trans] (-0.5, 1.5) -- (0.5, 1.5) -- (0.8, 1.8) -- (-0.2, 1.8) -- cycle;

    % Force Arrows
    \draw[force] (0.2, 2.4) -- (0.2, 1.4);
    \draw[force] (0.2, -2.4) -- (0.2, -1.4);

    % Label
    \node[font=\Large] at (0.2, -3.8) {compression};
\end{scope}

% -----------------------------------------------------
% 3. Shear
% -----------------------------------------------------
\begin{scope}[shift={(7.5,0)}]
    % Solid Block 
    \filldraw[fill=frontColor, draw=black] (-0.5, -1.5) -- (0.5, -1.5) -- (1.2, 1.5) -- (0.2, 1.5) -- cycle;
    \filldraw[fill=topColor, draw=black] (0.2, 1.5) -- (1.2, 1.5) -- (1.5, 1.8) -- (0.5, 1.8) -- cycle;
    \filldraw[fill=sideColor, draw=black] (0.5, -1.5) -- (0.8, -1.2) -- (1.5, 1.8) -- (1.2, 1.5) -- cycle;

    % Transparent Over-Block
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.8, -1.2) -- (-0.2, -1.2) -- cycle;
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.5, 1.5) -- (-0.5, 1.5) -- cycle;
    \draw[trans] (0.5, -1.5) -- (0.8, -1.2) -- (0.8, 1.8) -- (0.5, 1.5) -- cycle;
    \draw[trans] (-0.5, 1.5) -- (0.5, 1.5) -- (0.8, 1.8) -- (-0.2, 1.8) -- cycle;

    % Force Arrows
    \draw[force] (0.0, 1.65) -- (1.6, 1.65);

    % Label
    \node[font=\Large] at (0.4, -3.8) {shear};
\end{scope}

% -----------------------------------------------------
% 4. Bending
% -----------------------------------------------------
\begin{scope}[shift={(11.5,0)}]
    % Solid Block (Curving to the right to yield to the arrows)
    \filldraw[fill=frontColor, draw=black]
        (-0.5, -1.5) .. controls (0.0, -0.5) and (0.0, 0.5) .. (-0.5, 1.5) --
        (0.5, 1.5) .. controls (1.0, 0.5) and (1.0, -0.5) .. (0.5, -1.5) -- cycle;
    \filldraw[fill=topColor, draw=black]
        (-0.5, 1.5) -- (0.5, 1.5) -- (0.8, 1.8) -- (-0.2, 1.8) -- cycle;
    \filldraw[fill=sideColor, draw=black]
        (0.5, -1.5) .. controls (1.0, -0.5) and (1.0, 0.5) .. (0.5, 1.5) --
        (0.8, 1.8) .. controls (1.3, 0.8) and (1.3, -0.2) .. (0.8, -1.2) -- cycle;

    % Transparent Over-Block
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.8, -1.2) -- (-0.2, -1.2) -- cycle;
    \draw[trans] (-0.5, -1.5) -- (0.5, -1.5) -- (0.5, 1.5) -- (-0.5, 1.5) -- cycle;
    \draw[trans] (0.5, -1.5) -- (0.8, -1.2) -- (0.8, 1.8) -- (0.5, 1.5) -- cycle;
    \draw[trans] (-0.5, 1.5) -- (0.5, 1.5) -- (0.8, 1.8) -- (-0.2, 1.8) -- cycle;

    % Force Arrows
    \draw[force] (1.8, 1.2) -- (0.8, 1.2);
    \draw[force] (1.8, -1.2) -- (0.8, -1.2);
    \draw[force] (-1.8, 0) -- (-0.9, 0);

    % Label
    \node[font=\Large] at (0.2, -3.8) {bending};
\end{scope}

% -----------------------------------------------------
% 5. Torsion
% -----------------------------------------------------
\begin{scope}[shift={(15.5,0)}]
    % Solid Block 
    \filldraw[fill=frontColor, draw=black, line join=round] (-0.4, -1.5) -- (0.4, -1.5) -- (0.1, 0) -- (-0.5, 0) -- cycle;
    \filldraw[fill=sideColor, draw=black, line join=round] (0.4, -1.5) -- (0.7, -1.2) -- (0.4, 0.3) -- (0.1, 0) -- cycle;

    \filldraw[fill=sideColor, draw=black, line join=round] (-0.5, 0) -- (0.1, 0) -- (0.4, 1.5) -- (-0.2, 1.5) -- cycle;
    \filldraw[fill=topColor, draw=black, line join=round] (0.1, 0) -- (0.4, 0.3) -- (0.7, 1.8) -- (0.4, 1.5) -- cycle;

    \filldraw[fill=frontColor, draw=black, line join=round] (-0.2, 1.5) -- (0.4, 1.5) -- (0.7, 1.8) -- (0.1, 1.8) -- cycle;

    % Force Arrows
    \draw[force] (-0.6, 1.8) .. controls (-0.6, 1.5) and (0.8, 1.5) .. (0.9, 1.9);
    \draw[force] (0.7, -1.6) .. controls (0.7, -1.9) and (-0.6, -1.9) .. (-0.8, -1.5);

    % Label
    \node[font=\Large] at (0.1, -3.8) {torsion};
\end{scope}

\end{tikzpicture}
\end{document}
```

# Cauchy's Stress Theory 
Consider an infinitesimal plane within a material. The force acting on that surface is called the **traction force** denoted as $\bT^{(\bn)}$, dependent on the orientation of the plane defined by the normal vector $\bn$. It satisfies the *reciprocity property*, meaning the force on the opposite side of the plane is equal in magnitude, but opposite in direction: $\bT^{(-\bn)} = - \bT^{(\bn)}$. 

The total force experienced by a volume is given by the total traction force
$$
\iiint_{V} \bf dV = \oiint_{\del V} \bT^{(\bn)} dA
$$

**Cauchy's Stress Theorem** is defined as: $\bT^{(\bn)}$ is linear in $\bn$ (i.e. there is a matrix $\sigma$ called the **stress tensor**) such that $\bT^{(\bn)} = \sigma \bn$.

The net force at each point is defined as the divergence of the stress tensor: $\bf = \nabla \cdot \sigma$ (or written in index notation as $f^i = \del_j\sigma^{ij}$). For a material in equilibrium, the sum of these internal foces any any external forces must be zero:
$$
\nabla \cdot \sigma + \bf_{ext} = 0
$$
Furthermore, at equilibrium, the Cauchy stress tensor $\sigma$ must be symmetric.  ^a37527
- This can be shown by requesting zero net torque. 
- When it's not in equilibrium, the Cauchy stress tensor can be non-symmetric, such as [[Continuum Mechanics#Viscoelastic Materials|viscoelastic fluids]]. 
- For a different that we will see next, in pure elastic material, Cauchy stress $\sigma$ is always symmetric even at non-equilibrium.

## Alternative Stress Tensors
The Cauchy Stress Tensor is not the only way to represent stress. Consider the **deformation gradient**:
$$
\bF = 
\begin{bmatrix}
\frac{\del \phi^1}{\del X} & \frac{\del \phi^1}{\del Y} & \frac{\del \phi^1}{\del Z} \\
\frac{\del \phi^2}{\del X} & \frac{\del \phi^2}{\del Y} & \frac{\del \phi^2}{\del Z} \\
\frac{\del \phi^3}{\del X} & \frac{\del \phi^3}{\del Y} & \frac{\del \phi^3}{\del Z}
\end{bmatrix}
$$
And let $J = \det(\bF)$. 

The **First Piola-Kirchhoff Stress Tensor** is defined as 
$$
\bP = J \sigma \bF^{-\top}
$$
allowing us to calculate the net "world-force" at a point using the original coordinate (Lagrangian) grid $\bf \circ \phi = \nabla \cdot \bP$. This tensor is generally non-symmetric. 

The **Second Piola-Kirchhoff Stress Tensor** is defined as
$$
\bS = \bF^{-1} \sigma
$$
It is symmetric iff Cauchy is symmetric. 

# Equation of Motion
We first need to define the **strain**. Strain is a measure of how much a material has deformed from its rest state. The **right Cauchy-Green deformation** tensor is
$$
\bC = \bF^\top \bF
$$
And then the **Green-St Venant** strain 
$$
E = \frac{1}{2}(\bC - \bI)
$$

Next, we need to model the stress-strain relationship (deformation-"internal forces"). To calculate the 2nd Piola-Kirchhoff stress $\bS$, 
$$
\bS = \lambda \text{tr}(E) \bI + 2\mu E
$$
where $\lambda,\mu$ are the Lamé parameters, dictating the specific material properties.

To easily compute the forces, we convert it to the 1st Piola-Kirchhoff stress $\bP$:
$$
\bP = \bF \bS
$$
Now we want to find the actual force vector $\bf$ acting on each point in the original (Lagrangian) coordinate system by taking its divergence (like before!):
$$
\bf = \nabla \cdot \bP
\quad \text{or in index notation} 
\quad f^i = \frac{\del}{\del X^i} P^{i}_{j}
$$
Fianlly, applying Newton's second law to get the equation of motion:
$$
\rho_M \ddot{\phi} = \bf
$$

## Type-Sensitive Tensor Analysis
Having a type-sensitive tensor analysis will make it more transparent. In particular, theorems like [[#^a37527|Cauchy stress symmetry]] is just the result of type checking. 