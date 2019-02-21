import socket

http_host = "www.google.com"
http_port = 80
filename = "/"
HttpTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HttpTCPSocket.connect((http_host, http_port))
f = HttpTCPSocket.makefile('r', 0)
f.write("GET " + filename + " HTTP/1.0\n\n")
responce = f.read()
if responce:
    with open("g.html", "wb") as fout:
        fout.write(responce)


HttpTCPSocket.close()
