---
tags:
  - CSE_291G
---
# Exterior Algebra
The **exterior algebra** (or Grassmann algebra) $\bigwedge V^*$ is the algebraic structure formed by equipping the [[Vector Space|vector space]] of skew-symmetric tensors with the wedge product. It is a sibling space to the full [[Tensor Algebra]].

## Corollary (Dimension of Exterior Powers)
If $n$ is the dimension of the underlying vector space $V$ (i.e., the size of its basis set, $n = \dim(V)$), then the dimension of the $k$-th exterior power is:
$$
\dim\left(\bigwedge^k V^*\right) = \binom{n}{k} = \frac{n!}{(n-k)!k!}
$$

## Example (Exterior Powers in 3D Space)
In standard 3D space ($n=3$) with coordinates $(x, y, z)$, the dimension formula $\binom{3}{k}$ dictates the size of the basis for each exterior power. There are exactly four meaningful spaces:
1. **0-forms ($k=0$):**
   Dimension $\binom{3}{0} = 1$. A 0-form is simply a scalar.
   $$
   f \in \bigwedge^{0} V^{*} = \R
   $$
2. **1-forms ($k=1$):**
   Dimension $\binom{3}{1} = 3$. The basis is $\{dx, dy, dz\}$. A 1-form is a [[Dual Space#Definition (Covector)|covector]].
   $$
   \bigwedge^1 V^{*}
   = \{ \underbrace{u_{1} dx + u_{2}dy + u_{3}dz}_{\bu_{1-\text{form}}} \mid \bu \in \R^{3} \}
   $$
3. **2-forms ($k=2$):**
   Dimension $\binom{3}{2} = 3$. The basis consists of pairs of wedge products $\{dy \wedge dz, dz \wedge dx, dx \wedge dy\}$.
   $$
   \bigwedge^{2} V^{*} = \{\underbrace{w_1 dy \wedge dz + w_2 dz \wedge dx + w_3 dx \wedge dy }_{\bw_{2-\text{form}}} \mid \bw \in \R^{3}\}
   $$
4. **3-forms ($k=3$):**
   Dimension $\binom{3}{3} = 1$. The basis is a single volume element $\{dx \wedge dy \wedge dz\}$.
   $$
   \bigwedge^{3} V^{*} = \{\underbrace{f\, dx \wedge dy \wedge dz}_{f_{3-\text{form}}}\mid f \in \R\}
   $$

*(Note: Any exterior power where $k > 3$ is strictly $0$ in 3D space, because you would inevitably repeat a basis element, and by skew-symmetry $dx \wedge dx = 0$.)*

# Definition (Wedge Product / Exterior Product)
The **wedge product** extends the linear combination operator on differential forms, making the space of all differential forms into an **exterior algebra**.
$$
\wedge : \bigwedge^k V^* \times \bigwedge^\ell V^* \xrightarrow{\text{bilinear}} \bigwedge^{k+\ell} V^*
$$
This is kind of like a natural multiplication on [[Differential Forms]]. The wedge product is defined axiomatically by two rules:
1. **Associativity:** $(\alpha \wedge \beta) \wedge \gamma = \alpha \wedge (\beta \wedge \gamma)$
2. **Skew on 1-forms:** If $\alpha \in \bigwedge^1 V^*$, then $\alpha \wedge \alpha = 0$

Consequently, for any $k$-form $\alpha$ and $\ell$-form $\beta$:
$$
\alpha \wedge \beta = (-1)^{k\ell} \beta \wedge \alpha
$$

## Example (Wedge Product in 3D Space)
1. $\bu_{1-\text{form}} \wedge \bv_{1-\text{form}} = (\bu \times \bv)_{2-\text{form}}$
2. $\bu_{1-\text{form}} \wedge \bw_{2-\text{form}} = (\bu \cdot \bw)_{3-\text{form}}$

# Definition (Pairing with Vectors)
Just like a single covector pairs with a vector to produce a scalar, a $k$-form can be paired with $k$ vectors. We denote this pairing as:
$$
\omega \llbracket X_1, \dots, X_k \rrbracket
$$
and it will satisfy skew symmetry:
$$
\omega \llbracket X_1, \dots, X_i, \dots, X_j, \dots, X_k \rrbracket = -\omega \llbracket X_1, \dots, X_j, \dots, X_i, \dots, X_k \rrbracket
$$

## Theorem (Determinant Formula for Pairing)
If we have a decomposable $k$-form $\alpha^1 \wedge \dots \wedge \alpha^k$ (where each $\alpha^i$ is a covector), its pairing with $k$ vectors $X_1, \dots, X_k$ is computed via the determinant of their individual [[Dual Space#Dual pairing|dual pairings]]:
$$
(\alpha^1 \wedge \dots \wedge \alpha^k)\llbracket X_1, \dots, X_k \rrbracket = \det \begin{bmatrix} \langle \alpha^1 | X_1 \rangle & \dots & \langle \alpha^1 | X_k \rangle \\ \vdots & \ddots & \vdots \\ \langle \alpha^k | X_1 \rangle & \dots & \langle \alpha^k | X_k \rangle \end{bmatrix}
$$
This evaluation is skew-symmetric in both the vector arguments and the covector arguments.

## Remark (Determinant as a Skew-Symmetry Engine)
The determinant formula mathematically guarantees this skew-symmetry because of how the inputs are arranged in the matrix:
- **Columns (Vectors):** All pairings with $X_1$ are in the first column, $X_2$ in the second column, and so on. Swapping two input vectors physically swaps two columns in the matrix.
- **Rows (Covectors):** All pairings with $\alpha^1$ are in the first row, $\alpha^2$ in the second row, and so on. Swapping two covectors in the wedge product physically swaps two rows.

Because a fundamental axiom of the determinant is that swapping any two rows or columns multiplies the result by $-1$, the pairing inherently satisfies the skew-symmetry requirement for both its vector and covector arguments.

## Example (Pairings in 3D Space)
In 3D Euclidean space, the determinant pairing formula reproduces standard operations from vector calculus. If we represent 1-forms as vectors $\mathbf{u}$, 2-forms as vectors $\mathbf{w}$, and 3-forms as scalars $f$, their pairings with standard vectors ($\mathbf{u}_{\text{vec}}, \mathbf{v}_{\text{vec}}, \mathbf{w}_{\text{vec}}$) are exactly:
1. **1-form Pairing (Dot Product):**
   $$
   \mathbf{u}_{\text{1-form}}\llbracket \mathbf{v}_{\text{vec}} \rrbracket = \mathbf{u} \cdot \mathbf{v}_{\text{vec}} = \begin{bmatrix} u_1 & u_2 & u_3 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}
   $$
2. **2-form Pairing (Scalar Triple Product):**
   $$
   \mathbf{w}_{\text{2-form}}\llbracket \mathbf{u}_{\text{vec}}, \mathbf{v}_{\text{vec}} \rrbracket = \det \begin{bmatrix} | & | & | \\ \mathbf{w} & \mathbf{u}_{\text{vec}} & \mathbf{v}_{\text{vec}} \\ | & | & | \end{bmatrix}
   $$
   We can represent $\bw_{\text{2-form}}$ as a 3D vector $\bw$. This is computing the volume of the parallelpiped formed by all 3 vectors, precisely $\bw \cdot (\bu \times \bv)$. But this is precisely the [[Determinant]] of all three vectors. 
3. **3-form Pairing (Scaled Triple Product):**
   $$
   f_{\text{3-form}}\llbracket \mathbf{u}_{\text{vec}}, \mathbf{v}_{\text{vec}}, \mathbf{w}_{\text{vec}} \rrbracket = f \det \begin{bmatrix} | & | & | \\ \mathbf{u}_{\text{vec}} & \mathbf{v}_{\text{vec}} & \mathbf{w}_{\text{vec}} \\ | & | & | \end{bmatrix}
   $$
In particular, these are special cases because $\binom{3}{x} = 3$ for $x = 1,2$. This is why we can map the results to vectors for 1-forms and 2-forms. 

# Definition (Interior Product / Contraction)
Another fundamental operation on exterior powers is the **interior product** (or contraction), which extends the standard covector-vector pairing. It "inserts" a vector $X \in V$ into a $k$-form, returning a $(k-1)$-form:
$$
i_X : V \times \bigwedge^k V^* \xrightarrow{\text{bilinear}} \bigwedge^{k-1} V^*
$$
It's like as if we fed $1$ out of the $k$ needed vectors to the covector. The interior product satisfies three defining rules:
1. **Dual pairing:** For a 1-form $\alpha \in V^*$, $i_X \alpha = \langle \alpha | X \rangle$.
	1. We needed $1$, and fed $1$, so we get a scalar. 
2. **Nilpotent:** Applying the same vector twice yields zero: $i_X i_X \omega = 0$.
	1. We fed it the same vector twice. 
3. **Exterior Leibniz rule:** 
$$
i_X (\alpha \wedge \beta) = (i_X \alpha) \wedge \beta + (-1)^{\text{deg}(\alpha)} \alpha \wedge (i_X \beta)
$$

The pairing of a $k$-form with $k$ vectors is elegantly equivalent to successively applying the interior product $k$ times:
$$
\omega \llbracket X_1, \dots, X_k \rrbracket := i_{X_k} \dots i_{X_1} \omega
$$
Consequently, evaluating a contracted form $i_X \omega$ on $k-1$ vectors is identical to just slotting the contraction vector $X$ into the very first input slot of the original $k$-form:
$$
(i_X \omega)\llbracket X_1, \dots, X_{k-1} \rrbracket = \omega \llbracket X, X_1, \dots, X_{k-1} \rrbracket
$$
By recursively applying this insertion rule alongside the Exterior Leibniz rule, we mathematically recover the [[#Theorem (Determinant Formula for Pairing)|Determinant Formula]] for evaluating wedge products of 1-forms!

## Example (Interior Product in 3D Space)
1. $i_{\bu_{\text{vec}}} \bv_{1-\text{form}} = (\bu \cdot \bv)_{0-\text{form}}$
2. $i_{\bu_{\text{vec}}} \bw_{2-\text{form}} = (\bw \times \bu)_{1-\text{form}}$
3. $i_{\bu_{\text{vec}}} f_{3-\text{form}} = (f \bu)_{2-\text{form}}$


