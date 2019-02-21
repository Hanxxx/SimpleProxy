import socket

CHUNK_SIZE = 2048
http_host = "www.google.com"
http_port = 80
filename = "/"
HttpTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HttpTCPSocket.connect((http_host, http_port))
HttpTCPSocket.send("GET / HTTP/1.0\n\n".decode("UTF-8"))

chunk = HttpTCPSocket.recv(CHUNK_SIZE)
if chunk:
    with open(http_host + ".html", "wb") as fout:
        while chunk:
            fout.write(chunk)
            chunk = HttpTCPSocket.recv(CHUNK_SIZE)


HttpTCPSocket.close()