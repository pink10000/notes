---
tags:
  - MATH_187A
---
# Elliptic Curve Diffie-Hellman
Elliptic Curve Diffie-Hellman (ECDH) is the elliptic curve analogue of [[Diffie-Hellman]].

## Public Data
Choose:
- a prime $p$,
- an elliptic curve $E$ that is nonsingular modulo $p$,
- a point $P$ on $E$ modulo $p$.

These play the role of $(p, g)$ in ordinary Diffie-Hellman.

## Key Exchange
Alice chooses a secret integer $k_a$ and sends
$$
k_a P
$$

Bob chooses a secret integer $k_b$ and sends
$$
k_b P
$$

Alice computes
$$
k_a(k_b P) = k_a k_b P
$$
and Bob computes
$$
k_b(k_a P) = k_a k_b P
$$

So both obtain the same shared secret point
$$
k_a k_b P
$$

## Security Idea
Given $P$ and $Q = rP$, recovering $r$ is the **elliptic curve discrete logarithm problem**, which is believed to be hard.
