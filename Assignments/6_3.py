# Exercise 3: Encapsulate this code in a function named count, and generalize it 
# so that it accepts the string and the letter as arguments.
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(word, l):
    count = 0
    for letter in word:
        if letter == l:
            count += 1
    # print("The total of '%s' in %s is: %d" % (l, word, count)) #outdated
    print("The total of '{0}' in '{1}' is: {2}".format(l, word, count))

myword = input("Type a word: ")
myletter = input("Type a letter to check if it's present: ")

count(myword, myletter)