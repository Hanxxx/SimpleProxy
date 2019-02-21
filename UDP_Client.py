import socket


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.sendto("UDP test send data\n".encode("UTF-8"), ("localhost", 8888))

    print("data sent")

    udp_socket.close()


if __name__ == '__main__':
    main()