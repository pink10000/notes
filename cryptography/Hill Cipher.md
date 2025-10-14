---
tags:
  - MATH_187A
---
We first start with basic facts about matrices. 
- $\det M$ where $M \in \Z_{2 \times 2} = ad - bc$ if $M = [a, b; c, d]$. 
- $M$ is [[Modular Inversion#Theorem (Modular Inversion)|invertible]] $\bmod 26 \iff \gcd(\det M, 26) = 1$
- The inverse of $M \bmod 26$ is its regular inverse $\cdot r$. Indeed:
  $$
	M^{-1} = \begin{bmatrix}
	rd & -rb \\ -rc & ra
	\end{bmatrix}
	$$

# Method (Hill Cipher)
Our key is an invertible $2 \times 2$ matrix. 
1. Break [[Text#Definition (Plaintext, Ciphertext)|plaintext]] into pairs of $2$ letters
2. Encode the pair of $2$ letters as a $2 \times 1$ column vector
3. Encrypt by multiplying the Key on the left
4. Use alphabet-number correspondence to get [[Text|ciphertext]]. 
5. Decrypt is the same but with the inverse matrix.