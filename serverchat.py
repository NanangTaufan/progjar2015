#serverchat.py
#nanang taufan
#5113100183
import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a TCP/IP socket
sock2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Bind the socket to the port
server_address2 = ('localhost', 1010)
print >>sys.stderr, 'starting up on %s port %s' % server_address2
sock2.bind(server_address2)

# Listen for incoming connections
sock.listen(1)

# Listen for incoming connections
sock2.listen(1)

print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()
connection2, client_address2 = sock2.accept()

print >>sys.stderr, 'connection from', client_address
print >>sys.stderr, 'connection from', client_address2

while True:
    data = connection.recv(512)
    if not data :
	  print >> sys.stderr, 'disconnect from client'
	  break    

    else :
	  print >>sys.stderr, 'received "%s"' % data

  	print >>sys.stderr, 'sending data to client 2'
    	connection2.sendall(data)
    
    data2 = connection2.recv(512)
    if not data2 :
  	print >> sys.stderr, 'disconnect from client 2'
	  break
  
    else :
    	print >>sys.stderr, 'received "%s"' % data2
    	print >>sys.stderr, 'sending data to client'
    	connection.sendall(data2)    
connection.close()             
