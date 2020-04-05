#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
#Once "done" is entered, print out the total, count, and average of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except
#and print an error message and skip to the next number.

c = 0
total = 0

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break

    try:
        fnum = float(num)
        
    except:
        print("Invalid number")
        continue

    c = c+1
    
    total = total + fnum


print("Total is:", total)
print("Count is:", c)
try:
    print("Average is:", total/c)
except:
    print("Cannot calculate average when dividing by zero")






