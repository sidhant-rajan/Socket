from socket import *
HOST = "127.0.0.1"
PORT = 8080
s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))
i = True
while i is True:
	message = raw_input("Your Message: ")
	s.send(message)
	print "Awaiting reply"
	reply = s.recv(1024)
	print "Received ", repr(reply)

s.close()
