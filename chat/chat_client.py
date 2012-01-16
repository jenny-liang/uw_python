"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""
import socket 
import sys
import select

host = 'localhost' 
port = 50000 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))

quit = False

while not quit: 
    # Wait for input from stdin & socket
    inputready, outputready,exceptrdy = select.select([0, s], [],[])            
    for i in inputready:
	if i == 0:
	   data = sys.stdin.readline().strip()
	   if data != '':		        
	       s.send(data)
	   else:
	       print 'Shutting down.'
	       quit = True;
	elif i == s:
	    data = s.recv(size)
	    if data:
		print 'from (%s,%s):  %s' % (host, port, data) + '\n'
s.close() 


