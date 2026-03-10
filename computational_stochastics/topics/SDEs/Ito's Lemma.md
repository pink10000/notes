---
tags:
  - MATH_114
---
Continuation from [[Stochastic Differential Equations#Moments of the OU Process]]. We want to calculate higher order [[Moments#Probability Moments|moments]].

The idea is that we use a "stochastic" chain rule for computing $d(f(x))$ where $d$ is the differential operator. 

# Taylor Series (Big O notation)
Let $f : \R \to \R$ be [[Transformation of Random Variables#Transformation of Multivariate Random Variables|smooth]]. Then 
$$
f(a + \vepsi) = f(a) 
+ \underbrace{\vepsi f'(a)}_{O(\vepsi)} 
+ \underbrace{\frac{1}{2} \vepsi^{2} f''(a)}_{O(\vepsi^{2})}
+ \cdots 
$$
This comes from [[Taylor's Theorem]]. Similarly, we have [[Gradient#First-Order Taylor Expansion]] using [[Big O Notation]]. We rewrite it here to motivate the following lemma.

# Ito's Lemma 
Consider the 1D [[Stochastic Differential Equations|SDE]] for $X(t) \in \R$:
$$
dX = 
\underbrace{u(X) \, dt}_{O\left(d t\right)} + 
\underbrace{\sigma(X) \, dB}_{O\left(\sqrt{dt}\right)}
$$
Stochastic calculus differs from standard calculus. 

Recall that 
$$
dB \sim \sqrt{dt}\cdot Z \sim O\left(\sqrt{dt}\right)
$$
from [[Stochastic Differential Equations#Brownian Motion and SDE Formulation|the formulation]] and 
$$
\E{dB^{2}} = dt \implies dB^{2} \sim O(dt), dB \sim O\left(\sqrt{dt}\right)
$$
from [[Stochastic Differential Equations#Properties of Brownian Motion|properties of Brownian Motion]]. This implies $dX = O\left(\sqrt{dt}\right)$. 
> The idea here is that as the steps we take get smaller, i.e. $dt \to 0$, the noise $dB \sim \sqrt{dt}$ becomes larger in proportion with $dt$. For example, if $dt = 0.01$, then $dB \approx \sqrt{dt} = 0.1$, or $10$ times larger. The noise has a larger effect. 

The goal for Ito's Lemma is, given function $f(X)$ and $dX$, we want to find an expression or $df$. The strategy is to use the [[#Taylor Series (Big O notation)|Taylor expansion]] of $f$ up to $O\left(dt^{3/2}\right)$ and treating $dB^{2} = dt$ since $dB^{2} = \E{dB^{2}} + \vepsi$, and the [[Expectation|expectation]] is $dt$. 

Consider the transformation of $f(X)$:
$$
\begin{aligned}
df(X) 
&= f(X + dX) - f(X) \\
&= f'(X) \,dX + \frac{1}{2} f''(X) (dX)^{2} + \cdots 
\end{aligned}
$$
via [[Derivative#Theorem (Cauchy Mean Value Theorem)|MVT]]. Next, we can find $dX$ and $(dX)^{2}$ to $O(dt)$.
$$
\begin{aligned}
dX &= u(X)\, dt + \sigma(X) \, dB \\
(dX)^{2} 
&= (u\, dt + \sigma \,dB)^{2} \\
&= u^{2}(dt)^{2} + 2u\sigma(dt \, dB) + \sigma^{2}(dB)^{2} \\
&= O\left(dt^{2}\right) + O\left(dt \cdot dt^{1/2}\right) + O(dt) \\
&= O\left( dt^{3/2} \right)
\end{aligned}
$$
We can substitute this to get 
$$
\begin{aligned}
df(X) 
&= f'(X) [ u\, dt + \sigma \, dB] 
+ \frac{1}{2} f''(X) \left[ \sigma\, dt  + O\left( dt^{3/2} \right) \right]
+ O\left( dt^{3/2} \right) \\
&= \left(u(X)f'(X) +  \frac{1}{2} \sigma(X)^{2} f''(X) \right)\, dt + \sigma(X) f'(X)\, dB
\end{aligned}
$$
Note that the $O\left( dt^{3/2} \right)$ term is omitted from the final expression because in the context of stochastic calculus, this is a differential. So as $dt \to 0$, the big $O$ approaches $0$, becoming irrelevant. 

The final line is **Ito's Lemma**. 

## Remarks (Ito's Lemma)
As previously mentioned, this is the stochastic version of the chain rule:
- If $\sigma = 0$ (i.e. no noise, is deterministic), then $dX = u(X) \, dt$, such that $df = u(X)f'(X)\, dt = f'(X) dX$. 
- This works because $(dX)^{2} = (u \, dt)^{2} = O(dt^{2})$ which is small enough to ignore. See the derivation of $(dX)^{2}$ above.

In the stochastic case, $df \neq f'(X)\,dX$ at $O(dt)$ in general because $dX \sim O\left(\sqrt{dt}\right)$, so we need to work $O(dX^{2})$ to get expression correct to $O(dt)$. 

But what about the $(\sigma(X)\, dB)^{2}$ term?
# Discretization Dilemma
## ODE Case
In the ODE case, 
$$
\frac{dx}{dt} = u(x)
\quad\quad\quad x(0) = a
$$
Let $\delta t > 0$ and set $t_{i} = i \delta t$. Then via [[#Taylor Series (Big O notation)|Taylor expansion]],
$$
\begin{aligned}
x(t_{i+1}) 
&= x(t_{i}) + \delta t \frac{dx}{dt} \bigg|_{t = t_{i}} + O\left(dt^{2}\right) \\
&= x(t_{i}) + u(x(t_{i}))\delta t + O\left( \delta t^{2} \right)
\end{aligned}
$$
But then 
$$
\begin{aligned}
u(x(t_{i+1})) 
&= u(x(t_{i}) + O(\delta t)) \\
&= u(x(t_{i})) + O(\delta t)
\end{aligned}
$$
implying it is equal at $O(\delta t)$. Implying that 
$$
x(t_{i+1}) = x(t_{i}) + u(x(t_{i+1}))\delta t + O\left(\delta t^{2}\right)
$$
We get equivalent discretizations of $x(t)$, where 
$$
\begin{aligned}
x_{i+1} &= x_i + u(x_i) \delta t, &&\quad x_0 = a \\
\tilde{x}_{i+1} &= \tilde{x}_i + u(\tilde{x}_{i+1}) \delta t, &&\quad \tilde{x}_0 = a
\end{aligned}
$$
both $x_{i+1}, \tilde{x}_{i+1} \approx x(t_{i})$. Te reason they are "equal at $O(\delta t)$" is because $x(t)$ is differentiable and smooth (no noise). 
 > This effect is similar to how the [[Riemann-Stieltjes Integral]] evaluated on an interval from left to right via [[Riemann-Stieltjes Integral#Lemma (Riemann-Stieltjes Integrability)|Riemann Sums]] gives us the same value.

Note that "equal at $O(\delta t)$" is with respect to the Taylor expansion. 

## SDE Case
Consider the [[Stochastic Differential Equations|SDE]]:
$$
dX = u(X) \, dt + \sigma(X) \, dB
\quad\quad\quad X(0) = x_{0}
$$
Set $\delta t > 0$ and discretize up to $O(\delta t)$ **only**. 
$$
X_{i+1} = X_{i} + u(X_{i}) \delta t + \sigma(X_{i}) \sqrt{\delta t} \cdot Z_{i}
\quad\quad\quad X_{0} = x_{0}
$$
where $Z_{i} \sim \mathcal{N}(0, 1)$, the [[Normal#The Normal (Gaussian) Distribution|standard normal]], independent of $X_{i}$. This is **different** from 
$$
X_{i+1} = X_{i} + u(X_{i+1}) \delta t + \sigma(X_{i+1})\sqrt{\delta t} \cdot Z_{i}
$$
The first discretization is an example of an **Ito-SDE**. The noise $Z_{i}$ is independent of the current state $X_{i}$, and the expectation is $0$, so it does not push the particle in some specific direction. 
> This is the most common type of SDE, and [[Ito's Lemma]] holds for Ito-SDEs.

## Example 1 (Discrete-Time Step with Ito's Lemma)
We can derive with [[#Ito's Lemma]].
$$
\begin{aligned}
f(X_{i+1})
&= f\left(X_i + u(X_i) \delta t + \sigma(X_i) \sqrt{\delta t} Z_i\right) \\
&= f(X_i) + f'(X_i) \left[ u(X_i) \delta t + \sigma(X_i) \sqrt{\delta t} Z_i \right] 
+ \frac{1}{2} f''(X_i) \left[ \sigma(X_i)^2 \delta t Z_{i}^{2} \right] + O(\delta t^{3/2}) \\
%%  %%
&= f(X_{i}) + \left( f'(X_{i})u(X_{i}) + f''(X_i) \cdot \frac{1}{2} \sigma(X_{i}^{2}) \right) \delta t 
+ \underbrace{f'(X_i) \sigma(X_{i}) \sqrt{\delta t} Z_{i}}_{\text{only depends on $X_{i}$}} + O(\delta t^{3/2})
\end{aligned}
$$
giving us a discrete expression for $df \approx f(X_{i+1}) - f(X_{i})$. The [[Stochastic Differential Equations#Continuum Limit of the Random Walk|continuum limit]] gives [[Ito's Lemma]]. 