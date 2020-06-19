#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Urenregistratie

@author: Automatus

automatically registers worked hours

make a file in the same folder called Projects

this program is terminal based (at least so far)

an example of how things will appear in a file:
    Checked in for project x on Fri Feb 7 15:08:54 2020
    Checked out for project x on Fri Feb 7 15:10:02 2020
    Minutes worked: 1 New total minutes worked: 9
"""

import time
import re

# Program for registering hours worked on certain project

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
    print("\nChecked in on " + time.asctime(time.localtime()))
    file = open(ProjectChoice, "a")
    file.write("Checked in  on " + time.asctime(time.localtime()) + "\n")
    file.close

    # registering endtime and adding to total
    input("Type 0 and ENTER to check out\n")
    endtime = time.time()
    minutesworked = int((endtime - starttime)/60)
    if choice == -1:
        oldtotal = 0
    else:
        file = open(ProjectChoice, "r")
        oldtotal = re.sub("\D", "", file.readlines()[-2])
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
