---
tags:
  - MATH_190A
aliases:
  - subspace topology
---
# Definition (Subspace Topology)
Recall if $(X, \tau_{X})$ is a topological space and $A \subseteq X$, we define on $A$,
$$
\tau_{A} = \{ U \cap A \mid U \text{ open in } X\}
$$
and this does form a [[Topological Space|topology]] on $A$. This does this because the *canonical inclusion map* 
$$
i : A \hookrightarrow X
$$
is continuous. We check open $U \subset X$, such that $i^{-1}(U) = U \cap A$, which is open (relative to $A$). So, we have 
$$
(A, \tau_{A}) \xhookrightarrow{i} (X, \tau_{X})
$$
which is continuous. In fact, $\tau_{A}$ is the *smallest* topology on $A$ for which this inclusion map is continuous. 
## Lemma (Subspace Continuity by Canonical Inclusion) 
Given $A \subseteq X$ is a subspace, and $Z$ is a third space, then a map 
$$
f : Z \to A
$$
is [[Topological Continuity|continuous]] iff its composite $Z \to A \to^{i} X$ is continuous.

Proof:
$(\implies)$
We simply have the [[Topological Continuity#Theorem (Continuity by Composition in a Topology)|composition of continuous]] functions, which is continuous. 

$(\impliedby)$
Given $U$ open in $A$, WTS $f^{-1}(U)$ is open in $Z$. But we know $U = A \cap V$ for some open $V$ in $X$. Then $f^{-1}(U) = f^{-1}(A \cap V) = f^{-1}i^{-1}(V) = (i \circ f)^{-1}(V)$ which is open if $i \circ f$ is continuous. 

# Lemma (Universal Property of the Subspace Topology)
The [[Subspace Topology|subspace topology]] satisfies the property:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} 
	{(A, \tau_A)} & {(X, \tau)} \\ 
	{(Z, \tau_Z) } 
	\arrow["i", hook, from=1-1, to=1-2] 
	\arrow["f", from=2-1, to=1-1] 
	\arrow["{i \circ f}"', dotted, from=2-1, to=1-2] 
\end{tikzcd}
\end{document}
```
$f$ is [[Topological Continuity|continuous]] $\iff$ $i \circ f$ is continuous. 

This means that if you want to construct a continuous map *to* $A$, it is enough to find a continuous map to $X$ whose image lies in $A$. In fact, this property *characterizes* the subspace topology in the following sense:

if $\tau_{1}$ and $\tau_{2}$ are two topologies on $A$ which satisfies the property that for all test spaces and maps, then $\tau_{1} = \tau_{2}$. 

Proof:
Suppose we had 
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} 
	{(A, \tau_1)} & {(X, \tau)} \\ 
	{(A, \tau_2)} 
	\arrow["{i_1}", hook, from=1-1, to=1-2] 
	\arrow["{i_2}", hook, from=2-1, to=1-2]
	\arrow["{id_1}", shift left=2 ,from=1-1, to=2-1]
	\arrow["{id_2}", from=2-1, to=1-1]
\end{tikzcd}
\end{document}
```
with $\tau_{1}, \tau_{2}$ satisfying the property above. We observe that 
- $\id_{1}$ is continuous because $i_{2} \circ \id_{1} = i_{1}$ is continuous, and
- $\id_{2}$ is continuous because $i_{1} \circ \id_{2} = i_{2}$ is continuous
Hence the two $\id$ maps do form a [[Homeomorphisms|homeomorphsism]]. Continuity of both implies they have the exact same open sets. Thus, $\tau_{1} \subseteq \tau_{2}$, and $\tau_{2} \subseteq \tau_{1}$. 

> By `test`, we mean the conditions are written in some other space $Z$. 

# Gluing Lemma
If $\{U_{i}\}$ is an *open cover* of $X$, then a continuous function $f : X \to Y$ is the same as a collection of continuous functions 
$$
f_{i} : U_{i} \to Y
$$
which agree on all overlaps:
$$
f_{i} |_{U_{i} \cap U_{j}} = f_{j} |_{U_{i}\cap U_{j}}
$$
> *Open Cover* means open sets where the union covers $X$.

Proof: 
$(\implies)$
This is straightforward because $f|_{U_{j}} = f \circ i_{j} : U_{j} \xhookrightarrow{i_{j}} X \xrightarrow{f} Y$.  

$(\impliedby)$
The question is whether the global function $f$ created by setting
$$
f(x) = f_{i}(x) 
\quad\quad\quad
x \in U_{i}
$$
is continuous or not. Consider $V$ open in $Y$. Then 
$$
f^{-1}(V) = \bigcup_{i \in I} f^{-1}(V) \cap U_{i} 
$$
Now, 
$$
f^{-1}(V) \cap U_{i} = (f|_{U_{i}})^{-1}(V) = (f_{i})^{-1}(V)
$$
so it is open in $U_{i}$ because $f_{i}$ is continuous, using [[Topological Continuity#Definition (Topological Characterization of Continuity)]]. 

Fortunately, we know that an open subset $f^{-1}(V) \cap U_{i}$ of a subspace $U_{i}$ which is itself open on a subset of $X$, is open in $X$. Hence, 
$$
f^{-1}(V) = \bigcup \text{ sets open relative to } X
$$
so by [[Metric Space#Lemma (Openness and Closure)]], $f^{-1}(V)$ is open.

> This lemma describes how we can glue together multiple continuous functions, each defined on an open patch to create a single continuous function.

## Gluing Lemma (But Closed)
If $\{F_{i}\}_{i=1, \dots, n}$ is a covering by finitely many closed closed subsets, then a continuous function $f : X \to Y$ is the same as a collection of continuous $f_{i} : F_{i}\to Y$ which agree on overlaps. 

Proof:
The same as the Gluing Lemma but using $f^{-1}(\text{closed sets})$. Take note of the finiteness condition. 

> These lemmas are similar to how we prove a piecewise function is continuous. We break up the cases, just like how we break up $X$ to $U_{i}$ and prove continuity on each $U_{i}$. 


