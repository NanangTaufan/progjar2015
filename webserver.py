import sys

import BaseHTTPServer

from SimpleHTTPServer import SimpleHTTPRequestHandler

srvr = BaseHTTPServer.HTTPServer
hnd = SimpleHTTPRequestHandler

Protocol = 'HTTP/1.0'

if sys.argv[1]:
	port = int(sys.argv[1])
else:
	port = 8080
srvradrs = ('127.0.0.1', port)

hnd.protocol_version = Protocol
h = srvr(srvradrs, hnd)

print("The Server is success!")
h.serve_forever()	
