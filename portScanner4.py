import socket
from socket import gethostbyname
from datetime import *





def scanner(port):

    s = socket.socket()
    s.settimeout(0.1)

    try:
        s.connect((host, port))
        return True
    except:
        return False

host = input("Enter the host:")
ip = socket.gethostbyname(host) #convert url to ipv4

rangeMin = int(input("Min range to scan: "))
rangeMax = int(input("Max range to scan: "))

t1 = datetime.now()

for port in range(rangeMin, rangeMax + 1):
    if scanner(port):
        print("Port ", port, ": Open")
#    else:
#        print("Port ", port, ": Closed")

t2 = datetime.now()
totalTime = t2-t1

print("Scan completed in ", totalTime )
