# Exercise 4: There is a string method called count that is similar to the function in the previous exercise. 
# Read the documentation of this method at:
# https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs in "banana".

def count(word, l):
    count = word.count(l)
    print("The total of '{0}' in '{1}' is: {2}".format(l, word, count))

myword = input("Type a word: ")
myletter = input("Type a letter to check if it's present: ")

count(myword, myletter)