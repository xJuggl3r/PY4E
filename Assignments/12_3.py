# Exercise 3: Use urllib to replicate the previous exercise of 
# (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and 
# (3) counting the overall number of characters in the document. 
# Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

url = input("Type the full url you want to connect: ")
fhand = urllib.request.urlopen(url)
content = fhand.read()

# Since we only need to print the full file if it's <= 3000 
# we can specify the length (in bytes) to be read and print.    
print(content[:3001].decode().strip())

print("\nDocument length is {}".format(len(content)))