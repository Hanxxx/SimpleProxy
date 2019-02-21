import socket

HTTP_VERSION = 'HTTP/1.0'

class BasicServer:
    """
    Basic proxy server. Can forward browser's HTTP request and send response back.
    No support for cache.
    """
    def __init__(self, port=8011):
        # create socket and config it.
        self.ServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ServerSock.bind(("", port))


    def _parse_browser_request(self, browser_request):
        # Leave parse for later work
        return 'www.google.com', 80, '/', 'GET', 'host: www.google.com\r\n', None


    def start_proxy(self):
        # start listen and accept browser's requests
        self.ServerSock.listen(5)
        # we handle request in single thread
        while 1:
            connect_sock, connect_addr = self.ServerSock.accept()
            browser_request = ""

            while 1:
                chunk = connect_sock.recv(2048)
                if chunk == '':
                    break
                browser_request += chunk

            # got the browser request

            http_host, http_port, http_path, http_method, http_header, http_body = \
                self._parse_browser_request(browser_request)


