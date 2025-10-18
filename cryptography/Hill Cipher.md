---
tags:
  - MATH_187A
---
We first start with basic facts about matrices. 
- For $M \in \Z^{2 \times 2}, \det M = ad - bc$ if $M = [a, b; c, d]$. 
- $M$ is [[Modular Inversion#Theorem (Modular Inversion)|invertible]] $\bmod 26 \iff \gcd(\det M, 26) = 1$
- The inverse of $M \bmod 26$ is its regular inverse $\cdot r$. Indeed:
  $$
	M^{-1} = \begin{bmatrix}
	rd & -rb \\ -rc & ra
	\end{bmatrix}
	$$
# Example 1 
Which of the following matrices are invertible $\bmod 26$?
$$
\begin{bmatrix} 7 & 5 \\ 3 & 3 \end{bmatrix} \quad\quad \begin{bmatrix} 8 & 1 \\ 3 & 2 \end{bmatrix} \quad\quad \begin{bmatrix} 4 & 2 \\ 1 & 2 \end{bmatrix} \quad\quad \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}
$$
The determinants in order are $6, 13, 6, 5$. Then, using [[Affine Cipher#Definition (Decipher Function)]] we see the only invertible number is $5$.

# Method (Hill Cipher)
Our key is an invertible $2 \times 2$ matrix. 
1. Break [[Text#Definition (Plaintext, Ciphertext)|plaintext]] into pairs of $2$ letters
2. Encode the pair of $2$ letters as a $2 \times 1$ column vector
3. Encrypt by multiplying the Key on the left
4. Use alphabet-number correspondence to get [[Text|ciphertext]]. 
5. Decrypt is the same but with the inverse matrix.

## Example 2 
Use a Hill Cipher with key 
$$
A = \begin{bmatrix} 4 & 3 \\ 1 & 2 \\ \end{bmatrix}
$$
to encrypt the word `AREA`. So, `AREA -> AR EA`, which becomes 
$$
A
\begin{bmatrix}
0 \\ 17 
\end{bmatrix}
= 
\begin{bmatrix}
51 \\ 34
\end{bmatrix}
= B, I
$$
and so on. 

## Example 3
Decryption is done by multiplying by $A^{-1}$. Using the same $A$, decrypt `CRZX`. 

So, $\det A = 5$. Then the inverse modulo $26$ is $21$. Then the inverse is 
$$
A^{-1} = 
\begin{bmatrix}
21 \cdot 2 \equiv 16 \bmod 26 & 21 \cdot -3 \equiv 15 \bmod 26 \\ 
21 \cdot -1 \equiv 5 \bmod 26 & 21 \cdot 4 \equiv 6 \bmod 26 \\
\end{bmatrix}
$$
and so 
$$
A^{-1} 
\begin{bmatrix}
2 \\ 17 
\end{bmatrix}
=
\begin{bmatrix}
1 \\ 8 
\end{bmatrix}
$$
and so on. This is `BI + RD` 

## Lemma (Valid Hill Cipher)
A Hill Cipher key is valid iff its determinant is invertible modulo $n$, where $n$ is the size of the alphabet. 

Otherwise, it would not be decryptable. 