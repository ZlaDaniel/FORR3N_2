import socket
import sys
import os
HOST = ''                 
PORT = 3820

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))

socket.listen(1)
while (1):
    conn, addr = socket.accept()
    print('New client connected ..')
    reqCommand = conn.recv(1024).decode()
    print('Client> %s' %(reqCommand))
    if (reqCommand == 'quit'):
        break
    if (reqCommand == 'lls'):
        print("Successfully loaded every file!")
        #list1 = []
        for root, dirs, files in os.walk("."):  
            for filename in files:
                conn.sendall(bytes(filename, "utf-8"))
    else:
        string = reqCommand.split(' ', 1)   #in case of 'put' and 'get' method
        reqFile = string[1] 

        if (string[0] == 'put'):
            with open(reqFile, 'wb') as file_to_write:
                while True:
                    data = conn.recv(1024).decode()
                if not data:
                    file_to_write.write(data)
                    file_to_write.close()
                    break
            print('Receive Successful')
        elif (string[0] == 'get'):
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
            print('Send Successful')
