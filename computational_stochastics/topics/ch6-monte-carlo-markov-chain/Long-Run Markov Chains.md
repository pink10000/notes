---
tags:
  - MATH_114
---
# Example 1 (Stationary Distributions)
Consider a $2-$state [[Markov Chains|Markov Chain]] with $S = \{0, 1\}$.
$$
P = \begin{pmatrix}
3/4 & 1/4 \\ 1/6 & 5/6 \\
\end{pmatrix}
$$
and $\P(X_{1} = 0 \,|\, X_{0} = 0) = 3/4$ etc. Then 
$$
\lim_{n\to \infty} p^{n} = 
\begin{pmatrix}
0.4 & 0.6 \\ 0.4 & 0.6
\end{pmatrix}
= 
\begin{bmatrix}
\pi \\ \pi
\end{bmatrix}
$$
where $\pi = (0.4, 0.6)$ is the **stationary distribution**. 

Proof:

Let $\pi_{0} = (a_{0}, a_{1}) = (\P(X_{0} = 0), \P(X_{0} = 1))$. Note that $a_{0} + a_{1} = 1$. Then 
$$
\pi_{n} = [\P(X_{n} = 0), \P(X_{n} = 1)] = \pi_{0}p^{n}
$$
which implies that 
$$
\lim_{n\to \infty} \pi_{n} = \lim_{n \to \infty} \pi_{0} p^{n}
$$
from [[Markov Chains#Proposition (Stochastic Properties)]]. We get
$$
\lim_{n \to \infty} \pi_{0}p^{n}
= (a_{0}, a_{1}) \begin{pmatrix}
0.4 & 0.6 \\ 0.4 & 0.6 \\
\end{pmatrix}
= (0.4, 0.6)
= \pi 
$$
# Example 2 (Starting Distributions Don't Matter)
Suppose we have $3-$states and $S = \{0, 1, 2\}$ and 
$$
P = \begin{pmatrix}
3/4 & 1/4 & 0 \\ 1/8 & 2/3 & 5/24 \\ 0 & 5/6 & 1/6 \\
\end{pmatrix}
$$
With $\P$ being defined as usual. Then 
$$
\lim_{n\to\infty} p^{n} = \begin{pmatrix}
\pi \\ \pi \\ \pi
\end{pmatrix}
$$
where $\pi = (2/11, 4/11, 5/11)$. 

Set $\pi_{0} = (\P(X_{0} = i))$. Then $\pi_{n} = \pi_{0}p^{n}$ such that 
$$
\lim_{n\to \infty} \pi_{n} = \pi_{0} \cdot \begin{pmatrix}
\pi \\ \pi \\ \pi
\end{pmatrix}
= 
\left(
\pi(1) \cdot \sum_{i} \pi_{0}(i), \dots
\right)
= \pi 
$$
Because the sum of the starting distribution must equal $1$, it does not matter what distribution we start from. We will always return to stationary vector $\pi$. 

## Remark 
1. For any state $j$, the probability of a system being that state at time $n$ approaches a fixed value $\pi(j)$ as $n$ goes to infinity.
   $$
   \lim_{n\to \infty} \P(X_{n} = j) = \pi(j)
   $$
   Essentially, after enough time, the specific starting state is irrelevant. 
2. Once the distribution reaches the long-term state $\pi$, it stays there. The distribution is **invariant** under the transition matrix $P$.
   $$
   \begin{aligned}
   \pi = \lim_{n\to \infty} \pi_{n+1} 
   &= \lim_{n\to\infty} \pi_{0} p^{n+1} \\
   &= \lim_{n\to\infty} (\pi_{0} p^{n}) \cdot p \\
   &= \pi P
   \end{aligned}  
   $$
   So we get that $\pi$ is a row eigenvector of $P$. 
# Theorem (Average Transition Behavior)
For a Markov Chain, 
$$
\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} p_{k}(i, j)
= \lim_{n \to \infty} p_{n}(i, j) = \pi(j)
$$
We are essentially asking:
> If we simulated all possible Markov Chains from state $i$, what fraction of them would be in state $j$ on average? 

The idea is that even if we bounce around $j$, the average of those probabilities settles to $\pi(j)$.

Proof:
$$
\begin{aligned}
\frac{1}{n} \sum_{k=0}^{n-1} p_{k}(i, j) 
&= \frac{1}{n} \sum_{k=0}^{n-1} \P(X_{k} = j \,|\, X_{0} = i) \\
&= \frac{1}{n} \sum_{k=0}^{n-1} \E{\mathbb{1}(X_{k} = j) \,|\, X_{0} = i} \\
&= \E{ \frac{1}{n} \sum_{k=0}^{n-1} \mathbb{1}(X_{k} = j) \,|\, X_{0} = i } \\
&\to \pi(j)
\end{aligned}
$$
as $n \to \infty$. So, the mean fraction of the time spent in state $j$ is shown by $\pi(j)$. 

# Theorem (Time Average of the Indicator)
What if we ran every Markov Chain, but every time we reached state $i$ at some time $k$, we counted it. What fraction of the time do we spend on state $i$? More formally, what is 
$$
\frac{1}{n} \sum_{k=1}^{n} \mathbb{1}\{X_{k} = i\}
$$
where 
$$
\mathbb{1}(X_{k}) = \begin{cases}
1 & X_{k} = i \\ 
0 & \text{otherwise}
\end{cases}
$$
If $n \to \infty$ then this value converges to $\pi(i)$ for all $i \in S$.   

# Theorem (Law of Large Numbers for Markov Chains)
Instead of counting visits, we can count the "reward" of visiting specific states.
$$
\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} g(X_{k}) = \mathbb{E}_{\pi}(g(X))
$$

# Remarks (Markov Chain Computation)
- We can view [[Markov Chains]] as *evolutions* of probability vectors (PMFs): $\pi_{0}, \pi_{1}, \dots, \pi_{n+1} = \pi_{n}P$. But this is hard to compute for large state spaces (when $|S|$ is large). 
- Markov Chains are a random sequence of states $X_{0}, X_{1}, \dots \in S$, which is often easier to simulate. 
- Recall from [[Inversion#Discrete Case]] that we can generate discrete random variables $X$ where $\P(X = i) = p_{i}$ for $i \in \{1, 2, 3\}$ and $p_{1} + p_{2} + p_{3} = 1$. 

# Algorithm (Generate/Simulate Markov Chains)
**Input**: Transition matrix $P$ and an initial distribution $\pi_{0}$. 

**Output**: A Markov Chain $X_{0}, \dots, X_{n} \in S$ where $X_{k} \sim \pi_{k}$. 

1. Generate $X_{0} \sim \pi_{0}$. 
2. For $k = 1$ to $n$: 
	1. Generate $X_{k+1}$ from $p(X_{k}, -)$, the PMF over $S$ given by the $X_{k}$'th row of $P$.
3. Repeat this $N$ times to get a sample from $\pi_{n}$. 

The key idea is to generate the distribution $\pi$ by simulating Markov Chain $\{X_{n}\}^{\infty}_{n =0}$ with a stationary distribution $\pi$. Often $\pi$ is known up to a normalizing constant. By [[#Theorem (Average Transition Behavior)]], [[#Theorem (Time Average of the Indicator)]], and [[#Theorem (Law of Large Numbers for Markov Chains)]] this algorithm converges to $\pi$. 

## Remark (Discreteness)
This algorithm also works for discrete time and states. Let $X \in S$ be discrete random variables, e.g. $S = \{1, 2, \dots, N\}$. Then the *target* PMF of $X$ is 
$$
\pi = (\pi(1), \dots, \pi(N))
$$
where 
$$
\forall i \in S, \pi(i) = \P(X = i)
$$
Stationary distribution $\pi$ has a special [[Probability Distribution Function|PMF]] form:
$$
(i) = \frac{1}{Z} b(i) > 0
$$
for all $i \in S$, where $b(i) > 0$ are known and $Z > 0$ is an unknown normalization. In particular, 
$$
\sum_{i \in S} (i) = 1 \iff \sum_{i \in S} b(i) = Z
$$
> You can think of $b(i)$ as the "score" or weight of each state. If $b(i) > b(j)$, then state $i$ is more likely than state $j$. $Z$ is how we normalize the PMF $(i)$. 

In practice, $Z$ is hard to compute, as it is the sum of $N$ terms. $Z$ is called the **partition function** in statistical physics. 