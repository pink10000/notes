---
tags:
  - MATH_187A
---
# Elgamal
The Elgamal cryptosystem is a public key encryption scheme based on the difficulty of the [[Order#Discrete Logarithm|discrete logarithm problem]].

## Setup
Choose a prime $p$ and a primitive root $g$ modulo $p$.

Bob chooses a secret key $a$ and publishes
$$
A \equiv g^a \pmod p
$$

So the public key is $(p, g, A)$ and the private key is $a$.

## Encryption
To send a message $m$ modulo $p$, Alice chooses a random integer $k$ and computes
$$
\begin{aligned}
c_1 &\equiv g^k \pmod p \\
c_2 &\equiv mA^k \pmod p
\end{aligned}
$$

These powers modulo $p$ are computed efficiently using [[Binary Exponentiation]].

The ciphertext is the pair $(c_1, c_2)$.

## Decryption
Bob computes
$$
c_1^a \equiv (g^k)^a = g^{ka} \equiv A^k \pmod p
$$
and then recovers the plaintext by
$$
m \equiv c_2 (c_1^a)^{-1} \pmod p
$$

## Security Idea
An attacker sees $g^a$ and $g^k$, but recovering $a$ or $k$ from those values requires solving a discrete logarithm problem.
