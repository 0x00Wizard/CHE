#!/usr/bin/env python

import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOCK_STREAM, socket.SO_REUSEADDR, 1)
listener.bind(("localhost", 4444))
listener.listen(0)
print("[+] Waiting for incoming connection")
listener.accept()
print("[+] Got a connection")