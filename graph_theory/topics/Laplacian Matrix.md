---
tags:
  - CSE_291G
---
# Definition (Graph Laplacian)
The **Graph Laplacian** (or the **Laplacian Matrix**) is *a* matrix representation of a [[Graph|graph]]. It represents the edges of a graph similar to how an adjacency matrix is defined, but requires each row to sum to $0$. For example, given $K_{3}$, the adjacency graph is all $1$s, but the diagonals. However, the Laplacian matrix of $K_{3}$ is:
$$
\mathbf{L} = \begin{bmatrix}
2 & -1 & -1 \\
-1 & 2 & -1 \\
-1 & -1 & 2
\end{bmatrix}
$$
where for $v_1$, it has an edge to $v_2$ and $v_3$, so the first row has two $-1$s, and the diagonal is $2$ to make the row sum to $0$. The same applies for the other rows.

For directed graphs, either the in-[[Degree|degree]] or out-[[Degree|degree]] can be used to determine the diagonal entries. For example, for the directed graph $v_1 \to v_2 \to v_3$, the Laplacian matrix is:
$$
\mathbf{L} = \begin{bmatrix}
1 & -1 & 0 \\
0 & 1 & -1 \\
0 & 0 & 0
\end{bmatrix}
$$
Formally, it is defined by 
$$
\mathbf{L} = \mathbf{D} - \mathbf{A}
$$
where $\mathbf{D}$ is the degree matrix and $\mathbf{A}$ is the adjacency matrix. $\mathbf{D}$ is a diagonal matrix where the $i$-th diagonal entry is the degree of vertex $v_i$. 