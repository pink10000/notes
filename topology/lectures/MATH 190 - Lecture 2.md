---
tags:
  - MATH_190A
  - MATH_190A_Lecture
---
Review on 
- [[Metric Space]], 
- [[Continuity]], 
- [[Metric Space#Neighborhood|neighborhoods]]
- [[Metric Space#Open & Closed]] 
- 

# Proposition (Continuity around Neighborhoods)
If $f$ is continuous at $a \in X \iff$ for every neighborhood $N$ of $f(a)$, the inverse image $f^{-1}(N)$ is a neighborhood of $a$. 

Proof (Forward):
Given neighborhood $N$ of $f(a)$, that given $B_{\vepsi}(f(a))$ for some $\vepsi > 0$, then by continuity, $\exists \delta > 0$ such that 
$$
B_{\delta}(a) \subseteq f^{-1}\bigg(B_{\vepsi}(f(a))\bigg)
$$
which means 
$$
B_{\delta}(a) \subseteq f^{-1}(N)
$$
so $f^{-1}(N)$ is a neighborhood of $a \in X$.

Proof (Backward):
Given $B_{\vepsi}(f(a))$, this is a neighborhood of $f(a)$. Therefore by assumption, 
$$
f^{-1}(B_{\vepsi}(f(a)))
$$
is a neighborhood of $a$. Hence, $\exists \delta > 0$ such that
$$
B_{\delta}(a) \subseteq f^{-1}\bigg(B_{\vepsi}(f(a))\bigg)
$$
and it is continuous. 

# Theorem 
A function
$$
f: (X, d_{1}) \to (Y, d_{2})
$$
is **continuous everywhere** $\iff$ for every open set $U$ in $Y$, $f^{-1}(U)$ is open in $Y$. 

Proof: 
See [[Continuity#Proposition (Topological Characterization of Continuity)]]. 

In class, we proved it like this:

Given open $U$ in $Y$, take $a \in f^{-1}(U)$. Since $U$ is open, then it contains some $B_{\vepsi}(f(a))$ with $\vepsi > 0$. By continuity of $f$ at $a$, we have $\exists \delta > 0$ such that by the Triangle Inequality,
$$
\begin{aligned}
d(y, a) 
&\leq d(y, x) + d(x, a) \\
&\leq \delta + r \\
&\leq (\vepsi - r) + r \\
&\leq \vepsi
\end{aligned}
$$
such that 
$$
B_{\delta}(a) \subseteq f^{-1}\bigg( B_{\vepsi}(f(a)) \bigg) \subseteq f^{-1}(U)
$$
indeed, $f^{-1}(U)$ is a neighborhood of $a$. As $a$ arbitrary, this is true for $a \in f^{-1}(U)$.

Conversely, given $a \in X$ and $B_{\vepsi > 0}(f(a))$ in $Y$, WTS $\exists B_{\delta}(a) \subseteq f^{-1}(B_{\vepsi}(f(a)))$. We know $B_{\vepsi}(f(a))$ is an open set, so its preimage must also be open in $X$. Thus, it must contain $B_{\delta}(a)$. 