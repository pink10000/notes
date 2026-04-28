---
tags:
  - CSE_291G
  - MATH_100B
---
# Euclidean Group
The **Euclidean group** $E(n)$ is the group of all isometries of the [[Euclidean Space]] $\R^n$. These are transformations that preserve the Euclidean distance between any two points.

Any element $g \in E(n)$ can be represented as a transformation $g: \R^n \to \R^n$ of the form:
$$
g(\mathbf{x}) = \mathbf{R}\mathbf{x} + \mathbf{c}
$$
where $\mathbf{R}$ is an $n \times n$ orthogonal matrix (satisfying $\mathbf{R}^\top \mathbf{R} = I$) and $\mathbf{c} \in \R^n$ is a translation vector.

# Definition (Special Euclidean Group)
The **special Euclidean group** $\SE(n)$ is the subgroup of $E(n)$ consisting of orientation-preserving isometries. These are the transformations where the rotation part has determinant $1$:
$$
\SE(n) = \left\{ (\mathbf{R}, \mathbf{c}) \mid \mathbf{R} \in \SO(n), \mathbf{c} \in \R^n \right\}
$$
where $\SO(n) = \{ \mathbf{R} \in O(n) \mid \det(\mathbf{R}) = 1 \}$ is the [[Special Orthogonal Group]].

## Matrix Representation
Elements of $\SE(n)$ are often represented using homogeneous coordinates as $(n+1) \times (n+1)$ matrices:
$$
\begin{bmatrix}
\mathbf{R} & \mathbf{c} \\
\mathbf{0}^\top & 1
\end{bmatrix}
$$
The group operation (composition of transformations) then corresponds to matrix multiplication:
$$
\begin{bmatrix}
\mathbf{R}_1 & \mathbf{c}_1 \\
\mathbf{0}^\top & 1
\end{bmatrix}
\begin{bmatrix}
\mathbf{R}_2 & \mathbf{c}_2 \\
\mathbf{0}^\top & 1
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{R}_1\mathbf{R}_2 & \mathbf{R}_1\mathbf{c}_2 + \mathbf{c}_1 \\
\mathbf{0}^\top & 1
\end{bmatrix}
$$

## Semidirect Product Structure
The Euclidean group can be described as the semidirect product of the translation group and the orthogonal group:
$$
E(n) \cong \R^n \rtimes O(n)
$$
Similarly, $\SE(n) \cong \R^n \rtimes \SO(n)$.

# Relation to Rigid Body Dynamics
In the context of [[phys_sim/Rigid Body Dynamics|rigid body dynamics]], $\SE(3)$ represents the configuration space of a rigid body in 3D space. Each element of $\SE(3)$ describes a possible position and orientation of the body relative to a reference frame.
