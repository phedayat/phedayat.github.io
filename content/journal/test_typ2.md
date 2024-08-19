---
title: test_typ2
date: 2024-07-18
math: True
---

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

<!-- You can replace the ::: ::: with <details></details> -->
<details>
    <summary><b>Definition</b></summary>
    <blockquote>
        A <i>periodic function</i> is a function
        $f:\mathbb{R} \rightarrow \mathbb{R}$ for which there exists a <i>period</i>
        $P \in \mathbb{R}$ such that: for all $x \in \mathbb{R}$,
        $$f(x) = f(x + P)$$
    </blockquote>
</details>

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

<details>
    <summary><b>Fun Exercise</b></summary>
    <blockquote>
        Is the set of all periodic functions from $\mathbb{R}$ to $\mathbb{R}$ a subspace of $\mathbb{R}^{\mathbb{R}}$?
        <i>Linear Algebra Done Right</i> (3rd ed), Axler, Section 1.C, Exercise 9
    </blockquote>
    <span>
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
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\\\
& = f(x) + g(x) \\\\
& = (f + g)(x)
\end{aligned}$$ so we see that $f + g$ is periodic.

For case 2, let $P_{f + g} = P_{f}$. We get: $$\begin{aligned}
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\\\
& = f(x) + g\left( x + P_{f + g} \right) \\\\
& \neq (f + g)(x)
\end{aligned}$$

Let $P_{f + g} = P_{g}$ instead. We get: $$\begin{aligned}
(f + g)\left( x + P_{f + g} \right) & = f\left( x + P_{f + g} \right) + g\left( x + P_{f + g} \right) \\\\
& = f\left( x + P_{f + g} \right) + g(x) \\\\
& \neq (f + g)(x)
\end{aligned}$$

Both fail because for at least one of the terms, $P_{f + g}$ is *not* a
valid period for that function.

We know that $\mathcal{P}$ contains all periodic functions, meaning even
functions which have different periods, so if $f + g \notin \mathcal{P}$
when $P_{f} \neq P_{g}$, then $\mathcal{P}$ cannot be a vector space.
Thus, it can't be a subspace of ${\mathbb{R}}^{\mathbb{R}}$.
$\blacksquare$
    </span>
</details>