---
tags:
  - MATH_114
---
# Box-Muller Method
We want to determine how to generate $X \sim N(0, 1)$, the standard [[Normal]]. In particular, find $X$ that draws from the [[Probability Distribution Function|PDF]]
$$
X \sim \frac{1}{\sqrt{2\pi}}\exp \left( -\frac{1}{2}x^{2} \right)
$$
from $U[0, 1]$? Inversion is **computationally hard** since there is no closed form for the [[Cumulative Distribution Function|CDF]] $F_{X}$. 

The **Box-Muller Method** tells us to start with $X, Y \sim N(0, 1)$ independent RVs and work backwards to $U[0, 1]$ RVs. The [[Joint Distribution| joint PDF]] is 
$$
f_{X,Y} = \frac{1}{2\pi} \exp\left( -\frac{1}{2} (x^{2} + y^{2}) \right)
$$
Set $R = \sqrt{x^{2} + y^{2}}$ and $\theta = \arctan(y/x)$. The transformation is then 
$$
\begin{aligned}
(r, \theta) = T(x, y) &= \left(\sqrt{x^{2} + y^{2}}, \arctan\left(\frac{y}{x}\right) \right) \\ 
(x, y) = T^{-1}(x, y) &= (r\cos\theta, r\sin\theta)
\end{aligned}
$$
which gives us the Jacobian:
$$
\begin{vmatrix}
\del_{r}x & \del_{\theta}x \\
\del_{r}y & \del_{\theta}y \\
\end{vmatrix}
= 
\begin{vmatrix}
\cos\theta & -r\sin\theta \\
\sin\theta & r\cos\theta \\
\end{vmatrix}
= r
$$
Then, the joint PDF form the transformation is 
$$
f_{R,\Theta}(r, \theta)
= f_{X, Y}(x, y) \cdot \left|\frac{\del(x, y)}{\del(r, \theta)} \right|
= \frac{1}{2\pi}\exp\left(- \frac{1}{2} r^{2}\right)r
$$
By factoring, w can show that both $R, \Theta$ are independent. 
$$
(\star)\quad\quad\quad f_{R, \Theta} = f_{\Theta}(\theta) \cdot f_{R}(r)
$$
where 
$$
f_{\Theta}(\theta) = \frac{1}{2\pi} 
\quad\quad\quad 
f_{R}(r) = r\exp\left( -\frac{1}{2} r^{2} \right)
$$
are PDFs. This tells us that
$$
\Theta \sim U[0, 2\pi]
\quad\quad\quad
R \sim F_{R} 
= \int_{0}^{r} u \exp\left( -\frac{1}{2} u^{2} \right) \, du 
= 1 - \exp\left(-r^{2}/ 2\right)
$$
Let $U_{1}, U_{2} \sim U[0, 1]$ be two independent RVs. Then 
$$
\begin{aligned}
2\pi U_{1} &\sim U[0, 2\pi] && \text{(which represents $\Theta$)} \\ 
\left[-2 \ln(1 - U_{2}) \right]^{1/2} &\sim F_{R} && \text{(which represents $R$)}
\end{aligned}
$$
We can further simplify this; since we have a $1 - U_{2}$ term, and as $U_{2} \sim U[0, 1]$ then $1 - U_{2} \sim U[0, 1]$. 

---
Finally, that gives us the **Box-Muller Method**. 

Let $U_{1}, U_{2} \sim U[0, 1]$ be independent RVs. Then $X, Y$ defined below are $\sim N(0, 1)$ and independent by 
$$
\begin{aligned}
X &= \left( -2\ln U_{2} \right)^{1/2} \cos 2\pi U_{1} \\ 
Y &= \left( -2\ln U_{2} \right)^{1/2} \sin 2\pi U_{1} \\
\end{aligned}
$$
In particular, we use $(\star)$ to get the $\cos, \sin$ terms in the inverse operation. Indeed, 
$$
\begin{aligned}
X &= R\cos\Theta \\ 
Y &= R\sin\Theta \\
\end{aligned}
$$
This lets us recover $(X, Y)$ from
$$
(U_{1}, U_{2}) 
\to (R, \theta) 
\to (X, Y)
$$


