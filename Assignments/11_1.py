# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re

regex = input("Enter a regular expression to see if it has matches: ")
fname = input("Enter a file: ")
count = 0
try:
    fhand = open(fname)
except:
    print("File '{0}' not found, aborting.".format(fname))
    exit()

for line in fhand:
    line = line.rstrip()
    y = re.findall(regex, line) 
    if len(y) > 0:
        count +=1
print("File {0} had {1} lines that matched {2}".format(fname, count, regex))

