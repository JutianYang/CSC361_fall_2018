import sys
import time
from socket import *

def main():
    if len(sys.argv)!=3:
        print("Usage: python UDP_Pinger_Client.py <server IP address> <server port number>")
        sys.exit()
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    address = (server_ip, server_port)  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
	
    s.settimeout(1)

    # Ping 10 times
    for i in range(10):
        
        sendTime = time.time()
        message = 'PING ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
        clientSocket.sendto(message, remoteAddr)
        
        try:
            data, server = s.recvfrom(1024)
            recvTime = time.time()
            rtt = recvTime - sendTime
            print ("Message Received"+ data)
            print ("Round Trip Time"+ rtt)
            print ("\n")
        
        except timeout:
            print ("REQUEST TIMED OUT")
            print ("\n")
if __name__=="__main__":
    main()
