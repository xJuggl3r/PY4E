# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples 
# from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

edict = dict()
fname = input("Enter a file: ")
try:
    fhand = open(fname)
except:
    print("File not found, aborting")
    exit()

for line in fhand:
    words = line.rstrip().split()

    if len(words) < 3 or words[0] != 'From': continue
    edict[words[1]] = edict.get(words[1], 0) + 1 #smaller loop using .get() method

# Sort the dictionary by value
lst = list()
for email, count in list(edict.items()):
    lst.append((count, email))

lst.sort(reverse=True)

for key, value in lst[:1]:
    print(value, key)
