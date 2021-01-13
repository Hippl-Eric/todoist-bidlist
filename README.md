# todoist-bidlist
A convenient time saver to email your boss your todo list.


Key Features:
- Recieve request data from the [Todoist REST API](https://developer.todoist.com/rest/v1/#overview)
- Sort tasks using quick sort algorithm
- "Task" and "JSON_List" objects to organize tasks in parent-child structure
- Output tasks to formatted HTML
- Utilize the [pywin32](https://pypi.org/project/pywin32/) package to automate sending email through Microsoft Outlook

### Table of Contents

- [Background](#background)
- [File Summary](#file-summary)
    - [sfcbidlist.py](#sfcbidlist.py)
    - [classes.py](#classes.py)
    - [print_bid_list.py](#print_bid_list.py)
    - [bidlist_html.py](#bidlist_html.py)
    - [bidlist_outlook.py](#bidlist_outlook.py)
- [What I Learned](#what-i-learned)
- [Contact](#contact)

### Background

At my job, I am responsible for tracking and prioritizing incoming bid solicitations.  To do this, I use [Todoist](https://todoist.com/home), a user-friendly todo list web application.  My boss saw me using this one day during a screen share and asked me to email him the list.  Sure I said, only to later realize copy and pasting my todo list into email was a formatting nightmare.  There had to be a better way.  My first thought was to utilize web scrapping, but found that Todist has it's own  [REST API](https://developer.todoist.com/rest/v1/#overview).  Score!  So I built this.

### File Summary

#### sfcbidlist.py
Main script to create a list of tasks.  Calls Todist REST API.  Utilizes a quick sort algorithm to sort the tasks.

#### classes.py
Creates two (2) class objects: JSON_List and Task.  JSON_List includes method to insert tasks into parent-child relationship (task-subtask).

#### print_bid_list.py
Includes teo (2) helper functions: simple_print and printHTML.  simple_print, prints directly to the terminal.  printHTML returns an HTML formatted order list.  This HTML formatting is useful for web page rendering and outlook emails.

#### bidlist_html.py
Writes a quick HTML file in the local directory and opens the file using the webbrowser package.  Good solution for a PC that does not have Microsoft Outlook.

#### bidlist_outlook.py
Automates email delivery of HTML formatted list.  Uses win32com.client package to interact with Microsoft Outlook on users PC.

### What I Learned
- Reinforced knowledge interacting with external APIs
- Reinforced data structure and sorting algorithms
- Create HTML files with python
- Interact with the Windows API using win32com.client package in python

### Contact

Eric Hippler, [LinkedIn](https://www.linkedin.com/in/eric-hippler/), erichippler.com
