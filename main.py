import time

# Program for registering hours worked on certain project


# Showing available projects
# print("Available projects:")
# print("0. New project \n")

# choosing project
# ProjectChoice = input("Choose a number\n")

# registering starttime
starttime = time.time()
print("\nChecked in for " + "project x" + " on " + time.asctime(time.localtime()))
file = open("Registration.txt", "a")
file.write("Checked in for " + "project x" + " on " + time.asctime(time.localtime()) + "\n")
file.close

# registering endtime
print("0. check out\n")
input("Choose a number\n")
endtime = time.time()
minutesworked = int((endtime - starttime)/60)
print("\nChecked out for " + "project x" + " on " + time.asctime(time.localtime()))
print("Minutes worked: " + str(minutesworked) + "\n\n")
file = open("Registration.txt", "a")
file.write("Checked out for " + "project x" + " on " + time.asctime(time.localtime()) + "\n" + "Minutes worked: " + str(minutesworked) + "\n")
file.close
