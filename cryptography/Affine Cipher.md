---
tags:
  - MATH_187A
---
# Method 
By encoding letters as $A = 0, Z = 25$, the [[Caesar Cipher]] of a shift $5$ can be seen as applying the transformation 
$$
E(x) = (x + 5) \bmod 26
$$
We can try other linear operators:
$$
E(x) = (ax + b) \bmod 26
$$
If we want this to be decryptable, $E(x)$ must be injective (and thus forces surjectivity). We are merely just applying an **affine transformation** to the letters.
## Example 1 
Show that 
$$
E(x) = (2x) \bmod 26
$$
loses information but 
$$
E(x) = (3x) \bmod 26
$$
does not. 

We see that $E(x = 13) = 26 \bmod 26 = 0$, so $N \to A$, but $E(x = 0) = 0$, and $A \to A$. However, for each $x \in \N_{\leq 25}$, we have a unique $E(x)$. 

# Theorem (Valid Affine Cipher)
More generally, 
$$
E(x) = (ax + b) \bmod 26
$$
gives a valid Affine Cipher if and only if $a$ is [[Modular Inversion|invertible]] $\bmod 26$, which by the [[Modular Inversion#Theorem (Modular Inversion)|modular inversion theorem]] happens if and only if $\gcd(a, 26) = 1$. 

# Definition (Decipher Function)
Write 
$$
E(x) = (ax + b) \bmod 26
$$
with $\gcd(a, 26) = 1$. Let $r$ be an inverse of $a \bmod 26$. We write $y = ax + b$ which yields
$$
\begin{aligned}
y &= ax + b \\
y - b &= ax \\ 
r(y - b) &= rax \\
ry - rb &= x & \text{since } r \text{ is an inverse of } a \bmod 26
\end{aligned}
$$
Thus, 
$$
D(y) = (ry - rb) \bmod 26
$$
So for each number $0 \dots 26$, the following are the only invertible numbers (along with their inverse):
$$
1,1
\quad
3,9
\quad
5,21
\quad
7,15
\quad
11,19
\quad
17,23
\quad
25,25
$$

## Example 2
What is the decryption function for 
$$
E(x) = 3x + 10
$$
So, 
$$
D(y) = (9y - 90) \bmod 26 = (9y - 14) \bmod 26
$$
# Theorem (Affine Ciphers are Finite)
How many different Affine Ciphers are there? Since we have $12$ possible keys for $a$. Then for $b$, we have $\{0, \dots, 25\}$ possible choices $(26)$. We get $12 \cdot 26 = 312$ affine ciphers. 

For alphabet size $n$, note that the following invertible numbers are **coprime** with $26$. We apply the same rule for alphabet size $n$. 