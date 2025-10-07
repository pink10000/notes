---
tags:
  - MATH_190A
---

# Definition (Topological Characterization of Continuity)
If $(X, \tau_{x})$ and $(Y, \tau_{y})$  are [[Topological Space|topological spaces]], then we can define a function $f : X \to Y$ to be **continuous** if $\forall$ open $U\subseteq Y$, the preimage $f^{-1}(U)$ is open in $X$. This is correct if the topologies come from metrics. 

> This is also in [[Continuity#Proposition (Topological Characterization of Continuity)]].

## Example 1
1. Any map out of a space with the [[Topological Space#Definition (Discrete Topology)|discrete topology]] is continuous. 
2. Any map into a space with the [[Topological Space#Definition (Discrete Topology)|indiscrete topology]] is continuous.

Proof:
For $(1)$, every subset of $X$ is open. For $(2)$, the topology defined in $Y$ is only $\{\varnothing, Y\}$, which means the preimage for any of these sets is merely $\varnothing$ and $X$ respectively. 

## Example 2
If $\beta$ is a [[Base#Definition (Base/Basis)|basis]] for $\tau_{Y}$, then it's enough to check that $f^{-1}(B)$ is open in $X$, $\forall B \in \beta$. 

Proof:
$$
f^{-1}\left( \bigcup_{i \in I} B_{i} \right)
=
\bigcup_{i \in I}f^{-1}(B_{i})
$$
will be open. 

# Definition (Continuity at a Point)
The function $f: (X, \tau_{X}) \to (Y, \tau_{Y})$ is continuous at $a \in X$ if $\forall$ neighborhood $N$ of $f(a)$ in $Y$, the preimage $f^{-1}(N)$ is neighborhood of $a$ in $X$. 

# Theorem (Equivalence of Global & Pointwise Continuity)
A function $f : (X, \tau_{X)} \to (Y_{} ,\tau_{T})$ is **globally continuous** $\iff$ it is continuous at $a, \forall a \in X$.

Proof. 
$(\impliedby)$
Given $V \subseteq Y$ open, WTS $f^{-1}(V)$ is open in $X$. So take $a \in f^{-1}(V)$.  Continuity at this point says that since $V$ is a neighborhood of $f(a)$. we have $f^{-1}(V)$ is a neighborhood of $a$. Since $a$ was arbitrary, then $f^{-1}(V)$ is open.

$(\implies)$
Given $N$ a neighborhood of $f(a)$, then it contains some open $V$ where $f(a) \in V$. Then global continuity implies $f^{-1}(V)$ is open, but $a \in f^{-1}(V) \subseteq f^{-1}(N)$ and so $f^{-1}(N)$ is a neighborhood of $a$. 