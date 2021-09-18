---
layout: post
title: Programming is Fun
date: 2021-09-16
math: True
---
<h2 style="color: red; text-align: center;">WARNING: Removing this post soon.</h2>

A fun little issue I dealt with towards the end of Spring 2021: a friend of mine is writing a program for the Fermat primality test. Unforunately, it's not working correctly.

What is the Fermat primality test and why didn't my friend's program work?

The Fermat primality test is a method of checking whether an integer is a prime number or not (i.e. the only divisors of that integer are 1 and itself). The formal definition is as follows: Let \\(p\\) be an integer and \\(a\\) an integer that does not divide \\(p\\). Then \\(p\\) is prime if and only if

$$a^{p-1} \equiv 1$$

The beauty of this test is that it's an if and only if, meaning that this relation holds true if \\(p\\) is prime, but also if the relation is true, then \\(p\\) is prime. (A good question: which direction of the relation is more important?)

Now we answer the main question: why didn't program work? He had written it in Java and was testing it out with \\(a=1000\\), and \\(p=1249\\). If you reference WolframAlpha, you'll see that the primality test holds and \\(1249\\) is in fact prime. However, my friend couldn't get this answer from his program. He was actually getting \\(2147483647\\) over and over again.

If you feel like that number is special in some way, you'd be right. The aforementioned number he keeps getting as an answer is actually the _maximum value for an int_ in Java. This means that my friend's program was working, but overflowing the variable holding the result. I noticed this and assumed he just needed more space, so I suggested changing to a double or a long. However, even I had neglected to think about their maximum values, and how large \\(1000^{1248}\\) is. We realized, after some trials, I decided that maybe I should try writing the program in Python, simply because who knows what it will do without type safety. I was pleasantly surprised that it worked, and very quickly at that. Java doesn't have a primitice data type capable of storing that large of a number (emphasis on _primitive_).

The reason I even wanted to write about this is that I thoroughly enjoyed the process of helping my friend, and it was fun to figure out what the issue was, amongst the mountain of more difficult work I had to do during Spring 2021.