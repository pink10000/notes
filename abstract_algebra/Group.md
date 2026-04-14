---
tags:
  - MATH_100A
---
# Group
A **group** is a set $G$ together with a binary operation $\cdot : G \times G \to G$ that satisfies the following properties:
1. Closure: For all $a, b \in G$, $a \cdot b \in G$.
2. Associativity: For all $a, b, c \in G$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3. Identity: There exists an element $e \in G$ such that for all $a \in G$, $e \cdot a = a \cdot e = a$.
4. Inverse: For each $a \in G$, there exists an element $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$.

# Definition (Abelian Group)
An **Abelian group** is a group $G$ that also satisfies the commutativity property:
$$
a \cdot b = b \cdot a \quad \forall a, b \in G.
$$

# Definition (Free Group)
A group $G$ is called **free** if it has a basis, which is a subset $B \subseteq G$ such that every element of $G$ can be uniquely expressed as a finite product of elements of $B$ and their inverses.