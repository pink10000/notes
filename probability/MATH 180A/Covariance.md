# Definition (Covariance)
Covariance is a measure of the [[Joint Distribution|joint]] variability of two random variables. It indicates the direction of the linear relationship between the variables. 

If greater values of one variable mainly correspond with greater values of the other variable, the covariance is positive. If the opposite is true, the covariance is negative.
# Formulas
## Population Covariance
For two random variables $X$ and $Y$ with means $\mu_X$ and $\mu_Y$:
$$
\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]
$$
An alternative computational formula is:
$$
\text{Cov}(X, Y) = E[XY] - E[X]E[Y]
$$
## Sample Covariance
For a sample of size $n$ with sample means $\bar{x}$ and $\bar{y}$:
$$
q_{xy} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$
# Properties
Symmetry:
$$
\text{Cov}(X, Y) = \text{Cov}(Y, X)
$$
Self-Covariance (Variance):
$$
\text{Cov}(X, X) = \text{Var}(X)
$$
Linearity:
$$
\text{Cov}(aX + b, cY + d) = ac \cdot \text{Cov}(X, Y)
$$
Summation:
$$
\text{Cov}(X + Y, Z) = \text{Cov}(X, Z) + \text{Cov}(Y, Z)
$$
Independence:
If $X$ and $Y$ are independent, their covariance is zero. Note that the converse is not necessarily true (zero covariance does not imply independence, as the relationship could be non-linear).
$$
\text{Cov}(X, Y) = 0
$$
# Relation to Correlation
Covariance is scale-dependent, meaning its magnitude depends on the units of the variables. Correlation $\rho$ normalizes covariance to lie between -1 and 1.
$$
\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$
