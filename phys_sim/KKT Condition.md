---
tags:
  - CSE_291G
---
# Goal
Given a [[Derivative|differentiable]] function $f : M \to \R$, what is the condition for the minimizer of $f$? What if there are constraints? The general answer is the **Karush-Kuhn-Tucker (KKT) condition**, which is typically written in a coordinate-heavy form. 

Is there a high level understanding of KKT condition using the notion of [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] and [[Dual Space#Definition (Pushforward Operator)|pushforward]]? 

# Karush-Kuhn-Tucker (KKT) Condition
The problem is that we want to 
$$
\min_{x \in \R^n} E(x)
$$
subject to $g_i(x) = 0$ for $i = 1, \dots, m$ and $h_j(x) \leq 0$ for $j = 1, \dots, \ell$. 

The KKT Theorem states that the optimizer $x_0$ of the above problem satisfies 
$$
\nabla E|_{x_0} + \sum_{i=1}^m \lambda_i \nabla g_i|_{x_0} + \sum_{j=1}^\ell \mu_j \nabla h_j|_{x_0} = 0
$$
$$
\mu_1, \dots, \mu_\ell \geq 0
$$
$$
\sum_{j=1}^\ell \mu_j h_j(x_0) = 0
$$

## High Level Understanding of KKT Condition
Imagine you are a ball rolling down a 3D hill and you want to minimize your energy function $E(x)$. Reaching the bottom of the hill is the optimal solution. However, there are some constraints on where you can go. Consider when $g_i(x) = 0$. This is like saying there are rigid train tracks. The ball must stay exactly on this line. Consider the constraint $h_j(x) \leq 0$. These are like fences. The ball can roll freely inside the fenced yard ($h_j(x) < 0$) , but cannot cross the boundary ($h_j(x) = 0$). 

The KKT Theorem states that if the ball is at the optimal solution $x_0$, those three specific conditions must hold. 
1. This balances the forces. The gradient $\nabla E|_{x_0}$ is gravity pulling the ball down the hill. Without constraints, the ball would stop where gravity is zero ($\nabla E|_{x_0} = 0$). However, the train tracks and fences exert forces on the ball. It means the track $\nabla g$ and the fence $\nabla h$ are pushing the ball with exact, equal, and opposite forces to balance the gravity. The scalars $\lambda_i$ and $\mu_j$ are the strength of the forces. The net force must be $0$ for the ball to be at rest.
2. The second condition says the force from the fence must be pushing inward. If $\mu_j < 0$, the force from the fence is pushing outward, which means the ball is trying to cross the fence. This cannot be optimal because the ball can roll freely inside the fenced yard, so it can always find a better solution by rolling inside the yard. 
3. We know $\mu_j \geq 0$ from condition 2 and $h_j(x_0) \leq 0$ from the constraint. Since every single term in the sum $\sum_{j=1}^\ell \mu_j h_j(x_0)$ is non-positive, the only way for the sum to be $0$ is that every single term is $0$. In particular, for $\mu_j h_j (x_0)$ to equal $0$, one of two must be true.
	1. The ball is far away from the fence, meaning $h_j(x_0) < 0$. Because the ball is not touching the fence, there is no force from the fence, so $\mu_j = 0$. Thus the product is $0$.
	2. The ball is touching the fence, meaning $h_j(x_0) = 0$. The product is still $0$. (Note that $\mu_j > 0$).

# Definition (Annihilator Subspace)
The **annihilator subspace** of a [[Vector Space|subspace]] $W \subset U$ is a subspace $W^\circ \subset U^*$ defined by 
$$
W^\circ := \left\{ \lambda \in U^* \mid \langle \lambda|\vec{w} \rangle = 0, \forall \vec{w} \in W  \right\}
$$

> It's like the dual of the null space. 

# Definition (Polar Cone)
The **polar cone** of a subset $S \subset U$ is a subset $S^\circ \subset U^*$ defined by
$$
S^\circ := \left\{ \lambda \in U^* \mid \langle \lambda|\vec{s} \rangle \leq 0, \forall \vec{s} \in S  \right\}
$$

## Proposition (Convexity of Polar Cone)
The polar cone of any set is a convex cone.

## Proposition (Polar Cone of a Subspace)
The polar cone of a subspace is the annihilator space.

# Definition (Four Fundamental Subspaces)
The **four fundamental subspaces** of a linear map $A : U \to V$ are the following four subspaces:
1. Kernel
$$
\text{ker}(A) := \left\{ \vec{u} \in U \mid A\vec{u} = 0 \right\} \subset U
$$
2. Image
$$
\text{im}(A) := \left\{ A\vec{u} \in V \mid \vec{u} \in U \right\} \subset V
$$
3. Cokernel
$$
\text{ker}(A^*) := \{ \lambda \in V^* \mid A^* \lambda = 0 \} \subset V^*
$$
4. Coimage
$$
\text{im}(A^*) := \{ A^* \lambda \in U^* \mid \lambda \in V^* \} \subset U^*
$$

## Theorem (Fundamental Theorem of Linear Maps)
The four fundamental subspaces of a linear map $A : U \to V$ satisfy the following properties:
1. $\text{ker}(A)^\circ = \text{im}(A^*)$
	1. The coimage perfectly annihilates the kernel. 
2. $\text{ker}(A^*)^\circ = \text{im}(A)$
	1. The image perfectly annihilates the cokernel.
3. $\text{im}(A)^\circ = \text{ker}(A^*)$
	1. The cokernel annihilates the image.
4. $\text{im}(A^*)^\circ = \text{ker}(A)$
	1. The kernel annihilates the coimage.
Recall that $A^*$ is the [[Dual Space#Definition (Adjoint Linear Map)|adjoint linear map]] of $A$, where $A^{*} : V^{*}\to U^{*}$.  

Proof: Use the dual pairing.

Let $\lambda \in V^*$. We have $A^* \lambda \in \text{im}(A^*)$. Since $A^*$ is adjoint, then 
$$
\langle A^* \lambda | \vec{u} \rangle = \langle \lambda | A\vec{u} \rangle
$$
Let $u$ be some vector. As $Au = 0$, we have RHS is $0$ and thus LHS is $0$. In particular, it means $A^* \lambda \in \text{ker}(A)^\circ$ as it annihilates the kernel.

The proof is similar for the other three properties.

# Unconstrained Optimization
Let $M$ be a domain without boundary (e.g. $M = \R^n$). Let $E : M \to \R$ be a smooth function. The problem is that we want to minimize $E(x)$ for all $x \in M$. If $x_0$ is a minimizer, then 
$$
dE|_{x_0} \llbracket \mathring{x} \rrbracket = 0, \forall \mathring{x} \in T_{x_0} M
$$
Equivalently, $dE|_{x_{0}} = 0$. 

## Equality Constraints
Here, we discuss the "train tracks" and how they affect the optimality condition.

Let $M$ be an $n$-dimensional domain without boundary (e.g. M = $\R^n$). Let $S \subset M$ be a surface without boundary. Typically,
$$
S = \left\{ x \in M \mid g(x) = 0 \right\} 
\quad \text{for some} \quad g : M \to \R^m
$$
In that case, $S$ is $(n - m)$-dimensional. The problem is that we want to minimize $E(x)$ for all $x \in S$. For an unconstrained problem on $S$, the condition for an optimal $x_0 \in S$ is 
$$
dE|_{x_0} \llbracket \mathring{x} \rrbracket = 0, 
\quad
\forall \mathring{x} \in T_{x_0} S \subset T_{x_0} M
$$
Equivalently, $dE|_{x_0} \in (T_{x_0} S)^\circ$.

Now suppose $g : M \to Y$ where $Y$ is a [[Vector Space|vector space]], and $S$ is given by 
$$
S = g^{-1}\left(
  \{0_Y\} 
\right)
= \left\{ x \in M \mid g(x) = 0_Y \right\}
$$
What is $\left(T_{x_0} S\right)^\circ$ in terms of $g$? We observe that 
$$
T_{x_0} S = \text{ker}(dg|_{x_0})
$$
Therefore by [[#Theorem (Fundamental Theorem of Linear Maps)]], 
$$
\begin{aligned}
\left(T_{x_0} S\right)^\circ &= \left(\text{ker}(dg|_{x_0})\right)^\circ \\
&= \text{im}(dg|_{x_0}^*) \\ 
&= \left\{ dg|_{x_0}^* \llbracket \lambda \rrbracket \in T_{x_0} M^* \mid \lambda \in Y^* \right\}
\end{aligned}
$$
The optimality condition is that there exists $\lambda \in Y^*$ such that 
$$
dE|_{x_0} = dg|_{x_0}^* \llbracket \lambda \rrbracket
$$
In coordinate form,
$$
\frac{\partial E}{\partial x_i} \bigg|_{x_0} = \sum_{\alpha} \lambda_\alpha \frac{\partial g_\alpha}{\partial x_i} \bigg|_{x_0}
$$
The idea is that if we have found the minimizer point $x_0$ while trapped on a surface $S$, then no matter what direction we take on $S$ from $x_0$ (i.e. the tangent space $T_{x_0}S$), the energy function $E$ does not change (i.e. $dE|_{x_0} \llbracket \mathring{x} \rrbracket = 0$). However, this means that $dE|_{x_0}$ is actually in the annihilator subspace of the tangent space. Via the fundamental theorem of linear maps, we get that $dE$ is in the image of $dg^*$, such that there exists covector $\lambda \in Y^*$ such that $dE|_{x_0} = dg|_{x_0}^* \llbracket \lambda \rrbracket$. The resulting equation is the classic Lagrange multiplier form.

## Inequality Constraints
Here we discuss the "fences" and how they affect the optimality condition.

### Definition (Tangent Cone)
Let $M$ be a domain without boundary (e.g. $M = \R^n$). Let $S \subset M$ be a surface with boundary. Typically,
$$
S = \left\{ x \in M \mid h_i(x) \leq 0, \;  i = 1, \dots, \ell \right\}
$$
The problem is that we want to minimize $E(x)$ for all $x \in S$. 

For each $x \in S$, we define the **tangent cone** of $S$ at $x$ by
$$
C_x := \left\{ 
  \mathring{x} \in T_x M 
  \middle| 
  \mathring{x} \in \frac{d_{\gamma}(t)}{dt}\bigg|_{t=0} \text{ for some curve } \gamma : [0, 1] \to S
  \right\}
$$
A tangent cone may be a subspace, the entire tangent space $T_x M$, or some non-convex cone. If $x$ is the minimizer of $E$, then it means that there is no direction to go that decreases $E$. In particular, 
$$
dE|_{x_0} \llbracket \mathring{x} \rrbracket \geq 0
$$
or that 
$$
-dE|_{x_0} \llbracket \mathring{x} \rrbracket \leq 0
$$
which by definition of polar cone implies that
$$
-dE|_{x_0} \in C_{x_0}^\circ
$$
Physically, the covector $-dE$ points in the "downhill" direction. Since it lives inside the polar cone, then gravity is actively trying to push the ball *through* the fence, away from the valid yard. The fence stops the ball from falling further. 

### Translating to KKT via Pullbacks
We can map this back to our constraint functions $h_1, \dots, h_\ell$. Think of $\mathbf{h} = (h_1, \dots, h_\ell) : M \to \R^\ell$ as a map. Since the rule is that $\mathbf{h}(x) \leq 0$ for all $x \in S$, we have an "admissible set" in $\R^\ell$:
$$
A := \left\{ \mathbf{z} \in \R^\ell \mid z_1 \leq 0, \dots, z_{\ell} \leq 0 \right\}
$$
- The differential map $d\mathbf{h}_x$ pushes the complex tangent cone $C_{S,x}$ forward, flattening it into the simple, negative-quadrant cone $C_{A, h_x}$ in Euclidean space.
$$
(d\mathbf{h}_x)_* C_{S,x} = C_{A, h_x}
$$
- To find the polar cone on the manifold $M$, we find the polar cone on the negative quadrant in $\R^{\ell}$ and pullback via the adjoint map $(d\mathbf{h}_x)^*$.
$$
C_{S,x}^\circ = (d\mathbf{h}_x)^* C_{A, h_x}^\circ
$$

What is the polar cone of the negative quadrant? By definition, it is a strictly positive quadrant. Therefore, any covector living in polar cone $C_{A, h_x}^\circ$ must be a vector of positive numbers. Call this positive vector $\vec{\mu}$ where $\mu_j \geq 0$ for all $j$. Therefore 
$$
-dE = (d\mathbf{h}_x)^* \llbracket \vec{\mu} \rrbracket 
$$
where $\mu_j \geq 0$. So, when we write this in standard coordinate notation, the adjoint $(d\mathbf{h}_x)^*$ becomes the sum of the constraint gradients, yielding 
$$
-dE = \sum_{j=1}^\ell \mu_j dh_j
$$

# Example 1 
Consider the following diagram. 
```tikz
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.1]

% 1. Ground Rectangle
\fill[gray!50] (0,0) rectangle (11, -1.5);

% 2. Object body (Using hardcoded coordinates for a -30 deg rotation)
\draw[fill=purple!15, draw=black] (1.15, 3.0) -- (2.65, 5.6) -- (7.85, 2.6) -- (6.35, 0) -- cycle;

% 3. Internal frame axes
\draw (1.9, 4.3) -- (7.1, 1.3);
\draw (3.75, 1.5) -- (5.25, 4.1);

% 4. Origin point O
\fill (0,0) circle (1.5pt) node[above left] {$\mathbf{O}$};

% 5. Vectors (Guaranteed to render ON TOP of the purple block)
\draw[->, thick] (0,0) -- (4.5, 2.8) node[midway, above left] {$\mathbf{c}_{\text{world}}$};
\draw[->, thick] (4.5, 2.8) -- (6.35, 0) node[midway, below left] {$\mathbf{d}_{\text{body}}$};

% 6. Center and contact points (Rendered last to sit on top of arrow lines)
\fill (4.5, 2.8) circle (1.5pt); 
\fill (6.35, 0) circle (1.5pt);  

% 7. Labels and Equations
\node at (6.35, 0) [below=6pt] {$\mathbf{c}_{\text{world}} + \mathbf{d}_{\text{world}}$};
\node at (8.2, 2.8) [anchor=west] {$\mathbf{d}_{\text{world}} = \mathbf{R}^{\theta} \mathbf{d}_{\text{body}}$};

\end{tikzpicture}
\end{document}
```

Let the configuration space be all center of mass and rotation.
$$
M = \{ (\mathbf{c}_{\text{world}}, \theta) \in \R^2 \times \mathbb{S}^1 \}
$$
Here, $\mathbf{c}_{\text{world}} = [c_1, c_2]^{\top}$ is the position of the center of mass in the world frame, and $\theta$ is the rotation angle. We see that $\mathbf{R}^\theta$ is the rotation matrix and $\mathbf{d}_{\text{body}}$ is the vector from the center of mass to the corner in the body frame. The corner of the box is 
$$
\mathbf{x} = \mathbf{c}_{\text{world}} + \mathbf{R}^{\theta} \mathbf{d}_{\text{body}}
$$
There is an inequality constraint that the corner must be above the ground. When the corner is contact with the ground, what is the polar tangent cone in center of mass and rotation? 

So, 
$$
\begin{aligned}
\mathbf{x} &= \mathbf{c}_{\text{world}} + \mathbf{R}^{\theta} \mathbf{d}_{\text{body}} \\
\begin{bmatrix} x \\ y \end{bmatrix}_{(c, \theta)}
&= 
\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} 
+
\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
\begin{bmatrix} d_1 \\ d_2 \end{bmatrix} \\
\end{aligned}
$$
and so the height of the corner is represented by the following. Note that it must always be non-negative (in the air) and is equal to $0$ at the optimal solution (on the ground). 
$$
\begin{aligned}
y(\mathbf{c}, \theta) 
&= d_1 \sin\theta + d_2 \cos \theta + c_2 \\
% 
\begin{bmatrix} \frac{\partial y}{\partial c_1} & \frac{\partial y}{\partial c_2} & \frac{\partial y}{\partial \theta} \end{bmatrix}
&= \begin{bmatrix} 0 & 1 & d_1 \cos\theta - d_2 \sin\theta \end{bmatrix}
\end{aligned}
$$
Here we calculated the pushforward which is the Jacobian. The partial derivatives tell us exactly how much the corner moves up or down if we nudge the box horizontally, vertically, or rotatationally.

To find the geometric KKT conditions, we must pull that 1D force $\mu$ backward into our 3D configuration space. We do this by multiplying the transposed $(^*)$ Jacobian (the adjoint map!) by $\mu$. Therefore, the polar tangent cone 
- in the height space is $\{\mu \leq \theta\}$. 
- in $(\mathbf{c}, \theta)$ space is 
$$
\left\{
  \begin{bmatrix} 0 \\ 1 \\ d_1 \cos\theta - d_2 \sin\theta \end{bmatrix} \mu \middle| \mu \leq 0
\right\}
$$

This gives the set of vectors 
$$
\left\{
  \begin{bmatrix} 0 \\ \mu \\ (d_1 \cos\theta - d_2 \sin\theta) \mu \end{bmatrix} \middle| \mu \leq 0
\right\}
$$
where the horizontal force is $0$. This represents the fact that the ground does not push the box horizontally (i.e. no friction causing it to slide left or right). The vertical force (in the $c_2$ axis) is exactly the normal force $\mu$ from the ground, which is pushing up. It is the equal and exact opposite of the downward gravity force $-dE$. The rotational force is on $\theta$ axis; it is precisely the torque from the ground pushing up on the corner of angle $\theta$ from the ground. 

> Recall that torque is the cross product of force and distance. The force is $\mu$. The horizontal distance from the center of the mass to the corner is precisely $d_1 \cos\theta - d_2 \sin\theta$. 