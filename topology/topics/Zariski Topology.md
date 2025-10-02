---
tags:
  - MATH_190A
---
# Definition (Zariski Topology)
In algebraic topology, we use the **Zariski Topology** where the [[Metric Space#Open & Closed|open sets]] are the *complements* of the zero-sets (sets where the polynomial vanishes) of the polynomial function. 

In particular, when $X = \R$, the open sets are just the complements of the finite subsets of $\R$. This is also called **cofinite** topology on $\R$. 

## Lemma (Arbitrary Unions/Intersections of Cofinite Sets)
Let $X$ be infinite, and $A, B$ be finite. Then $(X - A)$ and $(X - B)$ are cofinite. Then, 
$$
\begin{aligned}
(X - A) \cup (X - B) &= X - (A \cap B) \\
(X - A) \cap (B - B) &= X - (A \cup B)
\end{aligned}
$$

# Definition (Subspace Topology)
If $(X, T)$ is a [[Topological Space]] and $A$ is any subset of $X$, then we can define a **subspace topology** $T_{A}$ on $A$ via 
$$
T_{A} =  \{ A \cap U : U \in T_{X} \}
$$
Checking the axioms,
1. $\varnothing \in T_{X} \implies A \cap \varnothing = \varnothing \in T_{A}$ and $A \subset X$, so $A \cap A = A \in T_{A}$. 
2. $\bigcup_{i \in I} (A \cap U_{i}) =  A \cap \left( \bigcup_{i \in I} U_{i} \right)$
3. $\bigcap_{i \in I} (A \cap U_{i}) = A \cap \left( \bigcap_{i \in I} U_{i} \right)$

## Example
Let $I = [0, 1] \subseteq \R$. Then considering set $[0, 1/2) \subset \R$ is open in this subspace. 
> A subset $B$ of $A$ can be open in $A$, but not open in $X$. See [[Induced Metric Space#Definition (Open/Closed Relative)]]. 

# Lemma (Intersection of Openness)
If $A$ is open in $X$, and $U$ open in $X$, then $A \cap U$ is also open in $X$. See [[Metric Space#Lemma (Openness and Closure)|lemma]].

# Lemma (Unique Smallest Topology)
Given *any* subset $\sigma \subseteq \mathcal{P}(X)$, there is a *unique smallest topology* $T(\sigma)$ containing $\sigma$ and its open sets are of form
$$
(*) \quad\quad\quad\quad
U = \bigcup_{i \in I} (S_{i,1} \cap S_{i,2} \cap \cdots \cap S_{i,n})
$$
where $S_{i,j} \in \sigma$. $n$ is some arbitrary finite positive integer.
> Technically, one can argue that the intersection of no things (when $\sigma = \varnothing$) is $X$ itself. 

Proof: 
Clearly, if $T \supseteq \sigma$, is a topology, it must contain all these sets. We can check axioms. Arbitrary unions of $(*)$ intersections are of the form 
$$
\bigcup_{i \in I} (S_{i,1} \cap \cdots \cap S_{i,n})
\cap 
\bigcup_{j \in J} (S_{j,1} \cap \cdots \cap S_{j,m})
=
\bigcup_{i \in I, j \in J} \text{summand 1} \cap \text{summand 2}
$$
We could also use the [[Induced Metric Space#Definition (Open/Closed Relative)]] because this holds $\iff$ holds for all finite intersections (by induction). 

This generating set $\sigma$ is called the **sub-basis** for the topology $T(\sigma)$.
# Definition (Base/Basis)
$\beta \subseteq \mathcal{P}(X)$ is a **base** (or **basis**) for the topology $T$ if any element $U \in T$ can be written as a union if any element $U \in T$ can be written as a union of elements in $\beta$. 
## Examples
In $\R$ with the standard topology, the set of all open intervals $(a,b)$ is a basis for the topology, since any open set of $\R$ can be written as a union of open intervals.  

In a [[Metric Space]] $(X, d)$, the $\{B_{\vepsi}(x), \vepsi > 0, x \in X\}$ forms a basis for the associated topology. 

# Definition (Sub-Base)
We say a collection $S$ of $\tau$ is a **subbasis** if all finite intersections of $S$ form a basis for $\tau$. A subbasis determines a 