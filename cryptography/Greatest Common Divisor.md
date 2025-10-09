---
tags:
  - MATH_187A
aliases:
  - GCD
  - GCDs
---
# Definition (GCD)
The **greatest common divisor** of two integers $b,c$ is denoted as $\gcd(b,c)$, the largest integer which divides both $b$ and $c$. 

## Lemma (Remainder by GCD)
In general, 
$$
\gcd(b, bq + r) = \gcd(b, r)
$$
for any integers $q, r$. This observation leads us the [[Euclidean Algorithm]].

## Example 1:
$$
\gcd(0, a)
$$
Since every number divides $0$, then this $\gcd$ of just $a$ is $a$. 