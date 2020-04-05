# Exercise 5: This program records the domain name (instead of the address) where the message was sent from 
# instead of who the mail came from (i.e., the whole email address). At the end of the program, 
# print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

#File handling
edict = dict()
fname = input("Enter a file: ")
try:
    fhand = open(fname)
except:
    print("File not found, aborting")
    exit()

#Getting lines into list
for line in fhand:
    line = line.rstrip().split()

    #Guardian code and finder
    if len(line) < 3 or line[0] != 'From': continue
    cpos = line[1].find("@")
    domain = line[1][cpos + 1 : ]
    
    #Putting domains in dict and creating histogram
    edict[domain] = edict.get(domain, 0) + 1 #smaller loop using .get() method

print(edict)