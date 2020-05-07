import socket
from socket import gethostbyname

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = input("Website you want to scan: ")
ip = gethostbyname(host)
port = int(input("Min range of port you want to scan: "))
maxPort = int(input("Max range of port you want to scan: "))


for x in range(port, maxPort + 1):
	con = s.connect_ex(ip, x)
	if(con == 0):
		print("Port %d: open" % (x,))
	s.close()
