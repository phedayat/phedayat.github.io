---
layout: page
title: Projects
permalink: /projects/
---

<h1 class="page-heading">Projects</h1>

#### _Personal Site_
##### No public repo available

You're already using this project! After two and a half years, I've finally built my personal site. The development didn't take that long, I just didn't do it. I hope you're enjoying the experience. Read about [how to set up a site similar to this](/2021/09/16/site-repls.html). You can also read about [my thoughts on this and how I've set it up](/2021/09/15/new-post.html).

---
<br>
#### _Team003 No Time To Cook_
##### [Visit the repo](https://github.com/cse110-fa21-group3/cse110-fa21-group3)

During Fall quarter 2021, I took a software engineering course. I was put in a group of ten and we were tasked with creating a CRUD app, specifically a recipe manager. I very quickly took on a leadership position as the back-end team lead, and helped setup a foundation so that we could get our web app to be functional as quickly as possible. I also managed (both in subscription and use) the recipe API we used, Spoonacular.

The project is written in HTML/CSS/JavaScript, without the use of external frameworks. Its features include webscraping recipes from other sites, adding custom recipes, and an insightful homepage that shows you a myriad of recipes to try.

While the project skeleton still exists, Spoonacular was a paid API that we no longer subscribe to. [Visit the skeleton!](https://notimetocook.netlify.app/)

---
<br>
#### _What's really making us happy?_
##### No public repo available
##### [Watch our project video](https://www.youtube.com/watch?v=46IGNEDuWRo)

In Fall quarter 2021, I took a data science class in which we formed groups to work on a DS project. My group chose to use the "World Happiness Report" dataset in order to glean what might be the biggest factor(s) in a citizen's happiness.

The dataset had over 1900 records spanning across 5 years from more than 190 countries. It used several fields to gather data about world happiness. My group and I did an EDA and used (multi)linear regressions to gain the insights we needed.

We came to the conclusion that people are happy when they have the freedom to make their own life choices and have family and friends to support them.

---
<br>
#### _Leetles' Advanced Calendar_
##### [Visit the repo](https://github.com/os-ucsd/leetles)

From February 2021 to March 2021, I worked with 3 other UCSD students to create a small open source project based around the theme of "Productivity tools in the Pandemic". We built a prototype "Advanced Calendar" which would allow a user to manage their classes and projects without having to clutter a single calendar.

We used Google Calendar and its API to run everything in the backend. I wrote JavaScript classes to handle using the API and user authentication. The whole project was written in vanilla HTML/CSS/JavaScript.

Read more about [my involvement in the project](/extra/).

My own offshoot of the idea exists as a less visually appealing lite version of the original Advanced Calendar. It still performs the basic functionality of creating and adding to calendars for specific projects/classes. It also displays upcoming events. It's essentially a fork of the original with less design.

---
<br>
#### _Expenses_
##### No public repo available

I recently moved back to La Jolla for my final year of undergrad, so I wanted a way to track my expenses. I used Google Sheets as a way of managing the expenses across several spreadsheets. Each one contains a table with some metrics off to the side. 

I built a premilinary Python class to interface with the sheet, using the Google Sheets and Drive APIs. I used Swift to build a small GUI to use on my desktop. Within it, I used PythonKit to allow Swift to use the class I wrote in Python. Currently, it's able to add a row to whichever spreadsheet the expense belongs to by taking input from the desktop app.

---
<br>
#### _Cookie Clicker Bot_
##### [Visit the repo](https://github.com/phedayat/sel_cookie)

Using Selenium in Python, I created a bot that plays the game ["Cookie Clicker"](https://orteil.dashnet.org/cookieclicker/). It begins by receiving 1000 clicks immediately. Each click from the script is referred to as a "rapid click". After the inital clicks, jobs for purchasing upgrades and products are scheduled. In regular intervals, they buy whatever upgrades and products they can given the cookies we have. A small GUI also appears that allows you to begin an arbitrary amount of rapid clicks or quit the bot.

I've been able to get this bot to work out of a repl to some degree of success.

---
<br>
#### _Star Generator_
##### [Visit the repo](https://github.com/phedayat/python-scripts/blob/master/turt.py)

Built using Python with Turtle, I wrote a script that generates stars of `n` vertices repeatedly. Basically it draws stacked stars. The stars are drawn using simple geometric formulas for regular polygons. They direct what the turtle does for any `n`-sided polygon.

The script is easily runnable through a repl, and in fact the first mockup was made there.

---
<br>
#### _SUMS Attendance Data Visualization_
##### [Visit the repo](https://github.com/phedayat/SUMS-Data)

Early in my SUMS publicity duties, I started learning Python again (since the last time I tried it in 2013) and used it to create a graph from SUMS publicity data. I used the sign-in sheet from each event we held during the 2018-2019 academic year as a reference. I created a simple plot that shows the trend in attendance across the different events. I used `pandas` for importing the CSV and parsing it, and `matplotlib` for creating the visual.

---
<br>
#### _Convex Hull Visualization (Graham scan)_
##### [Visit the repo](https://github.com/phedayat/python-scripts/tree/master/convex-hull-alg)

Using Python and Turtle, I created a visual for performing a Graham scan and finding the convex hull of a set of points. It draws out the convex hull, defining the edge of the set of points.