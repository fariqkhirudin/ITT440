import socket
from socket import gethostbyname

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Website to scan: ")
ip = socket.gethostbyname(host)

def portScanner(ip, port):
	try:
		s.connect((ip,port))
	except:
		return False
	else:
		return True

for portNumber in range(1,100):
	if portScanner(ip, portNumber):
		print("Port", portNumber, ": Open")
