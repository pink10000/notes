# Discrete (Mass)
The **conditional expectation** of $X$ given $Y$ is:
$$\E{X \mid Y = y} = \sum_{i} x_{i}\cdot f_{X|Y}(x_{i}\mid y)$$
Then, by the [[Law of Total Probability]] we get
$$\E{X} = \sum_{j}\E{X \mid Y = y_{j}}\cdot \P(Y = y_{j})$$
Given $g(x): \R \to \R$ like $g(x) = x^{2}$, the conditional expectation is 
$$\E{g(x) \mid Y = y} = \sum_{x_{i}} g(x_{i}) f_{X|Y}(x_{i}\mid y) $$

# Continuous (Density)
The **conditional expectation of** $X$ given $Y$ is:
$$\E{X \mid Y= y} = \int_{\R} x\cdot f_{X|Y}(x\mid y) dx$$
In which, by the [[Law of Total Probability]] we get
$$\begin{aligned}
\E{X} 
&= \int_{\R} \E{x \mid Y = y} \cdot f_{Y}(y) dy \\
&= \int_{\R}\int_{\R}x \cdot f_{X|Y}(x\mid y)dxdy
\end{aligned}$$
Intuitively, we are partitioning $X$ as parts of $Y$, and so finding the expectation of $X$ by conditioning on $Y$ is the same as simply finding its expectation. 

## Example 
Suppose $X,Y$ have a [[Joint Distribution|joint]] density function 
$$f_{X,Y}(x,y) = \frac{1}{y}e^{-\frac{x}{y} - y}, \quad \forall x,y > 0$$
What is $f_{X|Y}(x\mid y)?$ So, 
$$\begin{aligned}
f_{X|Y}(x\mid y) 
&= \frac{f_{X,Y}(x,y)}{f_{Y}(y)}
\end{aligned}$$
where
$$\begin{aligned}
f_{Y}(y)
&= \int_{0}^{\infty} f_{X,Y}(x,y)dx \\
&= \int_{0}^{\infty} \frac{1}{y}e^{-\frac{x}{y} - y} dx \\
&= \frac{1}{y} e^{-y} \int_{0}^{\infty} e^{\frac{-x}{y}dx}\\
&= \frac{1}{y} e^{-y} \left[-y e^{\frac{-x}{y}}\right]_{0}^{\infty} \\
&= e^{-y}
\end{aligned}$$
In particular, this is just the [[Exponential|exponential distribution]]. $Y \sim \Exp(1)$. This allows us to find
$$f_{X|Y}(x\mid y) = \frac{1}{y}e^{- \frac{x}{y}}$$
where the conditional distribution of $X$ given $Y = y$ is $\Exp\left(\frac{1}{y}\right)$. 

We now can find the expectations
$$
\E{X \mid Y = y} = y \quad \text{by mean of an exponential distribution}
$$
and 
$$\begin{aligned}
\E{X} 
&= \int_{0}^{\infty} \E{X \mid Y = y} \cdot f_{Y}(y) dy \\
&= \int_{0}^{\infty} y f_{Y}(y) dy \\
&= \E{Y} \\
&= 1
\end{aligned}$$

# General Properties
- Let $X,Y,Z$ be RVs defined on the same probability space $(\Omega, F, \P)$. 
- Let $g : \R \to \R$, $v: \R^{2}\to \R$ be such that
$$\E{|g(x)|} < \infty \quad\quad\quad \E{|v(x, y)|} < \infty$$
- As a shorthand, we can use
$$\E{g(x) \mid Y} = h(Y)$$
## Linearity
We have that 
$$\E{c_{1}g_{1}(X) + c_{2}g_{2}(Z) \mid Y = y}
= c_{1}\E{g_{1}(X) \mid Y = y} + c_{2}\E{g_{2}(Z)\mid Y = y}$$

## Positivity
If $g(X) \geq 0$ then $\E{g(X) \mid Y = y} \geq 0$.

## Affix Random Variable
$$\E{v(X, Y) \mid Y = y} = \E{v(X,y) \mid Y = y}$$
Given that we know $Y = y$, we can convey that information to $v$.

## Independence
If $X, Y$ are independent, then 
$$\E{g(X) \mid Y = y} = \E{g(X)}$$

## "Take out what is known"
$$\E{g(X)h(Y) \mid Y = y} = h(y) \cdot \E{g(X) \mid Y = y}$$

## Iterated Expectations 
$$\begin{aligned}
\E{g(X)h(Y)} \\
(1) \quad &= \int \E{g(X)h(Y) \mid Y = y} \cdot f_{Y}(y) dy \\
(2) \quad &= \mathbb{E}_{Y}\big[ h(Y)\cdot \E{g(X) \mid Y } \big]
\end{aligned}$$
where $(1)$ follows from [[Law of Total Probability]] and $(2)$ follows from [[Conditional Expectation#"Take out what is known"|"Take out what is known"]] 

This is the process of breaking down a *joint expectation* into *conditional expectations* and integrating over the distribution of the conditioning variable.