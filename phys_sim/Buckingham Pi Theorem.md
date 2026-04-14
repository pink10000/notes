---
tags:
  - CSE_291G
---
# Buckingham Pi Theorem 
Suppose we had a physical equation relating $n$ quantities $f(q_{1}, \ldots, q_{n}) = 0$. Suppose the $n$ quantities only involve $k$ independent physical [[Dimensional Analysis#Physical Dimensions|dimensions]]. Then the equation can be restated as 
$$
F(\Pi_{1}, \ldots, \Pi_{p}) = 0
$$
for some $p = n-k$ [[Dimensional Analysis#Dimensionless Dimension|dimensionless variables/parameters]] $\Pi_{1}, \ldots, \Pi_{p}$. We can express the dimension of each physical quantity $q_i$ as a product of the base dimensions $\dimB_{1}, \ldots, \dimB_{\ell}$, such that 
$$
[q_i] = \dimB_{1}^{m_{1i}} \cdots \dimB_{\ell}^{m_{\ell i}}
$$
Then, we take the logarithm of the dimensions 
$$
\log[q_i] = m_{1i} \log \dimB_{1} + \cdots + m_{\ell i} \log \dimB_{\ell}
$$
giving us a change of [[Vector Space#Theorem (Basis)|basis]] formula
$$
\left(
  \log[q_1] \quad\cdots\quad \log[q_n]
\right)
=
\left(
  \log \dimB_{1} \quad\cdots\quad \log \dimB_{\ell}
\right)
\underbrace{
\begin{pmatrix}
  m_{11} & \cdots & m_{1n} \\
  \vdots & \ddots & \vdots \\
  m_{\ell 1} & \cdots & m_{\ell n}
\end{pmatrix}
}_{\mathbf{M}}
$$
where $\mathbf{M}$ is the $\ell \times n$ dimension matrix. The physical quantities involve only $k$ independent dimensions $\iff$ the rank of $\mathbf{M}$ is $k$. Using the [[Rank-Nullity Theorem]], the null space of $\mathbf{M}$ has dimension $p = n-k$. 

Solving the equation $\mathbf{M} a_j = 0$ gives us the [[Vector Space#Theorem (Basis)|basis]] for the null space, size $p$. Indeed, 
$$
a_1 = \begin{pmatrix}
  a_{11} \\
  \vdots \\
  a_{1n}
\end{pmatrix}, \ldots, 
a_p = \begin{pmatrix}
  a_{p1} \\
  \vdots \\
  a_{pn}
\end{pmatrix}
$$
Then 
$$
\left(
  \log [q_1] \quad\cdots\quad \log [q_n]
\right) a_j = 0
$$
That is, 
$$
\Pi_j := C_j q_1^{a_{1j}} \cdots q_n^{a_{nj}}
$$
are $p$ dimensionless variables. This theorem mathematically proves how many parameters actually govern a physical system so that we can perform a test or a simulation. This allows us to reliably scale models (like a small car in a wind tunnel) to predict real-world performance. 

## Example 1 (Atomic Bomb)
We can use the Buckingham Pi Theorem to find the dimensionless parameters governing the blast radius of an atomic bomb. First, we'll identify the physical quantities involved. 

| Physical Quantity           |  Symbol  |          Dimension           |
| :-------------------------- | :------: | :--------------------------: |
| Radius of the fireball      |  $[r]$   |  $\dimM^0 \dimL^1 \dimT^0$   |
| Density of surrounding air  | $[\rho]$ | $\dimM^1 \dimL^{-3} \dimT^0$ |
| Energy released by the bomb |  $[E]$   | $\dimM^1 \dimL^2 \dimT^{-2}$ |
| Time since the ignition     |  $[t]$   |  $\dimM^0 \dimL^0 \dimT^1$   |

We get the dimension matrix 
$$
\mathbf{M} =
\begin{pmatrix}
  0 & 1 & 1 & 0 \\
  1 & -3 & 2 & 0 \\
  0 & 0 & -2 & 1
\end{pmatrix}
$$
Because of the rectangular shape, we have a one dimensional [[Null Space|null space]]. In particular, it is spanned by 
$$
a = \begin{pmatrix} -5 \\ -1 \\ 1 \\ 2 \end{pmatrix}
$$
This gives us the dimensionless variable
$$
\Pi = r^{-5} \rho^{-1} E^{1} t^{2} = \frac{E t^2}{\rho r^5}
$$
Since we only have dimensionless parameter, the physical law governing the explosion must take the form $F(\Pi) = 0$, which mathematically implies $\Pi = \text{constant}$. Let this constant be $C$. So, 
$$
\frac{E t^2}{\rho r^5} = C
$$
On smaller experiments, $C \approx 1.033$. Given (from the photograph), 
- $t = 0.006$ seconds
- $r = 80$ meters
- $\rho_{\text{TestSite}} = 1.1$ kg/m$^3$

then the energy released by the bomb is approximately
$$
\begin{aligned}
E 
&= C \rho r^5 t^{-2}  \\
&\approx 10^{14} \text{ joules} \\
&\approx 24 \text{ kilotons of TNT}
\end{aligned}
$$
With more frames, G.I. Taylor got $22$ kilotons of TNT using more frames. The ground truth was $20$ kilotons of TNT. 

> The original paper is [Taylor's "The Formation of a Blast Wave by a Very Intense Explosion"](https://royalsocietypublishing.org/doi/10.1098/rspa.1950.0049).

## Example 2 (Drag of a Car)
A moving car will experience aerodynamic drag. We can reasonably postulate there exists a function relating the following $5$ physical quantities:

| Physical Quantity  |  Symbol  |            Dimension            |
| :----------------- | :------: | :-----------------------------: |
| Car's length scale |  $[L]$   |    $\dimM^0 \dimL^1 \dimT^0$    |
| Car's speed        |  $[v]$   |  $\dimM^0 \dimL^1 \dimT^{-1}$   |
| Air density        | $[\rho]$ |  $\dimM^1 \dimL^{-3} \dimT^0$   |
| Air viscosity      | $[\mu]$  | $\dimM^1 \dimL^{-1} \dimT^{-1}$ |
| Drag force         |  $[F]$   |  $\dimM^1 \dimL^1 \dimT^{-2}$   |

We get the dimension matrix
$$
\mathbf{M} =
\begin{pmatrix}
  0 & 0 & 1 & 1 & 1 \\
  1 & 1 & -3 & -1 & 1 \\
  0 & -1 & 0 & -1 & -2
\end{pmatrix}
$$
The null space of $\mathbf{M}$ is two dimensional, spanned by
$$
a_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \\ -1 \\ 0 \end{pmatrix}
\quad\quad\quad
a_2 = \begin{pmatrix} -2 \\ -2 \\ -1 \\ 0 \\ 1 \end{pmatrix}
$$
such that 
$$
\begin{aligned}
\Pi_1 &= L^1 v^1 \rho^1 \mu^{-1} = \frac{\rho v L}{\mu} \\
\Pi_2 &= L^{-2} v^{-2} \rho^{-1} F^1 = \frac{F}{\rho L^2 v^2}
\end{aligned}
$$
By the Buckingham Pi Theorem, the physical law governing the drag force must take the form $F(\Pi_1, \Pi_2) = 0$, which mathematically implies $\Pi_2 = \Phi(\Pi_1)$ for some function $\Phi$. Note that $\Pi_1$ is the [[Dimensional Analysis#Example 3 (Navier-Stokes Equation)|Reynolds number]]. In other words, if we wanted to set up a wind tunnel so simulate this system, we'd need to ensure 
$$
\text{Re}_{\text{WindTunnel}} = \text{Re}_{\text{RealWorld}}
$$
such that the drag force in the wind tunnel is a scaled version of the drag force in the real world. In particular,
$$
\left(
  \frac{F}{\rho L^2 v^2}
\right)_{\text{WindTunnel}}
=
\left(
  \frac{F}{\rho L^2 v^2}
\right)_{\text{RealWorld}}
$$
From this equality, we can measure the force on the small model in the wind tunnel and use it to accurately calculate the force the full-sized car will experience in the real world.