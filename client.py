# coding: utf-8

import socket

hote = "127.0.0.1"
port = 15234

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

socket.send("Bonjour! je m'appelle Hadak".encode("UTF-8"))
socket.send("Envoiez-moi un message".encode("UTF-8"))
socket.send("Que des messages utf...les fichiers binaires pas encore".encode("UTF-8"))

print ("Close")
socket.close()
