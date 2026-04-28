---
tags:
  - MATH_190A
aliases:
  - embedding
  - embed
  - embedded
---
# Definition (Embedding)
An **embedding** of $(X, \tau_{X})$ in $(Y, \tau_{Y})$ is a map from $f : X \to Y$ which carries $X$ homeomorphically to its image. 

For example, imagine mapping our $S^{1}$ circle to a trefoil knot in $\R^{3}$. This however, is not a homeomorphism. 

Equivalently, $f$ is an embedding if:
- $f$ is injective,
- $f$ is [[Topological Continuity|continuous]], and
- the induced map
$$
f : X \to f(X)
$$
is a [[Topological Homeomorphisms|homeomorphism]], where $f(X)$ is given the [[Subspace Topology]] from $Y$.

So an embedding identifies $X$ with a subspace of $Y$ without changing its intrinsic topology.
