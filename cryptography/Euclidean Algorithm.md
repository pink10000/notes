---
tags:
  - MATH_187A
---
This algorithm helps us determine the [[Greatest Common Divisor|GCD]] of larger numbers efficiently. 

# Method (Euclidean Algorithm)
We can best do this by example. Consider 
$$
\gcd(85, 19)
$$
So, we have that 
$$
\begin{aligned}
85 &= \unl{4} \cdot 19 + \unl 9 \\
19 &= \unl 2 \cdot 9 + \unl 1 \\
9 &= \unl 1 \cdot 9 + \unl 0
\end{aligned}
$$
which is when it terminates. Thus, the $\gcd$ is $1$. We essentially reuse the [[Greatest Common Divisor#Lemma (Remainder by GCD)|GCD lemma]]. This leads us to the following:

# Bezout's Identity
Using the [[Euclidean Algorithm]], we see that $\exists r,s \in \Z$ such that 
$$
\gcd(m, n) = mr + ns
$$
## Example 1
Find $r,s$ for 
$$
\gcd(54, 15)
$$
So, 
$$
\begin{aligned}
54 &= 3 \cdot 15 + 9 \\
15 &= 1 \cdot 9 + 6 \\
9 &= 1 \cdot 6 + 3 \\
6 &= 2 \cdot 3 + 0
\end{aligned}
$$
So, the $\gcd$ is $3$. Now, working backwards from our work for GCD,
$$
\begin{aligned}
3 &= 1 \cdot 9 + (-1) \cdot 6 \\
6 &= 1 \cdot 15 + (-1) \cdot 9 \\
9 &= 1 \cdot 54 + (-3) \cdot 15 \\ 
\end{aligned}
$$
So then, 
$$
\begin{aligned}
3 
&= 1 \cdot 9 + (-1)\left[ 1 \cdot 15 + (-1)\cdot 9  \right] \\
&= 2 \cdot 9 + (-1) \cdot 15 \\
&= 2 \cdot \left[ 1 \cdot 54 + (-3) \cdot 15 \right] + (-1) \cdot 15 \\
&= 2 \cdot 54 + (-7) \cdot 15
\end{aligned}
$$
and so our $r = 2, s = -7$. 
