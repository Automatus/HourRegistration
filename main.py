#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Urenregistratie

@author: Automatus

automatically registers worked hours

an example of how things will appear in a file:
    Checked in for project x on Fri Feb 7 15:08:54 2020
    Checked out for project x on Fri Feb 7 15:10:02 2020
    Minutes worked: 1
    New total minutes worked: 9

info will also be stored in a SQL table
"""

import time
import re
import sqlite3
import os

# Program for registering hours worked on certain project

if not os.path.isfile(os.path.join(os.getcwd(), "Projects")):
    file = open("Projects", "w")
    file.close()

while True:
    # Showing available projects
    print("Choose your project:")
    file = open("Projects", "r")
    projects = file.readlines()
    projectslist = []
    x = 1
    print("0. New File")
    for line in projects:
        projectslist.append(line.strip())
        print(str(x) + ". " + line.strip())
        x += 1
    file.close()
    choice = int(input())-1
    if choice == -1:
        ProjectChoice = input("Name of new project:\n")
        file = open("Projects", "a")
        file.write(ProjectChoice + "\n")
        file.close()
    else:
        ProjectChoice = projectslist[choice]

    # registering starttime
    starttime = time.time()
    sqlstarttime = time.asctime(time.localtime())
    print("\nChecked in on " + time.asctime(time.localtime()))
    file = open(ProjectChoice, "a")
    file.write("Checked in  on " + time.asctime(time.localtime()) + "\n")
    file.close

    # registering endtime and adding to total
    input("Press ENTER to check out\n")
    endtime = time.time()
    sqlendtime = time.asctime(time.localtime())
    minutesworked = int((endtime - starttime)/60)
    if choice == -1:
        oldtotal = 0
    else:
        file = open(ProjectChoice, "r")
        oldtotal = re.sub("[^0-9]", "", file.readlines()[-2])
        # new: [^0-9]    old: \D
        file.close()
    newtotal = int(oldtotal) + minutesworked
    print("\nChecked out on " + time.asctime(time.localtime()))
    print("Minutes worked: " + str(minutesworked) + "\n" +
          "New total minutes worked: " + str(newtotal) + "\n")
    file = open(ProjectChoice, "a")
    file.write("Checked out on " + time.asctime(time.localtime()) + "\n" +
               "Minutes worked: " + str(minutesworked) + "\n" +
               "New total minutes worked: " + str(newtotal) + "\n")
    file.close

    conn = sqlite3.connect('urenregistratie.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS ''' + ProjectChoice + '''
                 (StartTime TINYTEXT,
                  EndTime TINYTEXT,
                  MinutesWorked TINYTEXT,
                  NewTotalMinutesWorked TINYTEXT);''')
    values = [sqlstarttime, sqlendtime, minutesworked, newtotal]
    conn.execute("INSERT INTO " +
                 ProjectChoice + " VALUES (?, ?, ?, ?)", values)
    # would be better to not use string operations in sql code, so be
    # carefull with naming projects for now :)
    # https://xkcd.com/327/
    conn.commit()
    conn.close()
