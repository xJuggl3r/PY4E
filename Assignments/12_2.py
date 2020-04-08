# Exercise 2: Change your socket program so that it counts the number of characters it has received and 
# stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document 
# and count the total number of characters and display the count of the number of characters at the end of the document.

import re
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Type the full url you want to connect: ")
words = url.split('/')
host = words[2]
count = 0

try:
    cmdhost = words[0]+"//"+host+"/"+words[-1]
except:
    if len(words[0]) > 4:
        print("Error: Insert the whole url, including http://.")

try:
    mysock.connect((host, 80))
except:
    print("Host '{0}' not found, aborting.\n".format(url))
    exit()  

cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(cmdhost).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(3000)
    length = re.findall('Content-Length: ([0-9]+)'.encode(), data)

    count = count + len(data)
    if len(data) < 1:
        break
    if len(data) >=3000:
        print(data.decode(),end='\n\n')
        break
    print(data.decode(),end='')
    print("Total count is {0}".format(length))
    

mysock.close()

print("Character count is:", count)
