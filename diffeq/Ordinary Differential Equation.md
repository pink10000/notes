---
tags:
  - MATH_20D
---
# Definition (Ordinary Differential Equation)
An **Ordinary Differential Equation (ODE)** is a mathematical equation that relates a function of a *single independent variable* (in physics, almost always time, $t$) to its derivatives. Formally, for a state vector $y:[0,T] \rightarrow \mathbb{R}^m$, an ODE specifies a constraint of the form
$$
F_t \left( y(t), \dot{y}(t), \ddot{y}(t), \ldots, y^{(n)}(t) \right) = 0 
\quad\quad\quad
\text{for all } t \in [0, T] 
$$
To solve an ODE means finding the specific trajectory $y(t)$ that satisfies this constraint for all moments in time, given a specific starting state. In particular, $y(t) = [y_1(t), y_2(t), \ldots, y_m(t)]^{\top}$. 

## Classification by Order
We can classify ODEs by their **order**, which is the highest derivative that appears in the equation. If $k=1$, we call the ODE a first order ODE. If $k=2$, we call it a second order ODE, and so on.

## Classification by Dimensionality
This defines the "size" of the state space, or the degrees of freedom of the system. If $m=1$, we call the ODE a scalar ODE. If $m>1$, we call it a system of ODEs, or a vector ODE.

## Classification by Linearity
Linearity dictates how easily a system can be solved analytically and how predictably it behaves.
- **Linear ODE:** The function $F$ is a linear combination of the state variables and their derivatives. There are no variables multiplied by each other, squared, or trapped inside transcendental functions like sine or cosine. They can generally be written in matrix form:
$$
\dot{y}(t) = A(t)y(t) + b(t)
$$
- **Nonlinear ODE:** The variables interact in non-proportional ways (e.g., $v^2$, $x \cdot v$, or $\sin(\theta)$). The pendulum equation ($\ddot{\theta} = -\frac{g}{L}\sin(\theta)$) is strictly nonlinear. Nonlinear systems can exhibit chaos, multiple equilibrium states, and are generally impossible to solve with exact formulas, making numerical step-by-step simulation strictly necessary.

## Classification by Time-Dependence (Autonomy)
The ODE $F$ is called **autonomous** if the function $F$ does not explicitly depend on time $t$. In this case, the rules governing the system's evolution are fixed and do not change as time progresses.

## Classification by Homogeneity
This distinction is primarily used when finding analytical (exact) solutions to linear equations.
- **Homogeneous:** The system has no external driving forces; the equation equals zero ($b(t) = 0$). If the system starts at rest at the origin, it will stay there forever. $F_t(\alpha u_1, \dots, \alpha u_k) = \alpha^r F_t(u_1, \dots, u_k)$.
- **Inhomogeneous:** The system includes an isolated forcing term ($b(t) \neq 0$) that drives the system independently of its current state. The complete solution requires finding the general homogeneous solution (how the system naturally wants to ring or oscillate) and adding a particular solution (how the system responds directly to the external force).

### Theorem (Homogeneous Solutions Form a Vector Space)
If $y_1(t)$ and $y_2(t)$ are solutions to a homogeneous linear ODE, then any linear combination 
$$
y(t) = c_1 y_1(t) + c_2 y_2(t)
$$
will also be a solution. That is, the set of all solutions to a homogeneous linear ODE forms a [[Vector Space]]. The dimension of this vector space is $km$. 

> Also known as the **Superposition Principle**, this is a fundamental property of linear systems that allows us to construct new solutions from known ones.

# Definition (Fundamental Solutions)
A set of basis for the solution space of homogeneous linear ODEs is called the **fundamental solutions**.

# Theorem (Affine Solution)
If the ODE is linear (but inhomogeneous), then the solution space is an **affine space**. That is, all solutions can be written as a solution plus linear combinations of the fundamental solutions to the homogeneous part of the ODE. 

> Visually, think of affine spaces as a shifted version of a vector space. In a vector space, $(0, 0, 0)$ is always a solution. In an affine space, there is some particular solution that serves as the "origin," and all other solutions can be reached by adding linear combinations of the homogeneous solutions to this particular solution. 

# Separable ODEs 
A first-order ODE is called **separable** if it can be written in the form
$$
\frac{dy}{dt} = g(t)h(y)
$$
For example, 
$$
\dot{y} = \lambda y \implies y = y_0 e^{\lambda t}
$$

## Remark (Non-Separable ODEs)
If a first order ODE is not separable, we can still solve it when it is linear. (First solve the homogeneous part, then solve the full system using variation of constants.) 

# Theorem (Reduction to First-Order Systems)
An $m$-th order ODE system of size $k$ is equivalent to a first-order ODE system of size $km$. 

For example, consider the second-order ODE for a pendulum:
$$
m \ddot{\theta} = - mg \sin(\theta) 
$$
We see that the motion is independent of the mass $m$, so we can simplify to
$$
\ddot{\theta} = -g \sin(\theta)
$$
To eliminate the second derivative $\ddot{\theta}$, we must define a new variable to represent the first derivative $\dot{\theta} = \omega$ or angular velocity. By substituting $\omega$ into the original equation, we can express the second-order ODE as a system of two first-order ODEs:
$$
\begin{cases}
\dot{\theta} = \omega \\
\dot{\omega} = -g \sin(\theta)
\end{cases}
$$
Finally, we can write this system in vector form as
$$
y = \begin{bmatrix} \theta \\ \omega \end{bmatrix}
\quad\quad\quad
\dot{y} = \begin{bmatrix} \omega \\ -g \sin(\theta) \end{bmatrix}
$$
Note that is system is strictly nonlinear. 

## Remark (Reduction to Higher-Order Systems)
The conversion preserves notions of linearity, homogeneity, and autonomy. At higher dimensions, linear ODEs can all be transformed to 
$$
\dot{y}(t) = \underbrace{A(t)y(t)}_{\text{square matrix}} + \underbrace{b(t)}_{\text{vector}}
$$
When $A$ depends on $t$, there is not an easy way of solving it (unless $A$ is $1 \times 1$). When $A$ is constant, we can solve its "eigenvalue problem" for the homogeneous solutions. Explicitly, homogeneous solutions are given by the matrix exponential $y(t) = e^{t A} y_0$. To find a solution with a nontrivial $b(t)$, use variation of constants.

To solve $\dot{y}(t) = Ay(t)$, the idea is that we can assume the solution takes the form of an exponential function, similar to scalar ODEs, but involving vectors.
$$
y(t) = ve^{\lambda t}
$$
Here, $v$ is a constant vector and $\lambda$ is a scalar constant. Derivation gives $\dot{y}(t) = \lambda ve^{\lambda t} = \lambda y(t)$. By substituting into the original equation, we get
$$
\begin{aligned}
\dot{y}(t) &= Ay(t) \\
\lambda y(t) &= Ay(t) \\
\lambda ve^{\lambda t} &= A \left(ve^{\lambda t}\right) \\
\end{aligned}
$$
Since $e^{\lambda t}$ is never zero, we can divide both sides by it to get
$$
\lambda v = Av
$$
Solving this equation amounts to finding the eigenvalues $\lambda$ and corresponding eigenvectors $v$ of the matrix $A$. 

# General Analytical Methods
Every ODE can be converted into $\dot{y}(t) = \mathbf{f}(t, y(t))$. Indeed, 
$$
\mathbf{f}(t, \cdot ) : \R^{mk} \rightarrow \R^{mk}
$$ 
can be through as of a [[Vector Field]] on $mk$-space and the solution is a path on this space tangential to the vector field (best when it is autonomous). For [[#Classification by Time-Dependence (Autonomy)|autonomous]] systems, points where $\mathbf{f}(y) = 0$ are called **steady states** or **static states**. 

Rather than solving the entire system, we can analyze how the system behaves very close to these steady states through linearization. By introducing a small perturbation $\vepsi y_{\text{perturb}}(t)$ around the steady state $y_{\text{static}}$, the function can be approximated using a [[Taylor's Theorem|Taylor series]] [[Gradient#First-Order Taylor Expansion|expansion]]. 
$$
\mathbf{f}(y_{\text{static}} + \vepsi y_{\text{perturb}}) \approx
\underbrace{\mathbf{f}(y_{\text{static}})}_{=0} + 
\vepsi \underbrace{A}_{Df|_{y_{\text{static}}}} y_{\text{perturb}}(t) +
O(\vepsi^2)
$$
and get 
$$
\frac{d}{dt} y_{\text{perturb}}(t) = A y_{\text{perturb}}(t)
$$
Note that $A$ is the Jacobian matrix of $\mathbf{f}$ evaluated at the steady state $y_{\text{static}}$. Indeed, this allows us to analyze the stability of the steady state by looking at the eigenvalues of $A$. 

For harder, more complex ODEs, we'll need [[Numerical Methods|Numerical Methods]] to solve them.
## Non-Autonomous Systems
For non-autonomous systems, one can still track stable "quasi-static" states that depends on time $t$. These are points where $\mathbf{f}_t(y_{\text{static}}, t) = 0$. This approach requires the assumption that the function $f$ changes with respect to time $t$ at a much slower rate than the system takes to relax back to its steady state. 

Consider the population of a species with the presence of an adversarial predator. 
$$
\dot{y} = y(1 - y) - a(t)
$$
where $a(t)$ is the population of the predator and $y$ is the population of the prey. 
