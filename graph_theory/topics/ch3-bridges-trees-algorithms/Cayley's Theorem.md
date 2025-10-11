---
tags:
  - MATH_154
---
How many [[Tree|trees]] on $n$ vertices are there? Given vertices labeled $1$ to $n$, how many ways can we add edges to make a tree?

- For $n=1$, there's only one tree. 
- For $n = 2$, there's still only one tree. 
- For $n = 3$, we have multiple possible [[Graph|graphs]], but we can only have one tree. If the vertices are labeled, then there are $3$ labeled trees. 
- For $n = 4$, we can get:
  ```mermaid
		  graph
			  1((1)) o--o 2((2));
			  1 o--o 3((3));
			  1 o--o 4((4));
	```
	or 
  ```mermaid
	  graph LR;
		  1((1)) o--o 2((2));
		  2 o--o 3((3));
		  3 o--o 4((4));
	```
  If the trees are labeled, we get $16$ total trees. 
- For $n = 5$, see [[Tree#Trees with $5$ Vertices|trees with 5 vertices]]. If labeled, there are $125$. 
- For $n = 6$, we have $1296$. 

In general, the formula is $n^{n-2}$. This is known as Cayley's Theorem.

# Cayley's Theorem
The number of labeled trees on $1,2, \dots, n$ vertices is $n^{n-2}$.

Proof: 
We want to find a bijection from 
$$
\{ \text{labeled trees on } n\}
\longleftrightarrow
\{ \text{ordered lists of } n - 2 \text{ numbers from } 1, 2, \dots, n  \}
$$
Start with a tree $T$. Repeatedly, we find the [[Tree#Definition (Leaf)|leaf]] with the smallest label. We add that label to $v$'s neighbors, and then remove $v$ from $T$. We do this until $T$ has only $2$ vertices. 

# Lemma (Counting Labeled Leaves)
$$
\{\text{leaves of original tree}\} 
= 
\{\text{number of } 1, \dots, n \text{ not in my list}\}
$$
Proof:
Given a leaf, 
```mermaid
graph LR;
	m((m)) o--o k((k));
```
We say $k$ can only be a leaf when at least one of its neighbors can be removed. But then this means $k$ will be added to the list. 

Given a list of numbers, maintain a list $V$ of remaining vertices, initially $1$ to $n$. Then repeatedly, find the smallest element in $V$ not in $L$. Connect it to the first element of $L$. Remove the element of $V$ and element of $L$. We repeat until $L$ is empty. Then connect remaining elements of $V$. 