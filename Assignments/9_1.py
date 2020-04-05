# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.

count = 0
fhand = open("words.txt")
mydict = dict()
for line in fhand:
    line = line.rstrip().split()

    for word in line:
        count += 1 #add a sequential value for the keys, since only keys are needed
        if word in mydict : continue
        mydict[word] = count

guess = input("Type a word to check if it is in the dictionary: ")

if guess in mydict:
    print("'%s' is in the dictionary" %guess)
else:
    print("The word '%s' is not in the dictionary" %guess)