import socket


class Grabber:
    def __int__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.3)
        self.socket.connect((self.socket, self.port))

    def read(self, length=1024):
        return self.socket.recv(length)

    def close(self):
        self.socket.close()


def main():
    grabber = Grabber("placeholder", "port")
    print(grabber.read())
    grabber.close()


if __name__ == '__main__':
    main()
