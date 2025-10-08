---
tags:
  - MATH_154
---
# Method (Depth First Search)
**Depth First Search (DFS)** keeps a list of vertices connected so far in order. It connects a new vertex to the most recent possible option. 

It also allows us to create a [[Tree#Definition (Spanning Tree)|spanning tree]] of a graph. For example, 
```mermaid
graph LR;
    1((1)) o--o 2((2));
    1((1)) o--o 3((3));
    2((2)) o--o 3((3));
    1((1)) o--o 7((7));
    2((2)) o--o 6((6));
    3((3)) o--o 4((4));
    3((3)) o--o 5((5));
    3((3)) o--o 7((7));
    4((4)) o--o 5((5));
    8((8)) o--o 4((4));
    4((4)) o--o 7((7));
    8((8)) o--o 5((5));
    5((5)) o--o 6((6));
    6((6)) o--o 7((7));
```
which, follows $v \to 2 \to 3 \to 4 \to 5 \to 6 \to 7$. But then it needs to backtrack since we cannot reach $8$. Thus, we go from $\color{red}7 \to 6 \to 5$ and then $5 \to 8$. This gives a new tree:
```mermaid
graph LR;
	1((1)) o--o 2((2));
	2 o--o 3((3));
	3 o--o 4((4));
	4 o--o 5((5));
	5 o--o 8((8));
	5 o--o 6((6));
	6 o--o 7((7));
```
In general, DFS trees create long skinny graphs. 

# Lemma (DFS Trees Connect Ancestors)
In a DFS tree, all other edges of $G$ connect ancestors.

Proof:
Instead of an ancestor, you can have a cousin:
```mermaid
graph LR;
	c((c)) o--o a((a));
	c o--o b((b));
	a o-.e.-o b;
```
where $c$ is some common ancestor and some edge $e$ that connects $a$ and $b$. But this cannot happen with DFS. This is because we will not connect $c$ to anything new until all of $a$'s neighbors have been added. So we must explore $e$ once we finish exploring $a$'s children.  




