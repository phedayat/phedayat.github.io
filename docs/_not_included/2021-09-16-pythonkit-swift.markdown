---
layout: post
title: Using PythonKit to connect your Swift app to an API
date: 2021-09-20
---

I moved about a month ago. In the spirit of getting a new place, I challenged myself to build a tool to help me keep track of my expenses. You can read about the "Expenses" project [here](/projects/). After building the initial prototype, I took it upon myself, as an added challenge, to build a desktop application for it; the point was that the application would make it easy for me to add entries to the Google Sheets in the background. It wasn't long before I realized my limited Swift knowledge and two months of Cocoa programming that I did in 2013 weren't sufficient to deal with the API calls I wanted to make to the Google Sheets API. I needed to find some way to easily make the API calls I wanted.

Python is an obvious choice for API work. It's easy to write scripts that make calls to APIs in Python, and even easier to use Google APIs because of the Google Python Client Library.

After doing some digging, I found out about [PythonKit](https://github.com/pvieito/PythonKit), a Swift framework that allows you to interact with Python code from within Swift. This is essentially the holy grail for a developer like myself: well versed in Python and I know enough Swift to make a simple interactive GUI. Long story short, I was able to succesfully connect my desktop application to my Google Sheets project using PyhonKit for the API calls. Here's how.

#### Setup PythonKit in Your Swift Code

If you look at the [repo for PythonKit](https://github.com/pvieito/PythonKit), you'll see instructions on how to import the framework into your Swift project. I'm going to assume that you're using Xcode for your project.

_DISCLAIMER: I'm not writing this with best practices in mind. This post is purely for getting this type of project up and running._

 1. Go into your project settings > Swift Packages. Select the "+"
 2. Paste the URL into the search bar, then press "Next"
 3. Press "Next" again
 4. Press "Finish"

<!-- Add in an image of step 4 or something -->

This should have imported the framework for use.

#### Setting Up Your Python Code

You can essentially write all of your Python code as normal.

My recommendation is to write classes for the API(s) you want to use. This way it's easier to manage the calls, processes, and general functionality within your code.

The important part of this section is including your Python code in your Swift project. `venv` is quite ubiqitous (or `virtualenv`, whichever), so I always start by creating a `venv` for my Python projects. You can include this in your Swift project as well.
 1. Go into your project settings > Targets > project name > Copy Bundle Resources
 2. Use the "+" to add any additional files and folders. This means your Python files (since they're not automatically included) and `venv` containing necessary modules. This will allow Swift to find your code

#### Using Your Python Code

To access the code you wrote, you'll import PythonKit into the corresponding Swift files where you need to access it.
```
import PythonKit
```

From there, you need to run:
```
let sys = Python.import("sys")
sys.path.append("/path/to/your/whole/project")
my_py_file = Python.import("your_file_name")
```

After this, you should be set to go. Everything should be in place for you to run Python code in Swift. For example, if you have a Python file called `main.py`, with a class called `Test_Class` in it, you can create a new instance of `Test_Class` the same way you access it in Python:
```
test_class_instance = my_py_file.Test_Class()
```

You will be able to access all of its properties and methods.

#### Remarks

I'd like to reiterate that best practices (for neither Swift nor Python) were not in mind during the writing of this post. In fact, even I hit the best practices wall while writing code for my project. I'd suggest doing research on both Swift and Python best practices; get used to their individual conventions. PythonKit opens up a lot of new possibilities for devs like myself.