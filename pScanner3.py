import socket


host = input("Website/IP to scan: ")
ip = socket.gethostbyname(host)

minPort = int(input("Min port: "))
maxPort = int(input("Max port: "))

try:
	for port in range(minPort, maxPort + 1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result == s.connect_ex((ip, port))
		if result == 0:
			print("Port %d: Open)" %(port))
		else:
			print("Port %d: Close)" %(port))

except:
	pass
