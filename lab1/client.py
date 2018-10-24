#Socket client example in python

from socket import *  #for sockets
import sys  #for exit

#create an INET, STREAMing socket
s = socket(AF_INET, SOCK_STREAM)
print 'Socket Created'
host = sys.argv[1]
port = int(sys.argv[2])
text = sys.argv[3]

#Connect to remote server
s.connect((host , port))
print 'Socket Connected to ' + host
#Send some data to remote server
message = "GET /"+text+" HTTP/1.0\n\n"

#Set the whole string
s.send(message)
print 'Request sent'
#Now receive data
reply = s.recv(10000)
print reply
s.close()
