# Exercise 6: Rewrite the program that prompts the user for a list of numbers and 
# prints out the maximum and minimum of the numbers at the end when the user enters "done". 
# Write the program to store the numbers the user enters in a list and 
# use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

numlist = list()

while True:
    num = input("Enter a number: ")

    if num == "done" : break

    try:
        fnum = float(num)  
    except:
        print("Invalid number")
        continue

    numlist.append(fnum)

print("Maximum is: ", max(numlist))
print("Minimum is: ", min(numlist))