---
tags:
  - MATH_190A
---
# Definition (Topological Space)
A **topological space** is a set $X$ together with a **topology**, $T_{X}$ which is a set of subsets of $X$ (such that $T_{X} \subseteq \mathcal{P}(X)$) that satisfy the following axioms:
1. $\varnothing \not \in T_{X}$ an $X \in T_{X}$ 
2. if $\{U_{i}\}_{i \in I}$ is a family of elements in $T_{X}$, then $\bigcup_{i \in I} U_{i} \in T_{X}$.  
3. if $U_{1}, \dots, U_{n}$ is a *finite* set of elements in $T_{X}$, then $\bigcap_{i =1}^{n} U_{i} \in T_{X}$  

Elements of $T_{X}$ are referred to as "open sets". 

## Examples
Any [[Metric Space]] $(X, d)$ is a topological space "naturally". 
1. The empty set is open. See [[Metric Space#Lemma (Openness and Closure)]].
2. If $\{U_{i}\}_{i\in I}$ is a collection of $d-$open (i.e. open with respect to the metric) sets and $x \in \bigcup_{i \in I} U_{i}$, then $x \in U_{j}$ for some $j \in I$. Since $U_{j}$ is open, then $\exists B_{\vepsi> 0}(x) \subseteq U_{j}$ and so $B_{\vepsi}(x) \subseteq \bigcup_{i\in I} U_{i}$. 
3. Given $U_{1}, \dots, U_{n}$ of open sets and a point $x \in \bigcap_{i=1}^{n}U_{i}$, then $x$ is in all $U_{i}$. Since each $U_{i}$ is open, then $\exists \vepsi_{i}> 0$ such that $B_{\vepsi_{i}}(x) \subseteq U_{i}$. Clearly, 
   $$
   x \in \bigcap_{i=1}^{n} B_{\vepsi_{i}}(x) \subseteq \bigcap_{i=1}^{n}U_{i}
	$$
	but since there are finite balls, we simply pick the small $\vepsi_{i}$. Indeed, $B_{\min_{i}(\vepsi_{i})}$ is open and thus in $T_{X}$.  

# Definition (Discrete Topology)
Any set $X$ has a **discrete topology** $T = \mathcal{P}(X)$, if *all* subsets are decided open. Also, there is an **in-discrete topology**
$$
T = \{\varnothing, X\}
$$
The idea that topologies on a trivial set $X$ can be *compared*. Indeed, there exists a natural notion of one containing another 
$$
T_{1} \supseteq T_{2}
$$
Here, we say that $T_{1}$ is *finer*, and $T_{2}$ is *coarser*. 

## Example
A finite set can be "topologized". 

Let $X = \{a\}$. Then $T = \{\varnothing, \{a\}\}$. 

Let $X = \{a, b\}$. Then there are $4$ possibilities for topologies of $X$. 
$$
\begin{aligned}
T
&= \{ \varnothing, \{a, b\} \} \\
&= \{ \varnothing, \{a\}, \{a, b\} \} \\
&= \{ \varnothing, \{b\}, \{a, b\} \} \\
&= \{ \varnothing, \{a\}, \{b\}, \{a, b\} \} \\
\end{aligned}
$$
Recall that $X = \{a, b\}$ must be in $T$. 

Let $X = \{a, b, c\}$. There are $29$ different topologies. 

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

This generating set $\sigma$ is called the **sub-basis** for the topology $T(\sigma)$. The notion of a sub-base is a more "primitive form" of a [[Base]]. 
# Theorem (Equivalent Closure in a Topology)
If we have a base for the topology, we can say 
$$
x \in \ovl{A} \iff \forall B \in \beta, B \cap A \neq \varnothing 
$$
# Definition (Neighborhood in a Topology)
A **neighborhood** of a point $x$ is any set which contains an open set containing $x$. We can denote it as $N_{x}$ or "$N$ of $x$". 

> This definition is not standard. Some call a neighborhood is merely an open set. Here, we say that neighborhoods don't necessarily have to be open or closed (or either!) but merely that it contains some open set. 

We can also say that 
$$
x \in \ovl{A} \iff \exists N_{x}, N_{x} \cap A \neq \emptyset 
$$
