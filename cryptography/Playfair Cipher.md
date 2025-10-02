---
tags:
  - MATH_187A
---
# Method
1. Generate a $5 \times 5$ grid using a keyword. Combine `I` and `J` into a single cell (treat them as the same letter).
	1. The unique letters of the keyword are placed first, row by row from top left to bottom right.
	2. Complete the matrix.
2. Remove all non-alphabet characters and capitalize everything
3. Replace all instances of `J` with `I`. 
4. Group the letters into pairs
5. If there are any pairs where both letters are the same, insert the letter `X` between the two letters of that pair and then regroup into pairs. 
6. If there is an unpaired letter at the end, insert the letter `X` after it. 
7. For each pair, if it has the same row, replace with the letters immediately to the right of it. If it is the same column, replace with letters immediately below it. If the pair is a "rectangle", then we select the opposite row letters.

# Examples
Keyword: `ALPHHABET`
```
A L P H B
E T C D F
G I K M N
O Q R S U
V W X Y Z
```
Let plaintext be `JELLY`. 
```
3. JELLY -> IELLY 
4. -> IE LL Y
5. -> IE LX LY
6. -> IE LX LY
7. -> GT PW HW
```

Now with the same matrix, let the plaintext be
```
HIDDEN JEWELS IN THE TREES
```
Then
```
HI DX DE NI EW EL SI NT HE TR EX ES
```
Applying step $7,8$ we get 
```
HI -> LM
DX -> CY
DE -> FT
NI -> GK
EW -> TV
EL -> TA
SI -> QM
NT -> IF
HE -> AD
TR -> CQ
EX -> CV
ES -> DO
```
