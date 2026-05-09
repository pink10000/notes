---
tags:
  - CSE_291G
---

# Applying Lagrangian Mechanics
From [[Rigid Body Dynamics]] we learned that a mechanical system is described by generalized coordinates $\bq$, velocities $\dot{\bq}$, and [[Lagrangian Mechanics#Definition (The Lagrangian)|Lagrangian]] $L(\bq, \dot{\bq}) = K - U$. Real motion is one that satisfies the [[Lagrangian Mechanics#Least Action Principle|Least Action Principle]]/[[Calculus of Variations#Euler-Lagrange Equation|Euler-Lagrange Equations]]. For rigid bodies, $\bq$ is not just a vector in $\R^{n}$ but inside configuration space $\SE(3)$. 

The theme was that mechanics is geometry (linear algebra) plus variational principles (calculus). This document takes that idea and applies it numerically to simulate physics.
# Simple Numerical Methods
Standard numerical methods for solving ODEs (e.g. [[Numerical Methods#Forward Euler Method|Forward Euler Method]], or [[Numerical Methods#Runge-Kutta Method (RK4)|RK4]]) look at $F = ma$ at a specific point in time and try to blindly guess the next geometric slope. A **variational integrator** is a numerical method that tries to preserve the underlying geometric structure of the system. It defines the total physical energy of the system across a span of time ("discrete action") and uses calculus to find the trajectory that minimizes this energy over time (least action paths). 

In particular, we see that in [[Numerical Methods#Example 1.2 (2nd Order Discretization)|this example]], when $\Delta t$ is larger (i.e. $0.9$), the system is stable in "asteroid belts". Although the system is a good approximation, as it never explodes, it is still only an approximation. We can improve the accuracy of the system by replacing the RHS of the example with 
$$
\frac{\theta_{i+1} - 2\theta_i + \theta_{i-1}}{\Delta t^2}
= 4 \arg \left(
  1 + \frac{\Delta t^2}{4} e^{-i\theta_i}
\right)
$$
where $\arg$ calculates the angle of a [[Complex Numbers|complex number]] in the complex plane. The result is that the system is stable for all $\Delta t$, and removes the "asteroid belts" that we see in the previous example. 

![[numerical_methods_comparison.png]]

This image represents the exact trajectories on the position-momentum plane, where $\bq$ is the $x-$axis and $\dot{\bq}$ is the $y-$axis.
# Störmer-Verlet Method
What if instead of discretizing an ODE, what if we discretize the action and take the [[Calculus of Variations|variational derivative]] to get the equations of motion? 

> [!idea] Main Idea
> Standard numerical methods look at the slope of the next discretized point. A variational integrator says "among all discrete paths, which one makes the discrete action stationary?"

Let $h$ denote the discrete timestep. A discrete [[Lagrangian Mechanics#Definition (The Lagrangian)|Lagrangian]] is a function 
$$
L_{h} : Q \times Q \to \R
$$
approximating the total action between two positions. The continuous Lagrangian is Kinetic Energy minus Potential Energy: 
$$
L(\bq, \dot{\bq}) = \frac{m}{2} |\dot{\bq}|^2 - U(\bq) 
$$
Since we simulate this, time is broken up into steps of size $h$. The discrete Lagrangian via the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) (from Calculus 1!) is:
$$
\begin{aligned}
L_h (\bq_i, \bq_{i+1}) 
&= \frac{h}{2} \left( 
  L\left(\bq_i, \frac{\bq_{i+1} - \bq_i}{h}\right) + L\left(\bq_{i+1}, \frac{\bq_{i+1} - \bq_i}{h}\right)
\right) \\ 
&= \frac{mh}{2} \left| \frac{\bq_{i+1} - \bq_i}{h} \right|^2 - \frac{h}{2} \left( U(\bq_i) + U(\bq_{i+1}) \right) \\
\end{aligned}
$$
So, the discrete [[Lagrangian Mechanics#Least Action Principle|total action of a path]] is 
$$
S_{h} (\bq_0, \ldots, \bq_N) = \sum_{k=0}^{N-1} L_h (\bq_k, \bq_{k+1})
$$
or the sum of all the discrte Lagrangian segments. Remember, we want to find the minimum of these segments.

> [!note] Functional
> Recall that this is the *total action functional* seen in [[Calculus of Variations#Euler-Lagrange Equation|here]] but discretized (approximating a curve with $N$ small segments)!

By the discrete [[Lagrangian Mechanics#Theorem (Least Action Principle)|least action principle]], $\frac{\del S_{h}}{\del \bq_k} = 0$ for all $k$. We can derive this similar to how we showed the LAP. Let 
$$
S = \sum_{k=0}^{N-1} L_h (\bq_k, \bq_{k+1}) 
$$
Then to apply LAP, we need to find a stationary point where small pertubations to the path do not change the total action. We need to find the first *variation* (the derivative via multivariable chain rule) denoted as $\mathring{S}$ and setting it to $0$. 
$$
\mathring{S} 
= \sum_{k=0}^{N-1} D_1 L_h (\bq_k, \bq_{k+1}) \cdot \mathring{\bq}_k 
+ \sum_{k=0}^{N-1} D_2 L_h (\bq_k, \bq_{k+1}) \cdot \mathring{\bq}_{k+1}
$$
The second term can be rewritten as
$$
\sum_{k=1}^{N-1} D_2 L_h (\bq_{k-1}, \bq_k) \cdot \mathring{\bq}_k
$$
such that
$$
\mathring{S}
= \sum_{k=1}^{N-1} \left( D_1 L_h (\bq_k, \bq_{k+1}) + D_2 L_h (\bq_{k-1}, \bq_k) \right) \cdot \mathring{\bq}_k = 0
$$
But for this to equal $0$, the inside terms must equal $0$ exactly. 
$$
D_{1} L_h (\bq_k, \bq_{k+1}) + D_2 L_h (\bq_{k-1}, \bq_k) = 0
$$
We can now compute the first derivative of $L_h$ with respect to $\bq_k, \bq_{k+1}$ gives us
$$
\begin{aligned}
D_1 L|_{\bq_k, \bq_{k+1}}
&= -\frac{m}{h^2} (\bq_{k+1} - \bq_k) - \frac{dU(\bq_k)}{2} \\
% 
D_2 L|_{\bq_{k-1}, \bq_k}
&= \frac{m}{h^2} (\bq_k - \bq_{k-1}) - \frac{dU(\bq_k)}{2} 
\end{aligned}
$$
implying that 
$$
- \frac{m}{h^2} (\bq_{k+1} - 2\bq_k + \bq_{k-1}) - dU(\bq_k) = 0
$$
Let
$$
\bF(\bq_k) := -dU(\bq_k) = m \frac{\bq_{k+1} - 2\bq_k + \bq_{k-1}}{h^2}
$$
This is different from RK4[^1]

[^1]: Why?

This gives us an explicitly timestep march, where $(\bq_{k-1}, \bq_k) \mapsto (\bq_k, \bq_{k+1})$ and so 
$$
\boxed{
  \bq_{k+1} = 2\bq_k - \bq_{k-1} + \frac{h^2}{m} \bF(\bq_k)
}
$$

> [!faq] Why is this better than [[Numerical Methods#Runge-Kutta Method (RK4)|RK4]]?
> The idea is that variational integrators preserve the geometric structure of the shape of motion in configuration space better than generic [[Ordinary Differential Equation|ODE]] solvers. 

> [!info] Stability
> See prior image. The Störmer-Verlet method is the variational integrator on the right. We see a cleaner phase portrait.

# Discrete Euler-Lagrange Equation
The discrete [[Calculus of Variations#Euler-Lagrange Equation|Euler-Lagrange equation]] is the stationarity condition for the discrete action
$$
S_h(\bq_0, \ldots, \bq_N) = \sum_{k=0}^{N-1} L_h(\bq_k, \bq_{k+1}).
$$
For each interior index $k = 1, \ldots, N-1$, varying $\bq_k$ while keeping the endpoints fixed gives
$$
D_2 L_h (\bq_{k-1}, \bq_k) + D_1 L_h (\bq_k, \bq_{k+1}) = 0
$$
This is the discrete analogue of the continuous Euler-Lagrange equation. In particular, it is the general variational principle from which methods such as [[#Störmer-Verlet Method]] are derived.

> [!info] Interpretation
> The two terms represent the two discrete action contributions meeting at the node $\bq_k$: one contribution comes from the interval $[\bq_{k-1}, \bq_k]$, and the other comes from the interval $[\bq_k, \bq_{k+1}]$. Their sum vanishes because the discrete path is stationary with respect to variations of the interior point $\bq_k$.
> 
> This is the discrete counterpart of the continuous idea that momentum is obtained from the velocity derivative of the Lagrangian:
> $$
> \bp = \frac{\partial L}{\partial \dot{\bq}}.
> $$
 
Accordingly, the discrete Lagrangian defines two discrete Legendre transforms
$$
\mathbb{F}L : (\bq, \dot{\bq}) \mapsto \left(\bq, \frac{\partial L}{\partial \dot{\bq}}(\bq, \dot{\bq}) \right)
$$
by replacing the velocity description with a pair of nearby configurations. Define $f_1, f_2 : Q \times Q \to T^*Q$ (the [[Dual Space#Definition (Cotangent Bundle)|contangent bundle]]) by
$$
\begin{aligned}
f_1 &: (\bq_1, \bq_2) \mapsto \left(\bq_1, -D_1 L_h (\bq_1, \bq_2)\right) \\
f_2 &: (\bq_1, \bq_2) \mapsto \left(\bq_2, D_2 L_h (\bq_1, \bq_2)\right) 
\end{aligned}
$$
The quantity
$$
\bp_k^- := -D_1 L_h(\bq_k, \bq_{k+1})
$$
is the left discrete momentum at $\bq_k$ (contribution from previous state), and
$$
\bp_k^+ := D_2 L_h(\bq_{k-1}, \bq_k)
$$
is the right discrete momentum at $\bq_k$ (contribution to next state). The discrete Euler-Lagrange equation is exactly the matching condition
$$
\bp_k^- = \bp_k^+.
$$
In terms of the maps $f_1$ and $f_2$, this says
$$
f_2(\bq_{k-1}, \bq_k) = f_1(\bq_k, \bq_{k+1}).
$$
Therefore, if $f_1$ is locally invertible[^2], we can solve for the next pair $(\bq_k, \bq_{k+1})$ from the previous pair $(\bq_{k-1}, \bq_k)$ by applying $f_2$ and then $f_1^{-1}$. This gives the marching rule
$$
(\bq_k, \bq_{k+1}) = f_1^{-1} \circ f_2 (\bq_{k-1}, \bq_k)
$$
[^2]: Here, "locally invertible" means that near a regular point, the phase-space data $(\bq_k, \bp_k)$ uniquely determines a nearby next configuration $\bq_{k+1}$. For the mechanical discrete Lagrangians used in this note, this holds whenever the discrete Lagrangian is regular, which is typically true for sufficiently small timestep $h$.

Thus the discrete EL equation gives an update map on $Q \times Q$, and through the maps $f_1, f_2$ it also induces the corresponding update on phase space $T^*Q$. We can visualize this as
```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]

% Define colors matching the reference image
\definecolor{topblue}{RGB}{65, 110, 185}
\definecolor{botteal}{RGB}{90, 170, 155}

% --- Nodes Top Row ---
\node (T1) at (2.5, 2.5) {\Large $(\mathbf{q}_{k-1}, \mathbf{q}_k)$};
\node (T2) at (7.5, 2.5) {\Large $(\mathbf{q}_k, \mathbf{q}_{k+1})$};
\node (T3) at (12.5, 2.5) {\Large $(\mathbf{q}_{k+1}, \mathbf{q}_{k+2})$};

% --- Nodes Bottom Row ---
\node (B1) at (0, 0) {\Large $(\mathbf{q}_{k-1}, \mathbf{p}_{k-1})$};
\node (B2) at (5, 0) {\Large $(\mathbf{q}_k, \mathbf{p}_k)$};
\node (B3) at (10, 0) {\Large $(\mathbf{q}_{k+1}, \mathbf{p}_{k+1})$};

% --- Top Horizontal Arrows (marching on QxQ) ---
\draw[|->, densely dotted, line width=1.5pt, topblue, shorten >=8pt, shorten <=8pt] 
    (T1) -- (T2);
\draw[|->, densely dotted, line width=1.5pt, topblue, shorten >=8pt, shorten <=8pt] 
    (T2) -- (T3);

% --- Bottom Horizontal Arrows (marching on qp) ---
\draw[|->, densely dotted, line width=1.5pt, botteal, shorten >=8pt, shorten <=8pt] 
    (B1) -- (B2);
\draw[|->, densely dotted, line width=1.5pt, botteal, shorten >=8pt, shorten <=8pt] 
    (B2) -- (B3);

% --- Diagonal Mapping Arrows ---
\draw[|->, line width=1.5pt, shorten >=6pt, shorten <=6pt] 
    (T1) -- (B1) node[midway, left, xshift=-2pt, yshift=4pt] {\Large $f_1$};
    
\draw[|->, line width=1.5pt, shorten >=6pt, shorten <=6pt] 
    (T1) -- (B2) node[midway, right, xshift=2pt, yshift=4pt] {\Large $f_2$};
    
\draw[|->, line width=1.5pt, shorten >=6pt, shorten <=6pt] 
    (T2) -- (B2) node[midway, left, xshift=-2pt, yshift=4pt] {\Large $f_1$};
    
\draw[|->, line width=1.5pt, shorten >=6pt, shorten <=6pt] 
    (T2) -- (B3) node[midway, right, xshift=2pt, yshift=4pt] {\Large $f_2$};
    
\draw[|->, line width=1.5pt, shorten >=6pt, shorten <=6pt] 
    (T3) -- (B3) node[midway, left, xshift=-2pt, yshift=4pt] {\Large $f_1$};

% --- Explanatory Text Labels ---
\node[topblue, font=\Large] at (6.5, 3.4) {marching on the $Q \times Q$ space};
\node[botteal, font=\Large] at (4.0, -0.9) {marching on the $q \times p$ space};

\end{tikzpicture}
\end{document}
```
The $q \times p$ space corresponds to the axes in the [[#Variational Integrators|image]].

# VI via Midpoint Rule
The midpoint rule is a variational integrator where the discrete Lagrangian is
$$
L_h(\bq_{0}, \bq_{1}) 
= \underbrace{h L\left( \frac{\bq_0 + \bq_1}{2}, \frac{\bq_1 - \bq_0}{h} \right)}_{\text{midpoint approximation}}
= \frac{mh}{2} \left| \frac{\bq_1 - \bq_0}{h} \right|^2 - h U\left( \frac{\bq_0 + \bq_1}{2} \right)
$$
The Euler-Lagrange equation is
$$
m \frac{\bq_{k+1} - 2\bq_k + \bq_{k-1}}{h^2} 
= \frac{1}{2} \left(
  \bf \left(\frac{\bq_{k-1} + \bq_k}{2}\right) + \bf\left(\frac{\bq_k + \bq_{k+1}}{2}\right)
\right)
$$
and equivalently,
$$
\begin{cases}
m \frac{\bq_{k+1} - \bq_k}{h} = \frac{\bp_{k+1} + \bp_k}{2} \\
\frac{\bp_{k+1} - \bp_k}{h} = \bf\left(\frac{\bq_{k+1} - \bq_k}{h}\right)
\end{cases}
$$
which is the implicit midpoint method. It is **implicit** because $\bq_{k+1}$ appears on both sides, so we cannot write a simple rule for it like in [[#Störmer-Verlet Method]]. 

# Discrete Liouville Theorem 
Marching on $q \times p$ space preserves the enclosed area of the marched loop. In particular, the area is a section on the graphs we see above. This means that all possible positions and momentum are conserved as the system evolves over time. 

The path the system takes between all the points may change, but the area of the path is preserved (even if the shape is complex). This geometric property is called **symplecticity** and is a consequence of the variational principle. This is precisely why variational integrators are better than generic ODE solvers: they preserve the underlying geometric structure of the system, which leads to better long-term stability and accuracy in simulations.

# Discrete Noether's Theorem
If the discrete Lagrangian has a [[Lagrangian Mechanics#Definition (Continuous Symmetry)|continuous symmetry]], 
$$
(\forall \bq_1, \bq_2 \in Q)
\quad\quad
\left\langle D_1 L(\bq_1, \bq_2) \mid \bX \right\rangle + \left\langle D_2 L(\bq_1, \bq_2) \mid \bX \right\rangle = 0
$$
then $\langle \bp_k|\bX\rangle$ is conserved (constant independent of $k$). 

For example, if we let a particle move along a wire in empty space and then translate the entire system, the Lagrangian is invariant to this translation. Mathematically, let $\bv$ be a constant vector representing the direction of symmetry, and let $\bq_k$ be the start and $\bq_{k+1}$ be the end of a discrete segment. The translation is by some amount $\vepsi$ along $\bv$ is $\bq \mapsto \bq + \vepsi \bv$.

```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.3]

% Define original points
\coordinate (qk)  at (0.2, 0.7);
\coordinate (qk1) at (3.2, 1.4);

% Define translated points (shifted by dx = +2.5, dy = -1.5)
\coordinate (tqk)  at (2.7, -0.8);
\coordinate (tqk1) at (5.7, -0.1);

% Draw original wire (gray)
\draw[thick, gray] (-0.5, -0.5) to[out=70, in=180] (2, 2) to[out=0, in=135] (4, 0.5);
\node[gray, above] at (2, 2) {Original Wire};

% Draw translated wire (gray, dashed)
\draw[thick, gray, dashed] (2.0, -2.0) to[out=70, in=180] (4.5, 0.5) to[out=0, in=135] (6.5, -1.0);
\node[gray, below] at (4.5, 0) {Translated Wire};

% Motion segment on original wire (blue)
\draw[->, ultra thick, blue] (qk) to[out=75, in=180] (2, 2) to[out=0, in=145] (qk1);
\filldraw[blue] (qk) circle (2.5pt) node[left, xshift=-4pt] {$\mathbf{q}_k$};
\filldraw[blue] (qk1) circle (2.5pt) node[above right, yshift=2pt] {$\mathbf{q}_{k+1}$};

% Motion segment on translated wire (purple)
\draw[->, ultra thick, purple] (tqk) to[out=75, in=180] (4.5, 0.5) to[out=0, in=145] (tqk1);
\filldraw[purple] (tqk) circle (2.5pt) node[left, xshift=-4pt] {$\mathbf{q}_k + \varepsilon\mathbf{v}$};
\filldraw[purple] (tqk1) circle (2.5pt) node[right, xshift=4pt] {$\mathbf{q}_{k+1} + \varepsilon\mathbf{v}$};

% Translation vectors (orange)
\draw[->, thick, dashed, orange] (qk) -- (tqk) node[midway, left] {$\varepsilon\mathbf{v}$};
\draw[->, thick, dashed, orange] (qk1) -- (tqk1) node[midway, right] {$\varepsilon\mathbf{v}$};

\end{tikzpicture}
\end{document}
```

Because the Lagrangian is invariant to this translation, we have its derivative with respect to $\vepsi$ must be $0$. 
$$
\frac{d}{d\vepsi} L(\bq_k + \vepsi \bv, \bq_{k+1} + \vepsi \bv) = 0
$$
By the chain rule, this is equivalent to
$$
D_1 L(\bq_k, \bq_{k+1}) \cdot \bv + D_2 L(\bq_k, \bq_{k+1}) \cdot \bv = 0
$$
Indeed, this is true for all $\bv$ and $k$ because of the symmetry.  

We can show this is true for momentum. Recall from earlier that the discrete momentum entering the current step $\bp_k$ and leaving the current step $\bp_{k+1}$[^3] are
$$
\begin{aligned}
\bp_k &= -D_1 L(\bq_k, \bq_{k+1}) \\
\bp_{k+1} &= D_2 L(\bq_k, \bq_{k+1})
\end{aligned}
$$
[^3]: The negative sign is from the original Discrete Euler-Lagrange equation as described previously.

Substituting into the symmetry condition gives us
$$
\begin{aligned}
\langle -\bp_k | \bv \rangle + \langle \bp_{k+1} | \bv \rangle &= 0 \\
\langle \bp_{k+1} | \bv \rangle &= \langle \bp_k | \bv \rangle
\end{aligned}
$$
Indeed, momentum along the direction of symmetry $\bv$ is conserved across all steps $k$.

> [!info] Idea
> This [article](https://math.ucr.edu/home/baez/noether.html) gives a nice intuitive explanation of Noether's theorem and how the ideas from [[Lagrangian Mechanics]] are used to show symmetry. 

# Definition (Time Reversal Symmetry)
In classical physics, the equations of motion are invariant under time reversal. If our discrete integrator satisfies the property that 
$$
L(q_1, q_2) = -L(q_2, q_1)
$$ 
then we say it is **time-reversal symmetric**. Indeed, the [[#Störmer-Verlet Method]] is time-reversal symmetric. 
$$
\begin{aligned}
\bq_{k+1} &= 2\bq_k - \bq_{k-1} + \frac{h^2}{m} \bF(\bq_k) && \text{forward} \\
\bq_{k-1} &= 2\bq_k - \bq_{k+1} + \frac{h^2}{m} \bF(\bq_k) && \text{reverse}
\end{aligned}
$$