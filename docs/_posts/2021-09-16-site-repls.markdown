---
layout: post
title: Using Replit to manage a GitHub Pages site
date: 2021-09-16
---

Let's talk about maintaining a GitHub Pages site through a repl hosted on Replit.

### What's Replit and Why Are We Using It?

[Replit](https://replit.com) is a site that hosts collaborative in-browser IDEs. They have a _lot_ of different preloaded languages you can choose to make a repl for. Repl stands for Read-Eval-Print-Loop. Think about when you type `python` into Terminal and get an interactive Python terminal. That's a repl. We'll be using Replit to host our editing environment.

To explain more, consider the tech stack we're going to use.
* GitHub Pages
* Jekyll
* Replit
* Markdown, Basic HTML/CSS

GitHub Pages will host the site itself, creating a URL for it and giving it a place to live. Jekyll will be used to incorporate the Ruby Gem infrastructure, making it easier to create custom content for the site. Replit will be used to host the environment we edit the site in. Markdown and HTML/CSS will be used for the actual content and layout of the site.

### Setup

How do we set this up? It's nice to know what we need, but what do we do? There's actually a specific order to doing this, so bear with me.

<ol>
    <li>
        Make an account with Replit and create a new repl from the template <span markdown="1">`Ruby`</span>.
        This will open an in-browser IDE environment. Take some time to get familiar with it.
    </li>
    <li>
        Using Replit's package manager (the cube in the left sidebar), search for and install <span markdown="1">`Jekyll`</span>. 
        This will be used to build the site. Wait for the installation to finish.
    </li>
    <li>
        Head into Replit's version control (the branching node in the left sidebar) and create a new repository. 
        You'll have to connect to your GitHub account. Give the repo the name "username.github.io", where "username" is your username, and select visibility. 
        Confirm the repo was created.
    </li>
    <li>
        Go into the repl Shell (<span markdown="1">_not_</span> the console), make sure you're in your root directory (the name of your 
        project), and type the following command:
        <span markdown="1">`bundle`</span>
    </li>
    <li>
        In the same repl shell, run: <span markdown="1">`mkdir docs; cd docs`</span>
    </li>
    <li>
        In the same repl shell, run:
        <span markdown="1">`bundle exec jekyll new .`</span>
    </li>
    <li>
        Make sure to commit and push your changes to the repo. Go back into Replit version control and enter in a message to describe what we just did (we created a new default site). Commit & Push.
    </li>
    <li>
        Within your repo, go into Settings > Pages and choose a source. You want to choose whichever
        branch contains the <span markdown="1">`docs`</span> directory.
    </li>
    <li>
        I would highly suggest selecting the option "Enforce HTTPS"
    </li>
    <li>
        Refresh the page and head to your site when it says it's published
    </li>
</ol>

That's it for setting up the boilerplate site through Jekyll and GitHub Pages. Now comes the process of designing the site to fit your needs.

### Site Design and Layout

One of the highlights of using Jekyll is that it can use gem-based plugins and themes. The default theme is "Minima" (at the time of writing, that's the theme being used on my site). Without going into too much detail, Jekyll uses "layouts" to construct your website. Think of them as template HTML files for different entities that can exist on your site. To edit the layouts for our theme, we'll need to copy the files from our theme and store them in `docs`.

All layouts in Jekyll are stored in a directory called `_layouts`. Go to `.bundle/ruby/version_number/gems` and find the folder containing the theme. If for some reason you can't find it, put `gem "theme_name"` in your `Gemfile` and run `bundle` in the shell from your root directory. This should install the theme in your `gems` directory.

Next, we need to copy the directories `_sass`, `_layouts`, and `_includes` into `docs` so we can actually make changes to the HTML and have it appear on the site.

Run `cp -R theme_dir/dir .` for each of the three directories in our theme directory. This should move everything from those folders, including the folder itself, into `docs`.

### Validating Through GitHub

Once all the layout files have been copied over, make a small change to see if it works. The process for updating the site works as follows:
1. Update the content in the repl
2. Using Replit's version control, commit and push the changes to the remote repo on GitHub
3. Confirm the changes are successful by monitoring the commit and waiting for the green checkmark
4. Visit the URL in the "Pages" setting of your repo to confirm that the changes are made. It may take some time for the changes to appear, so refresh the page if they don't show up immediately.

Try it with the new layout files we moved into our project, making a small change like adding a `<p></p>` tag.

### Remarks

While this isn't the ideal way to run the site, I've found that it works quite well without having to do everything on my local machine. While it would help to be able to use `jekyll serve` within the repl (you can't, or at least not easily), we're initially fine updating the site and viewing the changes in the deployed version.

An additional remark: through this post in particular, I learned that when trying to write inline Markdown within an HTML block, it doesn't work. Everything is rendered exactly. So, as a fix since we're using Kramdown Markdown rendering, we can surround the Markdown with `<span markdown="1"></span>` for it to render. In general, if you have a block of Markdown to render in an HTML block, passing `markdown="1"` will tell Kramdown to render it.