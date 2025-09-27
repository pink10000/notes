
We extend the definition of the [[Normal|Normal Distribution]] to higher dimensions. Indeed
$$
\mathcal{N}(\vec{\mu}, \Sigma)
$$
where $\vec{\mu} \in \R^{n}, \Sigma$ is a $n\times n$ positive symmetric definite matrix.

### Positive Symmetric Definite
A matrix $\mathbf{M}$ is symmetric if $m_{ij} = m_{ji}$ and positive definite if for every nonzero real column vector $x$, $x^{\intercal}\mathbf{M}x \geq 0$.    
https://en.wikipedia.org/wiki/Definite_matrix 

- For any real, invertible matrix $A$, the product $AA^{T} = \mathbf{M}$ is PSD. This is called the Cholesky Factorization.

# Bivariate Normal Distribution
Special case when $n = 2$. We say that $(X, Y)$ has bivariate normal distribution $N(\vec{\mu}, \Sigma)$ if the joint density 
$$
f_{X,Y}(x,y) = \frac{1}{2\pi\sqrt{\det \Sigma}}
\exp\left(
	-\frac{1}{2}
	\begin{bmatrix}x - \mu_{x} \\ y - \mu_{y}\end{bmatrix}^{\intercal} 
	\Sigma^{-1} 
	\begin{bmatrix}x - \mu_{x} \\ y - \mu_{y}\end{bmatrix}
\right)
$$
## Example 1
If $X \sim N(\mu_{1}, \sigma_{1}^{2})$ and $Y \sim N(\mu_{2}, \sigma_{2}^{2})$ are independent then $(X,Y)$ have bivariate normal distribution:
$$
N\left(
(\mu_{1},\mu_{2}), \begin{pmatrix} \sigma_{1}^{2} & 0 \\ 0 & \sigma_{2}^{2} \end{pmatrix}
\right)
$$
This is because we have the [[Joint Distribution]]: $f_{X,Y}(x,y) = f_{X}(x) f_{Y}(y)$ in which the resulting exponent is three matrices with
$$
\Sigma^{-1} = \begin{pmatrix} \frac{1}{\sigma_{1}^{2}} & 0 \\ 0 & \frac{1}{\sigma_{2}^{2}} \end{pmatrix}
$$

# Properties

## Normalization
- Let $Y_{1}, Y_{2} \sim N(0,1)$ and be independent.  
- Let $\Sigma$ be a 2x2 PSD where $\Sigma = AA^{T}$. 

Then 
$$
A\binom{Y_1}{Y_{2}} + \binom{\mu_1}{\mu_{2}}
$$
has bivariate normal distribution, 
$$
N\left( \begin{pmatrix} \mu_{1} \\ \mu_{2} \end{pmatrix}, \Sigma  \right)
$$
Conversely, if 
$$
\begin{pmatrix}Z_{1} \\ Z_{2}\end{pmatrix} \sim N(\vec{\mu}, \Sigma)
$$
then 
$$
A^{-1} \begin{pmatrix}Z_{1} - \mu_{1} \\ Z_{2} - \mu_{2}\end{pmatrix} 
\sim N\left( \begin{pmatrix}0\\0\end{pmatrix}, \begin{pmatrix}1&0\\0&1 \end{pmatrix} \right)
$$
which is how we can "normalize it".

### Proof:
We have that 
$$
\begin{aligned}
f_{Y_{1}, Y_{2}}(y_{1}, y_{2}) 
&= \frac{1}{2\pi}\exp\left( - \frac{1}{2} (y_{1}^{2} + y_{2}^{2}) \right) \\
&= \frac{1}{2\pi}\exp\left( -\frac{1}{2}
\left\langle
\binom{y_1}{y_{2}}, \binom{y_{1}}{y_{2}}
\right\rangle
\right)
\end{aligned}
$$
which is just 
$$
\begin{pmatrix}Y_{1} \\ Y_{2} \end{pmatrix}
\mapsto A \begin{pmatrix} Y_{1} \\ Y_{2} \end{pmatrix} +
\begin{pmatrix} \mu_{1} \\ \mu_{2} \end{pmatrix} = 
\begin{pmatrix} Z_{1} \\ Z_{2} \end{pmatrix}
$$
---
## Joint Conversion
What is the joint density of $(Z_{1},Z_{2})$? We can define the prior function as $g : \R^{2}\to \R^{2}$, where
$$
g\begin{pmatrix}X_{1}\\ X_{2}\end{pmatrix} = 
\begin{pmatrix}Z_{1}\\ Z_{2}\end{pmatrix}
$$
where
$$
\begin{aligned}
f_{Z_{1}, Z_{2}}(z_{1}, z_{2})
&= f_{X_{1}, X_{2}} \left( g^{-1}(z_{1}, z_{2}) \right) \cdot |\det Dg^{-1}(z_{1}, z_{2})|  \\
&= f_{X_{1}, X_{2}} \left( g^{-1}(z_{1}, z_{2}) \right) \cdot \frac{1}{|\det Dg(x_{1}, x_{2})| } \\ 
\end{aligned}
$$
where we multiply by the determinant because $g$ changes the volume or "space" in $\R^{2}$ since we are switching from one coordinate system to another. 
- The determinant encodes the notion of area and volume
- Multiplying by it fixes the transformation change so that the probabilities match in both coordinate systems.
--- 
Back to the [[Multivariate Normal#Proof|proof]], we can apply the inverse to the map. Let the map be $g$. 
$$
\begin{aligned}
g\begin{pmatrix}y_{1} \\ y_{2} \end{pmatrix}
&= A\binom{y_{1}}{y_{2}} + \binom{\mu_{1}}{\mu_{2}} \\
%% %%
g^{-1}\binom{z_{1}}{z_{1}} 
&=- A^{-1}\binom{z_{1}-\mu_{1}}{z_{2} - \mu_{2}} \\
Dg &= A \\
\end{aligned}
$$
- $g$ is an affine transformation (linear transformation given by $A$) then translated by $\mathbf{\mu}$. 
- $D$ is the Jacobian operator on $g$. 
--- 
Upon changing variables and application of the density function,
$$
\begin{aligned}
&= f_{X_{1}, X_{2}} \left( g^{-1}(z_{1}, z_{2}) \right) \cdot \frac{1}{|\det A| } \\ 
&= \frac{1}{2\pi |\det A|} \exp\left( 
-\frac{1}{2} \left\langle 
A^{-1} \binom{z_{1}-\mu_{1}}{z_{2}- \mu_{2}}, A^{-1} \binom{z_{1}-\mu_{1}}{z_{2}- \mu_{2}} 
\right\rangle 
\right) \\
&= \frac{1}{2\pi |\det A|} \exp \left( -\frac{1}{2}
\binom{z_{1}- \mu_{1}}{z_{2} - \mu_{2}}^{T}
\left[ (A^{-1})^{T}A^{-1} \right]
\binom{z_{1}- \mu_{1}}{z_{2} - \mu_{2}} 
\right)
\end{aligned}
$$
We read from here that $\binom{Z_{1}}{Z_{2}}$ has bivariate normal distribution with 
$$
\vec{\mu} = \binom{\mu_{1}}{\mu_{2}} \quad\quad\quad \Sigma^{-1} = (A^{-1})^{T}A^{-1}
$$
## Variance and Covariance
Suppose 
$$
\binom{X_1}{X_2} \sim N(\mu, \Sigma)
$$
then 
$$
\mu = \binom{\E{X_{1}}}{\E{X_2}} 
\quad\quad\quad 
\Sigma = \begin{pmatrix}
\var(X_{1}) & \Cov(X_{1},X_{2}) \\ \Cov(X_{1},X_{2}) & \var(X_{2}) \\
\end{pmatrix}
$$
which is the **mean vector** and the **covariance matrix**
### Proof
We use [[Multivariate Normal#Joint Conversion|joint conversion]] and [[Multivariate Normal#Normalization|normalization]] . So, we have 
$$
\begin{pmatrix}X_{1}\\ X_{2}\end{pmatrix}
= A \begin{pmatrix}Y_{1}\\ Y_{2}\end{pmatrix}
+ \binom{\mu_{1}}{\mu_{2}}
$$
where $AA^{T} = \Sigma$ and $Y_{1},Y_{2} \sim N(0, 1)$ and are independent. We denote $A = \begin{pmatrix} a&b \\ c&d \end{pmatrix}$. Then
$$
\begin{aligned}
\binom{X_{1}- \mu_{1}}{X_{2} - \mu_{2}} 
&= \begin{pmatrix}a & b \\ c & d \end{pmatrix} \binom{Y_{1}}{Y_{2}} \\
&= \begin{pmatrix}aY_{1} + bY_{2} \\ cY_{1} + dY_{2}\end{pmatrix}
\end{aligned}
$$
Then to find the variances:
$$
\begin{aligned}
\var(X_{1}) 
&- \var(aY_{1} + bY_{2}) \\
&= \var(aY_{1}) + \var(bY_{2}) \\
&= a^{2} + b^{2}
\end{aligned}
$$
and likewise for $\var(X_{2}) = c^{2} + d^{2}$. Next,
$$
\begin{aligned}
\Cov(X_{1}, X_{2})
&= \Cov(aY_{1}+ bY_{2}, cY_{1}+ dY_{2}) \\
&= ac\var(Y_{1}) + (ad + bc)\Cov(Y_{1},Y_{2}) + bd\var(Y_{2}) \\
&= ac + bd
\end{aligned}
$$
As $\Sigma  = AA^{T}$ , we get 
$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} a & c \\ b & d \end{pmatrix} = \begin{pmatrix} a^2 + b^2 & ac + bd \\ ac + bd & c^2 + d^2 \end{pmatrix}
$$
which follows from what we calculated before. For the means, we have that
$$
\begin{pmatrix}
X_{1} \\ X_{2}
\end{pmatrix}
= A
\begin{pmatrix}
Y_{1} \\ Y_{2}
\end{pmatrix}
+ \vec{\mu}
$$
which gives us:
$$
\begin{pmatrix}
\mathbb{E}[X_1] \\
\mathbb{E}[X_2]
\end{pmatrix}
= A
\begin{pmatrix}
\mathbb{E}[Y_{1}] \\
\mathbb{E}[Y_{2}]
\end{pmatrix}
+ \vec{\mu}
= \vec{\mu}
$$
## Equivalent Characterization of Bivariate Normal
$(X_{1},X_{2})$ have a bivariate normal distribution if and only if $\forall a,b \in \R$, $aX_{1}+ bX_{2}$ is a normal random variable.

### Proof:
Forward Direction.
Upon conversion to matrices through [[Multivariate Normal#Joint Conversion|joint conversion]]: 
$$
\binom{X_{1}}{X_{2}} = A\binom{Y_{1}}{Y_{2}} + \vec{\mu}
$$
where $Y_1,Y_{2} \sim N(0, 1)$. This gives us $aY_{1} + bY_{2}$. But this is normal for any $a,b \in \R$ by [[Convolutions#Example 2|convolutions]] which is shown in [[Normal#Sum of 2 Independent RVs]]. 

Reverse Direction.
Better explained with the Fourier transformation and is not covered. 

## Conditional Distribution
Let $(X,Y) \sim N(\mu, \Sigma)$. Then the [[Conditional Probability|conditional distribution]] of $Y$ given $X = x$ is
$$
N\left(
	\mu_{Y} + \rho \frac{\sigma_Y}{\sigma_{X}}(x - \mu_{X}),
	\sigma_{Y}^{2}(1 - \rho^{2})
\right)
$$
where $\rho$ is the [[Correlation]].  

### Corollary: [[Conditional Expectation]]
$$
\E{Y \mid X = x} = \mu_{Y}+ \rho \frac{\sigma_Y}{\sigma_{X}}(x - \mu_{X})
$$
$$
\var(Y \mid  X= x) = \sigma_{Y}^{2}(1 - \rho^{2})
$$

#### Proof:
If $(X,Y)$ has bivariate normal distribution, then the [[Joint Distribution]] is determined by 
$$
\binom{\mu_{X}}{\mu_{Y}}, \quad\quad\quad 
\begin{pmatrix} \var(X) & \Cov(X,Y) \\ \Cov(X,Y) & \var(Y)  \end{pmatrix}
$$
In particular, if $\Cov(X,Y) = 0$ then $X,Y$ are [[Lecture 1|independent]]. 

In general, think of $\Cov(X,Y)$ as an inner product for the bivariate normal distribution. So, 
$$
\begin{aligned}
\text{orthogonal} &\iff \text{independent} \\
\Cov(X,Y) = 0 &\iff X,Y \text{ are independent} \\
\end{aligned}
$$

We write $Z_{1}= \frac{X - \mu_X}{\sigma_{X}}$ such that $Z \sim N(0, 1)$.  Then 
$$
\begin{aligned}
\Cov(Y, Z_{1}) 
&= \E{ (Y - \E{Y})(Z_{1} - \E{Z_{1}}) } \\
&= \E{ (Y - \E{Y})Z_{1}} \\
&= \frac{1}{\sigma_{X}} \E{ (Y - \E{Y})(X - \mu_{X}) } \\
&= \frac{\Cov(Y,X)}{\sigma_{X}} \\
&= \frac{\rho \sigma_{X}\sigma_{Y}}{\sigma_{X}}  \\ 
&= \rho \sigma_{Y}
\end{aligned}
$$
then 
$$
\Cov(Y - \rho \sigma_{Y}Z_{1}, Z_{1} ) = 0
$$
since 
$$
\binom{Z_{1}}{Y - \rho \sigma_{Y}Z_{1}}
= \begin{pmatrix}
\frac{1}{\sigma_{X}} & 0 \\ -\rho \frac{\sigma_{Y}}{\sigma_{X}} & 1 \
\end{pmatrix}
\begin{pmatrix}
X - \mu_{X} \\ Y 
\end{pmatrix}
$$
is bivariate normal, we deduce that $Y - \rho \sigma_Y Z_{1}$ is independent of $Z_{1}$. So, 
$$
\begin{aligned}
Y
&= Y - \rho\sigma_{Y}Z_{1} + \rho \sigma_{Y}Z_{1} \\
&= Y_{2}+ \rho \frac{\sigma_{Y}}{\sigma_{X}}(X - \mu_{X}) \\
\end{aligned}
$$
and $Y_{2}$ has normal distribution and 
$$
\E{Y_{2}} = \E{Y - \rho \sigma_{Y} Z_{1}} = \mu_{Y}
$$
$$
\begin{aligned}
\var(Y_{2})
&= \var(Y - \rho\sigma_{Y}Z_{1}) \\
&= \var(Y) + (\rho\sigma_{Y})^{2}\var(Z_{1}) - 2(\rho\sigma_{Y})\Cov(Y, Z_{1}) \\
&= \sigma_{Y}^{2}+ \rho^{2}\sigma_{Y}^{2} - 2(\rho\sigma_{Y})(\rho \sigma_{Y}) \\
&= (1 - \rho^{2})\sigma_{Y}^{2}
\end{aligned}
$$