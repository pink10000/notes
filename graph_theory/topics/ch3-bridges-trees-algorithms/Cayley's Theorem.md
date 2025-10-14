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

**Tree $\to$ List:** We repeatedly remove the smallest index [[Tree#Definition (Leaf)|leaf]] and then add its neighbor to a list until the tree only has $2$ vertices left. 

**List $\to$ Tree**: Let $L$ be the list we want to convert. Let $V = \{1, \dots, n\}$ be a list of $n$ numbers. Repeatedly, we find the smallest element $v$ of $V$ not in $L$. Connect $v$ to the first element of $L$, and remove $v$ in $L$ and $V$. We do this until $L$ is empty. The remaining elements of $V$ get connected. 

```
Try:
L = [7, 2, 8, 6, 3, 1, 7]
V = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note that L has two less elements. Recall the formula!
```

We want to claim that by induction on $|S|$, that this is a bijection.  In particular, the base case $n = 2$ is boring. $S = \{x, y\}$, and we only have one tree where $x$ is connected to $y$. Now, assume $|S| = n$. What if $|S| = n + 1$?

Suppose we had tree $T$ with smallest leaf $\ell$. We could partition a tree as 
$$
\ell -(_{x}T')
$$
where $x$ is $\ell$'s only neighboring vertex. Then our list would be $x \circ \list(T')$. Since $\ell$ is the smallest leaf of $S$ not in our tree, then in our **List $\to$ Tree** algorithm, then we have $S - \{\ell\}$ in the next iteration. This also produces $\list(T')$. But then this is our inductive hypothesis, the exact $T$ we started with. 

This tells us our algorithms are inverses in one direction. 

Now, if $\ell$ is our smallest element of $S$ not in $L$, then $x$ is the first element of $L$, and $L = x \circ L'$ where is our list. Thus, we need to show how 
$$
(*)
\quad\quad\quad
S - \{\ell\} \circ L' \to T'
$$
that our list decomposes to tree $T'$. 
1. I claim our smallest leaf is $\ell$. 
2. I claim the proceeding [[#Lemma (Counting Labeled Leaves)]], which we prove after this. 
Then following **Tree $\to$ List** algorithm, with claim $(1)$, then by the inductive hypothesis, 
$$
\list(T') = L'
$$
Essentially, we turn our tree back to our list that we started with. Indeed, by claim $(2)$, we have $(*)$.
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
We say $k$ can only be a leaf when at least one of its neighbors can be removed. This means $k$ will be added to the list. Therefore, it will be added $\deg(k) - 1$ times. But as leaves have degree $1$, they will appear in the list $1 - 1 = 0$ times. 

# Generalized Cayley's Theorem
The number of [[Tree#Definition (Spanning Tree)|spanning trees]] of $K_{n}$ is equal to $n^{n-2}$.  


# Matrix-Tree Theorem
The number spanning trees of $G$ is equal to $\det(M')$ where $M'$ is defined as
$$
M = 
\begin{bmatrix}
M_{ii} = \deg(v_{i}) \\ \\
M_{ij} = 
\begin{cases}  
-1 & v_{i} \text{ adjacent to } v_{j} \text{ for } i \neq j \\ \\
0 & \text{otherwise}
\end{cases} 
\end{bmatrix}
$$
and $M' = M$ but remove the first row and column. 