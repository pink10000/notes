---
tags:
  - CSE_291G
---
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

