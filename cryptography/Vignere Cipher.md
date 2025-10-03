---
tags:
  - MATH_187A
---
This is like the [[Caesar Cipher]], but instead of adding the same shift to each letter position, we add a variable one. 
# Method
1. Convert keyword to the position in the alphabet. We index by $0$, so `A` is $0$. 
2. Add it to the ciphertext and [[Modulus|mod 26]].

For decryption, we subtract.

# Example 1
Keyword: `DOG`
Plaintext: `SWIM`

So, `DOG -> 3 14 6` and `SWIM -> 18 22 8 12`, so 
```
18 + 3  = 21 
22 + 14 = 36 -> 14
8  + 6  = 14
12 + 3  = 15
```

# Example 2 
Keyword: `AND`
Plaintext: `Six Meals`

```
A = 0
N = 13
D = 3
```
So, 
```
S -> 18 + 0  = 18
I -> 8  + 13 = 21
X -> 23 + 3  = 26 mod> 0
M -> 12 + 0  = 12
E -> 4  + 13 = 17
A -> 0  + 3  = 3
L -> 11 + 0  = 11
S -> 18 + 13 = 31 mod> 5
```
And so the ciphertext is `SVAMRDLF`.
