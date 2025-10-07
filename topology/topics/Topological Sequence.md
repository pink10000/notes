---
tags:
  - MATH_190A
---
# Definition (Topological Sequence)
If $(x_{n})_{n \in \N}$ is a **sequence** in $X$, then we say $x_{n} \to x$ (converges to $x$) if for any open set $U$ where $x \in U$, then $\exists N$ such that $\forall n \geq N, x_{n}\in U$. 

We say $x$ is a **limit** of the sequence. 

> In a [[Topological Space]], a sequence can have non-unique limits. Consider $\R$ with a double origin and we took $x_{n}= 1/n$, then we have two different limits of the sequence. 
>
> This is different from a [[Metric Space]] where a [[Sequences|sequence]] can only have $1$, unique limit point.

## Example 1
If $X$ has an [[Topological Space#Definition (Discrete Topology)|discrete topology]], then every sequence $\{x_{n}\}$ converges to every point. 