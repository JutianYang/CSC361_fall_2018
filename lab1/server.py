#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket

serverSocket.bind(("",7080))

serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 
    print 'Received connection from', addr
    try:
        message = connectionSocket.recv(10000)     
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = f.read()
        print (outputdata)             
        #Send one HTTP header line into socket
	connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n")

        #Send the content of the requested file to the client

        
        connectionSocket.sendall(outputdata)


        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n\r\n")

        #Close client socket
        connectionSocket.close()

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data
