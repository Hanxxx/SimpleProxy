import socket


def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("localhost", 9999))

    while 1:
        send_data = raw_input("Please type in the message\ntype blank line if you want to end\n")
        if send_data:
            tcp_socket.send(send_data.encode())
        else:
            break
    tcp_socket.close()


if __name__ == "__main__":
    main()
