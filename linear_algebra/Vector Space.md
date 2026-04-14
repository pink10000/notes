---
tags:
  - MATH_100B
  - CSE_291G
aliases:
  - vector spaces
  - vector space
---

# Definition (Vector Space)
A **vector space** over a [[Field|field]] $\mathbb{F}$ is a non-empty set $V$ together with a binary operation and a binary function that satisfy the following eight axioms. 

The binary operation called *vector addition* or simply *addition* assigns to any two vectors $\mathbf{v}, \mathbf{w} \in V$ a third vector $\mathbf{v} + \mathbf{w} \in V$. The binary function called *scalar multiplication* assigns to any scalar $a \in \mathbb{F}$ and any vector $\mathbf{v} \in V$ a vector $a\mathbf{v} \in V$.

| Axiom                                                                   | Description                                                                                                                                                          |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Associativity of addition                                               | $\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in V$, we have $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$.                       |
| Commutativity of addition                                               | $\forall \mathbf{u}, \mathbf{v} \in V$, we have $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$.                                                                 |
| Identity element of addition                                            | $\exists \mathbf{0} \in V$ such that for all $\mathbf{v} \in V$, $\mathbf{v} + \mathbf{0} = \mathbf{v}$.                                                             |
| Inverse elements of addition                                            | $\forall \mathbf{v} \in V$, there exists an element $-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$.                                         |
| Compatibility of scalar multiplication with field multiplication        | $\forall \mathbf{a}, \mathbf{b} \in \mathbb{F}$ and $\mathbf{v} \in V$, we have $\mathbf{a}(\mathbf{b}\mathbf{v}) = (\mathbf{a}\mathbf{b})\mathbf{v}$.               |
| Identity element of scalar multiplication                               | $\forall \mathbf{v} \in V$, we have $1\mathbf{v} = \mathbf{v}$, where $1$ is the multiplicative identity in $\mathbb{F}$.                                            |
| Distributivity of scalar multiplication with respect to vector addition | $\forall \mathbf{a} \in \mathbb{F}$ and $\mathbf{u}, \mathbf{v} \in V$, we have $\mathbf{a}(\mathbf{u} + \mathbf{v}) = \mathbf{a}\mathbf{u} + \mathbf{a}\mathbf{v}$. |
| Distributivity of scalar multiplication with respect to field addition  | $\forall \mathbf{a}, \mathbf{b} \in \mathbb{F}$ and $\mathbf{v} \in V$, we have $(\mathbf{a} + \mathbf{b})\mathbf{v} = \mathbf{a}\mathbf{v} + \mathbf{b}\mathbf{v}$. |

# Theorem (Basis)
Each vector space $V$ admits a **basis** $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n \in V$ so that every $\vec{u} \in V$ can be uniquely expressed as a linear combination of the basis vectors. That is, there is a unique $n$-tuple of scalars $(u^1, u^2, \ldots, u^n) \in \mathbb{F}^n$ such that
$$
\vec{u} = \sum_{i=1}^{n} u^i \vec{e}_i.
$$

The number $n$ of vectors in a basis is independent of the choice of basis. $n$ is called the **dimension** of $V$, denoted $\dim V$. Note that it could be infinite.

In a plain vector space $V$, there is no distinguished choice for a basis. Only the "dimensionless" Cartesian space $\R^n = \R \times \cdots \times \R$ has a special basis $\vec{e}_1 = (1, 0, \ldots, 0), \vec{e}_2 = (0, 1, \ldots, 0), \ldots, \vec{e}_n = (0, 0, \ldots, 1)$ called the **standard basis**. In general, there is no canonical way to identify a vector space with $\R^n$ for some $n$.

