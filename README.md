"# prototype2023" 

# Requirements

- Python 3.11
- Libraries in requirements.txt
- Internet access for database connection

# Project Overview

The app itself is very primitve, and the functionality is conveyed from the image in the portfolio itself. If you , the reviewers , have limited time for reviewing my portfolio, I recommend NOT going trough this.

---

This was the first prototype of the greater (all-included) pharmacy software. I started creating this in July 2024. As you can see, it is really bad. The entire software consists of these four screens (stitched together) . The entire app was coded in python using Tkinter, and had a MySQL database.

The main issue I had with this problem , besides the bad UI language choice, was I couldn't move forward to a new part of the software. This was the first prototype, and I started it as a challenge right after leaving my job at the pharmacy.

With this short-lasting motivation, I created these four components. However after finishing them, I had no idea of how to start the next component. It relied on the previous components. I had completed them so fast, not taking future dependencies into consideration. This thought me how to properly plan a project and not repeat mistakes like these again.

# Connection

The app needs to connect to the database in order to function properly. Without the database connection the screens would be empty, as all information is stored in the database. 

In the original prototype, the app used MySQL, however due to the last product using PostgreSQL, I recreated the original database design in PostgreSQL. The current populated tables are all example, manufactured information.

---

**Untouched version of the app is on the original branch.**

*I know making the database connection credentials is bad for security, however as the database doesn't contain any important information, I made them public anyways.*