---
tags:
  - MATH_187A
---
# Definition (Euler's Phi Function)
For a positive integer $n$, let $\phi(n)$ denote the number of integers $r$ with $0 \leq r < n$ and $\gcd(r, n) = 1$.

Equivalently, $\phi(n)$ counts the invertible residue classes modulo $n$.

## Basic Facts
If $p$ is prime, then
$$
\phi(p) = p - 1
$$
since every nonzero residue modulo $p$ is relatively prime to $p$.

More generally,
$$
\phi(p^{e}) = p^{e} - p^{e-1} = p^{e-1}(p-1)
$$
for every prime $p$ and integer $e \geq 1$.

If $\gcd(m, n) = 1$, then
$$
\phi(mn) = \phi(m)\phi(n)
$$
so $\phi$ is multiplicative on relatively prime inputs.

Combining this with the prime factorization of $n$, we get
$$
\phi(n) = n \prod_{p \mid n}\left(1 - \frac{1}{p}\right)
$$
where the product is over the distinct prime divisors of $n$.

# Theorem (Euler's Theorem)
If $\gcd(a, n) = 1$, then
$$
a^{\phi(n)} \equiv 1 \pmod n
$$

This generalizes [[Prime Number#Example 2|Fermat's little theorem]] when $n$ is prime.

## Example
Since $\phi(15) = 15(1 - 1/3)(1 - 1/5) = 8$, any integer $a$ relatively prime to $15$ satisfies
$$
a^8 \equiv 1 \pmod{15}
$$
