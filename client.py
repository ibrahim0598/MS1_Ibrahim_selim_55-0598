import socket
import select
import sys


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 442
client_socket.connect(('127.0.0.1', port))

while(True):
    message = input("enter your message:")
    client_socket.sendall(message.encode('utf-8'))

    if (message == 'CLOSE SOCKET'):
        client_socket.close()
        break

    response = client_socket.recv(1024).decode('utf-8')

    print('server:', response)




