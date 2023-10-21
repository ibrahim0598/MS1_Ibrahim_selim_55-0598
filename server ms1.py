import socket
import threading
import select
import sys


def threaded(client_socket,client_address):
    
    print('connected with', client_address)
    while(True):
        message = client_socket.recv(1024).decode('utf-8')
        if(not message):
            break
        if( message == 'CLOSE SOCKET' ):
           client_socket.close()
           print('connection closed')
           break
        response = message.upper()
        client_socket.sendall(response.encode('utf-8'))

def main():
    print("server is starting")
    server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 442
    server_socket.bind(('127.0.0.1',port))
    server_socket.listen(442)
    print("wait please , server is setting up")
    while(True):
       client_socket, client_address = server_socket.accept()
       threading.Lock().acquire()
       client_thread= threading.Thread(target=threaded,args=(client_socket,client_address))
       client_thread.start()
main() 
     
       



   