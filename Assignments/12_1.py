# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
# You can use split('/') to break the URL into its component parts so you can extract the host name 
# for the socket connect call. Add error checking using try and except to handle the condition where 
# the user enters an improperly formatted or non-existent URL.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Type the full url you want to connect: ")
words = url.split('/')
host = words[2]

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
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()