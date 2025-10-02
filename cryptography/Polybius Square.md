---
tags:
  - MATH_187A
---
# Method
Write all $26$ letters and $10$ numbers randomly in a $6 \times 6$ grid with columns and rows indexed by the word `ADFGVX`.
```
  A D F G V X
A N A 1 C 3 H
D 8 T B 2 0 M
F E 5 W R P D
G 4 F 6 G 7 I
V 9 J 0 K L Q
X S U V X Y Z
```
Then, for some [[Text|plaintext]], replace each letter with the $(\text{row}, \text{ column})$ index where it is placed. So 
```
Plaintext: WAR
W -> FF
A -> AD
R -> FG

Ciphertext: FFADFG
```

# Examples
| .     | **A** | **D** | **F** | **G** | **V** | **X** |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **A** | 2     | 1     | J     | U     | N     | E     |
| **D** | 1     | 7     | 8     | D     | C     | M     |
| **F** | B     | R     | T     | V     | W     | X     |
| **G** | A     | F     | 3     | G     | H     | 4     |
| **V** | I     | 5     | K     | L     | 6     | O     |
| **X** | P     | Q     | 9     | S     | Y     | Z     |
Let plaintext be `STARRY DYNAMO`. Then, 
```
S -> XG
T -> FF
A -> GA
R -> FD
R -> FD
Y -> XV

D -> DG
Y -> XV
N -> AV
A -> GA
M -> DX
O -> VX
```
which is our ciphertext. 