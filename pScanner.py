import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("IP you want to scan: ")
minPort = int(input("Min range of port you want to scan: "))
maxPort = int(input("Max range of port you want to scan: "))

port = minPort

def portScanner(port):
	while port <= maxPort:
		if s.connect_ex((host, port)):
			print("The port", port, "is closed")
			port += 1
		else:
       			print("The port", port, "is open")

while port <= maxPort:
	portScanner(port)
	port += 1
else:
	print("Scan completed")
#while minPort <= maxPort:
#	portScanner(port)
#	minPort += 1;
#else:
#	print("Scan completed")
