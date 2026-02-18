---
tags:
  - MATH_187A
---
# Method
Suppose we have a keyword `EMAIL`. 

1. Alphabetize keyword 
```
EMAIL --> AEILM
```
2. Calculate position of each letter in original keyword. So `A` is in position $3$ and thus $3$ is the first digit
```
A -> 3
E -> 1
I -> 4
L -> 5
M -> 2
```
3. We get $31452$. 

If we want to encrypt 
```
MEET ME AT NOON
```

Then since `len("EMAIL") = 5`, we encode this as 
```
MEETM
EATNO
ONQXJ
```
where `QXJ`is junk to fill the last line. This is then encrypted as 
```
EMTME
TENOA
QOXJN
```
by using $31452$. It tells us to use
- 3rd letter, `E`
- 1st letter, `M`
- 4th, `T`
- 5th, `M`
- 2nd, `E`

giving us the [[Text#Definition (Plaintext, Ciphertext)|ciphertext]]
```
EMTMETENOAQOXJN
```

# Examples
```
Keyword: Zeus
Plaintext: MTSQAGXY

ZEUS -> ESUZ -> 2431

MTSQ -> TQSM
AGXY -> GYXA

Corresponding Ciphertext: TQSMGYXA (B)
```