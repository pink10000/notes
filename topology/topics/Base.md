---
tags:
  - MATH_190A
---
# Definition (Base/Basis)
$\beta \subseteq \mathcal{P}(X)$ is a **base** (or **basis**) for the topology $\tau$ if any element $U \in \tau$ can be written as a union of elements in $\beta$. 
## Examples
In $\R$ with the standard topology, the set of all open intervals $(a,b)$ is a basis for the topology, since any open set of $\R$ can be written as a union of open intervals.  

In a [[Metric Space]] $(X, d)$, the $\{B_{\vepsi}(x), \vepsi > 0, x \in X\}$ forms a basis for the associated topology. 

# Theorem (Minimum Basis for Topology)
> What conditions on $\beta$ are necessary for it to generate a [[Topological Space|topology]]?

Suppose $\beta \subseteq \mathcal{P}(X)$ satisfies
1. $\forall x \in X, \exists B \in \beta$ such that $x \in B$. 
	1. All we are really saying is that $X$ can be written as a union of elements of $\beta$. 
2. $\forall B_{1},B_{2} \in \beta$ and any element $x \in B_{1}\cap B_{2}, \exists B_{3}\in \beta$ such that $x \in B_{3} \subseteq B_{1} \cap B_{2}$. 
	1. Also equivalent, is $\forall B_{1},B_{2}\in \beta, B_{1} \cap B_{2}$ can be written as a union of elements of $\beta$. 
	2. However $2 \not\!\!\!\implies 2.1$ because we can write $B_{1} \cap B_{2} = \bigcup_{x \in B_{1} \cap B_{2}} B_{3}$ 

then $\beta$ is a basis for a for a topology on $\tau$. The converse is also true. 

Proof:
$(\impliedby)$
Certainly if $\beta$ is a base for $\tau$, then the two conditions are satisfied since $X$ can be 
1. written as a union of elements of $\beta$. 
2. If $B_{1}, B_{2} \in \beta$ then $B_{1}\cap B_{2}$ is open. Therefore it can be written as a union by $2.1$. 

$(\implies)$
Merely check the finite intersection axiom. It is enough to do it pairwise and check 
$$
\left(
	\bigcup_{i \in I} B_{i}
\right)
\cap 
\left(
	\bigcup_{j \in J} B_{j}
\right)
= \bigcup_{i,j} B_{i} \cap B_{j}
$$
for $B_{i}, B_{j} \in \beta$. Then by $2.1$ this is just the union of elements of $\beta$.

## Example 1
In a [[Metric Space]] $X$, the set of all 
$$
B_{\vepsi}(x) 
\quad\quad\quad
\forall x \in X, \forall \vepsi > 0
$$
forms a base. 

## Example 2 
We can define a topology on $\R$ by setting
$$
\beta = \{\text{all intervals of the form} [a, b) : a < b\}
$$
We check: intersecting any two such things gives another one, so this is a basis. 

## Example 3
> We can define topologies on spaces that are not metric spaces.

The real line without a point. $\R \cap \{0'\}$ where
$$
\beta = \{ \text{all intersections of the form } (a, b) \text{ and where 0' replaces 0, if 0 } \in (a, b)\}
$$
Clearly any intersection of any two such basic open intervals is either another element of the same form or $(-a, 0) \cup (0, b)$ is the union of base elements.

## Remark
Bases are usually not unique. Any representation of an open set $U \in T$ as a union of base elements $U = \bigcup_{i \in I} B_{i}$ is almost certainly not unique. 

# Definition (Product of Spaces Base)
See [[Product of Spaces#Definition (Product of Spaces Base)]]. 

