---
tags:
  - MATH_187A
---
# Elliptic Curves Mod a Prime
Let
$$
E: y^2 = x^3 + ax + b
$$
where $a$ and $b$ are integers, and let $p$ be a prime.

We say that $E$ is **nonsingular modulo $p$** if its discriminant
$$
-16(4a^3 + 27b^2)
$$
is not divisible by $p$.

Then we can consider the solutions of the equation modulo $p$, together with the point at infinity $O$.

# Group Law
The same addition law from [[Elliptic Curves Over the Reals]] still works modulo $p$, except that slopes are computed using modular inverses.

So the set of points on $E$ modulo $p$ forms a finite abelian group.

# Order of a Point
If $P$ is a point on $E$ modulo $p$, then the order of $P$, denoted $\operatorname{ord}_{E,p}(P)$, is the smallest positive integer $r$ such that
$$
rP = O
$$

Since there are only finitely many points modulo $p$, every point has finite order.

# Divisibility Property
If
$$
rP = O
$$
then
$$
\operatorname{ord}_{E,p}(P) \mid r
$$

This is the elliptic curve analogue of the usual divisibility property of order in modular arithmetic.
