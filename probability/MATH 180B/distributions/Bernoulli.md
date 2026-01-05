# Definition
A discrete probability distribution for a random variable which takes the value 1 with probability $p$ and the value 0 with probability $q = 1 - p$. It represents a single experiment with a binary outcome (success/failure). It is denoted as $X \sim \text{Bernoulli}(p)$ or $\text{Be}(p)$.
# Probability Mass Function (PMF)
The probability function describes the likelihood of the two possible outcomes $k \in \{0, 1\}$.
$$
P(X=k) = \begin{cases} q = 1 - p & \text{for } k = 0 \\ p & \text{for } k = 1 \end{cases}
$$
This can also be expressed analytically as:
$$
P(X=k) = p^k (1-p)^{1-k} \quad \text{for } k \in \{0, 1\}
$$
# Cumulative Distribution Function (CDF)
The CDF is a step function.
$$
F(k) = \begin{cases} 0 & \text{for } k < 0 \\ 1 - p & \text{for } 0 \le k < 1 \\ 1 & \text{for } k \ge 1 \end{cases}
$$
# Key Statistics
Expectation (Mean):
$$
E[X] = p
$$
Variance:
$$
\text{Var}(X) = p(1 - p) = pq
$$
Moment Generating Function:
$$
M_X(t) = (1 - p) + pe^t
$$
## Relation to Binomial Distribution
The Bernoulli distribution is a special case of the Binomial distribution where the number of trials $n = 1$. Conversely, a Binomial distribution $B(n, p)$ is the sum of $n$ independent and identically distributed Bernoulli trials.