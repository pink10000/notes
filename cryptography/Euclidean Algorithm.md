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
19 &= \unl 2 \cdot 9 + \color{red}\unl 1 \\
9 &= \unl 1 \cdot 9 + \unl 0
\end{aligned}
$$
which is when it terminates. Thus, the $\gcd$ is $1$. We essentially reuse the [[Greatest Common Divisor#Lemma (Remainder by GCD)|GCD lemma]]. This leads us to the following:

## Example 1
How many divisions do we need until we see a remainder of $0$ when we use the algorithm to compute 
$$
\gcd(150, 90)
$$
So,
$$
\begin{aligned}
150 &= 1 \cdot 90 + 60 \\ 
90 &= 1 \cdot 60 + 30 \\
60 &= 2 \cdot 30 + 0 \\
\end{aligned}
$$
So, $3$ total divisions. Our $\gcd(150, 90) = 30$. 

# Bezout's Identity
Using the [[Euclidean Algorithm]], we see that $\exists r,s \in \Z$ such that 
$$
\gcd(m, n) = mr + ns
$$
## Example 2
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

## Example 3 
Find Bezout  coefficients for $\gcd(150, 90)$. 

So, from [[#Example 1]], we have  
$$
\begin{aligned}
30 &= (-1) \cdot 60 + 1 \cdot 90 \\
60 &= (-1) \cdot 90 + 1 \cdot 150 \\ 
\end{aligned}
$$
Then,
$$
\begin{aligned}
30 
&= (-1) \cdot 60 + 1 \cdot 90 \\
&= -[(-1) \cdot 90 + 1 \cdot 150] + 1 \cdot 90 \\
&= 2 \cdot 90 + (-1) \cdot 150
\end{aligned}
$$
and so $r = 2, s = -1$. 