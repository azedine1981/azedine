# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 15234))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))

        response = client.recv(255)
        if response != "":
                print(response)

print ("Close")
client.close()
stock.close()
