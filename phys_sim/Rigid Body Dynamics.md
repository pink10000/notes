---
tags:
  - CSE_291G
---
# Recap: Lagrangian Mechanics
Rigid body dynamics is an application of [[Lagrangian Mechanics]] to systems with specific geometric constraints.

Let the state be represented by **generalized coordinates** $\mathbf{q} \in Q$ and the [[Lagrangian Mechanics#Definition (Lagrangian)|Lagrangian]] be $L(\mathbf{q}, \dot{\mathbf{q}}) = K(\mathbf{q}, \dot{\mathbf{q}}) - U(\mathbf{q})$. The equations of motion are derived from the [[Lagrangian Mechanics#Theorem (Least Action Principle)|Least Action Principle]], which yields the **Euler-Lagrange equations**:
$$
\frac{\partial L}{\partial \mathbf{q}} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\mathbf{q}}} \right) = \mathbf{0}
$$

When applying the Lagrangian to the optimality for least action, we get 
$$
\underbrace{
  \frac{d}{dt} \left( \frac{\partial K}{\partial \dot{\mathbf{q}}} \right)
}_{\text{Change of momentum}}
=
\underbrace{
  \frac{\partial K}{\partial \mathbf{q}}
}_{\text{Fictitious force}}
\underbrace{
  -\frac{\partial U}{\partial \mathbf{q}}
}_{\text{Force}}
$$
If there is only kinetic energy and no potential energy then the resulting motion is called **pure inertial motion**. 

## Lagrangian in Newtonian Mechanics
The generalized coordinate $\mathbf{q}$ is a low dimensional parameterization of infinitely many atoms $a \in \cA$. There is[^1] a smooth function describing the physical 3D position of each atom as a function of $\mathbf{q}$:
$$
\begin{aligned}
\R^m &\xrightarrow{\mathbf{f}_a} \R^3 \\
\mathbf{x}_a &= \mathbf{f}_a(\mathbf{q}) \in \R^3
\end{aligned}
$$
[^1]: Why?
The kinetic and potential energy on $(\mathbf{q}, \dot{\mathbf{q}})$ by [[Dual Space#Definition (Pullback Operator for Functions)|pulling back]] the energies from 3D space
$$
K(\mathbf{q}, \dot{\mathbf{q}}) =
\int_{a \in \cA} \frac{1}{2} \bigg| 
d\mathbf{f}_{a}|_{\mathbf{q}} \llbracket \dot{\mathbf{q}} \rrbracket
\bigg|^{2}_{\R^3} \, da
% 
\quad\quad\quad
U(\mathbf{q}, \dot{\mathbf{q}}) = \int_{a \in \cA} u(\mathbf{f}_a(\mathbf{q})) \, da
$$
In general, the kinetic energy is a [[Definite Matrix|positive definite]] quadratic function of $\dot{\mathbf{q}}$[^2]. This defines an inner product
$$
\begin{aligned}
K(\mathbf{q}, \dot{\mathbf{q}}) 
&= \frac{1}{2} \flat_{\mathbf{q}}(\dot{\mathbf{q}}, \dot{\mathbf{q}}) \\
&= \frac{1}{2} \dot{\mathbf{q}}^{\top} \mathbf{M}(\mathbf{q}) \dot{\mathbf{q}}
\end{aligned}
$$
[^2]: Kinetic energy cannot be negative. Since kinetic energy here is expressed as a quadratic form in generalized velocities $\dot{\mathbf{q}}$, the matrix $\mathbf{M}(\mathbf{q})$ must be positive definite to ensure that $K$ is always positive for any nonzero $\dot{\mathbf{q}}$. Especially if we consider when $\dot{\mathbf{q}} = \bzero$, then $K(\mathbf{q}, \bzero) = 0$ for all $\mathbf{q}$. 

# Definition (Momentum, Generalized Coordinate)
The **momentum** for the generalized coordinate $\bq$ is defined as
$$
\bp = \frac{\partial K}{\partial \dot{\bq}} 
= \flat_{\bq}(\dot{\bq})
= \mathbf{M}_{\bq} \dot{\bq}
$$
This notion of momentum is the [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] of the momentum $1-$form from the moment of the classical particle system ($p = mv$). 

# Rigid Body Kinematics
A **rigid body** is a system of particles that maintains fixed distances between all pairs of particles. For a rigid body, the [[Degrees of Freedom (Physics)|degrees of freedom]] is given by the space of Euclidean transformations:
$$
Q = \SE(3) = \left\{
\begin{bmatrix}
&&&| \\
&\mathbf{R}_{3 \times 3}&& \mathbf{c} \\
&&&| \\
0&0&0&1
\end{bmatrix}
% 
\middle|
% 
\mathbf{R}^\top \mathbf{R} = I,
\quad\det(\mathbf{R}) = 1,
\quad\mathbf{c} \in \R^3
\right\}
= \{(\mathbf{R}, \mathbf{c}) \}
$$
Here, $\mathbf{R}$ is a rotation matrix and $\mathbf{c}$ is a translation vector. $\SE(3)$ represents the [[Euclidean Group#Definition (Special Euclidean Group)|special Euclidean group]], which is the group of all rigid transformations in three-dimensional space. 

Each element $\bq \in (\bR, \bc) \in Q$ is a transformation that maps a position in the body coordinate to a position in the world coordinate. For example, 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{xcolor}

\begin{document}
\begin{tikzpicture}[scale=1]

% Define colors to match the image
\definecolor{mypurple}{RGB}{125, 75, 175}
\definecolor{myblue}{RGB}{65, 110, 185}

% --- Body Frame (Purple) ---
\begin{scope}
    % Box
    \draw[mypurple, line width=1.5pt] (0, 0) rectangle (3.5, 1.5);
    
    % Point a
    \fill[mypurple] (2.5, 1.0) circle (3.5pt);
    
    % Label a
    \node[text=mypurple, font=\Large] at (2.5, 1.0) [above=13pt] {$\mathbf{a} \in \mathbb{R}^3_{\text{body}}$};
\end{scope}

% --- World Frame (Blue) ---
% Shifted up and right, rotated to match the image visually
\begin{scope}[shift={(4.0, 4.5)}, rotate=-50]
    % Box
    \draw[myblue, line width=1.5pt] (0, 0) rectangle (3.5, 1.5);
    
    % Point x (placed at the exact same local coordinates as point a)
    \fill[myblue] (2.5, 1.0) circle (3.5pt);
    
    % Save the coordinate to draw the label un-rotated in the global frame
    \coordinate (X_dot) at (2.5, 1.0);
\end{scope}

% Label x (drawn outside the scope so the text remains horizontally aligned)
\node[text=myblue, font=\Large] at (X_dot) [anchor=south west, xshift=10pt, yshift=3pt] {$\mathbf{x} \in \mathbb{R}^3_{\text{world}}$};

\end{tikzpicture}
\end{document}
```

is described by the transformation
$$
\begin{bmatrix}
{\color{#416eb9}x_1} \\ {\color{#416eb9}x_2} \\ {\color{#416eb9}x_3} \\ 1
\end{bmatrix}
= 
\begin{bmatrix}
&&&| \\
&\mathbf{R}_{3 \times 3}&& \mathbf{c} \\
&&&| \\
0&0&0&1
\end{bmatrix}
\begin{bmatrix}
{\color{#7d4baf} a_1} \\ {\color{#7d4baf} a_2} \\ {\color{#7d4baf} a_3} \\ 1
\end{bmatrix}
$$
## Tangent Vectors in Rigid Bodies
How can we describe a [[Dual Space#Definition (Tangent Space)|tangent vector]] $\dot{\bq} \in T_{\bq}Q$? 

>[!info] Differential 
> We can consider $(\dot{\bR}, \dot{\bc})$ but we'd need to account for the constraint that $\bR^\top \bR = I$.

Recall that since $\bR$ is a rotation matrix, it must be orthogonal, meaning that $\bR^\top \bR = I$. So, taking the derivative of both sides with respect to time, we get
$$
\begin{aligned}
\frac{d}{dt} (\bR^\top \bR) &= \frac{d}{dt} I \\
\dot{\bR}^\top \bR + \bR^\top \dot{\bR} &= \bzero \\
(\bR^\top \dot{\bR})^\top + \bR^\top \dot{\bR} &= \bzero \\
\end{aligned}
$$
Therefore $\bR^\top \dot{\bR}$ is a [[Skew-Symmetric Matrix|skew-symmetric matrix]]. Similarly, 
$$
\bR^\top \bR = I
\implies \bR\bR^\top = I
$$
Taking the derivative of both sides with respect to time, we get
$$
\begin{aligned}
\frac{d}{dt} (\bR\bR^\top) &= \frac{d}{dt} I \\
\dot{\bR}\bR^\top + \bR\dot{\bR}^\top &= \bzero \\
\dot{\bR}\bR^\top + (\dot{\bR}\bR^\top)^\top &= \bzero \\
\end{aligned}
$$
and so both $\bR^\top \dot{\bR}$ and $\dot{\bR}\bR^\top$ are skew-symmetric matrices. Let 
$$
\begin{aligned}
\bA &= \bR^\top \dot{\bR} \\
\bW &= \dot{\bR}\bR^\top
\end{aligned}
$$
Then $\dot{\bR} = \bR\bA = \bW\bR$. By [[Skew-Symmetric Matrix#Relation to Cross Product|theorem]], every skew-symmetric matrix is a cross product with a vector, such that 
$$
\dot{\bR} = \bR[\Omega \times] = [\omega \times]\bR
$$
where 
$$
\bA = [\Omega \times] = 
\begin{bmatrix}
0 & -\Omega_3 & \Omega_2 \\
\Omega_3 & 0 & -\Omega_1 \\
-\Omega_2 & \Omega_1 & 0
\end{bmatrix}
\quad\quad\quad
\bW = [\omega \times] = 
\begin{bmatrix}0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{bmatrix}
$$
We call $\Omega \in \R_{\text{body}}^3$ the **body coordinate angular velocity** and $\omega \in \R_{\text{world}}^3$ the **world coordinate angular velocity**. Indeed, one can verify that $\mathbf{\omega} = \bR \Omega$.

Thus, a tangent vector $\dot{\bq} \in T_{\bq}Q$ is represented by a 6D vector
$$
(\omega, \dot{\bc}) \in \R^3_{\text{world}} \times \R^3_{\text{world}}
\quad\quad\quad
(\Omega, \dot{\bc}) \in \R^3_{\text{body}} \times \R^3_{\text{world}}
$$
We can pick if we want to represent the angular velocity in the world coordinate or the body coordinate. In particular, suppose the $i-$th point in the body has position and mass 
$$
\ba_i \in \R^3_{\text{body}}
\quad\quad\quad
m_i \in \R_{\geq 0}
$$
then the translated position of the $i-$th point in the world coordinate $\R^3_{\text{world}}$ is
$$
\bx_i = \bR \ba_i + \bc
$$
and the velocity of the $i-$th point in the world coordinate is
$$
\begin{aligned}
\dot{\bx}_i 
&= [\omega \times] \bx_i + \dot{\bc} \\ 
&= \bR [\Omega \times] \ba_i + \dot{\bc} \\
&= \bR (\Omega \times \ba_i) + \dot{\bc}
\end{aligned}
$$
This makes sense because we get the world angular velocity contribution from $[\Omega \times]$. Then we can convert to the body angular velocity contribution by multiplying with $\bR$, and finally we apply [[Skew-Symmetric Matrix#Relation to Cross Product|theorem]] to show the cross product. 

With out velocity, we can compute the kinetic energy as
$$
\begin{aligned}
K(\bx, \dot{\bx})
&= \sum_{i \in \text{body}} \frac{m_i}{2} |\dot{\bx}_i|^2 \\
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left| \bR (\Omega \times \ba_i) + \dot{\bc} \right|^2 \\
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left| \bR (\Omega \times \ba_i) \right|^2 
+ \sum_{i \in \text{body}} m_i \langle \bR (\Omega \times \ba_i), \dot{\bc} \rangle
+ \sum_{i \in \text{body}} \frac{m_i}{2} |\dot{\bc}|^2 \\
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left| \Omega \times \ba_i \right|^2 
+ \sum_{i \in \text{body}} m_i \langle \bR(\Omega \times \ba_i),\dot{\bc} \rangle
+ \frac{m}{2} |\dot{\bc}|^2 \\
\end{aligned}
$$
In the first term, we can remote $\bR$ because the norm of a rotation matrix is $1$ (it preserves lengths). In the third term, $m$ is simply the total mass of the body. 

Consider the second term. All the operations listed are linear, and that $\bR, \Omega$ are not dependent on particle $i$, so we can factor them out of the summation:
$$
\sum_{i \in \text{body}} m_i \langle \bR(\Omega \times \ba_i),\dot{\bc} \rangle
= 
\left\langle \bR \left( \Omega \times \sum_{i \in \text{body}} m_i \ba_i \right), \dot{\bc} \right\rangle
$$
>[!info] Center of Mass
> Recall that the formula for calculating the position vector of the center of mass is
> $$
> \br_{\text{com}} = \frac{1}{m} \sum_{i \in \text{body}} m_i \ba_i
> $$

We can get 
$$
m\br_{\text{com}} = \sum_{i \in \text{body}} m_i \ba_i
$$
If we choose the body coordinate $\ba$ such that the center of mass is at the origin, then $\br_{\text{com}} = \bzero$ (recall it is relative to the body coordinate) and so 
$$
\sum_{i \in \text{body}} m_i \ba_i = m\br_{\text{com}} = \bzero
$$
Returning back to the kinetic energy, we get
$$
K(\bx, \dot{\bx})
= \sum_{i \in \text{body}} \frac{m_i}{2} \left| \Omega \times \ba_i \right|^2 
+ \frac{m}{2} |\dot{\bc}|^2
$$

# Theorem (Kinetic Energy Decoupling)
If the origin of the body coordinate is at the center of mass, then the kinetic energy is 
$$
K(\bq, \dot{\bq}) 
= \underbrace{
  \frac{m}{2} |\dot{\bc}|^2
}_{K_{\text{com}}(\dot{\bc})}
+
\underbrace{
  \sum_{i \in \text{body}} \frac{m_i}{2} \left| \Omega \times \ba_i \right|^2
}_{K_{\text{rot}}(\bR, \dot{\bR})}
$$
That is, the translation and rotation contributions to the kinetic energy are decoupled. Indeed, 
- the pure *translational* kinetic energy of the center of mass moving through space is the first term
- the pure *rotational* kinetic energy about the center of mass is the second term

# Definition (Inertia Tensor)
We can further expand the $K_{\text{rot}}(\bR, \dot{\bR})$ term.
$$
\begin{aligned}
K_{\text{rot}}(\bR, \dot{\bR})
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left| \Omega \times \ba_i \right|^2 \\
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left| [\ba_i \times]\Omega \right|^2 \\
&= \sum_{i \in \text{body}} \frac{m_i}{2} \left( \Omega^\top [\ba_i \times]^\top [\ba_i \times] \Omega \right) \\
&= \frac{1}{2} \Omega^\top \left( 
  \sum_{i \in \text{body}} m_i [\ba_i \times]^\top [\ba_i \times] 
\right) \Omega \\ 
&= \frac{1}{2} \Omega^\top \left( 
  \sum_{i \in \text{body}} m_i \left( |\ba_i|^2 I - \ba_i \ba_i^\top \right)
\right)
\end{aligned}
$$
There are many steps.
1. By the anti-commutative property of the cross product and [[Skew-Symmetric Matrix#Relation to Cross Product|theorem]] 
2. Since $[\ba_i \times] \Omega$ is a vector, its squared norm is equivalent to dot product with itself.  
3. We can factor out body angular velocity $\Omega$ since it is identical to every particle.
4. By [[Skew-Symmetric Matrix#Theorem (Skew-Symmetric Transpose Multiplication)|theorem]], we get the final line.

For a rigid body centered at the origin of the body coordinate, the **moment of intertia** or the **inertia tensor** is defined as
$$
\bI_{\text{body}}
= \sum_{i \in \text{body}} m_i \left( |\ba_i|^2 I - \ba_i \ba_i^\top \right)
$$
For a continuous object, we can replace the summation with an integral:
$$
\bI_{\text{body}} \iiint_{\ba \in \text{body}} \left(
  |\ba|^2 I - \ba \ba^\top
\right) \, dm_{\ba}
$$

## Inertia Tensor in Kinetic Energy
With the inertia tensor, we can express the total inertial kinetic energy (assuming the center of mass is at the origin) from [[#Theorem (Kinetic Energy Decoupling)]] as 
$$
K(\bq, \dot{\bq})
= \frac{m}{2} |\dot{\bc}|^2 + \frac{1}{2} \Omega^\top \bI_{\text{body}} \Omega
$$
where the $3 \times 3$ symmetric matrix $\bI_{\text{body}}$ is the moment of inertia which is time independent. 

Using the world coordinate, we can express the total inertial kinetic energy as
$$
K(\bq, \dot{\bq})
= \frac{m}{2} |\dot{\bc}|^2 + \frac{1}{2} \omega^\top \bI_{\text{world}} \omega
$$
where
$$
\bI_{\text{world}} = \bR \bI_{\text{body}} \bR^\top
$$
is the inertia in the world coordinate. For a rigid body, $\bI_{\text{body}}$ is time-independent. However, $\bI_{\text{world}}$ is dynamic, and co-rotates with the rigid body. 

> [!info] Inertia Tensor in World Coordinate
> In particular, we say it is dynamic because its axes of rotation changes with the rigid body's rotation with respect to the world coordinate axes. The fact that 
> $$
> \bI_{\text{world}} = \bR \bI_{\text{body}} \bR^\top
> $$
> means that finding its position in the world coordinate, we must update $\bI_{\text{world}}$ to reflect the object's current orientation. 
>
> As the rigid body rotates, $\bR$ changes, causing $\bI_{\text{world}}$ to change accordingly. This reflects how the distribution of mass relative to the world axes changes as the body rotates, even though the distribution of mass relative to the body axes (captured by $\bI_{\text{body}}$) remains constant.

## Theorem (Moment of Inertia Semi-Definiteness)
The moment of inertia is [[Definite Matrix#Definition (Positive Definite Matrix)|positive semi-definite]], and its $3$ eigenvalues satisfy the triangle inequality.

Proof:

WLOG, we can choose[^1] the basis that diagonalizes the inertia tensor, such that
$$
\bI = \begin{bmatrix}
\lambda_1 & 0 & 0 \\
0 & \lambda_2 & 0 \\
0 & 0 & \lambda_3
\end{bmatrix}
$$
[^1]: TODO: show that we can always choose such a basis.
Let 
$$
i_x = \int \frac{|x|^2}{2} \,dm
\quad\quad
i_y = \int \frac{|y|^2}{2} \,dm
\quad\quad
i_z = \int \frac{|z|^2}{2} \,dm
$$
These variables will act as "intermediates" to help us express the eigenvalues of the inertia tensor.

The diagonal entries (and thus the eigenvalues) of the inertia tensor are
$$
\lambda_1 = \int_\text{body} \left( |y|^2 + |z|^2 \right) \, dm = i_y + i_z
$$
and similarly $\lambda_2 = i_x + i_z$ and $\lambda_3 = i_x + i_y$. Because $i_{x}, i_{y}, i_{z}$ are all non-negative, then any sum of them must also be positive. Therefore $\lambda_1, \lambda_2, \lambda_3$ are non-negative. This proves that the inertia tensor is positive semi-definite. 

Moreover, we can check that the eigenvalues satisfy the triangle inequality.
$$
\begin{aligned}
\lambda_1 + \lambda_2 &\geq \lambda_3 \\
(i_y + i_z) + (i_x + i_z) &\geq i_x + i_y \\
2i_z &\geq 0
\end{aligned}
$$
and so we are done. 

> [!important] Main Idea
> Recall that the moment of inertia is defined as 
> $$
> I = mr^2
> $$
> where $m$ is the mass and $r$ is the distance from the axis of rotation (radius). The idea is that on each axis, the moment of inertia is the sum of the contributions from all mass elements, and each contribution is proportional to the square of the distance from that axis. 
> 
> In particular, if we consider the $x$-axis, then the distance from the $x$-axis for a mass element at position $(x, y, z)$ is $r^2 = y^2 + z^2$. 

# Definition (Spinning Top)
A rigid body is called a **spinning top** if a pair of eigenvalues of its inertia tensor are equal. That is, for the spinning top, there is a continuous family of rotation $\bQ$ so that 
$$
\bQ \bI_{\text{body}} \bQ^\top = \bI_{\text{body}}
$$

# Equations of Motion for Rigid Bodies
The equations of motion for a rigid body can be described as follows. Let
- $\bR$ be the rotation matrix representing the orientation of the rigid body
- $\bc$ be the translation vector representing the position of the center of mass of the rigid body
- $\omega$ be the world coordinate angular velocity
- $\Omega$ be the body coordinate angular velocity
- $\bI_{\text{body}}$ be the inertia tensor in the body coordinate
- $\bI_{\text{world}}$ be the inertia tensor in the world coordinate 

In total, 
$$
\text{Body-Frame Formulation}:
\begin{cases}
\dot{\bR} &= \bR [\Omega \times] \\
\bI_{\text{body}} \dot{\Omega} &= -\Omega \times (\bI_{\text{body}} \Omega) \\
m \ddot{\bc} &= -\frac{\del U}{\del \bc}
\end{cases}
$$
and likewise,
$$
\text{World-Frame Formulation}:
\begin{cases}
\dot{\bR} &= [\omega \times] \bR \\
\bI_{\text{world}} \dot{\omega} &= -\omega \times (\bI_{\text{body}} \omega) \\
\bI_{\text{world}} &= \bR \bI_{\text{body}} \bR^\top \\
m \ddot{\bc} &= -\frac{\del U}{\del \bc}
\end{cases}
$$

# Applying the Lagrangian to Rigid Bodies
Recall that the [[Lagrangian Mechanics#Definition (The Lagrangian)|Lagrangian]] is defined as $L = K - U$. If we assume there are no external forces, then the potential energy $U$ is $0$ and so $L = K$. From [[#Inertia Tensor in Kinetic Energy]], we can take the variation from only the rotational kinetic energy. 
$$
\int_{0}^{T} \frac{1}{2} \Omega(t)^\top \bI_{\text{body}} \Omega(t) \, dt
$$

## Theorem (Angular Momentum is Conserved in World Coordinate)
The conservation of angular momentum depends on which coordinate system we use. The **world coordinate angular momentum** is defined as 
$$
\mathbf{1} := \bI_{\text{world}} \omega
$$
We say that the world coordinate angular momentum is conserved if $\mathbf{1}$ is constant over time. In particular,
$$
\frac{d}{dt} \mathbf{1} = \bzero
$$
Since both $\bI_{\text{world}}$ and $\omega$ are [[## Inertia Tensor in Kinetic Energy|dependent on time]], we can apply the product rule to get
$$
\begin{aligned}
\bzero &= \frac{d}{dt} \mathbf{I}_\text{world} \omega \\
&= \dot{\bI}_{\text{world}} \omega + \bI_{\text{world}} \dot{\omega} \\
\end{aligned}
$$
The goal is to manipulate the first term so that is equal to one of the [[#Equations of Motion for Rigid Bodies|World-Frame Formulation]] equations of motion. Indeed, we can compute the product rule again 
$$
\begin{aligned}
\dot{\bI}_{\text{world}}
&= \frac{d}{dt} (\bR \bI_{\text{body}} \bR^\top) \\
&= \dot{\bR} \bI_{\text{body}} \bR^\top + \bR \bI_{\text{body}} \dot{\bR}^\top \\
\end{aligned}
$$
Recall that $\bI_{\text{body}}$ is time independent, so its derivative is $\bzero$. By equation 1 of the World-Frame Formulation, we can substitute $\dot{\bR} = [\omega \times] \bR$ to get
$$
\begin{aligned}
\dot{\bR} \bI_{\text{body}} \bR^\top + \bR \bI_{\text{body}} \dot{\bR}^\top 
&= ([\omega \times] \bR) \bI_{\text{body}} \bR^\top + \bR \bI_{\text{body}} (\bR^\top [-\omega \times]) \\
&= [\omega \times] \bI_{\text{world}} - \bI_{\text{world}} [\omega \times] \\
\end{aligned}
$$
Thus
$$
\dot{\bI}_{\text{world}}\omega = [\omega \times] \bI_{\text{world}} \omega - \bI_{\text{world}} [\omega \times] \omega
$$
Since $[\omega \times] \omega$ is equivalent to $\omega \times \omega$ (via [[Skew-Symmetric Matrix#Relation to Cross Product|theorem]]), and $\omega \times \omega = \bzero$ (by anti-commutative property of the cross product), we get
$$
\dot{\bI}_{\text{world}}\omega = [\omega \times] \bI_{\text{world}} \omega
$$
Substituting back into the product rule, we get
$$
\bzero = [\omega \times] \bI_{\text{world}} \omega + \bI_{\text{world}} \dot{\omega}
$$
which is exactly the second equation of the World-Frame Formulation. Therefore using the world coordinate angular momentum conserves angular momentum.

## Theorem (Angular Momentum is Not Conserved in Body Coordinate)
Imagine we are an ant glued to the rigid body flying around in empty space. Since we have the world frame angular momentum, translating it to the body frame is just a rotation. The **angular momentum in the body frame** is defined as 
$$
\bL := \bI_{\text{body}} \Omega
$$
Recall this is similar to the classical definition of angular momentum, $L = I \omega$ where $I$ is the moment of inertia and $\omega$ is the angular velocity. From how we derived the [[#Applying the Lagrangian to Rigid Bodies|integrand]], we know kinetic energy wrt to the body is 
$$
K = \frac{1}{2} \Omega^{\top} \bI_{\text{body}} \Omega 
$$
Thus, 
$$
\begin{aligned}
\frac{dK}{d\Omega} &= \bI_{\text{body}} \Omega \\
&= \bL \\
\end{aligned}
$$
We can reuse from [[#Theorem (Angular Momentum is Conserved in World Coordinate)|before]] that 
$$
\begin{aligned}
\mathbf{1} 
&= \bI_{\text{world}} \omega \\ 
&= (\bR \bI_{\text{body}} \bR^{\top})(\bR \Omega) \\ 
&= \bR \bI_{\text{body}} \Omega \\ 
&= \bR \bL
\end{aligned}
$$
and so $\bL = \bR^{\top}\mathbf{1}$. And since $\bR$ (and thus $\bR^{\top}$) is dependent on time, angular momentum is not conserved. 