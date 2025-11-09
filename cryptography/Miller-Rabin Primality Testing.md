---
tags:
  - MATH_187A
---
# Definition (Miller-Rabin Primality Testing)
Suppose $n$ is a positive odd integer and write $n - 1 = 2^{s}d$ for some positive integer $s$ and an odd number $d$. Suppose $a$ is an integer between $1$ and $n - 1$. If $n$ is prime, then one of the following congruence relations most hold true:
$$
\begin{aligned}
a^{d} &\equiv 1 \bmod n  \\
a^{d} &\equiv -1 \bmod n \\
a^{2d} &\equiv -1 \bmod n \\
a^{2^{2}d} &\equiv -1 \bmod n \\ 
&\vdots \\
a^{2^{s-1}d} &\equiv -1 \bmod n \\
\end{aligned}
$$
If $n$ is not a strong probable [[Prime Number|prime]] to base $a$, then $a$ is called a witness for the compositeness of $n$, or a Miller-Rabin witness for $n$. 

If $n = 2$, it is a prime. Otherwise, if $n$ is even, output not a prime. Otherwise, we repeat for $k$total random bases $a$ for $2 \leq a \leq n - 2$. If we end without showing that $a$ is a witness, then $n$ is a prime. 

If the number of times this is repeated is $k > 1$, the probability of being a prime is $\leq 1/4^{k}$. 
## Example 1 
Check that $221$ is a strong probable prime to the base $174$. 
1. $n = 221, a = 174$. 
2. $n - 1 = 220$
3. $220 = 2^{2} \cdot 55$
4. So, $s = 2, d = 55$.
5. Now, we check for $0 \leq r \leq s - 1$, so $r = 0,1$. 
	1. $a^{d} \equiv 1 \bmod 221 \to 174^{55} \equiv 1 \bmod 221$ 
	2. $a^{2^{0}d} \equiv -1 \bmod n \to 174^{55} \equiv -1 \bmod 221$
	3. $a^{2^{1}d} \equiv -1 \bmod n \to 174^{110} \equiv -1 \bmod 221$
6. Then, calculate
$$
\begin{aligned}
174^{55} \bmod 221 & \to 47 \bmod 221
\end{aligned}
$$
7. This is not $1$ or $-1$. Both fail.
8. Check 
$$
174^{110} \bmod 221 = (174^{55})^{2} \bmod 221 = 47^{2} \bmod 221 \to -1 \bmod 221
$$
This is true. This $221$ is a strong probable prime. 

## Example 2 
Check that $2$ is a witness for $221$. 
1. $n = 221, a = 2$.
2. $n - 1 = 220$
3. Then $220 = 2^{2} \cdot 55$
4. $s = 2, d = 55$
5. Check $0 \leq r \leq s -1$, and $r = 0,1$
	1. $a^{d} \equiv 1 \bmod 221 \to 2^{55} \equiv 1 \bmod 221$ 
	2. $a^{2^{0}d} \equiv -1 \bmod 221 \to 2^{55} \equiv -1 \bmod 221$
	3. $a^{2^{1}}d \equiv -1 \bmod 221 \to 2^{110} \equiv -1 \bmod 221$
6. Then, calculate 
	1. $2^{55} \equiv 128 \bmod 221$. Both conditions fail. 
	2. $2^{110} \equiv 30 \bmod 221$. 
7. Since both fail, $2$ is a witness for $221$'s composite. 