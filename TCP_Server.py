import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.bind(("", 9999))
    tcp_socket.listen(1)

    while 1:
        print("Waiting for client to connect...")
        connect_socket, addr = tcp_socket.accept()  # The process is blocked
        print("Connection from {}:{}".format(addr[0], addr[1]))
        while 1:
            recv_data = connect_socket.recv(1024)
            if recv_data:
                print("data received: {}".format(recv_data.decode()))
            else:
                break
        connect_socket.close()
        print("Connection close")

    tcp_socket.close()  # unreachable because of dead loop


if __name__ == '__main__':
    main()