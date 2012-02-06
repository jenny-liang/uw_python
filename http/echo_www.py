"""
hello_www.py - minimal web server + web application
"""

import socket 
import sys


page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
jenny-liang: %s
</body>
</html>
"""
#40 every ip address port.
host = '' 
port = 8082 # different default port than thirty_minute_webserver

# optional command line argument: port 
if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_www listening on port', port
s.listen(backlog) 

def get_request(stream):  #stream is boil down to the socket
    print "get_request",stream
    method = None
    while True:
        line = stream.readline()
        print line
        if not line.strip(): 
            break
        elif not method: 
            method, uri, protocol = line.split()
    return uri.lstrip("/")

while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    stream =  client.makefile('r+')       
    #data = client.recv(size) # HTTP request - not too big!  Just ignore contents
    url = get_request(stream)
    stream.close()
    client.send(page % url) # HTTP response - same for any request
    client.close()
