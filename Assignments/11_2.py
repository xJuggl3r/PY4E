# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re

fname = input("Enter a file: ")
count = 0
total = 0
try:
    fhand = open(fname)
except:
    print("File '{0}' not found, aborting.".format(fname))
    exit()

for line in fhand:
    line = line.rstrip()
    x = re.findall('New.\S*: ([0-9.]+)', line)
    if len(x) > 0:
        for value in x:
            value = int(value)
            total = total + value
            count +=1
average = total/count

print(int(average))