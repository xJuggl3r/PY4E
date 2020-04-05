# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
#  Write a program to open the file romeo.txt and read it line by line.
#  For each line, split the line into a list of words using the split function.
#  For each word, check to see if the word is already in a list.
#  If the word is not in the list, add it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

#open file
fhand = open("romeo.txt")

nlist = list()

#read line by line, strip the \n and split the words to a list
for line in fhand:
    mylist = line.rstrip().split()

    #if word is not in the new list, append it
    for word in mylist:
        if word in nlist: continue
        else: nlist.append(word)

nlist.sort()
print("Original list is:", mylist)
print("The new and sorted new list is:", nlist)