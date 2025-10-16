---
tags:
  - MATH_190A
---
# Definition (Product of Spaces)
Given a collection of [[Topological Space|spaces]] $\{X_{i}\}_{i\in I}$, we have the product
$$
\prod_{i \in I} X_{i} = \{(X_{i})_{i \in I} \}
$$
and comes with a *natural projection*:
$$
\begin{aligned}
\pi_{i} : \prod X_{i} &\to X_{i} \\
(x_{i})_{i \in I} &\mapsto x_{i}
\end{aligned}
$$

# Definition (Product Topology)
The **product topology** for $X$ is the smallest [[Topological Space|topology]] that makes all the $\pi_{i}$ [[Topological Continuity|continuous]]. 

This requires us to define open sets as things of the form 
$$
\pi_{i}^{-1}(U_{i}) = \prod_{
\substack{j \in I \\ i \neq j \implies V_{j} = X_{j} \\ i = j \implies V_{i} = U_{i}}
} V_{j}
$$
for $U$ open in $X_{i}$ and where $V_{j} = X_{j}$, except for $V_{i} = U$. 

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	{} && {} && {} & {} \\
	&&& {U \times Y} \\
	{} &&&&& \frown \\
	& {X \times V} && {U \times V} &&& {\prod_Y} \\
	{} &&&&& \smile \\
	{} && {(} && {)} & {} & Y \\
	&&& {\prod_X } && X
	\arrow[no head, from=1-1, to=1-6]
	\arrow[no head, from=1-1, to=6-1]
	\arrow[dashed, no head, from=1-3, to=6-3]
	\arrow[dashed, no head, from=1-5, to=6-5]
	\arrow[dashed, no head, from=3-1, to=3-6]
	\arrow[dashed, no head, from=5-1, to=5-6]
	\arrow[no head, from=6-6, to=1-6]
	\arrow[no head, from=6-6, to=6-1]
\end{tikzcd}
\end{document}
```
Notice that intersecting finitely many of these open sets from the base.

> This is similar to [[Subspace Topology]] where the subspace topology had an inclusion map, we have a [[Topological Continuity#Theorem (Equivalence of Global & Pointwise Continuity)|continuous]] map. 

# Definition (Product of Spaces Base)
A **base** $\beta$ for the product topology on $X$ is 
$$
\beta = \left\{ \prod_{i \in I} U_{i} 
\;|\;
U_{i}\text{ open in } X_{i}, \text{ but } U_{i} = X_{i} \text{ for all but finitely many } i \in I  \right\}
$$
This is indeed a base for a topology. Actually, it is a base arising from a sub-base. The condition where $U_{i}\subsetneq X_{i}$ only for finitely many $i \in I$ arises from the fact that the natural inclusion maps must be continuous, which we see in the following theorem.

# Theorem (Product Topology Properties)
The product topology has the following properties:
1. The projection maps $\pi_{i} : X \to X_{i}$ are all [[Topological Continuity|continuous]].
2. A map $f : Z \to \prod X_{i}$ is continuous $\iff$ all its composites $f_{i}= \pi_{i} \circ f$ are continuous. These are also know as coordinate functions. 
	1. $f$ is a function that extracts one of the coordinates.
	2. This means we have an easier way to test if a complicated function $f$ (in the sense that the codomain is a product of spaces) is continuous by checking the simpler coordinate functions. 
3. These two properties characterize the product topology, in the sense that it is unique.

The point is that set-theoretically, a function $Z \to \prod X_{i}$ is the same thing as a collection of coordinate functions
$$
f_{i} = \pi_{i} \circ f
$$
Categorically, 
$$
\hom_{\text{Top}}\left(Z, \prod X_{i}\right) \cong \prod_{i \in I} \hom_{\text{Top}}(Z, X_{i})
$$
where $\cong$ is a bijective correspondence. 

Proof:
1. Done. We proved it directly earlier.
2. Forward is by [[Topological Continuity#Theorem (Continuity by Composition in a Topology)|composition of continuous functions]]. For the backwards direction, take a basic open set of $\prod X_{i}$. So, let $B = \prod U_{i}$. But then
   $$
   f^{-1}(B) = \bigcap_{i \in I} (f_{i}^{-1})(U_{i})
   $$
   which is actually a finite intersection because $U_{i} = X_{i}$ for finitely many $i$. Thus, $f^{-1}(B)$ is open, and apply [[Topological Continuity#Definition (Topological Characterization of Continuity)|lemma]].
3. Same kind of tautological proof for [[Subspace Topology#Lemma (Universal Property of the Subspace Topology)|subspace topology]]. More specifically, if we assume we have two different product topologies, we find that both are subsets of each other, and thus equal (and unique).

## Example 1
Suppose $f : X \to Y$ is continuous, then let $\Gamma_{f}$ be its graph,
$$
\Gamma_{f} = \{ (x, f(x)) : x \in X \} \subseteq X \times Y
$$
Then 
$$
\Gamma_{f} \cong X
$$
is [[Topological Homeomorphisms|homeomorphic]]. The map
$$
\begin{aligned}
\phi : X &\to \Gamma_{f} \\
x &\to (x, f(x))
\end{aligned}
$$
is continuous. This is because $\Gamma_{f}$ inherits its topology (the [[Subspace Topology]]) from the product topology of $X \times Y$. We know that from subspace properties that 
$$
\begin{aligned}
\phi : X \to \Gamma_{f} \text{ is continuous} 
&\iff i \circ \phi : X \to X \times Y \text{ is continuous} \\
&\iff \pi_{X} \circ i \circ \phi, \pi_{Y} \circ i \circ \phi \text{ are continuous maps } X \to X, X \to Y \\
\end{aligned}
$$
by [[Subspace Topology#Lemma (Subspace Continuity by Canonical Inclusion)|lemma]]. The third map is just $\id_{X} : X \to X$ and the fourth is $f : X \to Y$. 
$$
\begin{aligned}
X \xrightarrow{\phi}
\Gamma_{f} \xrightarrow{i}
& X \times Y \xrightarrow{\pi_{X}} X \\
X \xrightarrow{\phi}
\Gamma_{f} \xrightarrow{i}
& X \times Y \xrightarrow{\pi_{Y}} Y \\
\end{aligned}
$$
Canonically, we are using 
$$
\pi_{X}|_{\Gamma_{f}} : \Gamma_{F} \to X
$$
which is continuous because it's $\pi_{X} \circ i$ since restricting the domain is the same "pre-composing" it with an inclusion map to the ambient space. Thus, by [[Topological Continuity#Theorem (Continuity by Composition in a Topology)|theorem]], it is continuous. 

Finally, we observe that $\phi$ and $\pi_{X}|_{\Gamma_{f}}$ are indeed mutually inverse. 

> Warning: We cannot do all proofs in this way. In particular, dealing with continuity of maps out of a product usually requires working with a basis. So with this, we can talk about maps *into* a product, not *out*.

## Example 2 
The [[Diagonal Map]] $X \to \prod_{i \in I} X$ (the space itself, not a typo) maps $x \mapsto (x)_{i \in I}$ is continuous because if $B$ is a [[Base#Definition (Base/Basis)|basis]] element for $\prod X$, then $B$ is of the form $\prod U_{i}$ where $U_{i}$ are open in $X$, but finitely many of them are equal to $X$. 

What is the inverse image under the diagonal under such a product set? The preimage means that we want $X$ to live inside $\prod X$ which requires $X$ is contained in these open sets $U_{i}$. In other words, $X$ is in the intersection of all these $U_{i}$. So 
$$
\begin{aligned}
\Delta^{-1}(B) 
&= \bigcap_{i \in I} U_{i} \\
&= \text{intersection of finite open sets} \\
&= \text{open}
\end{aligned}
$$
by being a finite intersection of open sets in a [[Topological Space|topological space]].

# Example 3
Note that [[#Example 2]] would not be continuous if we used the **Box Topology** on $\prod X$. Namely, setting the basis as
$$
\beta = \left\{ \prod U_{i} : U_{i} \text{ open in } X \right\}
$$
with no restriction on $U_{i}$. 
