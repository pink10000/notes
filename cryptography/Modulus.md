---
tags:
  - MATH_187A
---
# Basic Rules
Let $a \equiv a' \bmod n$ and $b \equiv b' \mod n$. Then 
- $a + b \equiv a' + b' \bmod n$
- $ab \equiv a'b' \bmod n$
- $a^{r} \equiv (a')^{r}\bmod n$ where $r \in \Z_{>0}$. 

It is not generally true that $a^{r} \equiv a^{r'} \bmod n$. 

# Example 1
$$
417 \cdot 22 \bmod 10
$$
This becomes 
$$
7 \equiv 417 \bmod 10 
\quad\quad\quad
2 \equiv 22 \bmod 10
$$
such that 
$$
7 \cdot 2 \bmod 10 \equiv 4
$$
# Example 2 
$$
333333 + 666 \bmod 3
$$
becomes $0$, since both are divisible by $3$.

# Example 3 
$$
7^{202320232023}\bmod 6
$$
So, since $7 \bmod 6 \equiv 1$, we have that 
$$
1^{202320232023} \bmod 6 \equiv 1
$$
# Example 4 (2.5.9)
Fix positive integers $k,n$. Suppose $a, a'$ are integers such that $a \equiv a' \bmod n$. It is not true in general that $k^{a} \equiv k^{a'} \bmod n$. Show is by example. 

Let $n = 5, k = 3, a' = 2, a = 17$. Then 
$$
17 \equiv 2 \bmod 5
$$
But then as $3$ is periodic as $3, 4, 2, 1$, we have that 
$$
3^{17} \bmod 5 \equiv 3
$$
And 
$$
3^{2} \bmod 5 \equiv 4
$$
and so 
$$
3 \neq 4
$$
We are done. 

# Example 5 (2.6.15)
Explain why $2$ is not invertible $\bmod 4$. 

Suppose by contradiction it is. Thus, $\exists x \in \Z$ where $2x \equiv 1 \bmod 4$. But when $x$ is even ($x = 2k$), then $4k \equiv 0 \bmod 4$, a contradiction. If is odd where $x = 2k + 1$, Then $4k + 2 \equiv 0 + 2 \bmod 4$ which is not $1$, another contradiction. 