# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers 
# and summing up the integers.

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
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        for value in x:
            value = int(value)
            total = total + value
            count +=1

print(total)