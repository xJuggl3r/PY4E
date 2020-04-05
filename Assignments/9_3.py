# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary 
# to count how many messages have come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

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

print(edict)



# edict = dict()
# c = 0
# fname = input("Enter a file: ")
# try:
#     fhand = open(fname)
# except:
#     print("File not found, aborting")
#     exit()

# for line in fhand:
#     line = line.rstrip().split()
#     if len(line) < 3 or line[0] != 'From': continue

#     if line[1] not in edict:
#         edict[line[1]] = 1
#     else:
#         edict[line[1]] += 1

# print(edict)
