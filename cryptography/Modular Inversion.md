---
tags:
  - MATH_187A
---
In modular arithmetic, addition, subtraction, and multiplication are all easy. Division
is subtle. 

# Theorem (Modular Inversion)
The number $a$ is **invertible** $\bmod n$ if and only if $\gcd(a, n) = 1$. In this case, an inverse of $a$ is the [[Euclidean Algorithm#Bezout's Identity|Bezout coefficient]] for $a$ is the identity
$$
ra + sn = 1
$$
Or that $r$ is *an* inverse of $a \bmod n$. 

## Example 1
Which of the following are invertible $\bmod 210$?
$$
3 \quad\quad\quad 4 \quad\quad\quad 5
$$
So, we can see that $\gcd(3, 210) = 3$, so it cannot be invertible. Then $\gcd(4, 210) = 2$ since both are even. Finally, $\gcd(5, 210) = 5$. None are invertible. 

## Example 2
Find an inverse of $54 \bmod 131$ if possible. So, by the [[Euclidean Algorithm]],
$$
\begin{aligned}
131 &= 2 \cdot 54 + 23 \\
54 &= 2 \cdot 23 + 8 \\
23 &= 2 \cdot 8 + 7 \\
8 &= 1 \cdot 7 + \color{red}1 \\
\end{aligned}
$$
And so the remainder is $1$, and so $\gcd(54, 131) = 1$. Now, using Bezout to find $r$, 
$$
\begin{aligned}
1 &= 1 \cdot 8 + (-1) \cdot 7 \\
7 &= 1 \cdot 23 + (-2) \cdot 8 \\
8 &= 1 \cdot 54 + (-2) \cdot 23 \\
23 &= 1 \cdot 131 + (-2) \cdot 54 \\
\end{aligned}
$$
Then,
$$
\begin{aligned}
1 
&= 1 \cdot 8 + (-1) \cdot 7  \\
&= 1 \cdot 54 + (-2) \cdot 23 + (-1) \cdot 23 + 2 \cdot 8 \\
&= 1 \cdot 54 + (-3) \cdot 23 + 2 \cdot 54 + (-4) \cdot 23 \\
&= 3 \cdot 54 + (-7) \cdot 23 \\
&= 3 \cdot 54 + (-7) \cdot 131 + 14 \cdot 54 \\
&= 17 \cdot 54 + (-7) \cdot 131
\end{aligned}
$$
Thus, $r = 17$, which is the inverse. 
