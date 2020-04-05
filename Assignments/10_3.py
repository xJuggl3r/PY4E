# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
import string
count = 0
fhand = open("words.txt")
mydict = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            count += 1
            if letter not in mydict:
                mydict[letter] = 1
            else:
                mydict[letter] += 1
# print(mydict)

lst = list()
for key, value in list(mydict.items()):
    lst.append((key, value))

lst.sort()

for key, value in lst:
    print(key, value)    
