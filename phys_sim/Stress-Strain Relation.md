---
tags:
  - CSE_291G
---
# Recall
Recall from [[Stress#Cauchy's Stress Theory]] that the Cauchy-Green tensor is given by $\bC = \bF^{\top}\bF$, or more preicsely $\bC = F^{*} \flat_{W}F$. 

Here, we **postulate** that energy depends on the [[Elasticity#^241ca7|frame indifferent induced metric]] and the potential energy takes the form $\mathcal U = U(C)$. 

The [[Elasticity#2nd Piola-Kirchhoff Stress]] is given by $S = 2 \frac{\del U}{\del \C}$. 

> How do we design how the system stores energy when stretched? 

# Postulate (Existence of Rest Metric)
We postulate there exists a time-independent metric $\flat_{M}$ on the material space. Then, we can define $\hat C = \sharp_{M}C$ where there is "no deformation" iff $\hat C = \operatorname{id}$, as seen in [[Elasticity#Actual Model]]. We write energy as $U(C) = \Psi(\hat C)\rho_{M}$ and $\Psi$ is the **specific internal energy** or **Helmholtz free energy**. 

[[Stress#Alternative Stress Tensors|2nd Piola-Kirchoff Stress]] is
$$
S = 2 \frac{\del U}{\del C} = 2 \sharp_M \frac{\del \Psi}{\del \hat C} \rho_{M}
$$

A **strain** is an expression of $\hat C$ that measures its [[Elasticity#Actual Model|deviation]] from $\text{id}$. For large deformations, Hencky strain is usually considered as the natural true strain. For small deformations, $\frac{\del\Psi}{\del \hat{C}} \approx \frac{\del \Psi}{\del E}$. 

# Small Deformations
An example energy is the St Venant-Kirchhoff energy, which is given by
$$
\Psi_{\text{StVK}}
= \frac{\lambda}{2} \operatorname{tr}(E)^{2} + \mu \operatorname{tr}(E^{2})
$$
with the corresponding stress 
$$
S = \sharp_M \left( \lambda \operatorname{tr}(E) \operatorname{id} + 2\mu E \right) \rho_{M}
$$
The Lame constants $\lambda, \mu$ describe how stress relate to the isotropic part of deformation and anisotropic part of deformation, respectively.

We can measure **Young's modulus** $E$ and **Poisson's ratio** $\nu$:
$$
\left\{
\begin{aligned}
E &= \frac{F/A}{\Delta \ell / \ell} \\
\nu &= -\frac{\Delta L'}{\Delta L}
\end{aligned}
\right.
$$
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}

% ==========================================
% COLOR THEME DEFINITIONS
% ==========================================
% Left Diagram Colors (Rod)
\definecolor{rodDark}{RGB}{60, 105, 175}
\definecolor{rodLight}{RGB}{140, 180, 245}
\definecolor{rodLightFace}{RGB}{170, 205, 250}
\definecolor{rodBorder}{RGB}{40, 80, 145}

% Right Diagram Colors (Cube)
\definecolor{topGreen}{RGB}{82, 206, 170}
\definecolor{frontGreen}{RGB}{36, 155, 122} % -y face
\definecolor{rightGreen}{RGB}{54, 180, 144} % +x face
\definecolor{topOrange}{RGB}{250, 153, 113}
\definecolor{frontOrange}{RGB}{219, 96, 50} % -y face
\definecolor{rightOrange}{RGB}{247, 121, 74} % +x / -x faces


% ==========================================
% LEFT DIAGRAM: 1D Uniaxial Tension
% ==========================================
\begin{scope}[shift={(-6, 0)}]
    
    % --- Dark Blue Section (Original Length) ---
    \fill[rodDark] (-1, -0.6) rectangle (4, 0.6); % Main body
    \fill[rodDark] (4, 0) ellipse (0.2 and 0.6);  % Right end cap
    \draw[thick, rodBorder] (4, -0.6) arc (-90:90:0.2 and 0.6); % Right edge visible arc
    
    % --- Light Blue Section (Extension) ---
    \fill[rodLight] (-3, -0.6) rectangle (-1, 0.6); % Main body
    \fill[rodLight] (-1, 0) ellipse (0.2 and 0.6);  % Curved 3D intersection overlapping dark body
    
    % --- Interface Border ---
    \draw[thick, rodBorder] (-1, -0.6) arc (-90:90:0.2 and 0.6); % Visible intersection curve
    
    % --- Front Face ---
    \filldraw[fill=rodLightFace, draw=rodBorder, thick] (-3, 0) ellipse (0.2 and 0.6);
    
    % --- Outline Borders ---
    \draw[thick, rodBorder] (-3, 0.6) -- (4, 0.6);
    \draw[thick, rodBorder] (-3, -0.6) -- (4, -0.6);

    % --- Force Arrow ---
    \draw[-{Stealth[scale=1.5]}, very thick, rodBorder] (-3.2, 0) -- (-5.2, 0) node[above, xshift=15pt, yshift=2pt] {\LARGE $F/A$};

    % --- Labels ---
    \node[font=\huge] at (1.5, -1.3) {$\ell$};
    \node[font=\huge] at (-2.0, 1.1) {$\Delta\ell$};

\end{scope}


% ==========================================
% RIGHT DIAGRAM: 3D Poisson's Ratio Effect
% ==========================================
\begin{scope}[shift={(4, 0)}, x={(0.8cm, -0.35cm)}, y={(0.55cm, 0.45cm)}, z={(0cm, 1cm)}]

    % --- 1. Left Force Arrow ---
    \draw[-{Stealth[scale=1.5]}, very thick] (-2.5, 0, 0) -- (-4.0, 0, 0);

    % --- 2. Left Orange Block (Extended, Shrunk Cross-Section) ---
    % -x face (End)
    \filldraw[fill=rightOrange, draw=black, very thin, line join=round] 
        (-2.5, -1.1, -1.1) -- (-2.5, 1.1, -1.1) -- (-2.5, 1.1, 1.1) -- (-2.5, -1.1, 1.1) -- cycle;
    % -y face (Side)
    \filldraw[fill=frontOrange, draw=black, very thin, line join=round] 
        (-2.5, -1.1, -1.1) -- (-1.5, -1.1, -1.1) -- (-1.5, -1.1, 1.1) -- (-2.5, -1.1, 1.1) -- cycle;
    % +z face (Top)
    \filldraw[fill=topOrange, draw=black, very thin, line join=round] 
        (-2.5, -1.1, 1.1) -- (-1.5, -1.1, 1.1) -- (-1.5, 1.1, 1.1) -- (-2.5, 1.1, 1.1) -- cycle;

    % --- 3. Green Block (Original Undeformed State) ---
    % -y face (Side)
    \filldraw[fill=frontGreen, draw=black, very thin, line join=round] 
        (-1.5, -1.5, -1.5) -- (1.5, -1.5, -1.5) -- (1.5, -1.5, 1.5) -- (-1.5, -1.5, 1.5) -- cycle;
    % +x face (End) - Partially occluded by the right orange block
    \filldraw[fill=rightGreen, draw=black, very thin, line join=round] 
        (1.5, -1.5, -1.5) -- (1.5, 1.5, -1.5) -- (1.5, 1.5, 1.5) -- (1.5, -1.5, 1.5) -- cycle;
    % +z face (Top)
    \filldraw[fill=topGreen, draw=black, very thin, line join=round] 
        (-1.5, -1.5, 1.5) -- (1.5, -1.5, 1.5) -- (1.5, 1.5, 1.5) -- (-1.5, 1.5, 1.5) -- cycle;

    % --- 4. Right Orange Block (Extended, Shrunk Cross-Section) ---
    % -y face (Side)
    \filldraw[fill=frontOrange, draw=black, very thin, line join=round] 
        (1.5, -1.1, -1.1) -- (2.5, -1.1, -1.1) -- (2.5, -1.1, 1.1) -- (1.5, -1.1, 1.1) -- cycle;
    % +x face (End)
    \filldraw[fill=rightOrange, draw=black, very thin, line join=round] 
        (2.5, -1.1, -1.1) -- (2.5, 1.1, -1.1) -- (2.5, 1.1, 1.1) -- (2.5, -1.1, 1.1) -- cycle;
    % +z face (Top)
    \filldraw[fill=topOrange, draw=black, very thin, line join=round] 
        (1.5, -1.1, 1.1) -- (2.5, -1.1, 1.1) -- (2.5, 1.1, 1.1) -- (1.5, 1.1, 1.1) -- cycle;

    % --- 5. Right Force Arrow ---
    \draw[-{Stealth[scale=1.5]}, very thick] (2.5, 0, 0) -- (4.0, 0, 0);

    % --- 6. Dimension Lines and Labels ---
    % L (Original Length)
    \draw[very thin] (-1.5, 1.5, 1.5) -- (-1.5, 2.0, 1.5);
    \draw[very thin] (1.5, 1.5, 1.5) -- (1.5, 2.0, 1.5);
    \draw[very thin] (-1.5, 1.8, 1.5) -- (1.5, 1.8, 1.5) node[midway, above=-1pt] {\Large $L$};

    % \Delta L (Axial Extension)
    \draw[very thin] (1.5, -1.1, 1.1) -- (1.5, -1.5, 1.1);
    \draw[very thin] (2.5, -1.1, 1.1) -- (2.5, -1.5, 1.1);
    \draw[very thin] (1.5, -1.3, 1.1) -- (2.5, -1.3, 1.1) node[midway, below=-1pt] {\Large $\Delta L$};

    % \Delta L' (Transverse Contraction - Vertical and Horizontal gaps)
    \draw[very thin] (1.5, -1.1, 1.1) -- (1.5, -1.1, 1.5) node[midway, right=10pt, above=1pt] {\Large $\Delta L'$};
    \draw[very thin] (1.5, -1.1, 1.5) -- (1.5, -1.5, 1.5) node[midway, below=10pt, left=5pt] {\Large $\Delta L'$};

    % --- 7. Coordinate Axis Triad ---
    \begin{scope}[shift={(-3, -3, -1.5)}]
        \draw[->, thick] (0, 0, 0) -- (1, 0, 0) node[right=-1pt] {\Large $x$};
        \draw[->, thick] (0, 0, 0) -- (0, 1, 0) node[right=-1pt] {\Large $y$};
        \draw[->, thick] (0, 0, 0) -- (0, 0, 1) node[above=-1pt] {\Large $z$};
    \end{scope}

\end{scope}

\end{tikzpicture}
\end{document}
```

- $E$ measures how much force is needed to stretch a material linearly (think of it like a spring constant). It is defined as stress over strain. 
- $\nu$ measures how much a material contracts in the directions perpendicular to the direction of stretching (how much a material thins out when you stretch it).

We get the Lame constants from $E$ and $\nu$:
$$
\left\{
\begin{aligned}
\lambda &= \frac{E\nu}{(1+\nu)(1-2\nu)} \\
\mu &= \frac{E}{2(1+\nu)}
\end{aligned}
\right.
$$

# Postulate (Isotropic Material)
A material is called **isotropic** if 
$$
\Psi(\hat C) = \Psi(R^{-1} \hat C R)
$$
for all "rotation" operators $R$ characterized by $R^* \flat_M R = \flat_M$. In $\R^3$, this means $R$ is in [[Special Orthogonal Group]] $\SO(3)$.

The energy is only a function of the eigenvalues (modulo permutations) ^c47084
$$
\text{eigenvalues}(\hat C) = \{\lambda_1, \lambda_2, \lambda_3\}
$$
These eigenvalues are the square of the eigenvalues of $\bY$ in polar decomposition $\bF = \bR \bY$. Equivalently, they are the square of the [[Singular Value Decomposition|singular values]] of $\bF$ or the square of "principal stretching".

How do we model $U$ such that $U(\bC) = u(\lambda_1, \lambda_2, \lambda_3)$? We can view the eigenvalues as the roots of a polynomial, and use the coefficient of the polynomial as our parameters:
$$
\{\lambda_1, \lambda_2, \lambda_3\} = \text{roots}\left( t^3 - I_1 t^2 + I_2 t - I_3 ; t\right)
$$
These coefficents are called the **principal invariants**:
$$
\begin{aligned}
I_1 &= \lambda_1 + \lambda_2 + \lambda_3 &&= \operatorname{tr}(\bC) \\
I_2 &= \lambda_1 \lambda_2 + \lambda_2 \lambda_3 + \lambda_3 \lambda_1 &&= \frac{1}{2}\left( \operatorname{tr}(\bC)^2 - \operatorname{tr}(\bC^2) \right) \\
I_3 &= \lambda_1 \lambda_2 \lambda_3 &&= \det(\bC)
\end{aligned}
$$
This is the [[Characteristic Polynomial]]:
$$
t^3 - I_1 t^2 + I_2 t - I_3 = \det(t \bI - \bC)
$$

which allows us to express the energy as a function of the principal invariants:
$$
U(\bC) = w(I_1, I_2, I_3)
$$

> [!faq] Why do we care about principal invariants?
> We can express the energy as a function of the principal invariants, which are easier to compute than the eigenvalues. 
> 
> Since an isotropic material has no preferred direction, its stored energy $\Psi$ can only depend on the principal stretches (the eigenvalues of $\hat C$). However, eigenvalues do not have a fixed order (they can swap), so a valid energy function must [[#^c47084|mod out permutation]], meaning it must yield the same energy regardless of how the eigenvalues are ordered. 
> 
> The principal invariants guarantee this symmetry, as the coefficients of the characteristic polynomial. Thus, we can model the energy as $U(\bC) = w(I_1, I_2, I_3)$.

### Theorem (No Fourth Invariants)
We only need three trace invariants to compute the system, no matter the material. 

So $I_{1} = \text{tr}(\bC)$. $\text{tr}(\bC^{2}) = I_{1}^{2} - 2I_{2}$. We also get $\text{tr}(\bC^{3}) = I_{1}^{3} - 3I_{1}I_{2} + 3I_{3}$. How do we find $\text{tr}(\bC^{k})$?

We use the [[Cayley-Hamilton Theorem]]:
$$
\bC^{3} - I_{1}\bC^{2} + I_{2} \bC - I_{3} = 0
$$
Mutiply by $\bC^{k}$ and take its trace:
$$
\begin{aligned}
0 &= \operatorname{tr}(\bC^{k+3}) - I_{1} \operatorname{tr}(\bC^{k+2}) + I_{2} \operatorname{tr}(\bC^{k+1}) - I_{3} \operatorname{tr}(\bC^{k})\\
\operatorname{tr}(\bC^{k+3}) &= I_{1} \operatorname{tr}(\bC^{k+2}) - I_{2} \operatorname{tr}(\bC^{k+1}) + I_{3} \operatorname{tr}(\bC^{k}) \\
\end{aligned}
$$
giving us a recursive formula to compute $\operatorname{tr}(\bC^{k})$ for all $k$.

## Chain Rule for Stress
We still need to calculate stress, and so we need to use the chain rule. Recall the [[Elasticity#2nd Piola-Kirchhoff Stress]]. Using the chain rule with $w$,
$$
\frac{\del U}{\del \bC}
= 
\frac{\del w}{\del I_{1}} \frac{\del I_{1}}{\del \bC}
+ \frac{\del w}{\del I_{2}} \frac{\del I_{2}}{\del \bC}
+ \frac{\del w}{\del I_{3}} \frac{\del I_{3}}{\del \bC}
$$
The scalar terms are easy to compute. However, the tensor terms are more involved. In particular, we need to compute $\frac{\del I_{k}}{\del \bC}$. 

Instead, define the characteristic polynomial as a function of a dummy variable $z$:
$$
P_\bC(z) = \det(z \bI - \bC) = z^n - I_1 z^{n-1} + I_2 z^{n-2} - \cdots + (-1)^n I_n
$$
We can use [[Jacobi's Formula]] to compute the derivative of the determinant:
$$
\frac{\del \det(A)}{\del A} = \det(A) A^{-\top}
$$
By applying Jacobi's formula to $A = z \bI - \bC$, we get:
$$
\begin{aligned}
\frac{\del P_\bC(z)}{\del \bC}
&= \frac{\del \det(z \bI - \bC)}{\del \bC} \\
&= -\det(z \bI - \bC) (z \bI - \bC)^{-\top} \\
&= -P_\bC(z) (z \bI - \bC)^{-\top} \\
% &= -\left( z^n - I_1 z^{n-1} + I_2 z^{n-2} - \cdots + (-1)^n I_n \right) (z \bI - \bC)^{-\top} \\
% &= -\frac{\del I_1}{\del \bC} z^{n-1} + \frac{\del I_2}{\del \bC} z^{n-2} - \cdots + (-1)^n \frac{\del I_n}{\del \bC}
\end{aligned}
$$
Note that applying the chain rule to the argument $z\bI - \bC$ with respect to $\bC$ introduces a negative sign to the Jacobi formula result.

We can also compute the derivative of $P_\bC(z)$ by differentiating its expanded scalar polynomial form term-by-term with respect to $\bC$:
$$
\frac{\partial P_\bC(z)}{\partial \bC} = -\frac{\partial I_1}{\partial \bC} z^{n-1} + \frac{\partial I_2}{\partial \bC} z^{n-2} - \cdots + (-1)^n \frac{\partial I_n}{\partial \bC}
$$
Because both methods describe the same derivative $\frac{\partial P_\bC(z)}{\partial \bC}$, we can equate them. 
$$
-\frac{\partial I_1}{\partial \bC} z^{n-1} + \frac{\partial I_2}{\partial \bC} z^{n-2} - \cdots + (-1)^n \frac{\partial I_n}{\partial \bC} = -P_\bC(z) (z \bI - \bC)^{-\top}
$$
Notice that $\frac{\partial I_k}{\partial \bC}$ is isolated as the coefficient for the $z^{n-k}$ term. To extract this specific coefficient from the right-hand side equation, we can take the $(n-k)$-th derivative with respect to $z$ and evaluate it at $z=0$ (similar to finding coefficients in a Maclaurin series). 

This provides the generalized formula for the derivative of the $k$-th principal invariant:
$$
\frac{\del I_k}{\del \bC} 
= (-1)^{n-k} \frac{1}{(n-k)!} \frac{d^{n-k}}{dz^{n-k}}\Bigg|_{z=0} \left( 
P_\bC(z)(z \bI - \bC)^{-\top} 
\right) 
$$

### Example: Fluid Potential
Consider a fluid where the energy potential $\Psi$ only depends on volume deformation, entirely ignoring the shearing part. This means the energy depends exclusively on the third invariant, $I_3 = \det(\bC)$:
$$
\Psi(\bC) = w(I_3)
$$

To find the [[Elasticity#2nd Piola-Kirchhoff Stress|2nd Piola-Kirchoff Stress]] $\bS$, we apply the chain rule using the derivative for $I_{3}$ and [[Jacobi's Formula]]:
$$
\bS = 2 \frac{\partial \Psi(\bC)}{\partial \bC} = 2 w' \frac{\partial \det(\bC)}{\partial \bC} = 2 w' \det(\bC) \bC^{-\top}
$$

Since $\bC = \bF^\top \bF$, we know $\det(\bC) = J^2$ (where $J = \det(\bF)$). We can then compute the [[Elasticity#1st Piola-Kirchhoff Stress Tensor|1st Piola-Kirchhoff Stress]] $\bP$:
$$
\begin{aligned}
\bP 
&= \bF \bS \\
&= 2 w' J^2 \bF \bC^{-\top} \\ 
&= 2 w' J^2 \bF (\bF^\top \bF)^{-\top} \\
&= 2 w' J^2 \bF \bF^{-1} \bF^{-\top} \\
&= 2 w' J^2 \bF^{-\top}
\end{aligned}
$$

Finally, transforming this into the Cauchy stress $\boldsymbol{\sigma}$ yields a purely hydrostatic pressure relationship $p \bI$:
$$
\boldsymbol{\sigma} = \frac{1}{J} \bP \bF^\top = \frac{2 w' J^2}{J} \bI = p \bI
$$