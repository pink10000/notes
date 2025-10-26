---
tags:
  - MATH_187A
---
# Definition (Index of Coincidence)
Let $N$ be the length of some text and for each letter $\alpha,$ let $N_\alpha$ be the number of times $\alpha$ occurs in this text. The **index of coincidence** of the text, denoted $\text{IC}$, is the number 
$$
\text{IC} = 26 \cdot \sum_{\alpha \in \{A, \dots, Z\}} \frac{N_\alpha(N_{\alpha}- 1)}{N(N - 1)}
$$
We can use this to break [[Vignere Cipher]].
# Lemma (Largest Possible IC)
The largest possible $\text{IC}$ is $26$. This is if $N_{\alpha} = N$ for some $\alpha$, but $N_{\alpha'} = 0$ for any $\alpha' \neq \alpha$. This text must be monographic (composed entirely of a single letter). 

# Theorem (Sufficient Length for Text)
Let $N$ be the length of some [[Text]] and for each letter $\alpha$, let $N_\alpha$ be the number of times $\alpha$ occurs in this text. Let
$$
p_{\alpha} = N_{\alpha} / N
$$
and if $N$ is very large, then 
$$
\text{IC} \approx 26 \sum_{\alpha \in \{A, \dots, Z\}} p_{\alpha}^{2}
$$

Proof: It suffices to show that if $N$ is very large, then
$$
\frac{N_{\alpha}^{2}}{N^{2}} \approx \frac{N_\alpha(N_{\alpha}- 1)}{N(N - 1)}
$$
but then this is trivial.

# Theorem (Equal Occurrence)
If $N_{\alpha}= N_{\alpha'}$ for any $\alpha, \alpha' \in \{A, \dots, Z\}$, such that  $N_{\alpha} = N/26$ then 
$$
\begin{aligned}
\text{IC} 
&= 26 \sum_{\alpha} \frac{N_\alpha(N_{\alpha}- 1)}{N(N - 1)} \\  
&= 26 \sum_{\alpha} \frac{N - 26}{26^{2}(N - 1)} \\
&= 26^{2} \cdot \frac{N - 26}{26^{2}(N - 1)} \\
&= \frac{N - 26}{N - 1} \\
\end{aligned}
$$
then as $N \to \infty, \text{IC} \to 1$. 

# Heuristic (English IC)
The IC of long English plaintext
1. typically around $1.75$
2. almost always between $1.5$ and $2.0$.