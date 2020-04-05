#Exercise 2: Write a program which repeatedly reads numbers until the user enters "done".
#Once "done" is entered, print out the total, count, and both the maximum and minimum of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except
#and print an error message and skip to the next number.

c = 0
total = 0
max = None
min = None

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

    if max is None or fnum > max:
        max = fnum
    
    if min is None or fnum < min:
        min = fnum

print("Total is:", total)
print("Count is:", c)
print("Maximum is: ", max)
print("Minimum is: ", min)