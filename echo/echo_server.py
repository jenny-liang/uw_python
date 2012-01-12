"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50000
"""

import socket 
import sys

host = '' 
port = 50000 

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM -- TCPIP POTOCAL 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_server listening on port', port
s.listen(backlog) 

while True: 
    client, address = s.accept() #socket is bidirectional: return client socket talking to that client with its address
    data = client.recv(size) 
    if data: 
        client.send('jenny-liang: %s' % data) # Tell the client which server is connected.
    print 'from %s: %s' % (address, data)
    client.close()  # close the connection and wait for another client to talk to another client.

