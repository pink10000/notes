---
tags:
  - MATH_187A
---
# Method
Choose a random permutation of the $26$ letters, this is the alphabet mapping. For example,
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
PVJWDCHTSKZFNQEYORIGAUMLXB
```
means that `A -> P, B -> V` and so on. To decrypt, simply read the table backwards. 


# Complexity 
In particular, since we can pick any permutation of letters, there are 
$$
26! \approx 4.033 \cdot 10^{26} \text{ permutations}
$$
possible Simple Substitution Ciphers. 