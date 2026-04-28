---
tags:
  - MATH_187A
---
# Binary Exponentiation
Binary exponentiation is a fast way to compute powers such as $a^n$ or $a^n \bmod m$.

The main idea is to write the exponent in base $2$:
$$
n = b_0 + 2b_1 + 2^2 b_2 + \cdots + 2^r b_r
$$
where each $b_i \in \{0,1\}$. Then
$$
a^n = a^{b_0}(a^2)^{b_1}(a^4)^{b_2} \cdots (a^{2^r})^{b_r}
$$

So instead of multiplying by $a$ a total of $n$ times, we repeatedly square and only multiply the powers whose binary digits are $1$.

## Modular Version
To compute $a^n \bmod m$, reduce modulo $m$ after each squaring and multiplication. This keeps the numbers small:
$$
\begin{aligned}
a^2 &\equiv a \cdot a \pmod m \\
a^4 &\equiv (a^2)^2 \pmod m \\
a^8 &\equiv (a^4)^2 \pmod m
\end{aligned}
$$

This is the standard method used in RSA, Elgamal, Diffie-Hellman, and Miller-Rabin.

## Example
Compute $3^{13}$:
$$
13 = 8 + 4 + 1
$$
so
$$
3^{13} = 3^8 \cdot 3^4 \cdot 3
$$
and the powers $3, 3^2, 3^4, 3^8$ can be built by repeated squaring.
