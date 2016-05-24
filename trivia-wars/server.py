import socket
from player import Player


class Server:
    def __init__(self, player_limit):
        self.player_limit = player_limit
        self.players = []
        self.player_count = 0
        self.server_socket = self.initialize_socket()

    @staticmethod
    def initialize_socket():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999
        server_socket.bind((host, port))
        return server_socket

    def initialize_game(self):
        print("Waiting for players....")
        self.server_socket.listen()
        while self.player_count != self.player_limit:
            client_socket, client_address = self.server_socket.accept()
            name = client_socket.recv(1024).decode("utf-8")
            self.players.append(Player(client_socket, client_address, name))
            client_socket.send("You joined successfully!".encode("utf-8"))
            print("Accepted connection from {}".format(client_address))
            self.player_count += 1
