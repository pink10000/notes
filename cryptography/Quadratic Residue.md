---
tags:
  - MATH_187A
---
# Definition (Quadratic Residue)
An integer $a$ is a **quadratic residue modulo $n$** if there exists an integer $x$ such that
$$
x^2 \equiv a \pmod n
$$

If no such $x$ exists, then $a$ is a quadratic nonresidue modulo $n$.

## Legendre Symbol
If $p$ is an odd prime, the **Legendre symbol** is defined by
$$
\left(\frac{a}{p}\right)
=
\begin{cases}
0 & \text{if } p \mid a \\
1 & \text{if } a \text{ is a quadratic residue mod } p \\
-1 & \text{if } a \text{ is a quadratic nonresidue mod } p
\end{cases}
$$

# Theorem (Euler's Criterion)
If $p$ is an odd prime and $p \nmid a$, then
$$
\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p
$$

Since the Legendre symbol is always $\pm 1$ in this case, this means
$$
a^{(p-1)/2} \equiv
\begin{cases}
1 \pmod p & \text{if } a \text{ is a quadratic residue mod } p \\
-1 \pmod p & \text{if } a \text{ is a quadratic nonresidue mod } p
\end{cases}
$$

This is useful for deciding whether a number is a square modulo a prime.
