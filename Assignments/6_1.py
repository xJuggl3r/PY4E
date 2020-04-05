# Exercise 1: Write a while loop that starts at the last character in the string 
# and works its way backwards to the first character in the string, 
# printing each letter on a separate line, except backwards.

word = input("Type a word to see it reversed: ")
index = len(word)-1
while index >= 0:
    letter = word[index]
    print(letter)
    index -= 1

# Loop to go forward instead of backward:
# index = 0
# while index < len(word):
#     letter = word[index]
#     print(letter)
#     index = index + 1