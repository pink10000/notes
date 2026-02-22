---
tags:
  - MATH_114
---
# Non-Stochastic Processes
For example, consider the ODE:

Let $x(t) \in \R$ for $t \in [0, \infty)$, and 
$$
\frac{dx}{dt} = x, \quad\quad x(0) = 1
$$
Then the solution is to consider $x(t) = Ae^{t}$. Then via $x(0) = 1$, we see $x(t) = e^{t}$. 

# Discretization
We can simulate/solve the ODE by discretizing it. Let $\delta t > 0$ be small and let $t_{n} = n\delta t$ for $n = 0, 1, 2, \dots$. How are $x(t_{n}), x(t_{n+1})$ related? We have 
$$
x(t_{n}) = \frac{dx}{dt} \bigg|_{t = t_{n}} \approx 
\frac{x(t_{n+1}) - x(t_{n})}{\delta t}
$$
which implies 
$$
x(t_{n+1}) \approx x(t_{n}) + x(t_{n}) \delta t
$$
```desmos-graph
left=-0.1; right=5;
bottom=-2;
---
y=e^{(x-1.5)} | 0.5<x<3.5 |blue
y=x-0.5 | 1.5<=x<=2.8 | purple

x=1.5 | orange | 0<y<1 
x=2.5 | orange |0<y<2.718

(1.5, 1)|black|label:x(t_n)
(2.5, 2.718)|blue|label:x(t_{n+1})
(2.5, 2)|purple|label:x(t_n)[1 + \delta t]

y=-0.5 | 1.5<x<2.5 |black
x=1.5 | -0.6<y<-0.4 |black
x=2.5 | -0.6<y<-0.4 |black

(1.5, -0.2)|open|black|label:t_n
(2.5, -0.2)|open|black|label:t_{n+1}
(2, -0.8)|open|black|label:\delta t
```
Consider the *difference equation*:
$$
x_{n+1} = x_{n} + x_{n} \delta t, \quad\quad x_{0} = 1, n = 0, 1, 2, \dots
$$
For example, 
$$
x_{1} = 1 + \delta t, \quad\quad x_{2} = (1 + \delta t)^{2}
$$
such that 
$$
x_{n} = (1 + \delta t)^{n}
$$
```desmos-graph
left=-1; right=7;
bottom=-1; top=4.5;
---
y=e^{(0.2x)} | 0<=x<=6.5 | blue

x=1.5 | orange | 0<y<1.35
x=3.0 | orange | 0<y<1.82
x=5.5 | orange | 0<y<3.0

(0, 1)|black|label:x_0
(1.5, 1.35)|blue|label:x(t_1)
(1.5, 1.1)|purple|label:x_1
(3.0, 1.82)|blue|label:x(t_2)
(3.0, 1.4)|purple|label:x_2
(5.5, 3.0)|blue|label:x(t)

(4.25, 1.0)|open|black|label:...|hidden
(4.25, -0.3)|open|black|label:...|hidden

(0, -0.3)|open|black|label:0
(1.5, -0.3)|open|black|label:\delta t
(3.0, -0.3)|open|black|label:2\delta t
(5.5, -0.3)|open|black|label:n\delta t = t'
```
showing how we can approximate the discrete solution $x_{n}$ to the continuous solution $x(t)$. But does it approach it?

Let $t' = t_{n} = n\delta t$ and consider the limit $n \to \infty, \delta t \to 0$ with $t'$ fixed
```desmos-graph
left=-1; right=7;
bottom=-3; top=2;
---
y=0 | 0<=x<=6 | black

x=1 | -0.1<=y<=0.1 | black
x=2 | -0.1<=y<=0.1 | black
x=3 | -0.1<=y<=0.1 | black
x=5 | -0.1<=y<=0.1 | black

(0,0) | black
(6,0) | black

(0, -0.4) | open | black | label:0
(6, -0.4) | open | black | label:t'
(4, 0.2) | open | black | label:...

y=0.4 | 1<=x<=2 | black
x=1 | 0.3<=y<=0.5 | black
x=2 | 0.3<=y<=0.5 | black
(1.5, 0.7) | open | black | label:\delta t

y = -1/7 x - 0.8 | 0 <= x <= 2.8 | black
y = -1.5x + 3 | 2.8 <= x <= 3 | black
y = 1.5x - 6 | 3 <= x <= 3.2 | black
y = 1/7 x - 11.6/7 | 3.2 <= x <= 6 | black

(3, -1.9) | open | black | label:n
```
Then
$$
x_{n} = \left(1 + \frac{t'}{n} \right)^{n} \to e^{t'} = x(t')
$$
as $n \to \infty$. 

Remarks:
- We can think of an ODE $\frac{dx}{dt} = x$ as a difference equation $x_{n+1} = x_{n} + x_{n} \delta t$ in the limit of $\delta t \to 0$. 
- For ODEs, it is typically easier to compute using a continuous picture.

# Continuum Limit of Difference Equations
Consider the difference equation $x_{n} \in \R$ with 
$$
x_{n+1} = x_{n} + \delta t  u, 
\quad\quad x_{0} = 0, 
\quad n= 0, 1, 2, \dots
$$
does this have a **continuum limit**? In particular, is there an $x(t)$ such that 
$$
x_{n} \to x(t) \text{ as } n \to \infty,\;\; \delta t \to 0 \text{ with } n \cdot \delta t = t? 
$$
Check $x_{1} = \delta t u, \dots , x_{n} = n \delta t u = ut$. So we approach $ut$. Thus, the continuum limit is 
$$
x(t) = ut, \frac{dx}{dt} = u
$$

Remark: Suppose we took 
$$
x_{n+1} = x_{n} + \delta t^{\alpha} u
$$
then 
$$
x_{n} = n \delta t^{\alpha} u = t \cdot \delta t^{\alpha - 1} u
$$
so that 
$$
x_{n} \to \begin{cases}
0 & \alpha > 1 \\
\infty & \alpha < 1
\end{cases}
$$
as $\delta t \to 0, n \to \infty, n \delta t = t$. This implies there is no continuum limit unless $\alpha = 1$. 
> We essentially are reducing the discrete step-wise system to an analytical model. It is a formal operation to recover a *differential* equation from a *difference* equation. 

> Intuitively, this is subdividing some interval of time $t$ into $n$ parts of size $\delta$, such that $n (\delta t) = t$. Non-existence of an $\alpha$ means that further subdivision diverges to infinity or collapses identically to $0$. In particular, we would be unable to map a discrete model to a continuous differential framework.