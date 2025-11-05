---
tags:
  - MATH_187A
---
# Theorem (Prime Factorization Bound)
Any composite integer $n \geq 2$ must have a prime factor $p$ such that $p \leq \sqrt{n}$. 

Proof: 

Let $n$ be composite. If all prime factors are $p > \sqrt{n}$, then $\exists b$ where $pb = n$. But then if $p > \sqrt{n}$, then $pb > b\sqrt{n} \iff n > b \sqrt{n} \iff \sqrt{n} > b$. But then the prime factors of $b$ must be smaller than $\sqrt{n}$, which are factors of $n$, a contradiction.

## Example 1
If $701$ prime? 

Proof:
If $701$ is composite, then it must have some prime factor under $\sqrt{701} \approx 26.5 > 26$. Then we can consider all primes under $\sqrt{701}$:
$$
2, 3, 5, 7, 11, 13, 17, 19, 23
$$
Fortunately, these are not divisible. Thus $701$ is not composite and prime. 

# Facts
- There are infinite primes.
- Primes are scarce 
- There are infinitely many pairs of primes such that $|p - q| \leq 246$. 
- Prime factorization is hard

# Euler Totient Function
For $n \in \Z_{+}$, let $\phi(n)$ denote the number of integers $r < n$ with $\gcd(n, r) = 1$. We also see that 
$$
\phi(n) = n \prod_{p|n}\left(1 - \frac{1}{p}  \right)
$$
Then $\phi(mn) = \phi(m)\phi(n)$. Proof by Chinese Remainder Theorem. 

## Example 2 
Is $\phi(2n) = \phi(n)$ true for any $n$?

Proof: By above, $\phi(2n) = \phi(2) \cdot \phi(n)$. But then $\phi(2) = 1$, so this is true. 
