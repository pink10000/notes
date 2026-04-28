---
tags:
  - CSE_291G
---
# Variational Integrators
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

Let $h$ denote the discrete timestep. A discrete [[Lagrangian Mechanics#Definition (The Lagrangian)|Lagrangian]] is a function 
$$
L_{h} : Q \times Q \to \R
$$
approximating the total action between two positions. For example, consider the trapezoidal rule. Suppose the original problem is 
$$
L(\bq, \dot{\bq}) = \frac{m}{2} |\dot{\bq}|^2 - U(\bq) 
$$
Then the discrete Lagrangian is
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
The trapezoidal rule is really about integrating the potential energy using the trapezoidal rule and integrating the kinetic energy using the midpoint rule (from Calculus 1!).

By the discrete [[Lagrangian Mechanics#Theorem (Least Action Principle)|least action principle]], $\frac{\del S_{h}}{\del \bq_k} = 0$ for all $k$. We can derive this similar to how we showed the LAP. Let 
$$
S = \sum_{k=0}^{N-1} L_h (\bq_k, \bq_{k+1}) 
$$
Then,
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

So, taking the first derivative of $L_h$ with respect to $\bq_k, \bq_{k+1}$ gives us
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
> 2 Body Problem

> [!info] Stability
> See prior image. The Störmer-Verlet method is the variational integrator on the right.  

# Discrete Euler-Lagrange Equation
The discrete [[Calculus of Variations#Euler-Lagrange Equation|Euler-Lagrange equation]] is
$$
D_2 L_h (\bq_{k-1}, \bq_k) + D_1 L_h (\bq_k, \bq_{k+1}) = 0
$$
We should think of "reading off momentum from velocity" as $\bp = \frac{\partial L}{\partial \dot{\bq}}$. So, 
$$
f : (\bq, \dot{\bq}) \mapsto \left(\bq, \frac{\partial L}{\partial \dot{\bq}}(\bq, \dot{\bq}) \right) 
$$
Define $f_1, f_2 : Q \times Q \to T^* Q$. Then 
$$
\begin{aligned}
f_1 &: (\bq_1, \bq_2) \mapsto \left(\bq_1, -D_1 L_h (\bq_1, \bq_2)\right) \\
f_2 &: (\bq_1, \bq_2) \mapsto \left(\bq_2, D_2 L_h (\bq_1, \bq_2)\right) 
\end{aligned}
$$
Then discrete Euler-Lagrange is the marching 
$$
(\bq_k, \bq_{k+1}) = f_1^{-1} \circ f_2 (\bq_{k-1}, \bq_k)
$$
We can also show this as 
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

# Example 2: Midpoint Rule
The midpoint rule is a variational integrator where the discrete Lagrangian is
$$
L_h(\bq_0 \bq_1) 
= h L\left( \frac{\bq_0 + \bq_1}{2}, \frac{\bq_1 - \bq_0}{h} \right)
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
which is the implicit midpoint method.