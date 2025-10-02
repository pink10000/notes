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

