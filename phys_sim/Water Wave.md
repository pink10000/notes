---
tags:
  - CSE_291G
---
# Wave Synthesis
We want to create digital ocean waves. Let the height field be $\eta(x, t)$. The sum of different frequencies can be expressed as a sum of different frequencies:
$$
\eta(x, t) = \sum_k h(k) \exp(i(k x - \omega t))
$$
where 
- $\lambda$ is the wavelength, and $p$ is the period.
- $k = 2\pi/\lambda$ 
- $\omega = 2\pi /p$.

There is a compatibility relation between $k$ and $\omega$ called the **dispersion relation**, $\omega = \omega(k)$. 

In continuous 2D, 
$$
\eta(\bx, t) = \int_{-\infty}^\infty \int_{-\infty}^\infty h(\bk) \exp(i(\bk \cdot \bx - \omega_\bk t)) \,dk_x dk_y
$$
Let $\eta$ be discretized on a rectangle of size $L_x \times L_y$ with the number of grids $N_x \times N_y$. So, 
$$
h = \texttt{FFT}_{\text{2D}}(\eta)
\quad\quad\quad
\eta = \texttt{IFFT}_{\text{2D}}(h)
$$
such that 
$$
\eta_{n_x, n_y}
= \frac{1}{N_x N_y}
\sum_{m_x = 0}^{N_x - 1} \sum_{m_y = 0}^{N_y - 1} h_{m_x, m_y} 
    \exp\left(
        2\pi i \left(
            \frac{m_x n_x}{N_x} + \frac{m_y n_y}{N_y}
        \right)
    \right)
    \exp\left(
        i\omega_{m_x, m_y} t
    \right)
$$
so
$$
\begin{aligned}
\bk &\approx \left(
    2\pi \frac{\tilde{m}_x}{L_x}, 2\pi \frac{\tilde{m}_y}{L_y}
\right) \\
\tilde{m} &= \left(
    m + \frac{N}{2} 
\right) \bmod N - \frac{N}{2} \\
\end{aligned}
$$

Wave synthesis boils down to 
- modeling the dispersion relation $\omega_{\bk}$,
- model the spectral energy density $h(\bk)$

