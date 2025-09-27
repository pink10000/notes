---
tags:
  - MATH_180B
---
- Let $\xi_{1}, \xi_{2}, \cdots$ be **independent, identically, distributed** RVs.
- Let $N$ be a discrete RV independent of $\xi_{i}$ that takes a value in $\N$. It is also pairwise independent to $\xi_{i}$.
- $X = \sum_{i=1}^{N} \xi_{i}$ is called a random sum

# Expectation of $X$
$$
\begin{aligned}
\E{\sum_{i=1}^{N} \xi_{i}} 
&= \mathbb{E}_{N}\left[ \E{\sum_{i=1}^{N} \xi_{i} \mid N}  \right] \\
&= \sum_{n=0}^{\infty} \P_{N}(n) \cdot \E{\sum_{i=1}^{N} \xi_{i}\mid N = n } \\
&= \sum_{n=0}^{\infty} \P_{N}(n) \cdot n \cdot \E{\xi_{i}} \\
&= \E{N} \cdot \E{\xi_{i}}
\end{aligned}
$$
1. Decompose to be conditional on $N$ since the summation depends on $N$
2. Since it is conditional on $N$, and we need to find the expectation, we can expand it out. 
3. Independence of $N$ to $\xi_{i}$.

# Variance of $X$
Denote $\E{\xi_{i}} = m$ and $\var(\xi_{i}) = \sigma^{2}$
$$
\begin{aligned}
\var(X) 
&= \E{(X - \E{X})^{2}} \\
&= \E{\left(\sum_{i=1}^{N} \xi_{i} - \E{N} \cdot m \right)^{2}} \\
&= \sum_{n=0}^{\infty} \E{ \left(\sum_{i=1}^{N} \xi_{i} - \E{N}\cdot m \right)^{2} \mid N = n } \cdot \P_{N}(n) \\ 
&= \sum_{n=0}^{\infty} \E{ \left( \sum_{i=1}^{N} \xi_{i} - (n \cdot m) + m(n - \E{N})\right)^{2} } \cdot \P_{N}(n) \\ 
\end{aligned}
$$
Upon expansion, we get three terms:
$$
\E{\left(\sum_{i=1}^{n}\xi_{i} - nm \right)^{2}}
$$
which is $n \cdot \var(\xi_{i})$. If we suppose $S$ is the summation, then $\E{S} = mn$ as $\E{\xi_{i}} = m$ and there are $n$ iid RVs. Then, we apply the definition of variance. 
$$
2\E{ \left( \sum_{i=1}^{n}\xi_{i} - nm \right) \cdot m(n - \E{N}) }
$$
which is $0$ since the left term of $\cdot$ is $0$. 
$$
\E{m^{2}\cdot\left(n - \E{N}\right)^{2}} = m^{2}\var(N)
$$
is our final term. So,
$$
\begin{aligned}
&= \sum_{n=0}^{\infty} \left( n\var(\xi_{i}) + m^{2}\var(N) \right) \cdot \P_{N}(n) \\
&= m^{2}\var(N) + \sum_{n=0}^{\infty} n\P_{N(n)} \sigma^{2} \\
\var(X) &= \sigma^{2}\E{N} + m^{2}\var(N)
\end{aligned}
$$
In summary,
$$
\begin{aligned}
\E{X} &= \E{N} \cdot \E{\xi_{i}} \\
\var(X) &= \E{N} \cdot \var(\xi_{i}) + (\E{\xi_{i}})^{2}\var(N)
\end{aligned}
$$

