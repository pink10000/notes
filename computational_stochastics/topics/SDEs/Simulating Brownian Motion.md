---
tags:
  - MATH_114
---
# Euler-Maruyama Method
We can simulate [[Stochastic Differential Equations#Definition (Brownian Motion, Wiener Process)|Brownian Motion (BM)]] via the discrete approximation of its independent increments.

Let $\delta t > 0, n \in \Z$ and $T = n \delta t$. Let $t_{k} = k \delta t$ for $k = 0, 1, 2, \dots, n$ and $t_{n} = T$. The objective is construct a discrete time process 
$$
X(t_{k}) = X_{k}
$$
such that $X_{k} \approx B(t_{k})$ for a standard BM, $B(t)$. The scaling factor $\sqrt{\delta t}$ arises directly from the [[Stochastic Differential Equations#Properties of Brownian Motion|property]] that Brownian increments are normally distributed with variance $\delta t$. 

Algorithm: (Euler, with notation as above)
1. Set $X_{0} = 0$
2. For $i = 0$ to $n - 1$, 
	1. Generate $Z \sim \mathcal{N}(0, 1)$
	2. Set $X_{i+1} = X_{i} + \sqrt{\delta t}Z$
3. Output $X_{0}, X_{1}, \dots, X_{n}$ to get $X(0), X(t_{1}), \dots, X(t_{n})$

This should look like path (similar to what a stock ticker would look like). We can do linear interpolation to connect $(t_{k}, X(t_{k}))$ to get approximate sample path $X(t)$. 

# BM with Drift
Let $X(t) = ut + \sqrt{2D}\cdot B(t)$ where $B(t)$ is a [[Stochastic Differential Equations#Brownian Motion and SDE Formulation|BM]]. Note that $u$ represents the **deterministic drift velocity**, and $D$ represents the **diffusion coefficient**. We can example the distribution of $X(t)$:
1. $\E{X(t)} = ut$, since $\E{B(t)} = 0$ by [[Stochastic Differential Equations#Properties of Brownian Motion|properties]]. 
2. $\var(X(t)) = \E{(X(t) - ut)^{2}} = \E{2D \cdot B(t)^{2}} = 2Dt$ 
Thus the marginal distribution is $X(t) \sim \mathcal{N}(ut, 2Dt)$. 
# SDE Notation 
Recall the SDE [[Stochastic Differential Equations#Brownian Motion and SDE Formulation|notation]]. We can extend this with drift:
$$
\underbrace{dX}_{\text{increment of $X$}} = \;\; 
\underbrace{u dt}_{\text{deterministic change in $t$}} + \;\; 
\underbrace{\sqrt{2D} \cdot dB}_{\text{scaled Brownian increment}}
$$
We can "integrate" to get $X(t) = ut + \sqrt{2D} B(t)$. 
> Stochastic integration is different in general! You need different frameworks, the [[Riemann-Stieltjes Integral]] fails due to infinite total variation.

# Euler's Method For BM with Drift
Let $\delta t > 0, n \in \Z, t_{k} = k\delta t$ for $k = 0, 1, \dots, n$. 
- Set $X_{0} = 0$
- For $i = 0$ to $n - 1$,
	- Generate $Z \sim \mathcal{N}(0, 1)$
	- $X_{i+1} = X_{i} + u \delta t + \sqrt{2 D \delta t} \cdot Z$
- Output $X_{0}, X_{1}, \dots, X_{n}$ 
$X_{i}$ approximates true solution to $X(t_{i})$.

## Remarks on Euler's Method 
- The continuous SDE is the formal limit of the discrete update rule as $\delta t \to 0$: 
  $$
  dX = u \cdot dt + \sqrt{2 D} \cdot dB(t)
  $$
- In Euler's Method, the discrete update computes the next state by adding the deterministic drift and the stochastic diffusion evaluated over the interval $\delta t$:
  $$
  X_{i+1} = X_{i} = u \delta t + \sqrt{2 D \delta t} \cdot Z
  $$
- We can think of a SDE solution $X(t)$ as a "continuum limit" of the solution to a discrete equation. 
- Intuitively, $dB$ is like $\sqrt{dt}\cdot Z$. Indeed, since $dB(t) = B(t + \delta t) = B(t) \sim \mathcal{N}(0, dt)$, then $\E{dB} = 0$ and $\E{dB^{2}} = dt$. 
- *Langevin notation*: divide by $dt$:
  $$
  \frac{dX}{dt} = u + \sqrt{2 D} \cdot \xi(t)
  $$
  here, $\xi(t)$ is "white noise". It is **not** a function! From above we get $dB/dt \sim Z/\sqrt{dt}$.

# Moments of BM with Drift
Evaluate the first moment by applying the expectation operator to the SDE.
$$
dX = u \cdot dt + \sqrt{2 D} \cdot dB
$$
Taking the [[Expectation]] yields $\E{dX} = u \,dt + \sqrt{2D} \cdot \E{dB}$. Since $\E{dB} = 0$, we isolate the deterministic component. The expectation operator commutes with the differential, generating an ordinary differential equation (ODE) for the mean
$$
d\E{X} = u dt \implies \frac{d}{dt} \E{X} = u 
$$
Integrating this yields $\E{X(t)} = ut$. From the discrete Euler approximation, the expectation of the difference equation strictly produces the same continuous limit: 
$$
X_{i+1} - X_{i} = u \delta t + \sqrt{2 D \delta t} \cdot Z \implies \E{X_{i+1}} - \E{X_{i}} = u \delta t + \sqrt{2D \delta t} \cdot \E{Z}
$$
Since $\E{Z} = 0$, the relation reduces to 
$$
\E{X_{i+1}} = \E{X_{i}} + u\delta t
$$
Dividing by $\delta t$ and evaluating the limit as $\delta t \to 0$ recovers the exact ODE:
$$
\begin{aligned}
\lim_{\delta t \to 0} \frac{\E{X_{i+1}} - \E{X_{i}}}{\delta t} &= u \\
\frac{d}{dt} \E{X} &= u \\
\end{aligned}
$$
