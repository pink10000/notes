---
tags:
  - MATH_20D
---

# Numerical Methods
When analytical solutions are not possible, we can use numerical methods to approximate the solution of an ODE. This is common because the ODEs are derived from physical laws. Given any differential equation, for example,
$$
\dddot{x} + \ddot{x} \ddot{x} + \sin(\ddot{x}) = 1
$$
we can convert to a first-order system (involving at most the first derivative). Let velocity $v = \dot{x}$ and acceleration $a = \ddot{x}$. Then we have
$$
\begin{cases}
\dot{x} = v \\
\dot{v} = a \\
\dot{a} = 1 - av - \sin(a)
\end{cases}
$$
Let $y = [x, v, a]^{\top}$. The ODE becomes $\dot{y} = \mathbf{f}(y)$. 

## Forward Euler Method
We can discretize time into time-frames. 
$$
y^{(n)} = y(n \Delta t)
$$
Then, we calculate the next state $y^{(n+1)}$ by using the current state $y^{(n)}$ and the derivative $\dot{y}^{(n)}$. The general idea is that 
$$
\frac{y^{(n+1)} - y^{(n)}}{\Delta t} \approx \mathbf{f}(y^{(n)})
$$
such that 
$$
y^{(n+1)} \approx y^{(n)} + \Delta t \cdot \mathbf{f}(y^{(n)})
$$
Recall that $\mathbf{f}$ is a vector-valued function that describes the change in the state $y$ at time $t$. 

Advantages
- There is an **explicit formula** formula for the next state.
- Computationally fast and easy to implement.
Limitations
- Not very accurate, unless $\Delta t$ is tiny. The error is proportional to $\Delta t^2$ from the Taylor expansion of $y(t + \Delta t)$.
- Can be energy increasing (violates conservation of energy). 

## Backward Euler Method
The backward Euler method is an implicit method that calculates the next state $y^{(n+1)}$ using the derivative at the next state rather than the current state. The formula is given by
$$
\frac{y^{(n+1)} - y^{(n)}}{\Delta t} \approx \mathbf{f}(y^{(n+1)})
$$
Advantages
- Energy decreasing (dissipating). This "looks" physical, i.e. it is more realistic as we expect energy to dissipate over time.
- Can take large time steps without instability. 
- Can incorporate collision.

Limitations
- Not very accurate, unless $\Delta t$ is tiny. 
- We have to solve implicitly for $y^{(n+1)}$ at each step, which can be computationally expensive.

# Runge-Kutta Method (RK4)
This method is accurate, stable, and explicit. 
$$
\begin{aligned}
k_1 &= \mathbf{f}(y^{(n)}) \\
k_2 &= \mathbf{f}\left(y^{(n)} + \frac{\Delta t}{2} k_1\right) \\
k_3 &= \mathbf{f}\left(y^{(n)} + \frac{\Delta t}{2} k_2\right) \\
k_4 &= \mathbf{f}\left(y^{(n)} + \Delta t k_3\right) \\
y^{(n+1)} &= y^{(n)} + \frac{\Delta t}{6} (k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}
$$
The idea is that we take a weighted average of the slopes at different points within the time step to get a better estimate of the next state. In most cases, the RK4 method works very well. There are other special algorithms (non-RK4) that are deigned to preserve energy or momentum.
- Variational integrator
- Symplectic integrator
- Lie group integrator

## Example 1
Consider the pendulum equation $m\ddot{\theta} = -mg \sin \theta$. Given $(\theta_i, \dot{\theta}_i)$ at time $t_i$, we can use the RK4 method to compute $(\theta_{i+1}, \dot{\theta}_{i+1})$ at time $t_{i+1} = t_i + \Delta t$.

Recall from [[#Reduction to First-Order Systems|example]] that 
$$
f(\theta, v) = \dot{y} = \begin{bmatrix} v \\ -\sin \theta \end{bmatrix}
$$
(we omit $g$ for simplicity). Then, we can compute the intermediate slopes as follows:
$$
k_1 = f(\theta_i, v_i) = \begin{bmatrix} v_i \\ -\sin \theta_i \end{bmatrix}
$$
To prepare for $k_2$, we need to use $k_1$ to project halfway forward $\frac{\Delta t}{2}$. This gives
$$
\begin{bmatrix}
\theta_{i + 1/2}^{*} \\
v_{i + 1/2}^{*} \\
\end{bmatrix}
= \begin{bmatrix} \theta_i \\ v_i \end{bmatrix} 
+ \frac{\Delta t}{2} \begin{bmatrix} v_i \\ -\sin \theta_i \end{bmatrix}
$$
such that 
$$
\begin{aligned}
\theta_{i + 1/2}^{*} &= \theta_i + \frac{\Delta t}{2} v_i \\
v_{i + 1/2}^{*} &= v_i - \frac{\Delta t}{2} \sin \theta_i
\end{aligned}
$$
Then, we can compute $k_2$ using the projected state:
$$
k_2 = f(\theta_{i + 1/2}^{*}, v_{i + 1/2}^{*}) =
\begin{bmatrix}
v_{i + 1/2}^{*} \\
-\sin \theta_{i + 1/2}^{*}
\end{bmatrix}
$$
Next, we can compute $k_3$ by projecting forward again using $k_2$:
$$
\begin{bmatrix}
\theta_{i + 1/2}^{**} \\
v_{i + 1/2}^{**} \\
\end{bmatrix}
= \begin{bmatrix} \theta_i \\ v_i \end{bmatrix} 
+ \frac{\Delta t}{2} \begin{bmatrix}v_{i + 1/2}^{*} \\ -\sin \theta_{i + 1/2}^{*} \end{bmatrix}
$$
such that
$$
\begin{aligned}
\theta_{i + 1/2}^{**} &= \theta_i + \frac{\Delta t}{2} v_{i + 1/2}^{*} \\
v_{i + 1/2}^{**} &= v_i - \frac{\Delta t}{2} \sin \theta_{i + 1/2}^{*}
\end{aligned}
$$
Then we can compute $k_3$ using the projected state:
$$
k_3 = f(\theta_{i + 1/2}^{**}, v_{i + 1/2}^{**}) =
\begin{bmatrix}
v_{i + 1/2}^{**} \\
-\sin \theta_{i + 1/2}^{**}
\end{bmatrix}
$$
Finally, we can compute $k_4$ by projecting forward using $k_3$:
$$
\begin{bmatrix}
\theta_{i + 1}^{***} \\
v_{i + 1}^{***}
\end{bmatrix}
= \begin{bmatrix} \theta_i \\ v_i \end{bmatrix} 
+ \frac{\Delta t}{2} \begin{bmatrix}
v_{i + 1/2}^{**} \\
-\sin \theta_{i + 1/2}^{**}
\end{bmatrix}
$$
such that
$$
\begin{aligned}
\theta_{i + 1}^{***} &= \theta_i + \Delta t v_{i + 1/2}^{**} \\
v_{i + 1}^{***} &= v_i - \Delta t \sin \theta_{i + 1/2}^{**}
\end{aligned}
$$
Then, we can compute $k_4$ using the projected state:
$$
k_4 = f(\theta_{i + 1}^{***}, v_{i + 1}^{***}) =
\begin{bmatrix}
v_{i + 1}^{***} \\
-\sin \theta_{i + 1}^{***}
\end{bmatrix}
$$
Plugging everything into the RK4 formula, we get
$$
\begin{aligned}
\begin{bmatrix}
\theta_{i+1} \\
v_{i+1}
\end{bmatrix}
&= \begin{bmatrix} \theta_i \\ v_i \end{bmatrix}
+ \frac{\Delta t}{6} \left( k_1 + 2k_2 + 2k_3 + k_4 \right) \\
% 
&= \begin{bmatrix} \theta_i \\ v_i \end{bmatrix}
+ \frac{\Delta t}{6} \left(
\begin{bmatrix} v_i \\ -\sin \theta_i \end{bmatrix} +
2 \begin{bmatrix}v_{i + 1/2}^{*} \\ -\sin \theta_{i + 1/2}^{*} \end{bmatrix} +
2 \begin{bmatrix}
v_{i + 1/2}^{**} \\ -\sin \theta_{i + 1/2}^{**}
\end{bmatrix} +
\begin{bmatrix}
v_{i + 1}^{***} \\ -\sin \theta_{i + 1}^{***}
\end{bmatrix}
\right)
\end{aligned}
$$

The choice of $\Delta t$ is crucial for the accuracy and stability of the numerical solution. Graphically, if $\Delta t = 0.1$, the numerical solution follows the true solution closely. However, if $\Delta t = 0.9$, we preserve no information about the true solution and the numerical solution diverges significantly from the true solution.

## Example 1.2 (2nd Order Discretization)
We can also use a second-order discretization method to solve the pendulum equation, or **central difference approximation** for a second derivative (in our case, acceleration). We consider 
$$
\begin{aligned}
v_{\text{forward}} &= \frac{\theta_{i+1} - \theta_i}{\Delta t} \\
v_{\text{backward}} &= \frac{\theta_i - \theta_{i-1}}{\Delta t}
\end{aligned}
$$
and take the average to find the acceleration:
$$
\begin{aligned}
a_i &= \frac{v_{\text{forward}} - v_{\text{backward}}}{\Delta t} \\
&= \frac{\theta_{i+1} - 2\theta_i + \theta_{i-1}}{\Delta t^2}
\end{aligned}
$$
But recall $\ddot{\theta} = a$, so we can rearrange to get
$$
\frac{\theta_{i+1} - 2\theta_i + \theta_{i-1}}{\Delta t^2}
= -\sin \theta_i 
$$
