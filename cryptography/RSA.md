---
tags:
  - MATH_187A
---
# RSA
RSA is a public key cryptosystem based on the fact that multiplying large primes is easy, while factoring their product is hard.

## Key Generation
Choose distinct large primes $p$ and $q$, and let
$$
n = pq
$$
Then
$$
\phi(n) = (p-1)(q-1)
$$

Choose an integer $e$ such that
$$
\gcd(e, \phi(n)) = 1
$$
and choose $d$ so that
$$
ed \equiv 1 \pmod{\phi(n)}
$$

The public key is $(n, e)$ and the private key is $d$.

## Encryption and Decryption
If the plaintext is an integer $m$ with $0 \leq m < n$, then the ciphertext is
$$
c \equiv m^e \pmod n
$$

These modular powers are computed efficiently using [[Binary Exponentiation]].

To decrypt, compute
$$
m \equiv c^d \pmod n
$$

## Why Decryption Works
Since $ed \equiv 1 \pmod{\phi(n)}$, there is some integer $k$ such that
$$
ed = 1 + k\phi(n)
$$
If $\gcd(m, n) = 1$, then [[Euler's Phi Function#Theorem (Euler's Theorem)|Euler's theorem]] gives
$$
m^{\phi(n)} \equiv 1 \pmod n
$$
so
$$
m^{ed} = m^{1 + k\phi(n)} = m(m^{\phi(n)})^k \equiv m \pmod n
$$

## Security
The security idea is that the public key reveals $n = pq$, but recovering $\phi(n)$ or $d$ requires factoring $n$ into $p$ and $q$.
