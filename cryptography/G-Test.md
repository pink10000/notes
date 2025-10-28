---
tags:
  - MATH_187A
---
# Definition (G-Test)
Suppose $X$ is a random variable with finitely many values $a_{1}, \dots, a_{n}$ and let $p_{i} = P(X = a_{i})$. Suppose we make $N$ observations of the values $a_{1}, \dots, a_{n}$ and that $O_{i}$ is the number of observations of $a_{i}$ that we made. 

Let $E_{i} = Np_{i}$, and define
$$
G = 2 \sum_{1=1}^{n} O_{i} \ln \left( \frac{O_{i}}{E_{i}} \right)
$$
If $O_{i} = 0$ for some $i$, then the summand is $0$. If there exists an $i$ such that $E_{i} = 0$ but $O_{i} \neq 0$, then $G = \infty$. 

## Gibbs' Inequality 
We have that 
$$
G \geq 0
$$
Moreover,
$$
G = 0 \iff (\forall i \in \N_{\leq n})(O_{i} = E_{i})
$$
Proof: 

$(\impliedby)$ If $O_{i}  = E_{i}$ then $\ln(O_{i}/E_{i}) = \ln1 = 0$, and $G = 0$. 

$(\implies)$ The summand is always non-negative, so it must be equal to $0$. 

> What this tells us is that if $G$ is small, then it matches our expectations. Otherwise the observation is out of ordinary. 

# Wilks' Theorem
Suppose the $N$ observations of the values $a_{1}, \dots, a_{n}$ that we make are in fact *independent* observations of the random variable $X$. For large values of $N$, the values of $G$ are well approximated by a chi-square distribution with $n - 1$ degrees of freedom. 

 The values of $G$ are well approximated by a chi-square distribution with $n - 1$ degrees of freedom. Indeed, the probability that $G$ lands inside some interval $(a, b)$ is 
$$
\int_{a}^{b} f_{n}(x) dx
$$
So for our $G$, the probability of observing a value of $G' > G$ is 
$$
\int_{G}^{\infty} f_{n}(x) dx = 1 - \int_{0}^{G}f_{n}(x) dx
$$
> This is how we decide if $G$ is small or large.

## Heuristic Addendum
The approximation of $G$ is good enough as long as the vast majority of the expected counts $E_{1}, \dots, E_{n}$ are all at least $5$.