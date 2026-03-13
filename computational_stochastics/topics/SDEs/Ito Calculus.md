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

## SDE Case (Ito-SDE)
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
> This is the most common type of SDE, and [[Ito Calculus]] holds for Ito-SDEs.

# Example 1 (Discrete-Time Step with Ito's Lemma)
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
giving us a discrete expression for $df \approx f(X_{i+1}) - f(X_{i})$. The [[Stochastic Differential Equations#Continuum Limit of the Random Walk|continuum limit]] gives [[Ito Calculus]]. 

# Example 2 (Simple Ito Lemma)
We can do a much easier example. What is $df$ for $f(x) = x^{2}$? Using [[#Ito's Lemma]], 
$$
\begin{aligned}
df
&= (-\alpha Xf' + Df'')\,dt + f'\sqrt{2D} \, dB \\
&= (-2\alpha X^{2} + 2D)\,dt + 2X\sqrt{2D}\, dB \\
\end{aligned}
$$
where $\alpha$ represents a constant to replace $u(X)$.

Because [[Stochastic Process|stochastic processes]] are nowhere differentiable, we cannot describe a simple [[Derivative|derivative]] of a function. Instead, we discuss how it updates deterministically and how multiplicative noise affects it. 

# Backwards Ito SDE
The first SDE of [[#SDE Case (Ito-SDE)]] is covered by Examples [[#Example 1 (Discrete-Time Step with Ito's Lemma)|1]] and [[#Example 2 (Simple Ito Lemma)|2]]. We can show the derivation for the second rule, where diffusion depends on the future state. This is the continuum limit of 
$$
X_{i+1} = X_{i} + u(X_{i+1})\delta t + \sigma(X_{i+1}) \sqrt{\delta t } \cdot Z_{i}
$$
for [[Normal#The Normal (Gaussian) Distribution|standard normal]] $Z_{i}$. Let $X_{i},Z_{i}$ be independent and $\delta t > 0$. The SDE of this discretized form is 
$$
dX = u(X)dt + \sigma(X) \bullet dB
$$
This is 
- **Anticipatory**: Diffusion term depends on future state.
- $\E{dX} \neq \E{u(X)}\, dt$ because the correlation between $\sigma(X_{i+1})$ and $dB$ creates additional drift. 
- The bullet $\bullet$ is used to represent the *backwards* Ito. This represents the anticipatory nature of the SDE.
> Not sure if continuum limit gives the correct SDE.

# Stratanovich SDE
We take the continuum limit of 
$$
X_{i+1} = X_{i} + u\left( \frac{X_{i} + X_{i+1}}{2} \right) \delta t 
+ \sigma \left( \frac{X_{i} + X_{i+1}}{2} \right)\sqrt{\delta t} Z_{i}
$$
where $Z_{i} \sim \mathcal{N}(0, 1)$ and $X_{i},Z_{i}$ are independent with $\delta t > 0$. The SDE is 
$$
dX = u(X)\, dt + \sigma(X) \, dB
$$
> Notation can **vary**. 
# Remarks (Ito v.s Ito Backwards)
The [[#SDE Case (Ito-SDE)|Ito-SDE]] can sometimes be written
$$
dX = u(X, t)\, dt + \sigma(X, t) \ast dB
$$
where the asterisk $\ast$ represents non-anticipatory updates. 

We consider Ito-SDEs most common since 
$$
\E{dX} = \E{u(X, t)} \,dt
$$
Different SDEs can be transformed into each other. Suppose $X(t)$ satisfies 
$$
d(X) = u(X) \, dt + \sigma(X) \bullet dB
$$
or the [[#Backwards Ito SDE|backwards Ito]]. Then 
$$
dX = \left( u(X) + \sigma(X)\sigma'(X) \right)\, dt + \sigma(X)\,dB
$$
represents the [[#SDE Case (Ito-SDE)|Ito SDE]]. In general, different SDEs have different chain rules. 

# Example 3 (Apply OU on Ito SDE)
We can analyze an [[Stochastic Differential Equations#Ornstein-Uhlenbeck Process (OU)|OU-process]] with [[#Ito's Lemma]]. Recall that OU-processes are of the following form. Let $X(t) \in \R$ with 
$$
dX = -\alpha X dt + \sqrt{2D}\, dB
\quad\quad\quad X(0) = x_{0}
$$
where $\alpha, D$ are constants and $D > 0$. We can take the [[Expectation|expectation]] to get 
$$
d\E{X} = -\alpha \E{X}dt
$$
Set $y(t) = \E{X(t)}$. Then 
$$
\frac{dy}{dt} = -\alpha y \implies y(t) = x_{0} \exp(-\alpha t) 
$$
giving us the general form for the expectation. Recall from [[#Example 2 (Simple Ito Lemma)|example 2]] that 
$$
d(X^{2}) = (-2 \alpha X^{2} + 2D)dt + 2X\sqrt{2D} \, dB
$$
On average, where is the particle spending time in? This means we need to take the expectation:
$$
\begin{aligned}
d\left(\E{X^{2}}\right)
&= (-2 \alpha \E{X^{2}} + 2D) dt + \underbrace{\E{2X \sqrt{2D}\, dB}}_{0 \text{ since Ito SDE}} \\
\frac{d}{dt} \left( \E{X^{2}} \right) &= -2\alpha \left( \E{X^{2}} \right) + 2D \\
\end{aligned}
$$
Letting $y(t) = \E{X^{2}}$, this amounts to solving 
$$
\frac{dy}{dt} = -2\alpha y + 2D
$$
where $y(0) = x_{0}^{2}$. Now we solve like a typical ODE. Write 
$$
y(t) = y_{h}(t) + y_{p}(t)
$$
and solve for the homogeneous solution:
$$
\frac{dy_{h}}{dt} = -\alpha y_{h} \implies y_{h}(t) = Ae^{-2 \alpha t}
$$
and the particular solution:
$$
0 = -2\alpha y_{p} + 2D 
\implies y_{p} = \frac{D}{\alpha}
$$
This implies that 
$$
y(t) = \E{X^{2}} = Ae^{-2\alpha t} + \frac{D}{\alpha}
$$
We can also solve via separating the variables:
$$
\begin{aligned}
\int \frac{1}{2D - 2\alpha y} \, dy &= \int dt \\
-\frac{1}{2\alpha } \log(2D - 2\alpha y) = t + C
\end{aligned}
$$
The rest is trivial. 

# Example 4 (Geometric BM)
Let $X(t) \in \R$. Consider **Geometric Brownian Motion**:
$$
dX = \mu X \, dt + \sigma X \, dB
\quad\quad\quad X(0) = x_{0}
$$
The expectation gives
$$
\begin{aligned}
d(\E{X}) 
&= \mu \E{X} \, dt + \underbrace{\E{\sigma X dB}}_{0 \text{ since Ito SDE}} \\
\frac{d}{dt}\E{X} &= \mu \E{X} \\
\E{X} &= x_{0}e^{\mu t}
\end{aligned}
$$
We can again apply this to $f(X) = X^{2}$ with [[#Ito's Lemma]] to find the second moment:
$$
\begin{aligned}
df &= \left( \mu X f' + \frac{1}{2} \sigma^{2}X^{2}f'' \right)\, dt + f' \sigma X dB \\ 
d(X^{2}) &= \left( 2 \mu X^{2} + \sigma^{2} X^{2} \right) dt + 2\sigma X^{2} dB \\
d\left(\E{X^{2}}\right) &= (2 \mu + \sigma^{2})\left(\E{X^{2}}\right) dt + 0\\
\frac{d}{dt}\left( \E{X^{2}} \right) &= (2\mu + \sigma^{2})\cdot \E{X^{2}} \\
\E{X^{2}} &= x_{0}^{2} \exp(2 \mu t)
\end{aligned}
$$
or the second [[Moments|moment]]. 
> **Context:** GBM is the standard model for stock prices because the noise is multiplicative ($X dB$). This ensures that returns $\frac{dX}{X}$ are independent of the absolute price level, and it prevents the price from ever becoming negative.

# Example 5 (Geometric BM with Log Expectation)
To solve the SDE exactly, we use Ito's Lemma on $f(X) = \log X$. So, 
$$
\begin{aligned}
d(\log X) 
&= \left(
\mu X \frac{1}{X} + \frac{1}{2} \sigma^{2}X^{2} \left(-\frac{1}{X^{2}}\right)  
\right) dt 
+ \frac{1}{\lambda} \sigma X dB \\ 
&=\underbrace{\left(\mu - \frac{1}{2} \sigma^{2} \right) dt + \sigma \, dB}_{\text{Brownian Motion with Drift!}}
\end{aligned}
$$
The result is [[Simulating Brownian Motion#BM with Drift|Brownian Motion with Drift]] where the coefficients are *constants*. This means that $\log X$ is [[Normal]]. 

Indeed, 
$$
\begin{aligned}
\E{\log X} &= \left(\mu - \frac{1}{2} \sigma^{2} \right)t + x_{0} \\
\var(\log X) &= \sigma^{2}t \\
\log X(t) &\sim \mathcal{N}\left[ 
    \left(\mu - \frac{1}{2} \sigma^{2} \right)t + x_{0},
    \sigma^{2}t
\right]
\end{aligned}
$$
> **Insight:** The $-\frac{1}{2}\sigma^2$ term is the "Ito Correction." It shows that volatility actually drags down the *median* growth of a stock, even if the *average* growth remains $\mu$.
# Example 6 (Arithmetic BM with Drift)
Consider an SDE with with constant [[Stochastic Differential Equations#General Stochastic Differential Equations|additive noise]] and [[Simulating Brownian Motion#BM with Drift|drift]]. Let $X(t) \in \R$ and 
$$
dX = u\, dt + \sqrt{2D} \, dB
\quad\quad\quad X(0) = x_{0}
$$
where $u, D$ are constants and $D > 0$. The [[Expectation|expectation]] gives the linear trend:
$$
\begin{aligned}
d\E{X} &= u\,dt \\
\frac{d}{dt}\E{X} &= u \\ 
\E{X(t)} &= ut + x_{0}  
\end{aligned}
$$
Using [[#Ito's Lemma]] with $f(X) = X^{2}$, 
$$
\begin{aligned}
df &= \left( 2u X + 2D \right)dt + 2X\sqrt{2D} \, dB \\
d\E{X^{2}} &= (2u \E{X} + 2D)dt \\
\frac{d}{dt} \E{X^{2}} &= (2u^{2}t + 2ux_{0}) + 2D \\
\E{X^{2}}&= u^{2}t^{2} + 2u x_{0} t + 2Dt + x_{0}^{2} \\
\end{aligned}
$$
This also gives us the variance. 
$$
\var X(t) = \E{X^{2}} - \left(\E{X}\right)^{2} = 2Dt
$$
We also know the full distribution:
$$
X(t)
= \int_{0}^{t} dX 
= \int_{0}^{t} udt' + \int_{0}^{t}\sqrt{2D} \,dB + x_{0}
= ut + x_{0} + \sqrt{2D}\, B(t)
$$
implying that $X(t) \sim \mathcal{N}(ut + x_{0}, 2Dt)$, since $B(t) \sim \mathcal{N}(0, t)$ by [[Stochastic Differential Equations#Definition (Brownian Motion, Wiener Process)|definition]].
> **Comparison:** Unlike GBM (where variance grows exponentially), Arithmetic BM has a variance that grows linearly with time ($2Dt$). This is used for physical diffusion (e.g., a particle in a flow) rather than finance, as it allows for negative values.

