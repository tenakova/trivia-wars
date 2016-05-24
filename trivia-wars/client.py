import socket


class Client:
    def __init__(self, server_ip_address, server_port):
        self.server_ip_address = server_ip_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_ip_address, self.server_port))
        print("Name: ", end="")
        name = input()
        self.client_socket.send(name.encode("utf-8"))
        message = self.client_socket.recv(1024).decode("utf-8")
        print(message)
