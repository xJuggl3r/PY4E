# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the "From" line by finding the time string and then splitting that string 
# into parts using the colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

hourdict = dict()
fname = input("Enter a file: ")
try:
    fhand = open(fname)
except:
    print("File not found, aborting")
    exit()

for line in fhand:
    words = line.rstrip().split()
    
    if len(words) < 3 or words[0] != 'From': continue
    time = words[5].split(":")
    hour = time[0]
    hourdict[hour] = hourdict.get(hour, 0) + 1 #smaller loop using .get() method
    
lst = list()
for hour, count in list(hourdict.items()):
    lst.append((hour, count))

lst.sort()

for hour, count in lst:
    print(hour, count)    
    