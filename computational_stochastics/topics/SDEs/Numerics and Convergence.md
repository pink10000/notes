---
tags:
  - MATH_114
---
# Example 1
Consider 1D [[Stochastic Differential Equations|SDE]], $X(t) \in \R$ with $t \in [0, T]$ and 
$$
dX = u(X)\, dt + \sqrt{2D(X)} \, dB
\quad\quad\quad X(t) = x_{0}
$$
We can use the [[Simulating Brownian Motion#Euler-Maruyama Method|Euler-Maruyama method]] to simulate this. 
1. Take $n \in \Z_{>0}$ and set $\delta t = T/n$. Let $t_{i} = i \delta t$. 
2. For $i = 0, \dots, n$ so $t_{n} = T$,
	1. Generate $Z_{i} \sim \mathcal{N}(0, 1)$, the [[Normal#The Normal (Gaussian) Distribution|standard normal]], iid with other $i$'s
	2. Define $Y_{0}^{\delta t}, Y_{1}^{\delta t}, \dots, Y_{n}^{\delta t}$ by:
		1. $Y_{0}^{\delta t} = x_{0}$ 
		2. $Y_{i+1}^{\delta t} = Y_{i}^{\delta t} + \delta t u\left( Y_{i}^{\delta t} \right) + \sqrt{\delta t}\sqrt{2D(Y_{i}^{\delta t})} \cdot Z_{i}$ 
3. Return $Y^{\delta t}$.

Here, $Y_{i}^{\delta t}$ approximates $X(t_{i}) = X(i \delta t)$, the continuous solution. In fact, $Y_{i}^{\delta t}$ **converges** to the true solution. We want to focus on time $T$, where $Y_{n}^{\delta t} \to X(T)$. 

# Definition (Discretized Strong Convergence)
In the above [[#Example 1|example]], we say $Y_{n}^{\delta t}$ **converges strongly** to $X$ at time $T$ with order $\beta$ if 
$$
\E{ |Y_{n}^{\delta t}- X(T)| } = O\left(\delta t^{\beta}\right)
$$
as $\delta t \to 0, n \to \infty$, and  $n \delta t = T$ fixed (for all function in this function class)

Remarks:
- Strong convergence: convergence of sample paths for *fixed* realization of $B(t)$. 
- *Weak*: convergence of distributions.
- Typically, we care about weak convergence. 
- [[Simulating Brownian Motion#Euler-Maruyama Method|Euler-Maruyama Method]] has strong order $1/2$ and weak order $1$.  