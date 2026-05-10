---
tags:
  - CSE_291G
---
[]()# Dissipative Systems
Hamilton's [[Lagrangian Mechanics#Theorem (Least Action Principle)|least action principle]] always gives us conservative forces. 
$$
\left(
  \int_0^T \left(K(\bq, \dot{\bq}) - V(\bq)\right) dt
\right)^{\circ} = 0
\implies 
\underbrace{
  \frac{d}{dt} \frac{\partial K}{\partial \dot{\bq}}
}_{\substack{\text{change of} \\ \text{momentum}}}
\;\;\;\;
\underbrace{
  - \frac{\partial K}{\partial \bq}
}_{\substack{\text{fictitious} \\ \text{force}}}
=
\underbrace{
  - \frac{\partial V}{\partial \bq}
}_{\substack{\text{conservative} \\ \text{force}}}
$$
This works for conservative systems, but what happens when we want to simulate a block sliding to a halt due to friction? The standard action functional doesn't work, because the friction force is non-conservative.

Traditionally, [D'Alembert's Principle](https://en.wikipedia.org/wiki/D%27Alembert%27s_principle) is a generalization of the least action that allows any force, including non-conservative forces like friction. The idea is to add "virtual work" done from any additional force. So, 
$$
\left(
  \int_0^T \left(K(\bq, \dot{\bq}) - V(\bq)\right) dt
\right)^{\circ} 
= \underbrace{
  \int_0^T \left\langle \bf_{nc}(\bq, \dot{\bq}) \mid \mathring{\bq} \right\rangle dt
}_{\substack{\text{virtual work from} \\ \text{any additional} \\ \text{forces}}}
\implies 
\frac{d}{dt} \frac{\partial K}{\partial \dot{\bq}} - \frac{\partial K}{\partial \bq} = - \frac{\partial V}{\partial \bq} + \bf_{nc}
$$

# Definition (Rayleigh Dissipation Function)
Can't dissipative forces be written as a derivative of some function? In 1873 Rayleigh observed the following: Suppose we have some "linear viscous"[^1] force.
$$
m\ddot{\bq} = 
\underbrace{
  - \frac{\partial V}{\partial \bq}
}_{\substack{\text{conservative} \\ \text{force}}}
\;\;
\underbrace{
  - \bB\dot{\bq}
}_{\substack{\text{damping force} \\ \text{linear in} \\ \text{velocity}}}
$$

[^1]: Imagine running your hand through water. As you move faster, the force pushing back on your hand gets stronger. The same principle is true for air resistance and friction between surfaces.

This linear damping is actually the [[Calculus of Variations|variation]] of some (quadratic) function:
$$
\bB\dot{\bq} = \frac{\partial}{\partial \dot{\bq}} R(\dot{\bq})
$$
where 
$$
R(\dot{\bq}) = \frac{1}{2} \dot{\bq}^\top \bB \dot{\bq}
$$
is called the **Rayleigh Dissipation Function**. $\bB$ here is a constant number (or matrix). The thicker the fluid, the "larger" $\bB$. Indeed, the force depends on the velocity $\dot{\bq}$. Here we defined $R$ via the power rule. 

## Rayleigh's Euler-Lagrange Equation
We can derive the equations of motion for a system with Rayleigh dissipation by modifying the least action principle. Given kinetic energy $K(\bq, \dot{\bq})$, potential energy $V(\bq)$, and a **dissipation function** $R(\bq, \dot{\bq})$, we have 
$$
\underbrace{
  \frac{d}{dt} \frac{\partial K}{\partial \dot{\bq}}
}_{\substack{\text{change of} \\ \text{momentum}}}
\;\;
\underbrace{
  - \frac{\partial K}{\partial \bq}
}_{\substack{\text{fictitious} \\ \text{force}}}
=
\underbrace{- \frac{\partial V}{\partial \bq}
}_{\substack{\text{conservative} \\ \text{force}}}
\;\;
\underbrace{- \frac{\partial R}{\partial \dot{\bq}}
}_{\substack{\text{dissipative} \\ \text{force}}}
$$
with respect to velocity. This construction accurately reflects reality if the mapping $\dot{\bq} \mapsto R(\bq, \dot{\bq})$ satsifies the following properties:
1. The mapping must be convex (second derivative is nonnegative). As velocity increases, the dissipative force must reliably increase or remain constant. 
2. It must be zero at $\dot{\bq} = 0$. The dissipative force only acts when there is some velocity. 
3. It must be nonnegative otherwise. This ensures adherence to the second law of thermodynamics. The dissipative force should always be doing negative work, so the system should be losing energy.

## Related Works
- Helmholtz's minimal dissipation principle
- Originally, Rayleigh only considered quadratic $R$. 
- After 1970's (Moreau) discovered that other non-quadratic $R$ can recover nonlinear forces like Coulomb friction and plasticity.
- There is a natural time discretization (Kane, Marsden, Ortiz, West 1999).

## Remarks
We can apply [[Lagrangian Mechanics#Noether's Theorem of Time Independence|Noether's theorem for time independence]] 
$$
\frac{d}{dt} \left(
  \frac{\partial K}{\partial \dot{\bq}} \dot{\bq} - K + V 
\right)
= - \frac{\partial R}{\partial \dot{\bq}} \dot{\bq}
$$
If $K$ and $R$ are quadratic (highest order of the variable in exactly $2$) in $\dot{\bq}$, then 
$$
\frac{\partial K}{\partial \dot{\bq}} \dot{\bq} = 2K
\quad\text{and}\quad
\frac{\partial R}{\partial \dot{\bq}} \dot{\bq} = 2R
$$
such that 
$$
\frac{d}{dt} \left(
  K + V
\right) = - 2R
$$
To design dissipation, just model the rate of energy dissipation. 

# Interlude (Equations of Motion for Discrete Time Dissipation)
Let's try dropping the continuous time derivative and model the discrete time energy loss. For simplicity, assume $K(\bq, \dot{\bq}) = \frac{1}{2} \dot{\bq}^\top \bM \dot{\bq}$. The equation of motion is 
$$
\bM \ddot{\bq} = - \frac{\partial V}{\partial \bq} - \frac{\partial R}{\partial \dot{\bq}}
$$ 
Suppose the space of positions is given by $Q = \R^m$ where each point has coordinate $\bq = (q_1, \dots, q_m)^\top$. Suppose the inertia is independent of position $\bq$ and 
$$
\text{KineticEnergy}(\dot{\bq}) = \frac{1}{2} \dot{\bq}^\top \bM \dot{\bq}
$$
and the potential energy is $U = U(q_1, \dots, q_m)$. Then the equation of motion is 
$$
(\bM \ddot{\bq})_i = -(dU)_i = - \frac{\partial U}{\partial q_i}
$$

# Symplectic & Backward Euler with Dissipation
We can discretize time $t^{(n)} = n \Delta t$. Denote the state at the $n-$th step as $\bq^{(n)}$. We can approximate the second time derivative as
$$
(\ddot{\bq})^{(n)} \approx \frac{1}{\Delta t^2} 
\left(
  \bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}
\right)
$$
Given $\bq^{(n-1)}, \bq^{(n)}$, solve for $\bq^{(n+1)}$. We use the Euler method. 

Symplectic (explicit):
$$
\frac{1}{\Delta t^2}
\left(
  \bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}
\right)
= -\bM^{-1} (dU)|_{\bq^{(n)}}
$$
Backward (implicit):
$$
\frac{1}{\Delta t^2}
\left(\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}\right)
= -\bM^{-1} (dU)|_{\bq^{(n+1)}}
$$

## Example 1: Damped Harmonic Oscillator
We can try to simulate a damped spring. Recall the equations of motion for a spring and its solved form:
$$
\begin{cases}
\ddot{q} + \omega^2 q = 0 \\
q(t) = a\cos(\omega t) + b\sin(\omega t)
\end{cases}
$$
From [[#Interlude (Equations of Motion for Discrete Time Dissipation)|interlude]], $\bM^{-1} dU|_{\bq} = \omega^{2} \bq$. The symplectic form is 
$$
\begin{aligned}
\frac{1}{\Delta t^2} \left(\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}\right) 
&= -\bM^{-1} (dU)|_{\bq^{(n)}} \\
\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)} &= -\Delta t^2 \left( \omega^{2} \bq^{(n)} \right) \\
\bq^{(n+1)} &= -\Delta t^2 \left( \omega^{2} \bq^{(n)} \right) + 2\bq^{(n)} - \bq^{(n-1)} \\
\bq^{(n+1)} &= -\bq^{(n-1)} + \left(2 - \Delta t^2 \omega^2\right) \bq^{(n)} \\
\end{aligned}
$$
We can express this as a matrix multiplication:
$$
\begin{bmatrix}
\bq^{(n)} \\ \bq^{(n+1)}
\end{bmatrix}
=
\begin{bmatrix}
0 & 1 \\
-1 & 2 - \Delta t^2 \omega^2
\end{bmatrix}
\begin{bmatrix}
\bq^{(n-1)} \\ \bq^{(n)}
\end{bmatrix}
$$
The determinant of the square matrix is $1$, so the symplectic form is volume-preserving (area). Both eigenvalue norms are $1$ when $\Delta t^2 \omega^2 < 4$ (conditional stability).

The backward form is 
$$
\begin{aligned}
\frac{1}{\Delta t^2} \left(\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}\right) 
&= -\bM^{-1} (dU)|_{\bq^{(n+1)}} \\
% 
\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)} &= -\Delta t^2 \left( \omega^{2} \bq^{(n+1)} \right) \\
\bq^{(n+1)} &= -\bq^{(n-1)} + 2\bq^{(n)} - \Delta t^2 \left( \omega^{2} \bq^{(n+1)} \right) \\
\bq^{(n+1)} &= \frac{-\bq^{(n-1)} + 2\bq^{(n)}}{1 + \Delta t^2 \omega^2}
\end{aligned}
$$
and likewise, 
$$
\begin{bmatrix}
\bq^{(n)} \\ \bq^{(n+1)}
\end{bmatrix}
=
\begin{bmatrix}
0 & 1 \\
-\frac{1}{1 + \Delta t^2 \omega^2} & \frac{2}{1 + \Delta t^2 \omega^2}
\end{bmatrix}
\begin{bmatrix}
\bq^{(n-1)} \\ \bq^{(n)}
\end{bmatrix}
$$
The determinant of the square matrix is $< 1$ and so the area shrinks. All eigenvalue norms are $< 1$ for all $\Delta t^2 \omega^2$ (unconditional stability). 

## Minimal Incremental Potential Principle
We can exploit the unconditional stability of the backward Euler method to design a variational principle for discrete time dissipation. Recall the backward Euler method:
$$
\frac{1}{\Delta t^2} \left(\bq^{(n-1)} - 2\bq^{(n)} + \bq^{(n+1)}\right) 
= -(dU)|_{\bq^{(n+1)}}
$$
Let's rearrange with $\bq_{\text{pred}} := 2\bq^{(n)} - \bq^{(n-1)}$. 
$$
\frac{1}{\Delta t^2} \left(\bq^{(n+1)} - \bq_{\text{pred}}\right) 
+ (dU)|_{\bq^{(n+1)}}
= 0
$$
This is actually an **optimality condition** for the following optimization problem:
$$
\bq^{(n+1)} = \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} + U(\bq)
\right)
$$
Sneakily, $\text{pred}$ stands for "predicted position". 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]

% Define custom colors to match the image
\definecolor{darkblue}{RGB}{45, 90, 160}
\definecolor{lightblue}{RGB}{150, 190, 240}
\definecolor{turquoise}{RGB}{50, 160, 150}

% Coordinates of the points
\coordinate (N1) at (0, 0);
\coordinate (N2) at (1.3, 0.9);
\coordinate (N3) at (2.6, 1.8);
\coordinate (N4) at (2.8, 1.2);

% --- Draw Connecting Lines and Arrow ---
% Dark blue straight line
\draw[darkblue, ultra thick] (N1) -- (N2);
% Dark blue arrow pointing up and right
\draw[darkblue, ultra thick, ->] (N2) -- (N3);
% Thin dashed black line
\draw[black, dashed, thin] (N3) -- (N4);

% --- Draw Nodes (circles) ---
% Dark blue nodes
\fill[darkblue] (N1) circle (3pt);
\fill[darkblue] (N2) circle (3pt);
% Light blue node
\fill[lightblue] (N3) circle (3pt);
% Turquoise node
\fill[turquoise] (N4) circle (3pt);

% --- Place Labels with Correct Colors and LaTeX Math ---
% q^{(n-1)} in dark blue, to the upper-left of N1
\node[anchor=south east, color=darkblue, xshift=-1pt, yshift=1pt] at (N1) {\Large $\mathbf{q}^{(n-1)}$};
% q^{(n)} in dark blue, to the upper-left of N2
\node[anchor=south east, color=darkblue, xshift=-1pt, yshift=1pt] at (N2) {\Large $\mathbf{q}^{(n)}$};
% q_{pred} in light blue, to the upper-left of N3
\node[anchor=south east, color=lightblue, xshift=-1pt, yshift=1pt] at (N3) {\Large $\mathbf{q}_{\text{pred}}$};
% q^{(n+1)} in turquoise, to the lower-right of N4
\node[anchor=north west, color=turquoise, xshift=1pt, yshift=-1pt] at (N4) {\Large $\mathbf{q}^{(n+1)}$};

\end{tikzpicture}
\end{document}
```

In terms of velocity, we can write
$$
\begin{aligned}
\bv_{\text{new}} &= \frac{1}{\Delta t} \left(\bq^{(n+1)} - \bq^{(n)}\right) \\
\bv_{\text{old}} &= \frac{1}{\Delta t} \left(\bq^{(n)} - \bq^{(n-1)}\right) \\
\end{aligned}
$$
with the following visualization:
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1]

% Define custom colors to match the image
\definecolor{darkblue}{RGB}{45, 90, 160}
\definecolor{lightblue}{RGB}{150, 190, 240}
\definecolor{turquoise}{RGB}{50, 160, 150}

% Coordinates of the points
\coordinate (N1) at (0, 0);
\coordinate (N2) at (1.5, 0.8);
\coordinate (N3) at (3.0, 1.8);
\coordinate (N4) at (3.2, 1.0);

% --- Draw Connecting Lines and Arrows ---
% Dark blue straight line
\draw[darkblue, ultra thick] (N1) -- (N2);

% Dark blue arrow pointing up and right (with label inline)
\draw[darkblue, ultra thick, ->] (N2) -- (N3) node[midway, above left, xshift=4pt] {\Large $\mathbf{v}_{\text{old}}$};

% Turquoise arrow pointing right (with label inline)
\draw[turquoise, ultra thick, ->] (N2) -- (N4) node[midway, below right, xshift=-4pt, yshift=0pt] {\Large $\mathbf{v}_{\text{new}}$};

% Dotted black connecting line
\draw[black, dashed, thin] (N3) -- (N4);

% --- Draw Nodes (circles) ---
% Dark blue nodes
\fill[darkblue] (N1) circle (3pt);
\fill[darkblue] (N2) circle (3pt);
% Light blue node
\fill[lightblue] (N3) circle (3pt);
% Turquoise node
\fill[turquoise] (N4) circle (3pt);

% --- Place Labels ---
% q^{(n-1)} in dark blue, to the upper-left of N1
\node[anchor=south east, color=darkblue, xshift=-1pt, yshift=1pt] at (N1) {\Large $\mathbf{q}^{(n-1)}$};
% q^{(n)} in dark blue, to the upper-left of N2
\node[anchor=south east, color=darkblue, xshift=-2pt, yshift=1pt] at (N2) {\Large $\mathbf{q}^{(n)}$};
% q_{pred} in light blue, to the upper-left of N3
\node[anchor=south east, color=lightblue, xshift=-1pt, yshift=1pt] at (N3) {\Large $\mathbf{q}_{\text{pred}}$};
% q^{(n+1)} in turquoise, to the lower-right of N4
\node[anchor=north west, color=turquoise, xshift=1pt, yshift=-1pt] at (N4) {\Large $\mathbf{q}^{(n+1)}$};

\end{tikzpicture}
\end{document}
```

So, the physical system will decide its new velocity by 
$$
\bv_{\text{new}} = \argmin_{\bv \in \R^m} \left(
  \frac{1}{2} \|\bv - \bv_{\text{old}}\|^{2}_{\bM} + U\left(\bq^{(n)} + \Delta t \bv\right)
\right)
$$

This equation is called the **minimal incremental potential principle**. In particular, the terms compete with one another: ^ba4064
1. The intertia term. It encourages the new velocity to be close to the old velocity. So any deviation from $\bv_{\text{old}}$ is penalized, scaled by the mass matrix $\bM$.
2. The potential term. The object is drawn toward lower energy states like falling under gravity or a spring returning to its rest position.

The true physical path is simply the exact velocity vector that minimizes the sum of these two penalties. Indeed, this means calculating the velocity for every time step requires a good numerical optimizer. 

For collision and contact, we can add "smooth barrier" functions in potential and perform optimization properly. 
$$
b(d, \hat{d}) = \begin{cases}
-\left(d - \hat{d}\right)^2 \ln\left(  \frac{d}{\hat{d}} \right) & \text{if } d < \hat{d} \\
0 & \text{if } d \geq \hat{d}
\end{cases}
$$
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[x=4.5cm, y=1.6cm, >=stealth]

% --- Safe Color Definitions ---
\definecolor{cdisc}{HTML}{1F78B4}   
\definecolor{cd1}{HTML}{D95F02}       
\definecolor{cd08}{HTML}{E6AB02}     
\definecolor{cd05}{HTML}{7570B3}   

% --- Grid and Axes ---
\draw[gray!70] (0,0) -- (1.6,0);
\draw[gray!70] (0,0) -- (0,3.6);

% X-ticks
\foreach \x in {0, 0.5, 1, 1.5} {
    \draw[gray!70] (\x, 0) -- (\x, -0.05);
    \node[below] at (\x, -0.05) {\x};
}

% Y-ticks
\foreach \y in {0, 1, 2, 3} {
    \draw[gray!70] (0, \y) -- (-0.02, \y);
    \node[left] at (-0.02, \y) {\y};
}

% Axis Labels
\node[below, yshift=-5pt] at (0.75, -0.2) {Distance};
\node[rotate=90, above, yshift=5pt] at (-0.1, 1.75) {Barrier energy};

% --- Function Plots ---
\begin{scope}
    % Clip the plotting area so asymptotic curves don't bleed out the top
    \clip (0, 0) rectangle (1.6, 3.6);

    % 1. Discontinuous (Blue L-shape)
    \draw[line width=1.2pt, cdisc] (0, 3.6) -- (0, 0.03) -- (1.6, 0.03); 

    % 2. C2, d = 1 (Orange)
    \draw[line width=1.2pt, cd1, domain=0.03:1, samples=100] plot (\x, {-(\x-1)*(\x-1)*ln(\x)});
    \draw[line width=1.2pt, cd1] (1, 0.02) -- (1.6, 0.02);

    % 3. C2, d = 0.8 (Yellow)
    \draw[line width=1.2pt, cd08, domain=0.03:0.8, samples=100] plot (\x, {-(\x-0.8)*(\x-0.8)*ln(\x/0.8)});
    \draw[line width=1.2pt, cd08] (0.8, 0.01) -- (1.6, 0.01);

    % 4. C2, d = 0.5 (Purple)
    \draw[line width=1.2pt, cd05, domain=0.03:0.5, samples=100] plot (\x, {-(\x-0.5)*(\x-0.5)*ln(\x/0.5)});
    \draw[line width=1.2pt, cd05] (0.5, 0) -- (1.6, 0);
\end{scope}

% --- Vertical Dashed Markers ---
\draw[dashed, cd1, thick] (1, 0) -- (1, 1);
\draw[dashed, cd08, thick] (0.8, 0) -- (0.8, 1);
\draw[dashed, cd05, thick] (0.5, 0) -- (0.5, 1);

% --- Legend ---
\begin{scope}[shift={(0.8, 3.3)}]
    \draw[line width=1.2pt, cdisc] (0, 0) -- (0.15, 0) node[right, text=black] {discontinuous};
    \draw[line width=1.2pt, cd1] (0, -0.35) -- (0.15, -0.35) node[right, text=black] {C2, $\hat{d}=1$};
    \draw[line width=1.2pt, cd08] (0, -0.7) -- (0.15, -0.7) node[right, text=black] {C2, $\hat{d}=0.8$};
    \draw[line width=1.2pt, cd05] (0, -1.05) -- (0.15, -1.05) node[right, text=black] {C2, $\hat{d}=0.5$};
\end{scope}

\end{tikzpicture}
\end{document}
```

# Adding Dissipation
Recall the backward Euler update on conservative systems:
$$
\bq^{(n+1)} = \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} + U(\bq)
\right)
$$
where $\bq_{\text{pred}} = 2\bq^{(n)} - \bq^{(n-1)}$. We can add dissipation by adding a **Rayleigh dissipation funtion**:
$$
\bq^{(n+1)} = \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} 
  + \underbrace{
  U(\bq)
  + (\Delta t) R\left(\bq^{(n)}, \frac{\bq - \bq^{(n)}}{\Delta t}\right)
  }_{\text{Effective Incremental Potential}}
\right)
$$
Equivalently, 
$$
\bv_{\text{new}} = \argmin_{\bv \in \R^m} \left(
  \frac{1}{2} \|\bv - \bv_{\text{old}}\|^{2}_{\bM} 
  + \underbrace{
    U\left(\bq^{(n)} + \Delta t \bv\right)
  + (\Delta t) R\left(\bq^{(n)}, \bv\right)
  }_{\text{Effective Incremental Potential}}
  \right)
$$
The third term also competes with the first two [[#^ba4064|terms]]. It is the *dissipation penalty*. The object wants to minimize the energy it bleeds out into the environment (i.e. heat from friction). Because $R$ is zero when velocity is zero, this term effectively pulls the optimal velocity closer to zero. 

Writing the system in $F=ma$, 
$$
\bM \frac{\bv_{\text{new}} - \bv_{\text{old}}}{\Delta t} = 
- \frac{\partial U}{\partial \bq} - \frac{\partial R}{\partial \bv}
$$

> [!note] Places to use a quadratic dissipation function
> 1. Car's shock absorber. It is a piston pushing through oil (or a viscous fluid). It restructs motion proportional to velocity.
> 2. Lubricated sliding. Two metal plates separated by a thin layer of oil. It creates a smooth, linear drag force. 

## Quasi-Static System
To study a dissipative system, we often consdier a **quasi-static regime**, where inertia is negligible. In this case, the system is in balance with potential force and external force at all times. So,
$$
\begin{aligned}
\xcancel{\bM \frac{\bv_{\text{new}} - \bv_{\text{old}}}{\Delta t}} 
&= - \frac{\partial U}{\partial \bq} - \frac{\partial R}{\partial \bv} \\
% 
\frac{\del R}{\del \bv} &= - \frac{\del U}{\del \bq} + \bf_{\text{ext}} \\
\end{aligned}
$$
For quadratic $R$, this determines a "terminal velocity" that the system will eventually reach. 

> [!idea] Intuition
> We can think of dragging a heavy block through thick mud (or an extremely viscous fluid). The block never really accelerates nor does it carry momentum. It's speed is dictated by how hard it is pulled against the mud's resistance. When the block is no longer being pulled, it stops.
> 
> This is as if the mass $\bM$ approaches zero (because we basically have zero momentum). This is why it is "quasi-static", because it's kind of still (static) but not quite (quasi).
>
> Importantly, the crossed out penalty term vanishes. 

Traditionally, for solving a general force, we solve some kind of relation between $\bf, \bq, \bv$. Here, $\bf_{\text{ext}}$ is an ireversible force that is *not* a function of $\bq$. 

## Dry Friction 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]

% --- Define Colors ---
\definecolor{topblue}{RGB}{135, 206, 250}
\definecolor{bottomgray}{RGB}{128, 128, 128}
\definecolor{highlightorange}{RGB}{255, 165, 0}
\definecolor{forcepurple}{RGB}{60, 0, 90} 

% =========================================================
% === Left Part: Macro View ===
% =========================================================

% Draw main blocks 
\filldraw[fill=topblue, draw=black, thick] (-4.5, 0.5) rectangle (-1.5, 1.5);
\filldraw[fill=bottomgray, draw=black, thick] (-4.5, -0.5) rectangle (-1.5, 0.5);

% Macro movement arrows
\draw[->, dashed, ultra thick] (-3.5, 1.7) -- (-1.8, 1.7);
\draw[->, dashed, ultra thick] (-2.5, -0.7) -- (-4.2, -0.7);

% Macro zoom box (Orange, dashed)
\draw[draw=highlightorange, dashed, thick] (-1.95, 0.3) rectangle (-1.65, 0.7);

% =========================================================
% === Right Part: Micro View (Zoomed Interface) ===
% =========================================================

% Micro View Border
\draw[draw=highlightorange, dashed, thick] (0, -1) rectangle (4, 2.5);

% Coordinates for the jagged interface
% Gray block surface (bottom)
\coordinate (G1)  at (0.5, 0.8);
\coordinate (GV1) at (1.0, 0.1);
\coordinate (G2)  at (1.5, 0.9);
\coordinate (GV2) at (2.0, 0.3);
\coordinate (G3)  at (2.5, 1.0);
\coordinate (GV3) at (3.0, 0.5);
\coordinate (G4)  at (3.5, 0.9);

% Blue block surface (top)
\coordinate (B1)  at (0.5, 0.9);
\coordinate (BV1) at (0.8, 0.2);
\coordinate (B2)  at (1.5, 1.0);
\coordinate (BV2) at (1.8, 0.4);
\coordinate (B3)  at (2.5, 1.1);
\coordinate (BV3) at (2.8, 0.6);
\coordinate (B4)  at (3.5, 1.0);

% Fill Gray Area (bottom)
\filldraw[fill=bottomgray, draw=black, thick] (0,-1) -- (0, 0.4) -- (G1) -- (GV1) -- (G2) -- (GV2) -- (G3) -- (GV3) -- (G4) -- (4, 0.5) -- (4,-1) -- cycle;

% Fill Blue Area (top)
\begin{scope}
  \clip (0,-1) rectangle (4, 2.5);
  \filldraw[fill=topblue, draw=black, thick] (0, 2.5) -- (0, 0.6) -- (B1) -- (BV1) -- (B2) -- (BV2) -- (B3) -- (BV3) -- (B4) -- (4, 0.6) -- (4, 2.5) -- cycle;
\end{scope}

% =========================================================
% === Details: Arrows, Points, Labels, Zoom Line ===
% =========================================================

% Connecting zoom arrow from macro to micro
\draw[->, highlightorange, thick] (-1.65, 0.5) to[out=45, in=150] (0, 1.8);

% Labels A-F (Yellow text)
\node[text=yellow, font=\bfseries] at (0.5, 0.55) {A};
\node[text=yellow, font=\bfseries] at (1.5, 0.65) {B};
\node[text=yellow, font=\bfseries] at (2.0, 0.5) {C};
\node[text=yellow, font=\bfseries] at (2.5, 0.75) {D};
\node[text=yellow, font=\bfseries] at (3.5, 0.65) {E};
\node[text=white, font=\bfseries] at (3.85, 0.65) {F}; % White for visibility on gray

% Force Arrows (Purple) and Contact points (Red circles)
\foreach \x/\y in {0.5/0.8, 1.5/0.9, 2.5/1.0, 3.5/0.9} {
    \fill[red] (\x, \y) circle (2pt);
    \draw[->, forcepurple, thick] (\x - 0.3, \y + 0.6) -- (\x, \y);
    \draw[->, forcepurple, thick] (\x + 0.3, \y - 0.6) -- (\x, \y);
}

% Micro movement arrows (top and bottom)
\draw[->, dashed, ultra thick] (1.5, 2.7) -- (3.0, 2.7);
\draw[->, dashed, ultra thick] (2.5, -1.2) -- (1.0, -1.2);

\end{tikzpicture}
\end{document}
```

We have some laws of friction:
- **Amonton's 1st law**: friction force is proportional to the normal force
- **Amonton's 2nd law**: friction force is independent of the contact area
- **Coulomb's law**: Once the motion starts, the friction force is independent of velocity.

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[x=1cm, y=1cm, scale=0.8, >=stealth]

% Define dark red for the arrows to better match the image
\definecolor{darkred}{RGB}{160, 10, 10}

% --- Ground Plane ---
\draw[ultra thick] (-3, -0.6) -- (3, -0.6);

% --- Upward Pointing Cone Area (Drawn FIRST so it renders behind the block) ---
% Fixed: Using absolute polar coordinates to ensure perfect symmetry
\fill[olive!20] (0, 0) -- (60:4.5) -- (120:4.5) -- cycle;

% --- Dashed Cone Outline ---
\draw[dashed, thick] (0, 0) -- (60:4.5);
\draw[dashed, thick] (0, 0) -- (120:4.5);

% --- Rectangular Block ---
\filldraw[fill=lightgray, draw=black, thick] (-1.0, -0.6) rectangle (1.0, 0.5);

% --- Center Point ---
\fill[black] (0, 0) circle (3pt);

% --- Vector Forces (all originating from center point) ---

% External Force (f_ext, horizontal-left)
\draw[->, darkred, ultra thick] (0, 0) -- (-2.2, 0);
\node[anchor=south, scale=1.4, darkred] at (-2.0, 0.1) {$\mathbf{f}_{ext}$};

% Gravitational Force (mg, vertical-down)
\draw[->, darkred, ultra thick] (0, 0) -- (0, -2.5);
\node[anchor=west, scale=1.4, darkred] at (0.1, -1.8) {$m\mathbf{g}$};

% Contact Force (f_c, slanted upward-left, inside the cone)
\draw[->, darkred, ultra thick] (0, 0) -- (110:2.8);
\node[anchor=south east, scale=1.4, darkred] at (110:2.8) {$\mathbf{f}_c$};

% --- Cone Label ---
% Placed along the right edge of the cone
\node[scale=2, black] at (60:3.5) [xshift=10pt, yshift=5pt] {$\mathcal{C}$};

\end{tikzpicture}
\end{document}
```

The force $\bf_{c}$ at contact lies in a **friction cone** (in the [[Dual Space#Definition (Dual Space)|dual space]] at contact). 
- At each point of contact, we have an outward normal ([[Dual Space#Definition (Covector)|covector]]) $\bn$. 
- The relative velocity between contact should satisfy $\langle \bn | \bv \rangle \geq 0$. 
- The normal ($\bf^{\perp}$) and tangent part ($\bf^{||}$) of the contact force, and tangent velocity ($\bv^{||}$) should satisfy the following relations:
  $$
  |\bf^{||}| \leq \mu \bf^{\perp} 
  \quad\quad\quad
  |\bf^{||}| < \mu \bf^{\perp} \iff \bv^{||} = 0
  $$
  where $\mu$ is the coefficient of friction. In the image above, $\mu$ dictates the width of the friction cone.
- When the tangent velocity is nonzero, the tangent force is in the same direction with it $\alpha \bf^{||} = \flat_{\R^3} \bv, \alpha \geq 0$

From physics, these two relations are merely:
1. **Static Friction** (stuck): If the required tangential force (the force pushing the object to the right) is strictly less than the boundary of the cone, the object is perfectly stuck and thus has zero tangential velocity.
2. **Kinetic Friction** (sliding): If the external push exceeds the cone's edge, the friction force maxes out at the cone boundary $|\bf^{||}| = \mu |\bf^{\perp}|$. The object begins to slide and the friction force points in the exact opposite direction of the motion. 

## Classical Approach for Contact
Suppose we want to model how a [[Rigid Body Dynamics#Rigid Body Kinematics|rigid body]] comes into contact with a wall or some other object. We first establish a set of points $\bp_i$ that will be in contact. Then 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]

% --- Color Palette ---
\definecolor{darkblue}{RGB}{34, 75, 139}
\definecolor{lightblue}{RGB}{128, 164, 214}
\definecolor{mypurple}{RGB}{121, 74, 154}
\definecolor{myteal}{RGB}{64, 160, 150}
\definecolor{blockblue}{RGB}{48, 101, 163}

% ==========================================
% Left Column (parameters for motion)
% ==========================================

% Header
\node[font=\sffamily\large, text=black] at (0, 4) {parameters for motion};

% Equations
\node[darkblue, font=\Large] at (0, 3.0) {$(\mathbf{c}, \mathbf{R}) \in Q$};
\node[darkblue, font=\Large] at (0, 1.8) {$(\dot{\mathbf{c}}, \dot{\mathbf{R}}) \in T_{(\mathbf{c}, \mathbf{R})}Q$};
\node[darkblue, font=\Large] at (0, 0.8) {$(\ddot{\mathbf{c}}, \ddot{\mathbf{R}}) \in T_{(\mathbf{c}, \mathbf{R})}Q$};

% Bottom Equation (T*)
\node[lightblue, font=\Large] at (-0.5, -1.2) {$T^*_{(\mathbf{c}, \mathbf{R})}Q$};

% Upward Arrow M^{-1}
\draw[->, ultra thick, black] (-0.5, -0.6) -- (-0.5, 0.4) node[midway, left=2pt, font=\Large] {$\mathbf{M}^{-1}$};


% ==========================================
% Middle Arrows (Mappings)
% ==========================================

% phi arrow
\draw[->, ultra thick, black] (1.8, 3.0) -- (2.8, 3.0) node[midway, above=2pt, font=\Large] {$\phi$};

% d(phi) arrow
\draw[->, ultra thick, black] (1.8, 1.8) -- (2.8, 1.8);
\node[font=\Large, black] at (2.5, 1.3) {$d\phi$};

% Dotted separator line
\draw[ultra thick, dotted, black] (4.5, 1.1) -- (4.5, -0.2);

% d(phi)* arrow
\draw[<-, ultra thick, black] (1.8, -1.2) -- (2.8, -1.2);
\node[font=\Large, black] at (2.5, -0.7) {$d\phi^*$};


% ==========================================
% Right Column (space of contact)
% ==========================================

% Header
\node[font=\sffamily\large, text=black] at (5.5, 4) {space of contact};

% Equations
\node[mypurple, font=\Large, anchor=west] at (3.2, 3.0) {$(\mathbf{p}_1, \cdots, \mathbf{p}_k) \in \mathbb{R}^3 \times \cdots \times \mathbb{R}^3$};
\node[mypurple, font=\Large, anchor=west] at (3.2, 1.8) {$(\dot{\mathbf{p}}_1, \cdots, \dot{\mathbf{p}}_k) \in \mathbb{R}^3 \times \cdots \times \mathbb{R}^3$};

% Bottom Equations (Forces)
\node[myteal, font=\Large, anchor=west] at (3.2, -1.2) {$(\mathbf{f}_1, \dots, \mathbf{f}_k) \in \mathcal{C}_1 \times \cdots \times \mathcal{C}_k$};
\node[myteal, font=\Large, anchor=west] at (5.0, -2.2) {$\subset \mathbb{R}^{3*} \times \cdots \times \mathbb{R}^{3*}$};


% ==========================================
% Graphic (Physics Diagram)
% ==========================================

\begin{scope}[shift={(1.0, 0)}] % Shift graphic slightly right to balance visual space
    
    % Gray Wall (Drawn first so it stays in background)
    \fill[lightgray] (8.0, -2.2) rectangle (13.2, -1.5); % Floor
    \fill[lightgray] (12.5, -1.5) rectangle (13.2, 3.5); % Right Wall

    % Semi-transparent sweeps/trails (showing motion down the wall)
    \fill[myteal, opacity=0.15] (11.0, -1.5) -- (10.0, -0.2) -- (11.5, 2.5) -- (12.5, 1.5) -- cycle;
    \fill[myteal, opacity=0.15] (11.0, -1.5) -- (10.5, -0.8) -- (11.8, 2.0) -- (12.5, 1.5) -- cycle;

    % Solid Blue Rigid Body Block
    % Geometry calculated manually: length ~3.35, width ~0.8, angled perfectly between contact points
    \fill[blockblue] (11.0, -1.5) -- (12.5, 1.5) -- (11.78, 1.86) -- (10.28, -1.14) -- cycle;

    % Contact Points (Purple Dots)
    \fill[mypurple] (11.0, -1.5) circle (4.5pt); % Bottom Contact p1
    \fill[mypurple] (12.5, 1.5) circle (4.5pt);  % Top Contact p2

    % Contact Labels
    \node[mypurple, below=6pt, font=\huge] at (11.0, -1.5) {$\mathbf{p}_1$};
    \node[mypurple, above left=6pt, font=\huge] at (12.5, 1.5) {$\mathbf{p}_2$};

\end{scope}

\end{tikzpicture}
\end{document}
```

This is computationally miserable. When a 3D object hits the floor, we have to keep track of the object's state $(\bc, \bR) \in Q$ and the contact space where the objects touch $(\bp_1, \dots, \bp_k) \in \R^3 \times \dots \times \R^3$. To know if an object is sliding or stuck, we need to view the object's linear and angular velocity $(\dot{\bc}, \dot{\bR})$ and map that to 3D velocities at every single contact point $(\dot{\bp}_1, \dots, \dot{\bp}_k)$.

This translation is done via the [[Jacobian]] denoted by $d\phi$. Conversely, the floor pushes back on those chair legs by friction and normal forces $(\bf_1, \dots, \bf_k)$. To know how those forces affect the chair's motion, we need to map the net force and net torque back to the cneter of pass. This is done via the dual (tranpose, since $\R^3$) of the Jacobian, denoted by $d\phi^*$.

We then need to solve for velocity and contact forces so that all conditions are satisfied. Because the body is rigid, all the particles are connected.
1. The friction force at point $\bp_1$ depends on its velocity.
2. But its velocity depends on the total rotation of the chair.
3. The total rotation of the chair depends on the forces pushing up on points $\bp_2, \bp_3, \bp_4$. 

Obviously, we cannot calculate them all in closed form. This is called the **Linear Complementarity Problem (LCP)**. The solver would have to guess if each point is stuck, sliding, or lifting off the ground. 

## Dissipation Function for Dry Friction
We can take a variational approach to dry friction.
$$
\begin{aligned}
\bM \frac{\bv_{\text{new}} - \bv_{\text{old}}}{\Delta t} &= 
- \frac{\partial U}{\partial \bq} - \frac{\partial R}{\partial \bv} \\
R(\bv) &= \mu|\bv|
\end{aligned}
$$

# Newmark Algorithm
We initally chose the Backward Euler method for its simplicity and unconditional stability. However, it is only "first order" accurate, meaning it introduces a lot of numerical error over time. 

Recall the backward Euler update:
$$
\bq^{(n+1)} = \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} 
  + U(\bq)
  + \Delta t R\left(\bq^{(n)}, \frac{\bq - \bq^{(n)}}{\Delta t}\right)
\right)
$$
where $\bq_{\text{pred}} := 2\bq^{(n)} - \bq^{(n-1)}$. The $\bq_{\text{pred}}$ assumes the object will continue moving at the same velocity as before, ignoring forces and acceleration. 

Now, let the incremental potential be
$$
\tilde{U}^{(n)}\left( \bq^{(n+1)} \right)
= U\left(\bq^{(n+1)}\right) 
+ \Delta t R\left((1-s)\bq^{(n)} + s\bq^{(n+1)}, \frac{\bq^{(n+1)} - \bq^{(n)}}{\Delta t}\right)
$$
The acceleration at current time can be read off from 
$$
\ba^{(n)} = \bM^{-1} \frac{\partial \tilde{U}^{(n)}\left(\bq^{(n)}\right)}{\partial \bq^{(n)}} 
$$
Velocity can be kept track of by 
$$
\bv^{(n)} = \bv^{(n-1)} + \Delta t\left( 
  (1 - \gamma) \ba^{(n-1)} + \gamma \ba^{(n)}
\right)
$$
$\gamma$ is a parameter that controls how much we trust the current acceleration $\ba^{(n)}$ vs the previous acceleration $\ba^{(n-1)}$. The prediction of the next time step 
$$
\bq_{\text{pred}}^{(n+1)}
:= \bq^{(n)} + \Delta t \bv^{(n)} + \frac{\Delta t^2}{2} (1 - 2\beta) \ba^{(n)}
$$
If we ignore the $\beta$ parameter for a moment, this prediction is actually the classic kinematic equation from basic physiscs, $x = x_0 + v + \frac{1}{2} at^2$. We are basically predicting the next position using the current velocity and current acceleration.

We then solve an optimization problem like before,
$$
\bq^{(n+1)} = \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} 
  + \beta \tilde{U}^{(n)}(\bq)
\right)
$$
This is the **Newmark algorithm**.

# Numerical Optimization for Contact
Since we have a variational formulation for contact and have shown that is simply an optimization problem, we can solve for contact forces and velocities using numerical optimization. This is a more direct approach than the classical LCP formulation.

Using the smooth barrier and dissipation function, every time step is actually one unconstrained optimization problem
$$
\operatorname*{minimize}_{\bx \in \R^m} \mathcal{L}(\bx)
$$
Here, $\bx$ may be velocity or position 
$$
\begin{aligned}
\bq^{(n+1)} &= \argmin_{\bq \in \R^m} \left(
  \frac{1}{2\Delta t^2} \|\bq - \bq_{\text{pred}}\|^{2}_{\bM} 
  + U(\bq)
  \right) \\
  % 
\bv_{\text{new}} &= \argmin_{\bv \in \R^m} \left(
  \frac{1}{2} \|\bv - \bv_{\text{old}}\|^{2}_{\bM} 
  + U\left(\bq^{(n)} + \Delta t \bv\right)
  \right)
\end{aligned}
$$
Note that the initial guess (from the state of the previous time frame) for optimization is usually very close to the optimizer. We can use [[Gradient#Second-Order Taylor Expansion|gradient descent]] using some metric $\flat = \bH$. 
$$
\bx^{(n+1)} \leftarrow \bx^{(n)} - \alpha \sharp(d\mathcal{L})_{\bx^{(n)}}
= \bx^{(n)} - \alpha \bH^{-1} 
\begin{bmatrix}
\partial \mathcal{L} / \partial x_1 \\
\vdots \\
\partial \mathcal{L} / \partial x_m \\
\end{bmatrix}
$$
Now, we just need to choose a good $\bH$ and a step size $\alpha > 0$. 
- Classic gradient descent uses $\bH = \bI$ and a small step size $\alpha$. This is very stable but can be slow to converge.
- Newton's method uses $\bH = \text{Hessian}(\mathcal{L})$. 
- Quasi-Newton methods use an approximation of the Hessian.
- Use line search for choosing $\alpha$. 