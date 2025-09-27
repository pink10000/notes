---
tags:
  - MATH_180B
---
It is the probability of all possible pairs of two random variables. 

## Discrete Case
Given $X, Y$ on $\Omega$ where 
$$
\begin{aligned}
X &: \Omega \to \{x_{1}, x_{2}, \cdots \} \\
Y &: \Omega \to \{y_{1}, y_{2}, \cdots \} \\
\end{aligned}
$$
The **joint probability mass function**:
$$
f_{X,Y}(x_{i},y_{i}) = P(X = x_{i}, Y = y_{i})
$$
where the **marginal distribution** is
$$
f_{X}(x) = \P(X = x_{i}) = \P\left(\bigcup_{y_{i}} \{X = x_{i}, Y = y_{i} \}\right) = \sum_{j}f_{X,Y}(x_{i}, y_{i})
$$
and similarly with $Y$.


#### Example
Let $\Omega$ be the infinite sequence of coin flips, 
$$
\{0,1\}^{\mathbb{N}} = \{w \mid w_{1}w_{2}\cdots , w \in \{0, 1\}\}
$$
and let each flip be independent and fair.

Suppose we had a RV, $X : \Omega \to \mathbb{R}$ where $X(\omega) = \omega_{1}+ \omega_{2}$, the sum of the first $2$ coin flips. 
- $X = \{0, 1, 2\}$ 
- $P_{X}(0) = P(X = 0) = P(\omega_{0} + \omega_{1} = 0) = 0.5^{2}= 0.25$ 
- $P_{X}(1) = P(\omega_{1} + \omega_{2} = 1 ) = 0.50$
- $P_{X}(2) = 0.25$ 

Conditional Distribution of $X$ given event $A = \{w_{1} = 0\}$. Or, 
$$
P(X = 0 \mid A) = \frac{P(X = 0, \omega_{1} = 0 )}{P(\omega_{1} = 0)} = \frac{0.25}{0.5} = 0.5
$$
$$
P(X = 1 \mid A) = \frac{P(X = 1, \omega_{1} = 0 )}{P(\omega_{1} = 0)} = \frac{0.25}{0.5} = 0.5
$$
Let $A$ be an event in $\Omega$ where $A \subseteq \Omega$. Then, let
$$
X : \Omega \to \{x_{1}, x_{2}, \cdots \}
$$
The [[Conditional Probability]] mass function of $X$ given $A$ is 
$$
P_{X}(x_{i} \mid A) = P(X = x_{i} \mid A)
$$


#### Example 
Throw $2$ fair dice $\{1, 2,3,4,5,6\}$. Let 
$$
X = \text{ sum of the two dice} \quad A =\{X \leq 5\}
$$
The sample space of $X$ is $\{2, 3, \cdots 10, 11, 12\}$. 
$$
P_{X}(2 \mid A) = \frac{P(X = 2, A)}{P(A)} = \frac{P(X = 2)}{P(A)}
$$
where $P(X = 2) = P(\{1, 1\}) = \left(\frac{1}{6}\right)^{2}$. 
- $P(X = 3) = P((1, 2), (2, 1)) = 2 \left(\frac{1}{6}\right)^{2}$ 
- $P(X = 4) = 3 \left(\frac{1}{6}\right)^{2}$
- $P(X = 5) = 4 \left(\frac{1}{6}\right)^{2}$

Returning back to $P_{X}(\cdot \mid A)$, we get
- $P_{X}(2 \mid A) = \frac{1 / 36}{1 / 36} \frac{1}{1 + 2 + 3 + 4} = \frac{1}{10}$ 
- $P_{X}(3 \mid A) = \frac{2}{10}$
- $P_{X}(4 \mid A) = \frac{3}{10}$
- $P_{X}(5 \mid A) = \frac{4}{10}$

We can find the expected value also:
$$
E[X \mid A] = \sum_{X_{i}}x_{i}P_{X}(x_{i}\mid A)
$$
We have:
$$
E[X \mid A] = 2 \cdot \frac{1}{10} + 3 \cdot \frac{2}{10} + 4 \cdot \frac{3}{10}+ 5 \cdot \frac{4}{10} = \frac{40}{10}= 4
$$
Without the conditional event $A$, 
$$
E[X] = 2\cdot E[D] = 2 \left( \frac{1}{6}(1 + 2 + 3 + 4 + 5 + 6) \right) = 2 \cdot 3.5 = 7
$$

