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
The **product topology** for $X$ is the smallest [[Topological Space|topology]] that making all the $\pi_{i}$ [[Topological Continuity|continuous]]. 

This requires us to define open sets as things of the form 
$$
\pi_{i}^{-1}(U) = \prod_{j\in I} V_{j}
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
Notice that intersecting finitely many of these things must give us an open set as well. 
# Definition (Product of Spaces Base)
A **base** $\beta$ for the product topology on $X$ is 
$$
\prod_{i \in I} U_{i} 
\quad\quad\quad
U_{i}\text{ open in } X_{i}, \text{ but } U_{i} = X_{i} \text{ for all but finitely many } i \in I 
$$
This is indeed a base for a topology. Actually, it is a base arising from a sub-base. The condition where $U_{i}\subsetneq X_{i}$ only for finitely many $i \in I$ arises from the fact that the natural inclusion maps must be continuous, which we see in the following theorem.

# Theorem (Product Topology Properties)
The product topology has the following properties:
1. The projection maps $\pi_{i} : X \to X_{i}$ are all [[Topological Continuity|continuous]].
2. A map $f : Z \to X = \prod X_{i}$ is continuous $\iff$ all its composites $f_{i}= \pi_{i} \circ f$ are continuous. These are also know as coordinate functions. 
   > This means we have an easier way to test if a complicated function $f$ (in the sense that the codomain is a product of spaces) is continuous by checking the simpler coordinate functions. 
3. These two properties characterize the product topology, in the sense that is unique.

Proof:
1. Done. We proved it directly earlier.
2. Forward is by [[Topological Continuity#Theorem (Continuity by Composition in a Topology)|composition of continuous functions]]. For the backwards direction, take a basic open set of $\prod X_{i}$. So, let $B = \prod U_{i}$. But then
   $$
   f^{-1}(B) = \bigcap_{i \in I} (f_{i}^{-1})(U_{i})
   $$
   which is actually a finite intersection because $U_{i} = X_{i}$ for finitely many $i$. Thus, $f^{-1}(B)$ is open, and apply [[Topological Continuity#Definition (Topological Characterization of Continuity)|lemma]].
3. Same kind of tautological proof for [[Subspace Topology#Lemma (Universal Property of the Subspace Topology)|subspace topology]]. More specifically, if we assume we have two different product topologies, we find that both are subsets of each other, and thus equal (and unique).