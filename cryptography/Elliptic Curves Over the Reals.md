---
tags:
  - MATH_187A
---
# Elliptic Curves Over the Reals
An elliptic curve over the reals is given by an equation
$$
y^2 = x^3 + ax + b
$$
where
$$
-16(4a^3 + 27b^2) \neq 0
$$

The condition on the discriminant says the curve is **nonsingular**, so it has no cusps or self-intersections.

# Point at Infinity
We adjoin one extra point, denoted $O$, called the **point at infinity**.

# Group Law
The points on the curve, together with $O$, form an [[Group#Definition (Abelian Group)|abelian group]].

## Geometric Addition
If $P$ and $Q$ are points on the curve:
- Draw the line through $P$ and $Q$ if $P \neq Q$.
- If $P = Q$, draw the tangent line at $P$.
- This line meets the curve at a third point.
- Reflect that third point across the $x$-axis.

The reflected point is defined to be $P + Q$.

## Identity and Inverses
- The identity element is $O$.
- If $P = (x, y)$, then
$$
-P = (x, -y)
$$
so $P + (-P) = O$.

# Order of a Point
If $P$ is a point on an elliptic curve $E$, the **order** of $P$ is the smallest positive integer $r$ such that
$$
rP = O
$$
if such an $r$ exists. Otherwise, the order is $\infty$.

Over the real numbers, most points have infinite order.
