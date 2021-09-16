---
layout: post
title: Using Replit to manage a GitHub Pages site
date: 2021-09-16
---

Let's talk about maintaining a GitHub Pages site through a repl hosted on Replit.

What's Replit and why are we using it?

[Replit](https://replit.com) is a site that hosts "collaborative in-browser IDEs" (right from their website). They have a _lot_ of different preloaded languages you can choose to make a repl for. Repl stands for Read-Eval-Print-Loop. Think about when you type `python` into Terminal and get an interactive Python terminal. That's a repl. We'll be using Replit to host our editing environment.

To explain more, consider the tech stack we're going to use.
* GitHub Pages
* Jekyll
* Replit
* Markdown, Basic HTML/CSS

GitHub Pages will host the site itself, creating a URL for it and giving it a place to live. Jekyll will be used to incorporate the Ruby Gem infrastructure, making it easier to create custom content for the site (this is not a plug for Jekyll). Replit will be used to host the environment we edit the site in. I encountered a lot of errors and setbacks trying to set up my environment on my local machine. I eventually gave up and decided to use a repl, to avoid the problems I was having with Ruby and Jekyll. Markdown and HTML/CSS will be used for the actual content and layout of the site.

How do we set this up? It's nice to know what we need, but what do we do? There's actually a specific order to doing this, so bear with me.

1. Make an account with [Replit]() and create a new repl from template `Ruby`.
    This will open an in-browser IDE environment. Take some time to get familiar with it.
2. Using Replit's package manager (the cube in the left sidebar), search for and install `Jekyll`. 
    This will be used to build the site. Wait for the installation to finish. 
    and select visibility. Confirm the repo was created.
3. Go into the repl Shell (_not_ the console), make sure you're in your root directory (the name of your 
    project), and type the following command:
    `bundle`
4. In the same repl shell, run: `mkdir docs; cd docs`
5. In the same repl shell, run:
    `bundle exec jekyll new .`
6. Create a new GitHub repository and once it loads, select "Connect to GitHub". Enter a name
    and select visibility. Confirm the repo was created.
7. Within your repo, go into Settings > Pages and choose a source. You want to choose whichever
    branch contains the `docs` directory.
8. I would highly suggest selecting the option "Enforce HTTPS"
9. Refresh the page and head to your site when it says it's published

That's it for setting up the boilerplate site through Jekyll and GitHub Pages.