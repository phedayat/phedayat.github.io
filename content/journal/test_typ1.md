---
title: test_typ1
date: 2024-07-18
math: True
---

# Journey to DFT

## Context 

This body of work was inspired by the paper [[Tree-Ring
Watermarks](https://arxiv.org/abs/2305.20030)]{.underline}, where they
make use of the Discrete Fourier Transform (DFT). While reading the
paper, I realized I knew nothing about the Fourier transform, neither
the continuous nor discrete cases. This work aims to connect the dots,
starting from basic theory and working our way up to the DFT.

When we consider how to begin, it seems overwhelming and almost
off-topic. There are plenty of posts online about the (D)FT, but a lot
of them focus on the perspective of *signal processing*. Here, I attempt
to create the post that I would've wanted when I first started reading.

\

## Periodic Functions

<div style="border: solid; padding: 1em;">
    <b>Definition:</b> A <i>periodic function</i> is a function
    $f:\mathbb{R} \rightarrow \mathbb{R}$ for which there exists a <i>period</i>
    $P \in \mathbb{R}$ such that: for all $x \in \mathbb{R}$,
    $$f(x) = f(x + P)$$
</div>

Classic examples of periodic functions are $\cos(x)$ and $\sin(x)$, both
of which have period $2\pi$.

The periodicity of the function implies that there exists an interval
containing all the values $f$ will ever take. From the definition, we
know $f(x) = f(x + P)$. This implies that $f(0) = f(P)$, meaning the
values of $f$ are in $\lbrack 0,P)$.

The period of a periodic function gives rise to several other properties
that you'd most commonly learn about in pre-calculus or an introductory
physics class.
