# Journey to DFT

## Context 

This article was inspired by the paper [[Tree-Ring
Watermarks](https://arxiv.org/abs/2305.20030)]{.underline}, where they
make use of the Discrete Fourier Transform (DFT). While reading the
paper, I realized I knew nothing about the Fourier transform, neither
the continuous nor discrete cases. This work aims to connect the dots,
starting from basic theory and working our way up to the DFT.

When we consider how to begin, it seems overwhelming and almost
off-topic. There are plenty of posts online about the (D)FT, but a lot
of them focus on the perspective of *signal processing*. Here, I attempt
to create the post that I would've wanted when I first started reading.

## Periodic Functions

::: rect

### Definition

A *periodic function* is a function
$f:\mathbb{R} \rightarrow \mathbb{R}$ for which there exists a *period*
$P \in \mathbb{R}$ such that: for all $x \in \mathbb{R}$,
$$f(x) = f(x + P)$$
:::

Classic examples of periodic functions are $\cos(x)$ and $\sin(x)$, both
of which have period $2\pi$.

The periodicity of the function implies that there exists an interval
containing all the values $f$ will ever take. From the definition, we
know $f(x) = f(x + P)$. This implies that $f(0) = f(P)$, meaning the
values of $f$ are in $\lbrack 0,P)$.

The period of a periodic function gives rise to several other properties
that you'd most commonly learn about in pre-calculus or an introductory
physics class.

Suppose we have a periodic function $f$ with a period $P$. Then we
define these properties:

-   Phase of $f$ : $\phi(t) = \frac{t}{P}$

-   Frequency of $f$ : $k = \frac{1}{P}$

The phase of $f$ can be described as the amount of the period you've
traveled so far, and the frequency describes how often a value occurs.
Think about the frequency like this: since the function is periodic, the
value at each point in the interval $\lbrack 0,P)$ will repeat
infinitely many times; how often that value appears is given by a single
fraction of the period.

::: rect

### Fun Exercise

> Is the set of all periodic functions from $\mathbb{R}$ to $\mathbb{R}$
> a subspace of $\mathbb{R}^{\mathbb{R}}$?
>
> ℄  *Linear Algebra Done Right* (3rd ed), Axler, Section 1.C, Exercise
> 9

Here, $\mathbb{R}^{\mathbb{R}}$ means the set of all continuous
functions $\mathbb{R} \rightarrow \mathbb{R}$. We proceed under the
assumption that $\mathbb{R}^{\mathbb{R}}$ is indeed a vector space. For
brevity, let
$\mathcal{P} = \left\{ f:\mathbb{R} \rightarrow \mathbb{R}|f\text{ is periodic} \right\}$.

In these types of problems, the first thing you should do is check if
the set they're asking about (in our case: $\mathcal{P}$) is itself a
vector space, which is a requirement for it to be a subspace.

The first property we check is if vector addition holds. Let
$f,g \in \mathcal{P}$. Suppose $f$ has period $P_{f}$ and $g$ has period
$P_{g}$, and consider $f(x) + g(x)$ for all $x \in {\mathbb{R}}$.

Since both functions are periodic, it's worth checking if their periods
hold. There are two cases to check:

1.  $P_{f} = P_{g}$

2.  $P_{f} \neq P_{g}$

For case 1, let $P_{f + g} = P_{f}$. We get that: $$\begin{aligned}
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\
 & = f(x) + g(x) \\
 & = (f + g)(x)
\end{aligned}$$ so we see that $f + g$ is periodic.

For case 2, let $P_{f + g} = P_{f}$. We get: $$\begin{aligned}
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\
 & = f(x) + g\left( x + P_{f + g} \right) \\
 & \neq (f + g)(x)
\end{aligned}$$

Let $P_{f + g} = P_{g}$ instead. We get: $$\begin{aligned}
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\
 & = f\left( x + P_{f + g} \right) + g(x) \\
 & \neq (f + g)(x)
\end{aligned}$$

Both fail because for at least one of the terms, $P_{f + g}$ is *not* a
valid period for that function.

We know that $\mathcal{P}$ contains all periodic functions, meaning even
functions which have different periods, so if $f + g \notin \mathcal{P}$
when $P_{f} \neq P_{g}$, then $\mathcal{P}$ cannot be a vector space.
Thus, it can't be a subspace of ${\mathbb{R}}^{\mathbb{R}}$.
$\blacksquare$
:::

We may also want to consider adjusting the argument to our periodic
function. What happens to our period when we compute $f(ax)$ for some
$a \in {\mathbb{R}}$?

Consider what happens: for whatever value we pass in, we go $a$ times
ahead. This means we finish the period $a$ times faster, and thus the
interval becomes $\lbrack 0,\frac{P}{a})$; the period of $f(ax)$ is
$$P_{f(ax)} = \frac{P_{f}}{a}$$.

The importance of periodic functions in our journey to the DFT is
twofold:

1.  All cases of the Fourier transform involve a rotation, and that
    rotation is defined by various forms of $\sin$ and $\cos$.

2.  In DFT, our function is *implicitly assumed to be periodic*.

We'll discuss the effects of discrete samples and periodicity later.

## Complex Rotations

As we'll discuss soon, the Fourier transform utilizes complex rotations
to *transform* the input function.

In the complex plane, we accept inputs in the form of complex numbers
$a + ib$. It's a known result in complex analysis that, via power
series, it can be shown that
$z = re^{i\theta} = r\cos(\theta) + ir\sin(\theta)$, where $r$ is the
magnitude of $z$ and $\theta$ is its angle with the real-axis.

Complex numbers are commonly written as vectors, where we assume the
first component is the real part and the second component is the
imaginary part: $$z = a + ib = \begin{bmatrix}
a \\
b
\end{bmatrix} = \begin{bmatrix}
r\cos(\theta) \\
r\sin(\theta)
\end{bmatrix}$$

Since we're using $\cos$ and $\sin$ with the same argument, they'll have
the same period. This perspective highlights how $re^{i\theta}$ models
rotation around the circle of radius $r$, for
$\theta \in \lbrack 0,2\pi)$.

Recall that $\sin$ and $\cos$ are periodic in $\mathbb{R}$, and this
periodicity extends to $\mathbb{C}$ (since complex numbers are pairs of
real numbers). Thus, both are still periodic functions over the complex
plane, with the added benefit of both being *nicely behaved* in
$\mathbb{C}$; this is a result of the functions being entire.

In can be proven further that $e^{i\theta}$ follows the rules of
exponents, allowing for expressions like
$e^{i\left( \theta_{1} + \theta_{2} \right)} = e^{i\theta_{1}}e^{i\theta_{2}}$
and $e^{ia\theta} = \left( e^{i\theta} \right)^{a}$.
