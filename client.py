'''
    Functionalities
        1. Instanciate connection
        2. Send data
        4. Receive data

    future improvements
    1. Better GUI
    2. timeout on both client and server
    3. close connection by client
'''
import socket
import sys
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


class Connection:
    def __init__(self) -> None:
        pass

    def start(self):
        pass

    def stop(self):
        pass


class Ping:
    """
        Check if the server is alive
    """
    def __init__(self):
        pass

    def __ping(self):
        return b'Hi'


class Data:
    """
        User can use data object to define the data to be sent
    """
    def __init__(self) -> None:
        self.__filename = ""
        self.__content = []

    def set(self, filename, content):
        self.__filename = filename
        self.__content = content

    def get(self):
        return (self.__filename, self.__content)


class Client(Connection, Ping):
    def __init__(self) -> None:
        Connection().__init__()
        Ping().__init__()
        
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.connect((HOST, PORT))

        #Connection.start()


    def ping_server(self):
        self.socket_obj.sendall(b'Hi')
        
    def transfer(self, data):
        if isinstance(data, Data):
            filename, content = data.get()
            self.socket_obj.send(filename)
            time.sleep(2)
            self.socket_obj.send(content)

        elif data == b"Hi":
            self.socket_obj.send(data)
        else:
            raise TypeError


    def receive(self,buffer_size=1024):
        return self.socket_obj.recv(buffer_size)        

#################################################
#                 Main APP
#################################################

# get Command line args (if exists)
if len(sys.argv) > 1:
    Host = sys.argv[1]
    PORT = int(sys.argv[2])


client = Client()
data = Data()

print(client.receive())
while True:

    filepath = input("Image name: ")

    with open(filepath,'rb+') as file:
        content = file.read()
        data.set(filepath.encode(), content)
        file.close()

    client.transfer(data)

    response = client.receive()
    print(response)

    ping = input("Ping? (y/n) ")
    if ping == "y":
        client.ping_server()
        ping_response = client.receive()
        print(str(ping_response))

    