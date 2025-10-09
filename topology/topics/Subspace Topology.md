---
tags:
  - MATH_190A
---
# Definition (Subspace Topology)
Recall if $(X, \tau_{X})$ is a topological space and $A \subseteq X$, we define on $A$,
$$
\tau_{A} = \{ U \cap A \mid U \text{ open in } X\}
$$
and this does form a [[Topological Space|topology]] on $A$. This does this because the canonical inclusion map 
$$
i : A \hookrightarrow X
$$
is continuous. We check open $U \subset X$, such that $i^{-1}(U) = U \cap A$, which is open (relative to $A$). So, we have 
$$
(A, \tau_{A}) \hookrightarrow^{i} (X, \tau_{X})
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