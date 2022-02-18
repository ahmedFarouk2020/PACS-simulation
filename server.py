""" 
    Functionalities:
        1. Use DB to store data come from sender
        2. Handle user [Multi-threading]
"""

from ctypes import sizeof
from xmlrpc.client import Binary
from DB import *
import socket

import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


if(len(sys.argv)) > 1:
    HOST = sys.argv[1]
    PORT = sys.argv[2]


class Server():
    def __init__(self) -> None:
        
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((HOST, PORT))
        self.__server.listen()
        self.__connection, self.__address = self.__server.accept()

        print(f"Connected to {self.__address[0]} on port {self.__address[1]}")

        self.__db = DB()


    def send(self,data: bytes):
        self.__connection.sendall(data)

    def receive(self, buffer_size=1024) -> bytes:
        return self.__connection.recv(buffer_size)

    def store_in_DB(self, filename, buffer_size=1024) -> None:
        ''' Store data locally then pass data to database '''

        temporary_file = open("temp.txt", mode='ab')
        
        while True:
            
            data = self.__connection.recv(buffer_size)
            
            # calculate size of data received
            # if 1024   --> client is not finished
            # if < 1024 --> client finish sending
            # if = 1024 but client finish sending --> not implemented yet (timeout)
            if len(str(data)[2:-1]) == (buffer_size/8):
                temporary_file.write(data)
            else:
                temporary_file.close()
                break

        temporary_file = open("temp.txt", mode='rb')
        content = temporary_file.read() # read all data in the file
        temporary_file.close()

        os.remove("temp.txt") # remove temporary file

        # remove {b,','} in filename -> b'filename.txt' 
        filename = str(filename)[2:-1]
        
        self.__db.store(filename, content)


server = Server()
server.send(b'Connection accepted!')

while True:
    client_request = server.receive()
    if client_request == b'Hi':
        server.send(b'Hi')

    else: # filename
        print("above store in DB")
        server.store_in_DB(client_request)
        server.send(b"image is saved!")



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)

#         conn.sendall(b"Connection accepted")
#         print(b"Connection accepted")
        
#         while True:
#             data = conn.recv(1024)
            
#             if data == b"Hi":
#                 conn.send(data)
#             elif data:
#                 print(data)
                
#                 with open(str(data)+".png",mode="ab") as file:
#                     while True:
#                         data = conn.recv(1024)
#                         if data:
#                             file.write(data)
                            
#                         break
#                     file.close()
#                     print("Image is saved")
#                     conn.sendall(b'Image is saved')