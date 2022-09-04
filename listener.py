#!/usr/bin/env python

import socket


class Listener:
    def __int__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOCK_STREAM, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection, address = listener.accept()
        print(f"[+] Got a connection from {str(address)}")

    def run(self):
        while True:
            command = input(">> ")
            self.connection.send(command)
            result = self.connection.recv(1024)
            print(result)
