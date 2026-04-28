---
tags:
  - CSE_291G
---
# Orthogonal Group
The **orthogonal group** $O(n)$ is the group of all $n \times n$ orthogonal matrices. These are matrices $\mathbf{R}$ such that:
$$
\mathbf{R}^\top \mathbf{R} = \mathbf{R} \mathbf{R}^\top = \mathbf{I}
$$
Orthogonal matrices represent linear transformations that preserve the [[Euclidean Space|Euclidean inner product]] and distance (isometries that fix the origin).

# Definition (Special Orthogonal Group)
The **special orthogonal group** $\SO(n)$ is the subgroup of $O(n)$ consisting of matrices with determinant $1$:
$$
\SO(n) = \{ \mathbf{R} \in O(n) \mid \det(\mathbf{R}) = 1 \}
$$
Matrices in $\SO(n)$ represent **rotations**. Matrices in $O(n)$ with determinant $-1$ represent improper rotations (rotations combined with a reflection).

# Properties
- **Compactness**: $\SO(n)$ and $O(n)$ are compact [[Manifold|manifolds]].
- **Isometry**: For any $\mathbf{x}, \mathbf{y} \in \R^n$ and $\mathbf{R} \in O(n)$, we have $\langle \mathbf{R}\mathbf{x}, \mathbf{R}\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$.
- **Lie Algebra**: The Lie algebra of $\SO(n)$, consists of all $n \times n$ [[Skew-Symmetric Matrix|skew-symmetric matrices]].

# 2D and 3D Cases
## SO(2)
Elements of $\SO(2)$ are rotation matrices in the plane:
$$
\mathbf{R}(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$
$\SO(2)$ is an Abelian [[Group]].

## SO(3)
Elements of $\SO(3)$ represent rotations in 3D space. 

# Relation to Physics
In [[Rigid Body Dynamics|rigid body dynamics]], $\SO(3)$ is used to represent the orientation of a rigid body in three-dimensional space.