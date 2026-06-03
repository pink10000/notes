---
tags:
  - CSE_291G
---
# Remark (Motivation via Integration)
Differential $k$-forms are fundamentally objects designed to be integrated over $k$-dimensional [[Orientable Surfaces|oriented surfaces]]. The standard integrals from multivariable calculus are actually integrations of differential forms:
1. **Line Integrals (1-forms):**
   Integrating a vector field $\mathbf{v}$ along a curve $\Gamma$ gives:
   $$
   \int_\Gamma \mathbf{v} \cdot d\mathbf{l} = \int_\Gamma \underbrace{v_1 dx + v_2 dy + v_3 dz}_{\text{differential 1-form}}
   $$
   The integrand is a differential 1-form, which corresponds to a [[Dual Space#Definition (Covector)|covector]] field.
2. **Flux Integrals (2-forms):**
   Integrating a vector field $\mathbf{w}$ across a surface $S$ gives:
   $$
   \int_S \mathbf{w} \cdot \mathbf{n} dA = \int_S \underbrace{w_1 dy dz + w_2 dz dx + w_3 dx dy}_{\text{differential 2-form}}
   $$
   The area element here is skew-symmetric (i.e., $dx dy = -dy dx$), which motivates the definition of 2-forms as skew-symmetric tensors in $T^*M \wedge T^*M$.
3. **Volume Integrals (3-forms):**
   Integrating a scalar function $f$ over a volume $V$ gives:
   $$
   \int_V f \, dx dy dz
   $$
   where $dx dy dz = -dy dx dz$.

This integration-based intuition naturally leads to the formal definition of differential forms as skew-symmetric tensors on a manifold.

# Definition (Differential Form)
Let $M$ be a [[Manifold]] and $V = T_p M$ be its [[Dual Space#Definition (Tangent Space)|tangent space]] at a point $p$. A **differential $k$-form** is a skew-symmetric tensor product of [[Dual Space#Definition (Covector)|covectors]]. 

Mathematically, it resides in the exterior power of the dual space (a subspace of the [[Tensor Algebra#Definition (Tensor Product Space)|tensor product space]]):
$$
\omega \in 
\underbrace{V^* \wedge \cdots \wedge V^*}_{k} 
= \bigwedge^k V^* 
\subset \bigotimes^k V^*
$$
If the basis for the dual space $V^*$ consists of the differentials of coordinate functions $dx^1, \dots, dx^n$, then the standard basis for $\bigwedge^k V^*$ is given by the wedge products:
$$
dx^I = dx^{i_1} \wedge \dots \wedge dx^{i_k}
$$
where $i_1 < \dots < i_k$. And $I = (i_{1}, \dots, i_{k})$.

*(For the algebraic properties of differential forms, including their dimensions, wedge products, pairings, and interior products, see [[Exterior Algebra]])*.

# Definition (Integration of k-form Field)
Let $\omega \in \Gamma(\bigwedge^k T^*M) = \Omega^k(M)$ be a $k$-form field, and let $S$ be a $k$-dimensional surface. The integral of $\omega$ over $S$ is defined via a [[Riemann-Stieltjes Integral|Riemann sum]] of the pairing over infinitesimal elements:
$$
\int_S \omega = \lim_{\text{partition refines}} \sum_{\text{all elements}} \omega|_p \llbracket v_1, \dots, v_k \rrbracket
$$
where $v_1, \dots, v_k$ span the tangent elements of the partition at point $p$.

> [!NOTE] Unpacking the Notation
> - $T^*M$ is the [[Dual Space#Definition (Cotangent Bundle)|cotangent bundle]] (the collection of all covector spaces at every point on the [[Manifold]]).
> - $\bigwedge^k T^*M$ is the bundle containing all possible $k$-forms at every point.
> - $\Gamma(\dots)$ denotes the space of "sections" of a bundle. Taking a section means smoothly (continuously) assigning one specific $k$-form to each point on the manifold.
> - $\Omega^k(M)$ is simply the standard shorthand notation for this space of sections. Therefore, $\omega \in \Omega^k(M)$ is the rigorous way to state that $\omega$ is a continuous **$k$-form field**.

> [!idea] Intuition
> Imagine that $k$ is actually $3$, so that we are in a 3D world. In particular, consider the Earth's surface, and that $M$, our [[Manifold]], is a zoomed in part of the surface that looks flat (looks like a [[Euclidean Space]] at each point, in 2D). We want to integrate a 2-form over a patch of grass or water, say $S$.
>
> At any point in the $p$ in the manifold, there is a tangent space $T_p M$. A vector field (a section of $TM$) assigns a physical direction and magnitude to each every point (like wind direction). We get two vectors $v_1, v_2$ which span the tangent elements of the partition at $p$.
> 
> If these two vectors span the grid on $S$, what is the $k-$form field $\omega \in \Omega^3(M)$? We can think of the $k-$form field $\omega$ as a continous field of wind sensors across the surface. At every point $p$, there is a specific 2-form $\omega|_p$, designed to do exactly one thing: it takes (or "eats") the two vectors $v_1, v_2$ and produces a scalar, the exact flux of the wind through the patch of grass at that point. 
>
> All together:
> $$
> \int_{S} \omega = \lim_{\text{partition refines}} \sum_{\text{all elements}} \underbrace{\omega|_p \llbracket v_1, v_2 \rrbracket}_{\text{flux at point } p}
> $$
> In words, we are taking the region $S$ and chopping it into an infinitesimal mesh. At each point $p$ in the mesh, there are two tangent vectors $v_1, v_2$ that span the local grid. Then we activate the sensor field $\omega$ at that point, giving us a scalar reading $\omega|_p \llbracket v_1, v_2 \rrbracket$. Finally, we sum up all these readings and take the limit as the mesh gets finer and finer, giving us the total flux of the wind through the entire patch $S$.
> 
> More generally, we can abstract integral over surfaces up to further dimensions and other types of $k$-forms. 

## Remark (Integration in 3D)
Following our 3D examples, this integration precisely reconstructs the classical vector integrals:
$$
\begin{aligned}
f(p) &= \int_p f_{0-\text{form}} \\
\int_\Gamma \mathbf{u} \cdot d\mathbf{l} &= \int_\Gamma \mathbf{u}_{1-\text{form}} \\
\int_S \mathbf{w} \cdot \mathbf{n} dA &= \int_S \mathbf{w}_{2-\text{form}} \\
\int_V f \, dV &= \int_V f_{3-\text{form}}
\end{aligned}
$$

# Definition (Change of Coordinates and Pullback)
Let $S$ be a $k$-dimensional surface parameterized by a domain $D$ as $S = \phi(D)$.
Changing coordinates yields:
$$
\int_S \omega = \int \dots \int_D \omega_{\phi(\mathbf{x})} \llbracket \phi_* e_1, \dots, \phi_* e_k \rrbracket dx_1 \dots dx_k
$$
This structure mirrors the [[Dual Space#Definition (Pullback Operator for Functions)|pullback]] operation from $M \to N$!

## Definition (Pullback)
Given a linear map $A: U \to V$, the **pullback** for $k$-forms acts like an [[Dual Space#Definition (Adjoint Linear Map)|adjoint]], pulling forms back from $V$ to $U$:
$$
A^* : \bigwedge^k V^* \xrightarrow{\text{linear}} \bigwedge^k U^*
$$
Defined by:
$$
(A^* \omega)\llbracket X_1, \dots, X_k \rrbracket := \omega \llbracket A X_1, \dots, A X_k \rrbracket
$$

For a nonlinear map $\phi: M \to N$, we have a canonical pullback for $k$-form fields (acting conceptually like back-propagation):
$$
\phi^* : \Omega^k(N) \xrightarrow{\text{linear}} \Omega^k(M)
$$
Defined point-wise as:
$$
(\phi^* \omega)_p \llbracket X_1, \dots, X_k \rrbracket := \omega_{\phi(p)} \llbracket \phi_* X_1, \dots, \phi_* X_k \rrbracket
$$
where $\phi_*$ is the [[Dual Space#Forward Pass (Pushforward)|pushforward]] (differential) of $\phi$.

## Theorem (Change of Coordinates using Pullback)
Using the pullback, the change of coordinates formula simplifies beautifully to:
$$
\int_{\phi(D)} \omega = \int_D \phi^* \omega
$$

## Example (Pullback in 3D Coordinates)
If we define the Jacobian matrix of the transformation $\phi$ as $\mathbf{F} := d\phi$ and let $J := \det \mathbf{F}$, the pullback operator maps our 3D vector forms:
$$
\begin{aligned}
\phi^* f_{0-\text{form}} &= f \circ \phi \\
\phi^*(\bv_{1-\text{form}}) &= (\mathbf{F}^T(\mathbf{v} \circ \phi))_{1-\text{form}} \\
\phi^*(\bw_{2-\text{form}}) &= \big(J\mathbf{F}^{-1}(\mathbf{w} \circ \phi)\big)_{2-\text{form}} \\
\phi^*(f_{3-\text{form}}) &= \big(J(f \circ \phi)\big)_{3-\text{form}}
\end{aligned}
$$
## Lemma (Homomorphism of Pullback)
The pullback is a homomorphism on the entire [[Exterior Algebra]]. It distributes over the wedge product:
$$
\phi^*(\alpha \wedge \beta) = (\phi^* \alpha) \wedge (\phi^* \beta)
$$
It also interacts cleanly with the interior product (acting as insertion):
$$
i_X(\phi^* \omega) = \phi^*(i_{\phi_* X} \omega)
$$

# Definition (Exterior Derivative)
The **exterior derivative** $d$ is an operator that generalizes the concept of taking a [[Dual Space#Remark (Types in Differential Calculus)|differential]], mapping $k$-form fields to $(k+1)$-form fields:
$$
d: \Omega^k(M) \to \Omega^{k+1}(M)
$$
The exterior derivative is defined by three rules:
1. For a scalar function $f \in \Omega^0(M)$, $df \in \Omega^1(M)$ is the standard differential of the function.
2. **Nilpotent:** $d(d\omega) = 0$ (often stated simply as $d^2 = 0$).
3. **Exterior Leibniz rule:**
$$
d(\alpha \wedge \beta) = (d\alpha) \wedge \beta + (-1)^{\text{deg}(\alpha)} \alpha \wedge (d\beta)
$$

## Example (Exterior Derivative in 3D Space)
1. $df_{0-\text{form}} = (\nabla f)_{1-\text{form}}$ (Gradient)
2. $d\bv_{1-\text{form}} = (\nabla \times \bv)_{2-\text{form}}$ (Curl)
3. $d\bw_{2-\text{form}} = (\nabla \cdot \bw)_{3-\text{form}}$ (Divergence)

## Lemma (Pullback and Exterior Derivative Commute)
The [[#Definition (Pullback)|pullback operator]] and the [[#Definition (Exterior Derivative)|exterior derivative]] commute:
$$
\phi^*(d\omega) = d(\phi^* \omega)
$$
> [!note] 
> This commutativity is a *profound* result that is often proven directly using the generalized Stokes' theorem. When translated into 3D coordinates using the mappings above, this single algebraic identity generates a host of non-obvious vector calculus identities!)

# Theorem (Generalized Stokes' Theorem)
The generalized [[Stokes Theorem]] connects integration of differential forms to the exterior derivative:
$$
\int_S d\omega = \oint_{\partial S} \omega
$$
In 3D, this single, elegant theorem perfectly unifies three classical theorems of vector calculus into one single mathematical identity:
1. **[[Fundamental Theorem of Calculus]] (0-forms):** $\int_a^b \nabla f \cdot d\mathbf{l} = f(b) - f(a)$
2. **Kelvin-Stokes Curl Theorem (1-forms):** $\iint_S (\nabla \times \mathbf{u}) \cdot \mathbf{n} dA = \oint_{\partial S} \mathbf{u} \cdot d\mathbf{l}$
3. **Gauss [[Divergence Theorem]] (2-forms):** $\iiint_V (\nabla \cdot \mathbf{w}) dV = \iint_{\partial V} \mathbf{w} \cdot \mathbf{n} dA$
