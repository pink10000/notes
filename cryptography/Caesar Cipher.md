---
tags:
  - MATH_187A
---
Also called **Shift Cipher**.
# Method
A **Caesar Cipher** will shift the alphabet $n$ times. For example,
```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
```
is a shift of $n = 1$. Thus, 
```
ZOOLOGY -> APPMPHZ
```

# Complexity
Since the shift is circular with period $26$, there are only $26$ possible shifts (including the identity, the $0$ shift). Let $n = 30$. Then we are shifting only $30 \bmod 26 \equiv 4$ times. 
