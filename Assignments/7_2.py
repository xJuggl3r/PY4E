# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values 
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter a file name to open: ")
fhand = open(fname)
c = 0
total = 0

for line in fhand:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cpos = line.find(":")
    number = line[cpos+1 :]
    fnumber = float(number)
    c = c+1
    total = total + fnumber

print("Average spam confidence:", total/c)
