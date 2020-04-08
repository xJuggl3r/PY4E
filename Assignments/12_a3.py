# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
# the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and 
# the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Fia.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: C

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# import requests

# # Set headers
# headers = requests.utils.default_headers()
# headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
link_line = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

while count >= 0:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5"
    req = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') # Retrieve all of the anchor tags
    print("Retrieving:", url)
    url = tags[link_line].get("href", None)
    count = count - 1