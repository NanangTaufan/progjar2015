#clientchat.py
#nanang taufan
#5113100183
import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8080)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


while True:
    # Send data
    message = raw_input ("type message: ")
    sock.sendall(message)
    data = sock.recv(512)
    print >>sys.stderr, 'client 2: "%s"' % data
