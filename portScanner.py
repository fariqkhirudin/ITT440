import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.40.135'
s.settimeout(5)

def pscan(port):
	if s.connect((ip,port)):
		return True
	else:
		return False

for x in range (9088,9091):
	if pscan(x):
		print('Port', x, ': Open')
	else:
		print('Port', x, ': Close')
