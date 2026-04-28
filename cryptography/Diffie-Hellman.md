---
tags:
  - MATH_187A
---
# Diffie-Hellman
Diffie-Hellman is a key exchange protocol based on the hardness of the [[Order#Discrete Logarithm|discrete logarithm problem]].

## Public Data
Choose a prime $p$ and a primitive root $g$ modulo $p$.

## Key Exchange
Alice chooses a secret integer $a$ and sends
$$
g^a \pmod p
$$

Bob chooses a secret integer $b$ and sends
$$
g^b \pmod p
$$

The modular exponentiations in this protocol are carried out using [[Binary Exponentiation]].

Alice computes
$$
(g^b)^a \equiv g^{ab} \pmod p
$$
and Bob computes
$$
(g^a)^b \equiv g^{ab} \pmod p
$$

So both obtain the shared secret
$$
g^{ab} \pmod p
$$

## Security Idea
An eavesdropper sees $g^a$ and $g^b$, but computing $g^{ab}$ from this information is believed to be hard.

This is called the **computational Diffie-Hellman problem**.
