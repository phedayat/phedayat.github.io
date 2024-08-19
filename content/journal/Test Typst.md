---
title: Test Typst
date: 2024-07-17
math: true
---

<!-- # Fourier

The integral we're interested in is:
$$\int_{- \infty}^{\infty}f(x)e^{- isx}dx$$

$f$ is a complex-valued function, and the integrand will evaluate to a
complex number at each input (for some $s$). Thus, the integral is a
complex integral, and we can split it into real and imaginary
components.

Recall that $$e^{- ix} = \cos(x) + i\sin(x)$$ for all $x \in \mathbb{R}$. Then:

$$\begin{aligned}
    &= \int_{- \infty}^{\infty} f(x) \cos( - sx) + i\sin( - sx) dx \\\\
    &= \int_{- \infty}^{\infty} f(x) \cos( - sx) + if(x)\sin( - sx)dx \\\\
    &= \int_{- \infty}^{\infty} f(x) \cos( - sx)dx + i\int_{- \infty}^{\infty}f(x)\sin( - sx)dx
\end{aligned}$$

$$\begin{aligned}
       x &= \int \\\\
        &= \int \\\\
        &= \int
    \end{aligned}$$

Now we have two integrals which can be computed over $\mathbb{R}$. -->

# Fourier

The integral we're interested in is:
$$\int_{- \infty}^{\infty}f(x)e^{- isx}dx$$

$f$ is a complex-valued function, and the integrand will evaluate to a
complex number at each input (for some $s$). Thus, the integral is a
complex integral, and we can split it into real and imaginary
components.

Recall that $$e^{- ix} = \cos(x) + i\sin(x)$$ for all
$x \in \mathbb{R}$. Then:

$$\begin{aligned}
 & = \int_{- \infty}^{\infty}f(x)\left( \cos( - sx) + i\sin( - sx) \right)dx \\\\
 & = \int_{- \infty}^{\infty}f(x)\cos( - sx) + if(x)\sin( - sx)dx \\\\
 & = \int_{- \infty}^{\infty}f(x)\cos( - sx)dx + i\int_{- \infty}^{\infty}f(x)\sin( - sx)dx
\end{aligned}$$
