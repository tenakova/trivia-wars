class Player:
    def __init__(self, socket, ip_address, name):
        self.score = 0
        self.color = None
        self.socket = socket
        self.ip_address = ip_address
        self.name = name
