---
tags:
  - MATH_190A
---
# Definition (Metrizable)
A [[Topological Space]] $(X, \tau)$ is **metrizable** if $\exists$ a metric
$$
d : X \times X \to \R_{\geq 0}
$$
which induces the topology $\tau$. 

## Remark (Non-Hausdorff Spaces are not Metrizable)
Any non-[[Hausdorff Property|Hausdorff]] space is clearly non metrizable by [[Hausdorff Property#Theorem (Metric Spaces are Hausdorff)]]. 

# Making a Product of Metric Spaces
Suppose we had a bunch of [[Metric Space|metric spaces]] $\{(X_{i}, d_{i})\}_{i \in I}$. Can we metrize the product in a way that induces the [[Product of Spaces#Definition (Product Topology)|product topology]]? 

If $I$ is finite, then this is straightforward. 

## Theorem (Product Space is Metrizable)
If $(X_{i}, \tau_{i})_{i \in I}$ are metrizable spaces with metrics $d_{i}$ then 
$$
\left(\prod X_{i}, \text{ product topology} \right)
$$
is metrizable by writing 
$$
d_{\infty}(\unl{x}, \unl{y}) = \max\{  d_{i}(x_{i}, y_{i}) \}
$$
where $\unl{x}$ and $\unl{y}$ are "tuples" in the product space.

Proof: 

We use the principle: Suppose $\beta_{1},\beta_2$ are two bases. To show that the two topologies are the same, we just need to show that  $\forall B_{1}\in \beta_{1}$, for any $x \in B_{1}$, there $\exists B_{2} \in \beta_{2}$ containing $x$ contained in $B_{1}$, and vice versa. 

If $U_{1} \times U_{2} \times \cdots \times U_{n}$ is a basic (part of the basis) open set of the product topology containing some $x$, we can find some 
$$
B_{\vepsi_{i}}(x_{i}) \subseteq U_{i} 
\quad\quad\quad
\text{ for any } \vepsi > 0
$$
Take the minimum since we have some open set of finite product.  
$$
\vepsi = \min\{ \vepsi_{1}, \dots, \vepsi_{n}\}
$$
We get
$$
B_{\vepsi}^{d_{\infty}}(\unl{x}) \subseteq U
$$
Indeed, 
$$
B_{\vepsi}^{d_{\infty}}(\unl{x}) = B_{\vepsi}(x_{1}) \times \cdots \times B_{\vepsi}(x_{n})
$$
which is a basis element for the product topology.

## Remark (Different Metric for Product Space)
It would still work if we used 
$$
d_{1}(\unl{x}, \unl{y}) = \sum d_{i}(x_{i}, y_{i})
$$
In fact, these are equivalent metrics (i.e. give the same topology). The proof is slightly different since we have a different $\vepsi$. At a "higher" level, the epsilon balls are no longer a rectangle, but a "diamond" in $\R^{2}$.

# Metrizable Infinite Spaces
Naively, we'd define 
$$
D(\unl{x}, \unl{y}) = \sup \{ d_{i}(x_{i}, y_{i}) \}
$$
but this will probably be infinite. A better way is to replace each metric $d_{i}$ with the *bounded* metric corresponding to it. 
$$
\ovl{d_{i}}(x_{i}, y_{i}) = \min\{d_{i}(x_{i}, y_{i}) \}
$$
We would check $\ovl{d_{i}}$ is a metric and induces the same topology as $d_{i}$. We then set 
$$
D(\unl{x}, \unl{y}) = \sup_{i \in I}\{ \ovl{d_{i}}(x_{i}, y_{i}) \}
$$
but this gives the *uniform* topology on the product, which is different from the [[Product of Spaces#Definition (Product Topology)|product topology]] (in general).

If  is uncountable, in general we cannot define metric that induces the product.

Suppose that $I$ is countable. Ultimately, the solution requires us to make the metrics "shrink". In particular, consider a countable product 
$$
\prod_{i \in \N}(X_{i}, d_{i})
$$
and define 
$$
D(\unl x, \unl y) := \sup_{i \in \N} \left\{ \frac{\ovl{d}(x_{i}, y_{i})}{i} \right\}
$$
where the [[Diameter|diameter]] of $x_{i}$ is now $1/i$ instead of $1$. We have to check two things. One, this is indeed a metric. 
- If all the points are the same, the [[Supremum|supremum]] is $0$. And indeed, if two points are different, then at least one element is greater than $0$. 
- For the same reasoning, it is symmetric. 
- For each $d_{i}$, we know 
  $$
  \begin{aligned}
  \ovl d_{i}(x_{i},z_{i}) /i
  &\leq \ovl d(x_{i}, y_{i})/i + \ovl d_{i}(y_{i}, z_{i})/i \\
  &\leq D(\unl x, \unl y) + D(\unl{y}, \unl z) \\ 
  \end{aligned}
  $$
  Hence $\sup_{i}$ of the LHS is also $\leq$ to the RHS, and the triangle inequality is satisfied. 
Then we need to show it is actually the product topology. We have to show that basic open sets of the $D$ metric on this space can be written as basic epsilon balls in the product topology and conversely. 

Now we need to show the topologies coincide. Given $V$ open in the $D-$topology containing $\unl x$, we can find $\vepsi > 0$ such that 
$$
B_{\vepsi}^{D}(\unl x) \subseteq V
$$
Now choose $M$ such that $1/N < \vepsi$ by [[Archimedean Property]] and let
$$
U = B_{\vepsi}^{d_{1}}(x_{1}) \times \dots \times B_{\vepsi}^{d_{n}}(x_{n}) \times \text{whole spaces}
$$
