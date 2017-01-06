# import socket
from socket import *
#from socket import socket, bind, isten, recv, send
HOST = "127.0.0.1"
PORT = 8080
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
i = True
while i is True:
	data = conn.recv(1024)
	print "Received ", repr(data)
	if not data: break
	reply = raw_input("Reply: ")
	conn.sendall(reply)

conn.close()