from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)
ServerPort = 9998

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Fill in start

tcpSerSock.bind(("", ServerPort))

tcpSerSock.listen(1)

# Fill in end

while 1:
    print('Ready to server...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(2048).decode()
    print(message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check whether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServe finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start

        tcpCliSock.close()

        # Fill in end
        print('Read from cache')
    # Error handling for file not found in the cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            # Create a temporary file on this socket and ask port 80 for the file requested
            fileobj = c.makefile('r', 0) # Instead of using send and recv, we can use makefile
            fileobj.write("GET " + "http://" + filename + "HTTP/1.0\n\n") # If this line does not work, write separate lines for "Get..." and "Host..."
            


