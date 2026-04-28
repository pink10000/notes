---
tags:
  - MATH_187A
---
# Definition (Order Modulo $n$)
If $\gcd(a, n) = 1$, the **order** of $a$ modulo $n$, denoted $\operatorname{ord}_{n}(a)$, is the smallest positive integer $r$ such that
$$
a^r \equiv 1 \pmod n
$$

By [[Euler's Phi Function#Theorem (Euler's Theorem)|Euler's theorem]], such an $r$ exists whenever $\gcd(a, n) = 1$.

# Theorem
If $r = \operatorname{ord}_{n}(a)$, then
$$
a^k \equiv 1 \pmod n \iff r \mid k
$$

In particular, the order divides any exponent that sends $a$ back to $1$ modulo $n$.

# Primitive Roots
An integer $g$ is a **primitive root modulo $n$** if
$$
\operatorname{ord}_{n}(g) = \phi(n)
$$

If $p$ is prime and $g$ is a primitive root modulo $p$, then
$$
g, g^2, \dotsc, g^{p-1}
$$
run through all nonzero residue classes modulo $p$.

# Discrete Logarithm
Fix a primitive root $g$ modulo a prime $p$. For each nonzero residue class $j \pmod p$, there is a unique integer $i$ with $1 \leq i \leq p-1$ such that
$$
g^i \equiv j \pmod p
$$
This exponent $i$ is the **discrete logarithm** of $j$ base $g$, written
$$
\log_g(j \bmod p) = i
$$

Computing discrete logarithms is believed to be hard in general.

# Order of a Power
If $\operatorname{ord}_{n}(a) = r$, then
$$
\operatorname{ord}_{n}(a^d) = \frac{r}{\gcd(d, r)}
$$

This is useful in the analysis of [[Elgamal]] and [[Diffie-Hellman]].
