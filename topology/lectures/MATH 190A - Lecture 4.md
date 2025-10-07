---
tags:
  - MATH_190A
  - MATH_190A_Lecture
---
[[Base]]

# Closed Sets
A set $A \subseteq X$ is closed $\iff$ $X - A$ is open. By DeMorgan, we see that 
1. $\varnothing, X$ are closed
2. Arbitrary intersection of closed sets is closed. 
$$
\bigcap_{i \in I}F_{i} 
= 
\bigcap_{i\in I} (X - U_{i})
= 
X - \bigcap_{i\in I } U_{i}
$$
3. Finite unions of closed sets are closed. 

## Remark 
Clearly knowing open sets is equivalent to knowing the closed sets. We can define a topology by defining the closed sets satisfying these three axioms.

# Interior and Closure
For any set $A \subseteq (X, \tau)$ let 
$$
A' \equiv \text{Int}(A) := \bigcup_{U \text{open}, U \subseteq A} U \subseteq A
$$
this is clearly an open set $\subseteq A$. Furthermore $\Int(A) = A \iff A$ is open. 

Alternatively, this is the "largest" open set inside $A$ (with the notion of inclusion). 

Similarly
$$
\ovl{A} \equiv \text{Cl}(A) := \bigcap_{F \text{ closed}, F \supseteq A} F
\supseteq A
$$
this is a closed set containing $A$. 
1. $A$ is closed $\iff \ovl{A} = A$ 
2. Alternatively, this is the "smallest" closed set $\supseteq A$. 

It is a consequence of DeMorgan that 
$$
\ovl{A} = X - (X - A)'
$$
Note that 
$$
\Int(A) = \{x \in A : \exists \text{ open set } U, x \in U \subseteq A \}
$$

Hence 
$$
\begin{aligned}
x \in \ovl{A}
&\iff x \not\in \Int(X - A) \\
&\iff \nexists \text{ open } U \text{ containing } x \text{ inside } X - A \\
&\iff \forall \text{ open } U \text{ containing } x, U \not\subseteq X - A \\
&\iff \forall \text{ open } U \text{ containing } x, U \cap A \neq \varnothing
\end{aligned}
$$
