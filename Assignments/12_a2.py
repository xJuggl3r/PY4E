# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
# and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_411320.html (Sum ends with 73)

# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file 
# except for lines like the following:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
# You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them 
# to integers and add them up to complete the assignment.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")   
sum = 0  
tags = soup('span')  

# Look at the parts of a tag  
for tag in tags:  
    sum += int(tag.contents[0])  
print ('Count = ', len(tags))  
print ('Sum = ', sum)  