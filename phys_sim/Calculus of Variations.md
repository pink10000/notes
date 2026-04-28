---
tags:
  - CSE_291G
---
# General Idea
In calculus, we take [[Derivative|derivatives]] of functions of a few variables. In *calculus of variations*, we take derivatives of functions of functions (also called *functionals*). The main purpose of this is to formulate the optimization problem over function spaces and derive its optimality condition ([[KKT Condition]]).

These optimality conditions are often differential equations, called Euler-Lagrange Equations, and most physical equations arise as Euler-Lagrange equations of some optimization problem. That way, we can "design one optimal functional" instead of "modeling forces". 

# Example 1
Let
$$
M = \{ y : [0, T] \to \R \mid y(0) = y_0, y(T) = y_T \}
$$
be the manifold of all possible valid trajectories of a particle in one dimension, from $y_0$ to $y_T$ in time $T$. A single "point" on this manifold is an entire function $y(t)$. Because it takes infinitely many values (one for each $t$), we can think of $M$ as an infinite-dimensional manifold.

Let $\mathcal{E} : M \to \R$ be the [[Dual Space#Definition (Covector)|covector]] where
$$
\mathcal{E}(y) := \int_{t=0}^T \left( \frac{1}{2} y'(t)^2 + \cos(y(t)) \right) \, dt
$$
The problem is, what is the optimality condition for
$$
\min_{y \in M} \mathcal{E}(y)
$$
If we fixed some $p \in M$, the [[Dual Space#Definition (Tangent Space)|tangent space]] $T_{y}M$ represents all valid perturbations we can apply to $y$ without leaving the [[Manifold]]. This perturbation is $\mathring{y}$. So, for perturbed path $y(t) + \vepsi \mathring{y}(t) \in M$, it must satisfy the fixed boundary conditions. In particular, 
$$
T_y M = \{ \mathring{y} : [0, T] \to \R \mid \mathring{y}(0) = 0, \mathring{y}(T) = 0 \}
$$
Visually, we have 

```desmos-graph
left=-1; bottom=-1;
right=9;
---
y_0 = 2 | hidden
y_T = 6 | hidden
T = 8 | hidden

L(x) = y_0 + \frac{y_T - y_0}{T} x \{0 \le x \le T\} | hidden

f(x) = L(x) + 1.2 \sin(\frac{\pi x}{T}) \{0 \le x \le T\} | #673ab7
g(x) = f(x) + 1.2 \sin(\frac{\pi x}{T}) \{0 \le x \le T\} | #d1c4e9
h_1(x) = f(x) - 1.2 \sin(\frac{\pi x}{T}) \{0 \le x \le T\} | #d1c4e9
h_2(x) = L(x) - 2 \sin(\frac{\pi x}{T}) \{0 \le x \le T\} | #d1c4e9
v(x) = 1.2 \sin(\frac{\pi x}{T}) \{0 \le x \le T\} | #1976d2

(0, y_0) | BLACK | label:y_0
(T, y_T) | BLACK | label:y_T
(T, 0) | BLACK | label:T
(0, 0) | BLACK | label:0
(T \cdot 0.8, v(T \cdot 0.8)) | hidden | label:\dot{y}

x = T \{0 \le y \le y_T\} | DASHED | #bdbdbd

X_a = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
x = X_a \{f(X_a) \le y \le g(X_a)\} | #90caf9
y = g(X_a) + 2(x - X_a) \{X_a - 0.15 \le x \le X_a\} | #90caf9
y = g(X_a) - 2(x - X_a) \{X_a \le x \le X_a + 0.15\} | #90caf9
```
where the blue curve at the bottom represents one example of a perturbation $\mathring{y}$, and the purple curves represent some examples of $y$. 

The optimality condition is
$$
d\mathcal{E}_y \llbracket \mathring{y} \rrbracket = 0
$$
for all $\mathring{y} \in T_y M$, just like the first derivative test for optimality in regular calculus. Geometrically, this means the covector itself is zero. I.e. if we were at the bottom of some "energy bowl", no matter which direction $\mathring{y}$ we perturb, the energy will not change. Indeed,
$$
\begin{aligned}
0 
&= d\mathcal{E}_y \llbracket \mathring{y} \rrbracket \\
&= \frac{d}{d\vepsi} \bigg|_{\vepsi=0} \mathcal{E}(y + \vepsi \mathring{y}) \\
&= \frac{d}{d\vepsi} \bigg|_{\vepsi=0} \int_{t=0}^T \left( \frac{1}{2} (y'(t) + \vepsi \mathring{y}'(t))^2 + \cos(y(t) + \vepsi \mathring{y}(t)) \right) \, dt \\
&= \int_{t=0}^T \left( y' \mathring{y}' - \sin(y) \mathring{y} \right) \, dt \\
&= -\int_{t=0}^T \left( y'' + \sin(y) \right) \mathring{y} \, dt  
\quad\quad\quad\text{via integration by parts}  \\ 
&\!\!\!\implies 0 = y''(t) + \sin(y(t))
\end{aligned}
$$
which is precisely the [[Ordinary Differential Equation#Theorem (Reduction to First-Order Systems)|physical equation of motion]] for a pendulum. 

> Physics is just optimization over function spaces.

# Euler-Lagrange Equation 
We can derive the optimality condition for a more general functional. Suppose we have the same conditions as above but with 
$$
\mathcal{E}(y) := \int_{t=0}^T L(t, y(t), y'(t)) \, dt
$$
for some integrand $L : [0, T] \times \R^m \times \R^m \to \R$. The directional derivative is then 
$$
\begin{aligned}
d\mathcal{E}_{\mathbf{y}}[\![\mathring{\mathbf{y}}]\!] &= \left.\frac{d}{d\vepsi}\right|_{\vepsi=0} \mathcal{E}(\mathbf{y} + \vepsi \mathring{\mathbf{y}}) \\
&= \int_{0}^{T} \left.\frac{\partial}{\partial \vepsi}\right|_{\vepsi=0} 
L(t, \mathbf{y}(t) + \vepsi \mathring{\mathbf{y}}(t), \mathbf{y}'(t) + \vepsi \mathring{\mathbf{y}}'(t)) \, dt \\
% 
&= \int_{0}^{T} \left\langle \frac{\partial L}{\partial \mathbf{y}}_{(t, \mathbf{y}(t), \mathbf{y}'(t))} \middle| \mathring{\mathbf{y}}(t) \right\rangle dt + \int_{0}^{T} \left\langle \frac{\partial L}{\partial \mathbf{y}'}_{(t, \mathbf{y}(t), \mathbf{y}'(t))} \middle| \mathring{\mathbf{y}}'(t) \right\rangle dt \\
&= \int_{0}^{T} \left\langle \frac{\partial L}{\partial \mathbf{y}}_{(t, \mathbf{y}(t), \mathbf{y}'(t))} \middle| \mathring{\mathbf{y}}(t) \right\rangle dt - \int_{0}^{T} \left\langle \frac{d}{dt}\left(\frac{\partial L}{\partial \mathbf{y}'}_{(t, \mathbf{y}(t), \mathbf{y}'(t))}\right) \middle| \mathring{\mathbf{y}}(t) \right\rangle dt \\
&= \int_{0}^{T} \left\langle \frac{\partial L}{\partial \mathbf{y}}_{(t, \mathbf{y}(t), \mathbf{y}'(t))} - \frac{d}{dt}\left(\frac{\partial L}{\partial \mathbf{y}'}_{(t, \mathbf{y}(t), \mathbf{y}'(t))}\right) \middle| \mathring{\mathbf{y}}(t) \right\rangle dt
\end{aligned}
$$
in particular,
1. We expanded the definition of directional derivative
2. We applied the multivariate chain rule since $\vepsi$ appears in both $\mathbf{y}$ and $\mathbf{y}'$
3. We took the partial derivative of $L$ with respect to $\vepsi$. The use of $\langle, \rangle$ is just to denote the dot product between the gradient and the perturbation. Here, it is the inner product in $\R^m$.
4. We applied integration by parts to move the derivative from $\mathring{\mathbf{y}}'$ to $\frac{\partial L}{\partial \mathbf{y}'}$. The boundary term vanishes since $\mathring{\mathbf{y}}(0) = \mathring{\mathbf{y}}(T) = 0$.
5. We factored out $\mathring{\mathbf{y}}$ via [[Square Matrices#Definition (Inner Product Structure or Metric)|linearity of the inner product]]. 

## Theorem (Euler-Lagrange Equation)
The optimality condition $d\mathcal{E}_{\mathbf{y}}[\![\mathring{\mathbf{y}}]\!] = 0$ for all $\mathring{\mathbf{y}} \in T_{\mathbf{y}}M$ is equivalent to the following system of ordinary differential equations:
$$
\frac{\partial \mathcal{E}}{\partial \mathbf{y}} (t) = 
\frac{\partial L}{\partial \mathbf{y}}_{(t, \mathbf{y}(t), \mathbf{y}'(t))} - \frac{d}{dt}\left(\frac{\partial L}{\partial \mathbf{y}'}_{(t, \mathbf{y}(t), \mathbf{y}'(t))}\right) = 0
$$
called the **Euler-Lagrange Equation**.

# Applications in Physics
The Euler-Lagrange equations are foundational to physics. For detailed derivations of Newton's laws, conservation of energy, and rotational dynamics from variational principles, see [[Lagrangian Mechanics]].

# Example 2 (Hanging Chain)
What is the shape of a hanging chain on two poles? It is the curve with the lowest potential energy with fixed total length. 
Let the shape be the function graph 
$$
y = f(x)
$$
First, we want to describe the physical geometry of the curve. Any section of the chain forms a right triangle microscopically. With the Pythagorean theorem, we have that the length of the chain 
$$
ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx = \sqrt{1 + f'^2} dx
$$
The total length is found by integrating $ds$ along the curve
$$
\mathcal{L}(f) = \int_{a}^{b} ds = \int_{a}^{b} \sqrt{1 + f'^2} dx
$$
The total gravitational potential energy is
$$
\mathcal{E}(f) = \int_{a}^{b} f \sqrt{1 + f'^2} dx
$$
We must minimize $\mathcal{E}$. However, without any constraints, the chain would drop straight down into infinity (to achieve negative infinite potential energy). So we must constrain it to have a fixed length $\ell$. Thus, the constraint is $\mathcal{L}(f) - \ell = 0$. The [[KKT Condition]] for minimizing $\mathcal{E}$ with constraint $\mathcal{L} - \ell = 0$ says that there exists some $\lambda$ such that
$$
d\mathcal{E} + \lambda d\mathcal{L} = 0 \iff 
d\tilde{\mathcal{E}} = 0 
\text{ where }
\tilde{\mathcal{E}} = \mathcal{E} + \lambda \mathcal{L} = \int_{a}^{b} (f + \lambda) \sqrt{1 + f'^2} dx
$$
We want to minimize $\tilde{\mathcal{E}}$. By applying Noether's theorem of time independence (in this case, "time" is just the $x$-axis), we have that 
$$
\frac{\del L}{\del f'} f' - L = c 
$$
implying that 
$$
(f + \lambda)\left(
\frac{f'^2}{\sqrt{1 + f'^2}} - \sqrt{1 + f'^2} \right) 
= c
$$
such that 
$$
\begin{aligned}
f' &= \pm \frac{1}{c} \sqrt{(f + \lambda)^2 - c^2} \\ 
\frac{df}{\sqrt{(f + \lambda)^2 - c^2}} &= \pm \frac{1}{c} dx \\
\int \frac{df}{\sqrt{(f + \lambda)^2 - c^2}} &= \pm \int \frac{1}{c} dx \\
\cosh^{-1} \left( \frac{f + \lambda}{c} \right) &= \pm \frac{x}{c} + c_1 \\
f(x) &= c \cosh\left( \frac{x}{c} + c_2 \right) - \lambda
\end{aligned}
$$

# Example 3 (Mass Spring System)
Consider a [[Graph|graph]] $G = (V, E)$ where each vertex is assigned a mass $m_i$ and position $x_i$. Each edge is assigned a spring with a spring constant $k_e$. The total kinetic energy and potential energy is 
$$
K = \sum_{i \in V} \frac{1}{2} m_i |\dot{x}_{i}|^{2}
\quad\quad\quad
U = \sum_{e=(i,j) \in E} \frac{1}{2} k_{e} |x_i - x_j|^2
$$
The Euler-Lagrange equation for this gives 
$$
\frac{d}{dt} \frac{\partial L}{\partial \dot{x}_i} = - \frac{\partial L}{\partial x_i}
\quad\implies\quad 
m_i \ddot{x}_i = -\frac{\partial U}{\partial x_i}
$$
We can find the derivative with respect to one vertex position
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.0]

% Define colors
\definecolor{poscol}{RGB}{112, 48, 160}     % Purple
\definecolor{straincol}{RGB}{68, 114, 196}  % Blue
\definecolor{energycol}{RGB}{158, 72, 14}   % Brown
\definecolor{botcol}{RGB}{69, 160, 144}     % Teal

% Matrices
\node[draw=poscol, very thick, inner sep=2pt] (Pos) at (0,0) {
    $\begin{pmatrix}
    \color{poscol}\mathbf{x}_1 \\ \vdots \\ \color{poscol}\mathbf{x}_i \\ \vdots \\ \color{poscol}\mathbf{x}_{|\mathcal{V}|}
    \end{pmatrix}$
};

\node[draw=straincol, very thick, inner sep=2pt] (StrainX) at (4.5,0) {
    $\begin{pmatrix}
    (d{\color{poscol}\mathbf{x}})_1 \\ \vdots \\ (d{\color{poscol}\mathbf{x}})_e \\ \vdots \\ (d{\color{poscol}\mathbf{x}})_{|\mathcal{E}|}
    \end{pmatrix}$
};

\node[draw=straincol, very thick, inner sep=2pt] (StrainL) at (8.5,0) {
    $\begin{pmatrix}
    \ell_1 \\ \vdots \\ \ell_e \\ \vdots \\ \ell_{|\mathcal{E}|}
    \end{pmatrix}$
};

\node[draw=energycol, very thick, inner sep=2pt] (Energy) at (12,0) {
    $\begin{pmatrix}
    \frac{1}{2}k_1\ell_1^2 \\ \vdots \\ \frac{1}{2}k_e\ell_e^2 \\ \vdots \\ \frac{1}{2}k_{|\mathcal{E}|}\ell_{|\mathcal{E}|}^2
    \end{pmatrix}$
};

% Titles
\node[align=left, text=poscol, font=\bfseries] at (0, 2.8) {Position\\variable};
\node[align=left, text=straincol, font=\bfseries] at (6.25, 2.8) {Strains\\\normalfont(measurement of deformation)};
\node[align=left, text=energycol, font=\bfseries] at (12, 2.8) {Local energy\\\normalfont(depending only on\\certain strains)};

% Bottom Boxes
\node[draw=botcol, very thick, text=botcol, inner sep=6pt] (Force) at (0, -3.2) {\Large $\mathbf{f}_i = \mathrm{div}(\boldsymbol{\sigma})$};
\node[align=center, text=botcol, font=\bfseries] at (0, -4.2) {Force\\\normalfont(aggregate of stress)};

\node[draw=botcol, very thick, text=botcol, inner sep=6pt, minimum width=6cm] (Stress) at (6.25, -3.2) {\Large $\boldsymbol{\sigma}_e = k_e(d\mathbf{x})_e \hspace{2cm} k_e\ell_e$};
\node[align=center, text=botcol, font=\bfseries] at (6.25, -4.2) {Stress\\\normalfont(dual space of strains)};

% Connecting Arrows & Text
% Pos -> StrainX
\draw[->, lightgray, thick] ([yshift=1.2cm]Pos.east) -- ([yshift=0.7cm]StrainX.west);
\draw[->, lightgray, thick] ([yshift=0.7cm]Pos.east) -- ([yshift=0.2cm]StrainX.west);
\draw[->, lightgray, thick] ([yshift=0.2cm]Pos.east) -- ([yshift=0.2cm]StrainX.west) node[midway, above, text=straincol, yshift=-2pt] {\textbf{+}};
\draw[->, lightgray, thick] ([yshift=-0.2cm]Pos.east) -- ([yshift=0.7cm]StrainX.west) node[midway, above, text=straincol, yshift=-2pt] {\textbf{--}};
\draw[->, lightgray, thick] ([yshift=-0.9cm]Pos.east) -- ([yshift=-0.9cm]StrainX.west) node[midway, above, text=straincol, yshift=-2pt] {\textbf{--}};
\draw[->, lightgray, thick] ([yshift=-1.4cm]Pos.east) -- ([yshift=-0.9cm]StrainX.west) node[midway, above, text=straincol, yshift=-2pt] {\textbf{+}};

\node[align=left, anchor=west] at (1, 1.8) {define \\ $(d\mathbf{x})_e =$ \\ ${\color{poscol}\mathbf{x}}_{\text{dst}(e)} - {\color{poscol}\mathbf{x}}_{\text{src}(e)}$};

% StrainX -> StrainL
\draw[->, lightgray, thick] ([yshift=1.2cm]StrainX.east) -- ([yshift=1.2cm]StrainL.west);
\draw[->, lightgray, thick] ([yshift=0.7cm]StrainX.east) -- ([yshift=0.7cm]StrainL.west);
\draw[->, lightgray, thick] ([yshift=0cm]StrainX.east) -- ([yshift=0cm]StrainL.west) node[midway, below, text=straincol] {\Large $\frac{d\mathbf{x}_e}{\ell_e}$};
\draw[->, lightgray, thick] ([yshift=-1.4cm]StrainX.east) -- ([yshift=-1.4cm]StrainL.west);

\node[align=center] at (6.70, 1.8) {define \\ $\ell_e = |(d{\color{poscol}\mathbf{x}})_e|$};

% StrainL -> Energy
\draw[->, lightgray, thick] ([yshift=1.2cm]StrainL.east) -- ([yshift=1.2cm]Energy.west);
\draw[->, lightgray, thick] ([yshift=0cm]StrainL.east) -- ([yshift=0cm]Energy.west) node[midway, below, text=straincol] {\large $k_e\ell_e$};
\draw[->, lightgray, thick] ([yshift=-1.4cm]StrainL.east) -- ([yshift=-1.4cm]Energy.west);

% Energy -> U (arrows converging)
\node[text=energycol] (EndPt) at (14.2, 0) {$U$};
\draw[->, lightgray, thick] ([yshift=1.4cm]Energy.east) -- (EndPt.west);
\draw[->, lightgray, thick] ([yshift=0.6cm]Energy.east) -- (EndPt.west);
\draw[->, lightgray, thick] ([yshift=0cm]Energy.east) -- (EndPt.west);
\draw[->, lightgray, thick] ([yshift=-0.6cm]Energy.east) -- (EndPt.west);
\draw[->, lightgray, thick] ([yshift=-1.4cm]Energy.east) -- (EndPt.west);

\end{tikzpicture}
\end{document}
```

One interesting thing to note is that this is similar to a feed forward neural network. We input raw vertex positions and they transform step by step into a single scalar output $U$. 
1. The first transformation layer subtracts the position of the source vertex from the position of the destination vertex to get the edge vector. 
2. The second transformation layer normalizes (calculates the magnitude) the edge vector to get the current physical length of the string. 
3. The third transformation layer computes the local energy of each edge via the formula $\frac{1}{2} k_e \ell_e^2$.
4. The sum of the individual spring energies gives us the total potential energy of the system.

Now, like in machine learning, we do a backward pass. To find the force on a specific vertex $i$, we must compute $\frac{\partial U}{\partial \mathbf{x}_i}$. Because the energy was calculated through a chain of operations, we must use the multivariate chain rule to backpropagate the gradient through the computational graph. 

On each edge $e$ of the graph, we can compute $\mathbf{\sigma}_e = k_e (d\mathbf{x}_e)$, which is the stress (stiffness times strain) on that edge. To get the actual force $\mathbf{f}_i$ actuing on each node, the chain rule requires us to sum up the stress vectors from all the edges that touch that specific node. Indeed,
$$
f_i = \text{div}(\mathbf{\sigma})
$$
where $\text{div}$ is the graph divergence operator. Thus, the force on a node is the aggregate of the stress from all edges touching that node.

## Remark 
But of course, since this is just like machine learning, we can efficiently compute the forces on all nodes by matrix multiplications. Truly, we have 
$$
\begin{bmatrix}
m_1 &  \\ 
& \ddots  \\
&& m_i  \\
&&& \ddots \\
&&&& m_{|\mathcal{V}|} \\
\end{bmatrix}
\begin{bmatrix}
\ddot{\mathbf{x}}_1 \\
\vdots \\
\ddot{\mathbf{x}}_i \\
\vdots \\
\ddot{\mathbf{x}}_{|\mathcal{V}|} \\
\end{bmatrix}
= 
\underbrace{
  -\mathbf{d}^{\top}
  \begin{bmatrix}
  k_1 \\
  & \ddots \\
  && k_e \\
  &&& \ddots \\
  &&&& k_{|\mathcal{E}|} \\
  \end{bmatrix}
  \mathbf{d}
}_{\text{Graph Laplacian}}
\begin{bmatrix}
\mathbf{x}_1 \\
\vdots \\
\mathbf{x}_i \\
\vdots \\
\mathbf{x}_{|\mathcal{V}|} \\
\end{bmatrix}
$$
where the left side is global Newton's Second Law $F = ma$ and the right side is the restorative spring forces. Note that $\mathbf{K}(\mathbf{dx})$ here is Hooke's Law (forces on linear springs). The $\mathbf{d}^{\top}$ is actually the [[Dual Space#Definition (Adjoint Linear Map)|adjoint linear map]] (recall that the transpose is the adjoint of a linear map with respect to the standard inner product) acting as the discrete gradient. The multiplication of $\mathbf{d}^{\top} (\mathbf{K} \mathbf{dx})$ sums up all the converging spring tensions onto their shared nodes, calculating the net force on each node.

It's particularly important to mention the [[Laplacian Matrix|Graph Laplacian]] shown in the diagram. The final system becomes 
$$
\mathbf{M} \ddot{\mathbf{x}} = -\mathbf{L} \mathbf{x}
$$
where $\mathbf{L}$ encodes the connectivity of the graph and the stiffness of each edge. 

> This is a beautiful result. 