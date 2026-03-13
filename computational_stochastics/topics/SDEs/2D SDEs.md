---
tags:
  - MATH_114
---
# 2D SDEs
We can generalize [[Stochastic Differential Equations|SDEs]] to $\R^{2}$. A particle can be represented as 
$$
\left( X(t), Y(t) \right) \in \R^{2}
$$
moving in 2D with random kicks. 
$$
\begin{aligned}
dX &= u(X, Y) dt + \sqrt{2D_{1}(X, Y)} \, dB_{1} \\
dY &= v(X, Y) dt + \sqrt{2D_{2}(X, Y)} \, dB_{2} \\
\end{aligned}
$$
for functions $u,v, D_{1}, D_{2} : \R^{2} \to \R$ and independent [[Stochastic Differential Equations#Brownian Motion and SDE Formulation|Brownian Motions]] $B_{1}(t)$ and $B_{2}(t)$. 

> The 2D nature was actually Brown's [original observation](https://en.wikipedia.org/wiki/Brownian_motion#:~:text=Brown%20was%20studying%20plant%20reproduction%20when%20he%20observed%20pollen%20grains%20of%20the%20plant%20Clarkia%20pulchella%20in%20water%20under%20a%20simple%20microscope). 

# 2D Ito's Lemma
We can generalize [[Ito Calculus#Ito's Lemma|Ito's Lemma]] to find $df$ for $f(X, Y)$. The strategy is to do [[Ito Calculus#Taylor Series (Big O notation)|Taylor expansion]] to $O(dt)$. The same assumptions hold from [[#2D SDEs|above]].
$$
\begin{aligned}
df &= f(X + dX, Y + dY) - f(X, Y) \\
&= dX (\partial_{x} f) + dY (\partial_{y} f) + \frac{1}{2} 
\begin{pmatrix} dX & dY \end{pmatrix} 
\begin{pmatrix} 
    \partial^2_{xx} f & \partial^2_{xy} f \\ 
    \partial^2_{xy} f & \partial^2_{yy} f 
\end{pmatrix} 
\begin{pmatrix} dX \\ dY \end{pmatrix} + O(dt^{3/2}) \\
&= \left( 
    u \frac{\partial f}{\partial x} + v \frac{\partial f}{\partial y} + D_1 \frac{\partial^2 f}{\partial x^2} + D_2 \frac{\partial^2 f}{\partial y^2} \right) dt 
+ \frac{\partial f}{\partial x} \sqrt{2 D_1} \, dB_{1} + \frac{\partial f}{\partial y} \sqrt{2 D_2} \, dB_{2}
\end{aligned}
$$

# Example 1 (Active Particle on a Line)
```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.2]

% 1. Horizontal axis
\draw (-3, 0) -- (3, 0);

% 2. Circle and center point
\draw (0, 0) circle (0.6cm);
\fill (0, 0) circle (2pt);

% 3. Labels
\node at (0, -0.4) {$x(t)$};
\node (theta) at (1.5, 0.4) {$\theta(t)$};

% 4. The Vector
\draw[->, thick] (0,0) -- (40:1.1cm);

% 5. The curved pointer line (Simplified for TikZJax)
\draw[->, bend left=20] (theta.west) to (0.3, 0.2);

\end{tikzpicture}
\end{document}
```
The diagram depicts $\theta(t)$ providing rotational noise with the particle moving right on the line. 
$$
\begin{aligned}
dX &= v \cos \theta \,dt &&+ 0 &&   ,\quad X(0) = 0 \\
d\theta &= 0 &&+ \sqrt{2D} \, dB && ,\quad \theta(0) = 0 
\end{aligned}
$$
The particle tries to move in the $\theta-$direction but is constrained to the line. 
> A 2D active particle needs $3$ SDEs to simulate it. 

How far does the particle **move**? We can measure the expectation. 
$$
\begin{aligned}
d(\E{X}) &= v\E{\cos\theta} \, dt \\ 
\frac{d}{dt} \E{X} &= v \E{\cos \theta } \\
\end{aligned}
$$
How to find $\E{\cos \theta}$? We can use [[#2D Ito's Lemma]]! For $f(X, \theta)$, we have 
$$
\begin{aligned}
df_{1} 
&= \left( u \frac{\partial f}{\partial x} + v \frac{\partial f}{\partial y} + D_1 \frac{\partial^{2} f}{\partial x^{2}} + D_{2} \frac{\partial^{2} f}{\partial y^{2}} \right) dt \\
&= \left(0 + 0 + (0) + D \cdot (-\cos \theta)   \right) \, dt\\
&= -D\cos(\theta) \, dt
\end{aligned}
$$
for the deterministic part. For the noise part, 
$$
\begin{aligned}
df_{2} 
&= 0 + -\sin(\theta) \sqrt{2D} \,dB \\
\end{aligned}
$$
Thus, 
$$
df = df_{1} + df_{2} = -D\cos(\theta) \,dt - \sqrt{2D}\sin(\theta) \,dB
$$
Taking the expectation, 
$$
\begin{aligned}
d\E{\cos \theta} &= -D\E{\cos \theta}dt - 0 \\
\frac{d}{dt}\E{\cos \theta} &= -D\E{\cos\theta} \\
\E{\cos \theta} &= \cos(0) e^{-Dt} \\ 
&= e^{-Dt} \\
\end{aligned}
$$
Going back to our original expectation, 
$$
\frac{d}{dt}\E{X} = ve^{-Dt}
$$
Integrating,
$$
\begin{aligned}
\E{X(t)} 
&= \int_{0}^{t} ve^{-Ds} \, ds \\
&= \left[-\frac{v}{D}e^{-Ds}\right]_{0}^{t} \\
&= -\frac{v}{D}\left( e^{-Dt} - 1 \right) \\
&= \frac{v}{D}\left( 1- e^{-Dt} \right) \\
\end{aligned}
$$
as desired. 