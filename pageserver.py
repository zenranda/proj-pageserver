"""
  CS322 Project 1
  Author: Marc Leppold
  A trivial web server in Python. Adapted from starter code.

  Based largely on https://docs.python.org/3.4/howto/sockets.html
  This trivial implementation is not robust:  We have omitted decent
  error handling and many other things to keep the illustration as simple
  as possible.
  
  Contains 3 pages - home.html, trivia.html and colors.html.
  All three are barebones  but contain unique .css.
  
  Usage: Request <ip address>:8000/FILE [html or css only]

"""

import CONFIG    # Configuration options. Create by editing CONFIG.base.py
import argparse  # Command line options (may override some configuration options)
import socket    # Basic TCP/IP communication on the internet
import _thread   # Response computation runs concurrently with main program 
import os        # Needed for directory validation.

def listen(portnum):
    """
    Create and listen to a server socket.
    Args:
       portnum: Integer in range 1024-65535; temporary use ports
           should be in range 49152-65535.
    Returns:
       A server socket, unless connection fails (e.g., because
       the port is already in use).
    """
    # Internet, streaming socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to port and make accessible from anywhere that has our IP address
    serversocket.bind(('', portnum))
    serversocket.listen(1)    # A real server would have multiple listeners
    return serversocket

def serve(sock, func):
    """
    Respond to connections on sock.
    Args:
       sock:  A server socket, already listening on some port.
       func:  a function that takes a client socket and does something with it
    Returns: nothing
    Effects:
        For each connection, func is called on a client socket connected
        to the connected client, running concurrently in its own thread.
    """
    while True:
        print("Attempting to accept a connection on {}".format(sock))
        (clientsocket, address) = sock.accept()
        _thread.start_new_thread(func, (clientsocket,))


## HTTP response codes, as the strings we will actually send. 
##   See:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
##   or    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
## 
STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"

def respond(sock):
    """
    This server responds only to GET requests (not PUT, POST, or UPDATE).
    Any valid GET request is answered with the appropriate file. 
    A 403 or 404 error message will be issued if the request is invalid or tries to access forbidden areas.
    """
    request = sock.recv(1024)  # We accept only short requests
    request = str(request, encoding='utf-8', errors='strict')
    print("\nRequest was {}\n".format(request))

    parts = request.split()
    
    if len(parts) > 1 and parts[0] == "GET":
        transmit(STATUS_OK, sock)

        path = parts[1]                                       #our page's path
  
        if any(x in path for x in ['~','..','//']):          #if URL contains banned characters
            transmit((STATUS_FORBIDDEN), sock)
        
        elif not any(x in path for x in ['.css','.html']):    #if the wrong kind of file is requested
            transmit((STATUS_FORBIDDEN), sock)
  
        elif not os.path.isfile('.\\pages/' + path[1:]):      #if URL doesn't correspond to a path
            print('.\\pages/' + path[1:])
            transmit((STATUS_NOT_FOUND), sock)
        
        else:
            with open('.\\pages/' + path[1:], 'r') as body:
                main = body.read()
            transmit(main, sock)
    else:
        transmit(STATUS_NOT_IMPLEMENTED, sock)        
        transmit("\nI don't handle this kind of request: {}\n".format(request), sock)

    sock.close()
    return 

def transmit(msg, sock):
    """It might take several sends to get the whole message out"""
    sent = 0
    while sent < len(msg):
        buff = bytes( msg[sent: ], encoding="utf-8")
        sent += sock.send( buff )
    

###
#
# Run from command line
#
###

def get_options():
    """
    Options from command line or configuration file.
    Returns namespace object with option value for port
    """
    parser = argparse.ArgumentParser(description="Run trivial web server.")
    parser.add_argument("--port", "-p",  dest="port", 
                        help="Port to listen on; default is {}".format(CONFIG.PORT),
                        type=int, default=CONFIG.PORT)
    options = parser.parse_args()
    if options.port <= 1000:
        print("Warning: Ports 0..1000 are reserved by the operating system")
    return options
    

def main():
    options = get_options()
    port = options.port
    sock = listen(port)
    print("Listening on port {}".format(port))
    print("Socket is {}".format(sock))
    serve(sock, respond)
    
main()
