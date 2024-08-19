#set text(size: 12pt)
#set math.vec(delim: "[")

#show link: underline

= Journey to DFT

== Context   
This article was inspired by the paper #link("https://arxiv.org/abs/2305.20030")[Tree-Ring Watermarks], where they make use of the Discrete Fourier Transform (DFT). While reading the paper, I realized I knew nothing about the Fourier transform, neither the continuous nor discrete cases. This work aims to connect the dots, starting from basic theory and working our way up to the DFT.

When we consider how to begin, it seems overwhelming and almost off-topic. There are plenty of posts online about the (D)FT, but a lot of them focus on the perspective of _signal processing_. Here, I attempt to create the post that I would've wanted when I first started reading.

== Periodic Functions
#rect(inset: 1em)[
  === Definition
  A _periodic function_ is a function $f: bb(R) arrow.r bb(R)$ for which there exists a _period_ $P in bb(R)$ such that: for all $x in bb(R)$, $ f(x) = f(x+P) $
]

Classic examples of periodic functions are $cos(x)$ and $sin(x)$, both of which have period $2 pi$.

The periodicity of the function implies that there exists an interval containing all the values $f$ will ever take. From the definition, we know $f(x) = f(x+P)$. This implies that $f(0) = f(P)$, meaning the values of $f$ are in $bracket.l 0, P paren.r$.

The period of a periodic function gives rise to several other properties that you'd most commonly learn about in pre-calculus or an introductory physics class.

Suppose we have a periodic function $f$ with a period $P$. Then we define these properties:

- Phase of $f$ : $display(phi.alt(t) = t / P)$

- Frequency of $f$ : $display(k = 1 / P)$

The phase of $f$ can be described as the amount of the period you've traveled so far, and the frequency describes how often a value occurs. Think about the frequency like this: since the function is periodic, the value at each point in the interval $bracket.l 0, P paren.r$ will repeat infinitely many times; how often that value appears is given by a single fraction of the period.

#rect(inset: 1em, outset: 1.4em)[
  === Fun Exercise
  #quote(
    attribution: [
      _Linear Algebra Done Right_ (3rd ed), Axler, Section 1.C, Exercise 9
    ], 
  quotes: false, 
  block: true)[
    Is the set of all periodic functions from $bb(R)$ to $bb(R)$ a subspace of $bb(R)^bb(R)$?
  ]

  Here, $bb(R)^bb(R)$ means the set of all continuous functions $bb(R) arrow.r bb(R)$. We proceed under the assumption that $bb(R)^bb(R)$ is indeed a vector space. For brevity, let $cal(P) = {f : bb(R) arrow.r bb(R) bar.v f "is periodic"}$.

  In these types of problems, the first thing you should do is check if the set they're asking about (in our case: $cal(P)$) is itself a vector space, which is a requirement for it to be a subspace.

  The first property we check is if vector addition holds. Let $f, g in cal(P)$. Suppose $f$ has period $P_f$ and $g$ has period $P_g$, and consider $f(x)+g(x)$ for all $x in RR$.

  Since both functions are periodic, it's worth checking if their periods hold. There are two cases to check:
  + $P_f = P_g$
  + $P_f eq.not P_g$ 

  For case 1, let $P_(f+g) = P_f$. We get that: 
  $ 
    (f+g)(x+P_(f+g)) &= f(x+P_(f+g))+g(x+P_(f+g)) \
    &= f(x)+g(x) \
    &= (f+g)(x) 
  $
  so we see that $f+g$ is periodic.

  For case 2, let $P_(f+g) = P_f$. We get:
  $
    (f+g)(x+P_(f+g)) &= f(x+P_(f+g)) + g(x+P_(f+g)) \
    &= f(x)+g(x+P_(f+g)) \
    &eq.not (f+g)(x)
  $
  
  Let $P_(f+g) = P_g$ instead. We get:
  $
    (f+g)(x+P_(f+g)) &= f(x+P_(f+g)) + g(x+P_(f+g)) \
    &= f(x+P_(f+g))+g(x) \
    &eq.not (f+g)(x)
  $

  Both fail because for at least one of the terms, $P_(f+g)$ is _not_ a valid period for that function.

  We know that $cal(P)$ contains all periodic functions, meaning even functions which have different periods, so if $f+g in.not cal(P)$ when $P_f eq.not P_g$, then $cal(P)$ cannot be a vector space. Thus, it can't be a subspace of $RR^RR$. $qed$
]

We may also want to consider adjusting the argument to our periodic function. What happens to our period when we compute $f(a x)$ for some $a in RR$?

Consider what happens: for whatever value we pass in, we go $a$ times ahead. This means we finish the period $a$ times faster, and thus the interval becomes $bracket.l 0, P/a paren.r$; the period of $f(a x)$ is $ P_(f(a x)) = P_f / a $.

The importance of periodic functions in our journey to the DFT is twofold:
+ All cases of the Fourier transform involve a rotation, and that rotation is defined by various forms of $sin$ and $cos$.
+ In DFT, our function is _implicitly assumed to be periodic_.

We'll discuss the effects of discrete samples and periodicity later.

== Complex Rotations
As we'll discuss soon, the Fourier transform utilizes complex rotations to _transform_ the input function.

In the complex plane, we accept inputs in the form of complex numbers $a+i b$. It's a known result in complex analysis that, via power series, it can be shown that $z = r e^(i theta) = r cos(theta) + i r sin(theta)$, where $r$ is the magnitude of $z$ and $theta$ is its angle with the real-axis.

Complex numbers are commonly written as vectors, where we assume the first component is the real part and the second component is the imaginary part:
$
  z = a + i b = vec(a, b) = vec(r cos(theta), r sin(theta))
$

Since we're using $cos$ and $sin$ with the same argument, they'll have the same period. This perspective highlights how $r e^(i theta)$ models rotation around the circle of radius $r$, for $theta in bracket.l 0, 2 pi paren.r$.

Recall that $sin$ and $cos$ are periodic in $RR$, and this periodicity extends to $CC$ (since complex numbers are pairs of real numbers). Thus, both are still periodic functions over the complex plane, with the added benefit of both being _nicely behaved_ in $CC$; this is a result of the functions being entire.

In can be proven further that $e^(i theta)$ follows the rules of exponents, allowing for expressions like $e^(i (theta_1 + theta_2)) = e^(i theta_1) e^(i theta_2)$ and $e^(i a theta) = (e^(i theta))^a$.