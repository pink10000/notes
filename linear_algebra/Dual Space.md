---
tags:
  - CSE_291G
---
# Definition (Linear Map)
Let $U,V$ be two [[Vector Space|vector spaces]]. A map $A: U \to V$ is **linear** if 
$$
A(\vec{u}_{1} + \vec{u}_{2}) = A(\vec{u}_{1}) + A(\vec{u}_{2})
\quad \text{and} \quad
A(c\vec{u}) = c A(\vec{u})
$$

## Theorem (Set of Linear Maps is a Vector Space)
The set $\left(U \xrightarrow{\text{linear}} V\right)$ of all linear maps from $U$ to $V$ is a vector space.

# Definition (Covector)
A **covector** on a [[Vector Space|vector space]] $V$ is a scalar-valued linear function 
$$
\alpha : V \xrightarrow{\text{linear}} \mathbb{R}
$$
A covector is a linear function that takes in a vector and outputs a scalar. Geometrically, it is best to visualize a covector as a set of equidistant, parallel hyperplanes. In 2D, these are parallel lines. In 3D, they are parallel planes. They are like "slabs". It is best to visualize them by its [[Level Set|level sets]]. 

# Definition (Dual Space)
The **dual space**
$$
V^* = \left\{ \alpha : V \xrightarrow{\text{linear}} \mathbb{R} \right\}
$$
of a [[Vector Space|vector space]] $V$ is the vector space of all covectors on $V$. The elements of $V^*$ are called **dual vectors** or [[#Definition (Covector)|covectors]]. The **dual pairing** is denoted by 
$$
\alpha(\vec{u}) = \langle \alpha | \vec{u} \rangle = \alpha \llbracket \vec{u} \rrbracket
$$
It is the act of "feeding" a vector $\vec{u}$ into a covector $\alpha$ to get a scalar value. Visually, evaluating the dual pairing means counting the number of times the vector's arrow pierces through the hyperplanes of the covector. If the arrow runs perfectly parallel to the covector's lines, it pierces $0$, and the pairing is $0$. If the arrow stretches across $3$ level-set lines, the pairing evaluates to $3$. 

## Theorem (Dimension of Dual Space)
The dimension of the dual space $V^*$ is equal to the dimension of the original vector space $V$. That is,
$$
\dim V^* = \dim V
$$
If $V$ is a finite-dimensional vector space, then $\dim V^{**} = \dim V$. 

# Theorem (Dual Basis)
Let $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n$ be a [[Vector Space#Theorem (Basis)|basis]] for a finite-dimensional vector space $V$. Then there is a unique **dual basis** $\beta^1, \beta^2, \ldots, \beta^n \in V^*$ so that 
$$
\langle \vec{e}_i | \beta^j \rangle 
= \delta_i^j
= \begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \neq j
\end{cases}
$$
where $\delta_i^j$ is the **Kronecker delta**. If we write 
$$
\vec{u} = \sum_{i=1}^{n} u^i \vec{e}_i
$$
using a basis, then we would write a covector $\alpha$ as
$$
\alpha = \sum_{j=1}^{n} \alpha_j \beta^j
$$
The dual pairing simply becomes 
$$
\langle \alpha | \vec{u} \rangle = \sum_{i=1}^{n} \alpha_i u^i
$$
Likewise to the visualization of the dual pairing, given some basis vector $\vec{e}_{1}\in V$, the corresponding $\beta^{1}$ dual vector means that the pairing evaluates to $1$, or that it crosses the covector slab exactly once. 

# Conventional Notation 
Vectors are conventionally columnar. Covectors are row vectors. The dual pairing is automatic
$$
\begin{bmatrix}
\alpha_1 & \cdots & \alpha_n 
\end{bmatrix}
% 
\begin{bmatrix}
u^1 \\ \vdots \\ u^n
\end{bmatrix}
= \sum_{i=1}^{n} \alpha_i u^i
$$
Vectors are labeled with an upper index $u^i$ and covectors are labeled with a lower index $\alpha_j$. We can also use the bra-ket notation, where the vector $\vec{u}$ is written as a "ket" $|\vec{u}\rangle$ and the covector $\alpha$ is written as a "bra" $\langle \alpha|$. The dual pairing is then written as $\langle \alpha | \vec{u} \rangle$. There is also Penrose graphical notation. 

# Definition (Adjoint Linear Map)
For each [[#Definition (Linear Map)|linear map]] $A: U \to V$, there is a linear map called its **adjoint** $A^{\top}: V^* \to U^*$ defined by 
$$
\langle A^{\top} \beta | \vec{u} \rangle = \langle \beta | A\vec{u} \rangle
$$ 
for all $\vec{u} \in U$ and $\beta \in V^*$. The adjoint map is also denoted as $A^*$. 


# Definition (Tangent Space)
The **tangent space** $T_p M$ at $p$ is the vector space of perturbations for point $p$. 
$$
T_p M = \left\{ (p, v) \right\}
$$
This is a family of vector spaces. In type theory, tangent spaces form a [[Dependent Type|dependent type]]. This is because it depends on the point $p$. 

# Definition (Tangent Bundle)
The **tangent bundle** is the space of all perturbation data
$$
TM = \bigsqcup_{p \in M} T_p M
$$
In type theory, the tangent bundle is a [[Dependent Type|sum dependent type]]. It helps because we can say that 
$$
x \in TM \iff \exists p \in M \text{ such that } T_p M \ni x
$$

# Definition (Cotangent Space)
The **cotangent space** $T_p^* M$ at $p$ is the [[Dual Space|dual space]] of [[#Definition (Tangent Space)|tangent space]]. 

# Definition (Cotangent Bundle)
The **cotangent bundle** is the space of all covectors
$$
T^* M = \bigsqcup_{p \in M} T_p^* M
$$

# Definition (Vector Field, Covector Field)
A **vector field** is a function of the following type
$$
\begin{aligned}
X : M &\to TM \\
X(p) &\in T_p M
\end{aligned}
$$
We also call a vector field a *section of the tangent bundle*. 
$$
X \in \Gamma(TM) = \{ X : M \to TM \mid X_p \in T_p M \}
$$
In type theory, this is a [[Dependent Type|product dependent type]]. This is because the output type $T_p M$ depends on the input $p$.

Similarly, a **covector field** $\alpha \in \Gamma(T^* M)$ is a function if type
$$
\begin{aligned}
\alpha : M &\to T^* M \\
\alpha(p) &\in T_p^* M
\end{aligned}
$$
We also call a covector field a *1-form*, and denote $\Gamma(T^* M) = \Omega^1 (M)$. 

# Types in Differential Calculus
Let
$$
f \in \left(M \xrightarrow{\text{nonlinear}} \R \right)
$$
The **differential** of a function $f$ at a point $p$ is a linear map that approximates the change in $f$ near $p$. It is a [[#Definition (Covector)|covector]] field
$$
df \in \Gamma(T^* M) = \Omega^1 (M)
$$
where at any specific point $p$, we have $df|_p \in \left(T_p M \xrightarrow{\text{linear}} \R\right) = T_p^* M$. 

# Definition (Directional Derivative)
The perturbation at a point is a tangent vector 
$$
v_p \in T_p M
$$
The **directional derivative** of $f$ at $p$ in the direction of $v_p$ is the dual pairing:
$$
df|p \llbracket v_p \rrbracket \in \R
$$
Geometrically, let $\gamma : (- \vepsi, \vepsi) \to M$ be any curve satisfying $\gamma(0) = p$ and $\gamma'(0) = v$. Then we can compute the directional derivative as the rate of change of $f$ along the curve:
$$
df_p \llbracket v \rrbracket = \frac{d}{dt} f(\gamma(t)) \bigg|_{t=0}
$$
This function $df$ depends *linearly* in $v$, but generally *nonlinearly* in $p$. Each data $(p, v)$ admits a representing curve $\gamma$ that passes through $p$ with velocity $v$ at $t = 0$.

What about with with partial derivatives?

# Definition (Coordinate System)
A **coordinate system** is a family of functions 
$$
x^1, \ldots, x^n \in \left(M \xrightarrow{\text{nonlinear}} \R\right)
$$
so that $dx^1 |_p, \ldots, dx^n |_p \in T_p^* M$ is a [[Vector Space#Theorem (Basis)|basis]] at evert $p \in M$. 

The partial derivatives defined are the coefficients for the [[Dual Space#Definition (Covector)|covector]] $df$ under this coordinate-induced covector basis:
$$
df = \sum_{i=1}^{n} \frac{\partial f}{\partial x^i} dx^i
$$

# Definition (Riemannian Manifold)
Let $M$ be a [[Manifold]] (domain). A **Riemannian manifold** is a manifold $M$ together with an [[Square Matrices#Definition (Inner Product Structure or Metric)|inner product structure]] $\flat_p : T_p M \to T_p^* M$ at every point $p \in M$. 

In general, given a Riemannian manifold, we don't expect to find a coordinate system so that the coordinate vectors are orthonormal everywhere. The failure to find an everywhere-orthonormal coordinate is the non-Euclidean-ness of the Riemannian manifold.

# Definition (Gradient Vector)
Let $(M, \flat)$ be a [[#Definition (Riemannian Manifold)|Riemannian manifold]]. The **gradient** of a function $f \in C^\infty(M)$ at $p \in M$ is defined by 
$$
\text{grad}_p f := \sharp_p d_p f \in T_p M
$$
The gradient does not require coordinates and has little to do with partial derivatives. In index notation, it is 
$$
(\text{grad} f)^i = \sharp^{ij} \frac{\partial f}{\partial x^j}
$$
The correct way of writing gradient descent is 
$$
\frac{d}{dt} x^i = - \sharp^{ij} \frac{\partial f}{\partial x^j}
$$

# Chain Rules
The differential of a function $f: M \to \R$ at a point $p$ is a linear map $df|_p: T_pM \to \R$. This concept generalizes to a map between manifolds $\phi : M \to N$.

## Definition (Pushforward Operator)
The **pushforward operator** $\phi_*$ (also called the *differential* or *Jacobian*) of a map $\phi : M \to N$ is a map between tangent bundles:
$$
\begin{aligned}
\phi_* : TM &\to TN \\
\phi_*(u_p) &:= d\phi|_p u_p
\end{aligned}
$$
Geometrically, it "pushes" a velocity vector $u_p$ at $p \in M$ to a velocity vector at $\phi(p) \in N$. In coordinates, this is matrix-vector multiplication by the Jacobian.

## Definition (Pullback Operator for Functions)
The **pullback operator** $\phi^*$ for functions takes a function on the target space and "pulls" it back to the source space:
$$
\begin{aligned}
\phi^* : (N \to \R) &\xrightarrow{\text{linear}} (M \to \R) \\
\phi^*(g) &:= g \circ \phi
\end{aligned}
$$
If $g$ is a scalar field on $N$, then $\phi^*g$ is a scalar field on $M$.

## Definition (Pullback Operator for Covectors)
The **pullback operator** $\phi^*$ for covectors is the [[#Definition (Adjoint Linear Map)|adjoint]] of the pushforward. It pulls covectors (1-forms) on $N$ back to $M$:
$$
\begin{aligned}
\phi^* : T^*N &\to T^*M \\
\phi^*(\beta_{\phi(p)}) &= (d\phi|_p)^{\top}(\beta_{\phi(p)})
\end{aligned}
$$
The defining property is the dual pairing: $\langle \phi^* \beta | u \rangle = \langle \beta | \phi_* u \rangle$.

# Backpropagation and Machine Learning
In machine learning, we often have a composition of maps (layers) $\phi_1, \phi_2, \ldots, \phi_k$ and a final scalar loss function $L: \R^n \to \R$.

### Forward Pass (Pushforward)
The forward pass is the computation of the maps themselves: $x \mapsto y_1 \mapsto y_2 \mapsto \ldots \mapsto \text{Loss}$. The *sensitivity* of the output to a perturbation $\delta x$ is computed by the pushforward:
$$
\delta \text{Loss} = L_* (\phi_k)_* \ldots (\phi_1)_* \delta x
$$
This is the "forward-mode" differentiation.

### Backward Pass (Pullback)
Backpropagation is the **pullback of the loss differential**. We start with the differential of the loss function $dL$, which is a covector (a row vector of partial derivatives). We want to find how the loss changes with respect to the input $x$.

Using the property $(\psi \circ \phi)^* = \phi^* \circ \psi^*$, we pull the covector $dL$ back through the layers:
$$
dx = \phi_1^* \phi_2^* \ldots \phi_k^* dL
$$
Notice the order is reversed. In each step, we apply the adjoint of the local Jacobian (the transpose of the weight matrix in linear layers) to the "incoming" gradient covector. 

**Why use pullbacks?** 
If the input $x$ is high-dimensional (e.g., an image) and the output is a single scalar (the loss), it is computationally much cheaper to pull back a single covector than to push forward a basis of the entire tangent space. This is why "reverse-mode" autodiff (backprop) is the standard for deep learning.

## CNN Example
In a CNN, the trainable parameters consist of the weights within the convolutional kernels (filters) and their associated biases. Let the manifold $M$ represent the space of all possible parameter values. Each point $p \in M$ is a specific setting of the parameters at some training step. The [[#Definition (Tangent Space)|tangent space]] $T_p M$ represents all possible perturbations to the parameters at that point. When an optimizer like SGD updates the parameters, it is essentially moving in the tangent space $T_p M$ to a new point $p'$ by some update rule. 

CNN's operate on feature maps (multi-dimensional arrays, tensors). Let a single convolutional layer be a map $\phi$ from an input tensor space to an output tensor space. 
$$
\phi : \R^{H \times W \times C_{\text{in}}} \to \R^{H' \times W' \times C_{\text{out}}}
$$
where $H,W$ is the height and width of the input feature map, and $C_{\text{in}}, C_{\text{out}}$ are the number of input and output channels, respectively. The input tensor $x$ is a vector in this domain. The [[#Forward Pass (Pushforward)|pushforward]] (or differential) denoted by $\phi_*$ or $d\phi$, represents the Jacobian of the convolutional operation. Geometrically, if we perturb the input tensor $x$ by a small amount $\delta x$, the pushforward tells us how the output tensor changes: 
$$
\delta y = \phi_* \delta x
$$
Because convolution is a linear operation, the pushforward is simply the convolution itself.

The network concludes with a scalar loss function
$$
L : \R^{H' \times W' \times C_{\text{out}}} \to \R
$$
The differential of the loss function $dL$ is a [[#Definition (Covector)|covector]], belonging to the [[#Definition (Cotangent Space)|cotangent space]] $T^*_{\phi(x)} \R^{H' \times W' \times C_{\text{out}}}$. It is a linear functional waiting to be fed a perturbation vector to tell us how the loss changes. To compute the gradient with respect to the input $x$, we do not invert the matrix. Instead, we use the [[#Definition (Pullback Operator for Covectors)|pullback]] of the convolutional layer, $\phi^*$. The pullback is the adjoint of the pushforward
$$
\phi^* \beta = (d \phi)^{\top} \beta
$$
In the specific context of a CNN, the adjoint of a convolution operation is mathematically equivalent to a transposed convolution (also known as a deconvolution). This is why the backpropagation step in a CNN involves a transposed convolution. During backpropagation, the loss covector $\beta$ is pulled back through the layers by applying a transposed convolution using the same kernel weights. This mathematically mirrors the equation 
$$
dx = \phi^* dL
$$
Eventually, this yields the gradient of the loss with respect to the input $x$, the covector 
$$
dL_p \in T^*_p M
$$
Since we cannot directly add a covector to a vector (manifold), we need a tangent vector. This requires the Riemannian metric $\sharp_p : T_p M \to T_p^* M$ to convert the covector $dL_p$ into a tangent vector
$$
\text{grad}_p L = \sharp_p dL_p \in T_p M
$$
This vector $\text{grad}_p L$ represents the direction of steepest ascent in the tangent space. 

> The following is unrelated to the class, but this section was further elaborated via Gemini 3.1 pro. 

To get back to the original parameter space, we need to apply the "exponential map" $\exp_p : T_p M \to M$ to move from the tangent space back to the manifold. The idea is to "start at $p$, face in the direction of the gradient, and walk the straightest possible path (geodesic)". To update our weights, we scale our gradient vector by a learning rate $\eta$ and then apply the exponential map:
$$
p_{t+1} = \exp_{p_t}(-\eta \text{grad}_{p_t} L)
$$
and so on. In practice, this notation is never used because we always assume the parameter manifold $M$ is a perfectly flat Euclidean space $\R^n$. It's geometry is trivial, so the "straightest possible path" is just a straight line.

# Theorem (Derivative and Pullback Commute)
Let $\phi : M \to N$ be a map between manifolds, and let $f : N \to \R$ be a function on the target manifold. Then the following holds:
$$
\phi^*(df) = d(\phi^* f)
$$

# Theorem (Pushforward Distributes over Composition)
Let $\phi : M \to N$ and $\psi : N \to P$ be maps between manifolds. Then the pushforward distributes over composition:
$$
(\phi_1 \circ \cdots \circ \phi_k)_* = (\phi_1)_* \cdots (\phi_k)_*
$$
This is the same as the chain rule for derivatives. 

# Theorem (Pullback Distributes over Composition and Reverses Order)
Let $\phi : M \to N$ and $\psi : N \to P$ be maps between manifolds. Then the pullback distributes over composition and reverses order:
$$
(\phi_1 \circ \cdots \circ \phi_k)^* = (\phi_k)^* \cdots (\phi_1)^*
$$
Because the pullback is the adjoint (transpose) of the pushforward, distributing it across a composition reverses the order of operations. This is why backpropagation goes in the reverse order of the forward pass.