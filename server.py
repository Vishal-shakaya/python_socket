# import threading
import socket 
from _thread import *

# Define required parameters :
PORT = 5050
# dynamicly get your ip : 
HOST = socket.gethostbyname(socket.gethostname()) #192.168.0.110
FORMAT = 'utf-8'
HEADER = 1024 # Buffer size
ADDR = (HOST , PORT)
# print_lock = threading.Lock()

# Define socket type TCP , using Addressing protocol: 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Receive data from client : 
# socket not send plain text thats why using utf-8 encode string :
# Header : use to get msg with same buffer size as client msg buffer use : 
# if succefully get data then send confirmation to the client : 
def ClientHandler(connection):
    connected = True 
    while connected:
        data = connection.recv(HEADER)
        if not data:
            # print_lock.release()
            print('bye')
            break;  
        print(str(data.decode(FORMAT)))
        connection.send('message_send'.encode(FORMAT))
     
    connection.close()
        

# 1. Listen incomming connection: 
# 2. Accept all connection :
# 3. Create Client Thread :
# 4. Close the connection :   
def Start():
    server.listen()
    listining = True
    while listining:
        conn, addr = server.accept()
        print(f'[CONNECTED]-> {addr}')
        # print_lock.acquire()
        start_new_thread(ClientHandler, (conn,))
    server.close()
    
print('****[ SERVER STARTING ]****')
Start()