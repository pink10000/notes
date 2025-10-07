---
tags:
  - MATH_190A
---
# Definition (Accumulation Points)
Given a set $A$ in $X$, the *derived set* is 
$$
A' = \{ x \in X \mid \forall N_{x},  N_{x} \cap (A - \{x\}) \neq \varnothing \}
$$
These points are called **accumulation points**. Note that $N_{x}$ is the neighborhood of $x$, and that $x$ may or may not be in $A$. 


> Also know as [[Metric Space#Limit Point|limit points]]. 
> Related:  [[Topological Space#Definition (Neighborhood in a Topology)]]


## Example 1
$$
A = \{0\} \cup \left\{ \frac{1}{n} \mid n \geq 1 \right\} \subseteq \R 
$$
We see that for $x = 0$, every neighborhood of $x$ must contain some other point in $A$. We prove by [[Archimedean Property]]. So, $\ovl{A} = A$. 

Here, the only accumulation point is $0$. 
## Example 2
$$
B = \left\{ \frac{1}{n} \mid n \geq 1  \right\}
$$
Again, for $x = 0$ every neighborhood must contain some other point in $B$. But as $0 \not\in B$, we see $\ovl{B} = A$. 

Likewise, the only accumulation point is $0$.

# Theorem (Relationship with Accumulation Points and Closure)
$$
\ovl{A} = A \cup A'
$$
where $\ovl{A}$ is the [[MATH 190A - Lecture 4#Interior and Closure|closure]] of $A$. 

Proof:
$(\supseteq)$:
Certainly $A \subseteq \ovl{A}$. If $x \in A'$ then every neighborhood of it meets $A \backslash \{x\}$ which means $x \in \ovl{A}$. 

$(\subseteq)$: Let $x \in \ovl{A}$. If $x \in A$, then $x \in A \cup A'$. If $x \not \in A$ then every neighborhood of $x$ meets $A$, since it is a point of the closure. But then every neighborhood of $x$ meets $A = A \backslash \{x\}$. Hence $x \in A'$. 

# Theorem (Closure with Accumulation Points)
$A$ is closed $\iff$ it contains all of its accumulation points.

