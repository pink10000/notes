---
tags:
  - CSE_291G
---
# Definition (Circulation)
For incompressible fluids, we can define the **circulation** of the fluid. Imagine drawing a closed loop $C_0$ in the fluid and connecting a specific set of fluid particles. As the fluid flows, those specific particles move and deform into a new loop, denoted by $C_{t} = \phi_{t}(C_{0})$ where $\phi_{t}$ is the [[Continuum Mechanics#Postulate 1|flow map]] ($\dot{\phi_{t}} = \bu_{t} \circ \phi_{t}$).

The **circulation** of the velocity along the curve is the line integral of the velocity field $\bu_t$ around that moving loop:
$$
\Gamma_{C_{t}} := \oint_{C_{t}} \bu_{t} \cdot d\ell = \oint_{C_{t}} \bu_{t}^{\flat}
$$
where $\flat$ is the [[Dual Space#Definition (Riemannian Manifold)|metric dual operator]] that creates the covector from the original vector field. 
```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}

% --- Color Theme (Tweak RGB values here) ---
% Surface Gradient (Dark Slate)
\definecolor{surfTop}{RGB}{70, 80, 95}
\definecolor{surfMid}{RGB}{35, 45, 55}
\definecolor{surfBot}{RGB}{15, 20, 30}

% Vector Flow Lines (Neon Cyan)
\definecolor{flowColor}{RGB}{0, 255, 255}

% Foreground Loops (Vibrant Orange)
\definecolor{loopFront}{RGB}{255, 140, 0}
% Background Loops (Darker Orange for depth)
\definecolor{loopBack}{RGB}{150, 70, 0}

% Text Labels
\definecolor{textColor}{RGB}{240, 240, 240}


% --- Surface (Manifold) ---
\draw[thick, draw=surfTop, top color=surfTop, bottom color=surfBot, middle color=surfMid]
  plot [smooth cycle, tension=0.75] coordinates {
    (-4.5, 0)
    (-3.5, 2.5)
    (0, 1.8)
    (3.5, 2.5)
    (4.5, 0)
    (3.5, -2.5)
    (0, -1.8)
    (-3.5, -2.5)
  };

% --- Background Loops (Right Arcs) ---
% Loop C (left)
\begin{scope}[shift={(-2, 0.2)}, rotate=-10]
    \draw[thick, loopBack] (0, -1.5) arc (-90:90:0.5 and 1.5);
    \draw[thick, loopBack, ->] (0, -1.5) arc (-90:0:0.5 and 1.5); 
\end{scope}

% Loop Ct (right)
\begin{scope}[shift={(2, -0.1)}, rotate=-10]
    \draw[thick, loopBack] (0, -2) arc (-90:90:0.7 and 2);
    \draw[thick, loopBack, ->] (0, -2) arc (-90:20:0.7 and 2); 
\end{scope}

% --- Vector Field Flow Lines ---
% Line 1 (Top)
\draw[thick, flowColor, ->] (-3.2, 1.2) to[out=-15, in=185] (-0.2, 0.9);
\draw[thick, flowColor, ->] (-0.2, 0.9) to[out=5, in=195] (2.4, 1.3);

% Line 2 (Mid-Top)
\draw[thick, flowColor, ->] (-3.0, 0.5) to[out=-10, in=180] (-0.2, 0.3);
\draw[thick, flowColor, ->] (-0.2, 0.3) to[out=0, in=190] (2.5, 0.5);

% Line 3 (Mid-Bottom)
\draw[thick, flowColor, ->] (-3.0, -0.2) to[out=-20, in=170] (-0.2, -0.5);
\draw[thick, flowColor, ->] (-0.2, -0.5) to[out=-10, in=160] (2.6, -0.8);

% Line 4 (Bottom)
\draw[thick, flowColor, ->] (-3.2, -0.8) to[out=-10, in=175] (-0.2, -0.9);
\draw[thick, flowColor, ->] (-0.2, -0.9) to[out=-5, in=155] (2.3, -1.5);

% --- Foreground Loops (Left Arcs) ---
% Loop C (left)
\begin{scope}[shift={(-2, 0.2)}, rotate=-10]
    \draw[thick, loopFront] (0, 1.5) arc (90:270:0.5 and 1.5);
    \draw[thick, loopFront, ->] (0, 1.5) arc (90:160:0.5 and 1.5); 
\end{scope}
\node[font=\large, text=textColor] at (-2.3, -1.6) {$C$};

% Loop Ct (right)
\begin{scope}[shift={(2, -0.1)}, rotate=-10]
    \draw[thick, loopFront] (0, 2) arc (90:270:0.7 and 2);
    \draw[thick, loopFront, ->] (0, 2) arc (90:160:0.7 and 2); 
\end{scope}
\node[font=\large, text=textColor] at (2.7, -1.5) {$C_t$};

\end{tikzpicture}
\end{document}
```

# Theorem (Kelvin's Circulation Theorem)
Suppose the [[Continuum Mechanics#Definition (Flow Velocity)|flow velocity]] $\bu_{t}$ satisfies the [[Euler Arnold Equations#Background|Euler equation]]:
$$
\frac{\partial}{\partial t} \bu_{t} + \nabla_{\bu_{t}} \bu_{t} = -\nabla p_{t}
$$
Kelvin's Circulation theorem states that if you follow a closed loop of fluid particles as they flow, the circulation around that specific loop will remain perfectly constant over time. That is,
$$
\frac{\partial}{\partial t} \Gamma_{C_{t}} = \frac{d}{dt} \oint_{C_t} \bu_t \cdot d\ell = 0
$$

## Abstract Formulation & Proof
We can further abstract this. By converting the velocity vector field into a covector field via $\bu \cdot dl = \bu^\flat$, we can take the [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] on the domain and get:
$$
\frac{d}{dt} \oint_{C_t} \bu \cdot dl 
= 
\frac{d}{dt} \oint_{C_t} \bu^\flat 
=
\frac{d}{dt} \oint_{C_0} \left( \phi_t^* \bu^\flat \right) 
= 
\oint_{C_0} \frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
= 0
$$
for all closed curves $C_0$.

**Proof**:

We compute the integrand. 
$$
\begin{aligned}
  \frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
  &= \frac{d}{dt} \left[ (d\phi)^\top \bu  \right] \\ 
  &= \underbrace{(d\dot{\phi})}_{d(u \circ \phi)} \,\bu + (d\phi)^\top \dot\bu \\
  &= \left[ (\nabla \bu) d\phi \right]^\top \bu - (d \phi)^\top \left( \nabla_\bu \bu + \nabla p \right) \\
  &= (d\phi)^\top \left[ (\nabla \bu)^\top \bu - \nabla_\bu \bu + \nabla p  \right] \\
\end{aligned}
$$
via 
1. product rule
2. substitution with the flow map and the [[Euler Arnold Equations#Background|Euler Equation]].
3. factorization and simplification 

Then, let 
$$
-\nabla \tilde{p} = (\nabla \bu)^\top \bu - \nabla_\bu \bu - \nabla p
$$
be a new spatial gradient to absorb those inner terms. Thus, 
$$
\frac{d}{dt} \left( \phi_t^* \bu^\flat \right) 
= 
(d\phi)^\top [ -\nabla \tilde{p} ]
=
-\phi_t^* (d\tilde{p})
$$
Therefore 
$$
\begin{aligned}
\frac{d}{dt} \oint_{C_t} \bu \cdot dl 
&= \oint_{C_0} \frac{d}{dt} \left( \phi_t^* \bu^\flat \right)  \\
&= \oint_{C_0} -\phi_t^* (d\tilde{p}) \\
&= \oint_{C_t} d\tilde{p}  \\
&= 0
\end{aligned}
$$
where the last line is via [[Stokes Theorem]], since the curl of a gradient field is $0$.
