# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary 
# using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
# and print how many messages the person has.

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
    line = line.rstrip().split()

    if len(line) < 3 or line[0] != 'From': continue
    edict[line[1]] = edict.get(line[1], 0) + 1 #smaller loop using .get() method


# Max loop
bigcount = None
bigemail = None

for email, count in edict.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)