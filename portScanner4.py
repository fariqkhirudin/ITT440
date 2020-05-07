import socket
from socket import gethostbyname
from datetime import *


def scanner(host, port):
    s = socket.socket()
    s.settimeout(0.1)

    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

host = input("Enter the host:")
ip = socket.gethostbyname(host)

rangeMin = int(input("Min range to scan: "))
rangeMax = int(input("Max range to scan: "))

t1 = datetime.now()

for port in range(rangeMin, rangeMax + 1):
    if scanner(ip, port):
        print("Port ", port, ": Open")

t2 = datetime.now()

totalTime = t2-t1
#    else:
#        print("Port ", port, ": Closed")
print("Scan completed in ", totalTime )
