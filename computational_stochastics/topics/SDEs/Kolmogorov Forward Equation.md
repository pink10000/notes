---
tags:
  - MATH_114
aliases:
  - FPE
---
# Example 1
Consider [[Stochastic Differential Equations|SDE]] for particle $X(t) \in \R$ with 
$$
dX = -V'(X) \, dt + \sqrt{2D} \, dB
\quad\quad\quad D > 0 \text{ constant}
$$
$V(X)$ is called a **potential**. The SDE represents "go in the direction of $-V'(X)$ plus some noise". The drift $-V'(X)\, dt$ moves the particles to the nearest well (negative means it will decrease) and diffusion here means it will get random kicks. 
```tikz
\begin{document}
\begin{tikzpicture}
  % Global settings for consistent styling
  \tikzset{
    potential/.style={thick},
    guide/.style={dashed, thick},
    force/.style={->, thick},
    particle/.style={circle, draw, thick, inner sep=0pt, minimum size=10pt}
  }

  % Horizontal X-axis (shortened for just the left graph)
  \draw[->, thick] (-4.5, 0) -- (4.5, 0) node[right] {$X$};

  % Central V-axis
  \draw[->, thick] (0, 0) -- (0, 5) node[right] {$V$};

  % Double well curve using standard smooth plot
  \draw[potential] plot[smooth, tension=0.7] coordinates {(-3.5, 4.5) (-2, 1) (0, 2.5) (2, 1) (3.5, 4.5)};

  % Dashed guide lines near the minima
  \draw[guide] (-2, 0) -- (-2, 4.5);
  \draw[guide] (2, 0) -- (2, 4.5);

  % Horizontal arrows indicating direction of force/motion
  \draw[force] (-3.2, 2.8) -- (-2.4, 2.8);
  \draw[<-, thick] (-1.6, 2.8) -- (-0.8, 2.8);
  \draw[force] (0.8, 2.8) -- (1.6, 2.8);
  \draw[<-, thick] (2.4, 2.8) -- (3.2, 2.8);

  % Particle on the right slope with an arrow pointing down towards the well
  \node[particle] (p) at (3.0, 3.2) {};
  \draw[force] (2.9, 2.9) -- (2.2, 1.4); 

\end{tikzpicture}
\end{document}
```
# Kolmogorov Forward Equation
Let $p(x, t)$ be the [[Probability Distribution Function|PDF]] of $X(t)$, so $\lim_{|x| \to \infty} p(x, t) = 0$. What happens to $p(k, t)$ as $t \to \infty$? Recall [[Ito Calculus#Ito's Lemma|Ito's Lemma]]: for any function $f$, 
$$
df = (-V' f' + Df'') \, dt + f'\sqrt{2D} \, dB 
$$
Take the expectation, 
$$
\begin{aligned}
d(\E{f(x)}) 
&= \E{-V' f' + Df''} \, dt + \E{f' \sqrt{2D} \, dB} \\
(\star) \quad\quad\quad
\frac{d}{dt} \E{f(X(t))} &= \E{-V'f' + Df''} \\
\end{aligned}
$$
If $f, V'f', Df''$ all have the same form, then we get an ODE which we can solve. E.g. if they're all $\sim X^{2}$ then we would have an ODE for $y(t) = \E{X(t)^{2}}$. 

Instead, we will use $p(x, t)$ to write down both sides of $(\star)$.
$$
\begin{aligned}
\frac{d}{dt}\E{f(X)} 
&= \frac{d}{dt} \left[ \int_{-\infty}^{\infty} dx \, f(x) p(x, t) \right] \\
&= \int_{-\infty}^{\infty} dx \, f(x) \frac{\del p}{\del t}
\end{aligned}
$$
and 
$$
\E{-V' f' + Df''} 
= \int_{-\infty}^{\infty} dx \, (-V'(x) f'(x) + Df''(x)) \cdot p(x, t)
$$
The goal is write this as an integral against $f$, $\int \boxed{\phantom{1em}} \, f\,dx$ and equate this with the LHS. We'll do this by [[Integration By Parts]]. 

Starting with the expectation on the RHS:
$$
\begin{aligned}
RHS
&=\int_{-\infty}^{\infty} (-V'f'+Df'')p \,dx\\
&=-\int_{-\infty}^{\infty} V'pf'\,dx + \int_{\infty}^{\infty} Dpf''\,dx
\end{aligned}
$$
Apply integration by parts to the first term:
$$
-\int_{-\infty}^{\infty}(V'p)f'\,dx
=\left[-V'pf\right]_{-\infty}^{\infty}+\int_{-\infty}^{\infty}(V'p)'f\,dx
$$
Since $p(x,t)\to0$ as $x\to\pm\infty$, the boundary term vanishes:
$$
-\int_{-\infty}^{\infty}(V'p)f'\,dx=\int_{-\infty}^{\infty}(V'p)'f\,dx
$$
Apply integration by parts to the second term:
$$
\int_{-\infty}^{\infty}(Dp)f''\,dx
=\left[Dpf'\right]_{-\infty}^{\infty}-\int_{-\infty}^{\infty}Dp'f'\,dx
$$
The boundary term vanishes again:
$$
\int_{-\infty}^{\infty}(Dp)f''\,dx
=-\int_{-\infty}^{\infty}Dp'f'\,dx
$$
Substitute these back into the RHS equation:
$$
RHS=\int_{-\infty}^{\infty}(V'p)'f\,dx-\int_{-\infty}^{\infty}Dp'f'\,dx
$$
Apply integration by parts a second time to the remaining $f'$ term (the second term):
$$
-\int_{-\infty}^{\infty}(Dp')f'\,dx
=\left[-Dp'f\right]_{-\infty}^{\infty}+\int_{-\infty}^{\infty}(Dp')'f\,dx
$$
The boundary term vanishes, leaving (assuming constant $D$):
$$
\int_{-\infty}^{\infty}Dp''f\,dx
$$
Combine the terms to express the entire RHS as an integral against $f$:
$$
RHS=\int_{-\infty}^{\infty}\left((V'p)'+Dp''\right)f\,dx
$$
Equate the RHS with the LHS:
$$
\int_{-\infty}^{\infty}\frac{\partial p}{\partial t}f\,dx
=\int_{-\infty}^{\infty}\left(\frac{\partial}{\partial x}(V'p)+D\frac{\partial^2p}{\partial x^2}\right)f\,dx
$$
Since this holds for any (reasonable) function $f$, the integrands must be equal, yielding the **Kolmogorov Forward Equation** equation:
$$
\frac{\partial p}{\partial t}
=\frac{\partial}{\partial x}(V'p)+D\frac{\partial^2p}{\partial x^2}
$$
This is also called the **Fokker-Planck Equation**.

> The reason why the boundary terms head to $0$ is because $p(x, t) \to 0$ as $x \to \pm \infty$. The idea is that since $p(x, t)$ is a PDF, $\int_{-\infty}^{\infty} p(x, t) \, dx = 1$, and so $p(x, t)$ must taper off (i.e. go to $0$) as we integrate over this infinite range to ensure it is equal to $1$. Likewise, $\del p / \del x \to 0$. 

For $V(X) = 0$ we get
- SDE: $dX = \sqrt{2D} \, dB$
- FPE: $\frac{\del p}{\del t} = D \frac{\del^{2} p}{\del x^{2}}$ 

# Stationary Distributions 
The FPE works with the same SDE as [[#Example 1|before]]. 
$$
\frac{\del p}{\del t} = \frac{\del }{\del x}\left(
V'(x) p + D\frac{\del p}{\del x} 
\right)
$$
where $p(x, t)$ is a [[Probability Distribution Function|PDF]] of $X(t)$. Suppose there is a stationary distribution 
$$
p(x, t) \to p_{0}(x) \text{ as } t \to \infty
$$
Then $p_{0}(x)$ must satisfy the FPE. But 
$$
\frac{\del p_{0}}{\del t} = 0 
\quad\quad\quad
(\text{stationary})
$$
implying that 
$$
0 = \frac{\del}{\del x} \underbrace{
\left( V'(x) p_{0} + D \frac{\del p_{0}}{\del x} \right) 
}_{\text{constant}}
\implies 
V'(x) p_{0} + D\frac{\del p_{0}}{\del x} = A
$$
Typically $p_{0}, \frac{\del p_{0}}{\del x} \to 0$ as $|x| \to \infty$, so $A = 0$. We get
$$
\begin{aligned}
V'(x) p_{0} + D \frac{\del p_{0}}{\del x} &= 0 \\
V'(x) + D \frac{1}{p_{0}} \frac{\del p_{0}}{\del x} &= 0 \\
\frac{\del}{\del x}\left( V(x) + D\log p_{0} \right) &= 0 \\
\end{aligned}
$$
The inner term is still constant. So, 
$$
\begin{aligned}
V(x) + D \log p_{0} &= c \\
p_{0}(x) &= \frac{1}{Z} \exp\left( -\frac{1}{D} V(x) \right)
\end{aligned}
$$
where $Z$ is the [[Gibbs Sampler#Example 1 (Glauber Dynamics for Ising Model)|partition function/normalization]]. (Recall this is intractable.)

Remarks:
- [Boltzmann Distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution) for energy $V(x)$ and temperature $D$. 
- Common in statistical mechanics because it arises from SDE.
- Because $V(x)$ is negative in the exponent, the probability $p_{0}(x)$ will be highest where $V(x)$ is the lowest. The particle is most likely to be found at the very bottom of potential wells. We can see this in [[#Example 1]]'s graph. 

> We want to ask what does the probability cloud look like after the system has been running for an infinitely long time. Eventually, the "spread" of the random noise $D$ will reach a perfect equilibrium. The probability cloud will stop changing shape. Mathematically, that is equivalent to setting the time [[Derivative|derivative]] $\del p_{0} / \del t = 0$.  

## Algorithm using Euler-Maruyama
We can use [[Simulating Brownian Motion#Euler-Maruyama Method|Euler-Maruyama]] for the SDE. 
- $X_{i+1} = X_{i} + V'(X_{i}) \delta t + \sqrt{2 \delta t} \cdot Z_{i}$
- $Z_{0}, Z_{1}, \cdots, \sim \mathcal{N}(0, 1)$ iid. 
- $X_{n} \sim f$ as $n \to \infty$. 

This also works in higher dimensions:
$$
d\unl{X} = -\nabla V(\unl{x}) \, dt + \sqrt{2D} \, d\unl{B}
$$
This SDE has a [[Probability Distribution Function|PDF]] 
$$
p(x, t) \to \frac{1}{Z} \exp\left( 
- \frac{1}{D} V(\unl{x})
\right)
$$
as $t \to \infty$. We can solve PDEs numerically by simulating it is a corresponding SDE. For example, we can use the [[Stochastic Differential Equations#Ornstein-Uhlenbeck Process (OU)|OU process]]:
$$
dX = -V'(X)\,dt + \sqrt{2D} \, dB
\quad\quad\quad X(t) \in \R
$$
has potential $V(X) = \frac{1}{2} \alpha X^{2} \implies V'(X) = \alpha X$. Then, the PDF $p(x, t)$ has
$$
\lim_{t \to \infty} p(x, t) \to p_{0}(x) = \frac{1}{Z} 
\exp\left( 
\frac{-\alpha x^{2}}{2D}
\right)
\sim \mathcal{N}\left(0, \frac{D}{\alpha}  \right)
$$
For general $V$, the local min $x_{0}$ gives $V'(x_{0}) = 0$. This implies that 
$$
V(x) \approx V(x_{0}) + \frac{1}{2} V''(x_{0})(x - x_{0})^{2}
$$
for $x$ close to $x_{0}$ via [[Ito Calculus#Taylor Series (Big O notation)|Taylor Series]]. Thus, 
$$
X(t) \text{ approximately } \sim \mathcal{N} \left(x_{0} , \frac{D}{V''(x_{0})} \right)
$$
as $t \to \infty$. The hopping ability is 
$$
\sqrt{ \frac{D}{V''(x_{0})} } \sim |x_{1} - x_{0}|
$$
where $x_{1}$ is the bottom of the second well. If $\sigma$ is smaller than the distance between the well, then the particle will be unable to jump to the second well. However, if $D$ is high enough (imagine this is the temperature), then the particle can jump to $x_{1}$. 
