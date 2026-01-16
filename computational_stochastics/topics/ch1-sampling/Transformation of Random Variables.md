---
tags:
  - MATH_114
---
We want to define this more generally. What if we wanted to do some transformation on the RV $X$? 

# Lemma (Change of Variables)
Let $X$ be a RV $X \sim f_{X}$. Let $\alpha : \mathbb{R}\to \mathbb{R}$ a real-valued function that is [[Derivative#Definition|continuously differentiable]](i.e. $f_{X}'$ is [[Continuity#Definition (Set)|continuous]]) with $\alpha' > 0$ (so that $\alpha$ is strictly increasing, and therefore invertible). Let $Y = \alpha(x)$, a [[Probability Distribution Function|PDF]]. Then 
$$
f_{Y}(y) = \frac{f_{X}(x)}{\alpha'(x)} \quad\quad\quad (x = \alpha^{-1}(y))
$$

Proof: 

Given $X,Y$ as RVs and $Y = \alpha(X)$, then if we take $y \in \R$ with $x = \alpha^{-1}(y)$, then 
$$
\begin{aligned}
F_{Y}(y) 
&= P(Y \leq y) \\
&= P(\alpha(X) \leq \alpha(x)) \\ 
&= P(X \leq x) && \quad (\star) \\
&= F_{X}(x)
\end{aligned}
$$
we have that $F_{Y}(y) = F_{X}(x)$. We can differentiate to get the [[Probability Distribution Function|PDF]]. 
$$
\begin{aligned}
F_{Y}(y) &= F_{X}(x) \\ 
f_{Y}(y) \cdot \alpha'(x) &= f_{X}(x)
\end{aligned}
$$
> We work with the CDF because the events are nicer to manipulate arithmetically.

What if $\alpha$ is **strictly decreasing**, where $\alpha' < 0$? We get the same argument, but the step $(\star)$ means we can do 
$$
P(\alpha(X) \leq \alpha(x)) \implies P(x \leq X) = 1 - F_{X}(x)
$$
Again, by differentiation to get the [[Probability Distribution Function|PDFs]], 
$$
\begin{aligned}
F_{Y}'(y) \frac{dy}{dx} &= -F_{X}'(x) \\
f_{Y}(y) \alpha'(x) &= -f_{X}(x)
\end{aligned}
$$
and since $\alpha' < 0$, then both PDFs are positive (or rather, non-negative) then we are fine. In general, for $\alpha$ [[Monotonic|strictly increasing/decreasing]], then 
$$
f_{Y}(y) = \frac{f_{X}(x)}{| \alpha' (x)|}
$$
## Remark (Change Must be Monotonic)
In particular, if $\alpha$ is not [[Monotonic]], we cannot say anything about $Y$, since it would no longer be injective. For example, consider $Y = X^{2}$. 

## Example 1 
Let $X \sim N(0, 1)$ the standard [[Normal]] distribution and $Y = \alpha(x) = \sigma X + \mu$. The PDFs of $f_{X}, f_{Y}$ of $X, Y$ respectively, are related by 
$$
\begin{aligned}
f_{Y}(y) 
&= \frac{f_{X}(x)}{\alpha'(x)} \\
&= \frac{1}{\sigma} \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2} x^{2} \right) \\
&= \frac{1}{\sqrt{2\pi \sigma^{2}}} \exp\left( -\frac{1}{2\sigma^{2}} (y - \mu)^{2} \right) \\
&\implies Y \sim N(\mu, \sigma^{2})
\end{aligned}
$$
In particular, the second step is achieved be seeing that $X = \alpha^{-1}(y) = \frac{y - \mu}{\sigma}$. 

# Transformation of Multivariate Random Variables
Let $\unl{X} = (X_{1}, \dots, X_{n}) \in \R^{n}$ be a vector valued RV. The [[Joint Distribution]] of $\unl{X}$ is defined by 
$$
F_{\unl{X}}(\unl{x}) = P(X_{1} \leq x_{1}, \dots, X_{n} \leq x_{n}) 
\quad\quad\quad
\forall \unl{x} = (x_{1}, \dots, x_{n}) \in \R^{n}
$$
If we assume that the joint PDF exists, then it is defined as 
$$
f_{\unl{X}} : \R^{n} \to [0, \infty)
$$
is related by 
$$
F_{\unl{X}} (\unl{x}) = \int_{-\infty}^{x_{n}}\dots \int_{-\infty}^{x_{1}}
f_{\unl{X}}(u_{1}, \dots, u_{n}) \,du_{1}\dots du_{n}
$$
---
Let $T : \R^{n} \to \R^{n}$ be an invertible[^1] transformation with "sufficiently smooth"[^2] components. 
$$
\begin{aligned}
T : \R^{n} &\to \R^{n} \\ 
\unl{x} &\mapsto \unl{y} = T(\unl{x}) \\ 
&\quad\,\,\, \unl{x} = T^{-1}(\unl{y})
\end{aligned}
$$
Recall these are vector valued functions. The Jacobian for $T^{-1}$ is determined by 
$$
J(\unl{y}) = \det\left( \frac{\del x_{i}}{\del y_{j}} \right)
$$
where $T^{-1}$ maps a vector from the codomain to $\unl{x}$ is the domain. In particular, $T^{-1}(\unl{y}) = \unl{x}$. This tells us that each component $x_{i}$ of $\unl{x}$ is defined as a function of $y_{j}$ in $\unl{y}$, the prerequisite for calculating the Jacobian. 

[^1]: To guarantee surjectivity. 
[^2]: This means that it's derivative $T'$ is continuous, or that it is of class $C^{1}$. See [here](https://en.wikipedia.org/wiki/Smoothness). 

---
## Theorem (Multivariate Change of Variables)
Suppose $\unl{X} \in \R^{n}$ is a RV with [[Joint Distribution|joint PDF]] $f_{\unl{X}}$. Then the joint density of $\unl{Y}$ is given by 
$$
f_{\unl{Y}}(\unl{y}) = f_{\unl{x}} \left(T^{-1}(\unl{y}) \right) \cdot |J(\unl{y})| 
$$
Proof:

The idea is to work with the CDF and then work towards the PDF by deriving $n$ times. So, consider this hyperbox in $\R^{n}$:
$$
B = \prod_{i=1}^{n} (a_{i}, b_{i}]
$$
Then via definition of joint probabilities,
$$
\begin{aligned}
P(\unl{X} \leq B) 
&= P(a_{1} \leq x_{1} \leq b_{1}, \dots, a_{n} \leq x_{n} \leq b_{n}) \\ 
&= \int_{B} f_{\unl{X}}(x) \, d\unl{x} \\ 
&= \int_{T(B)} f_{\unl{X}}(T^{-1}(\unl{y})) \,|J(\unl{y})| \, d{\unl{y}} \\ 
\end{aligned}
$$
And since $\unl{X} \in B \iff \unl{Y} = T(\unl{X}) \in T(B)$, then we can change the domain of the integral. But also, this tells us that 
$$
\begin{aligned}
\int_{T(B)} f_{\unl{Y}}(\unl{y}) \, d\unl{y} 
&= P(Y \in T(B)) \\ 
&= \int_{T(B)} f_{\unl{X}}(T^{-1}(\unl{y})) \,|J(\unl{y})| \, d{\unl{y}} \\ 
\end{aligned}
$$
which 
$$
\implies f_\unl{Y}(\unl{y}) = f_{\unl{X}}(T^{-1}(\unl{y})) \cdot |J(\unl{y})|
$$

