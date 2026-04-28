---
tags:
  - MATH_187A
---
# Elliptic Curve Elgamal
Elliptic Curve Elgamal is an elliptic curve version of [[Elgamal]].

The main extra complication is that the plaintext must first be encoded as a point on the elliptic curve.

## Setup
Choose:
- a prime $p$,
- an elliptic curve $E$ that is nonsingular modulo $p$,
- a point $P$ on $E$ modulo $p$.

Bob chooses a secret integer $a$ and publishes
$$
Q = aP
$$

## Encryption
Suppose the message has been encoded as a point $M$ on the curve.

Alice chooses a random integer $k$ and computes
$$
\begin{aligned}
C_1 &= kP \\
C_2 &= M + kQ
\end{aligned}
$$

The ciphertext is the pair $(C_1, C_2)$.

## Decryption
Bob computes
$$
aC_1 = a(kP) = k(aP) = kQ
$$
and recovers the message by
$$
M = C_2 - aC_1
$$

## Security Idea
Security depends on the difficulty of the elliptic curve discrete logarithm problem.
