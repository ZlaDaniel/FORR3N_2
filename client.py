import socket
import sys
import os
HOST = '10.220.226.51'    # server name goes in here
PORT = 3820

def ls(commandName):
    for root, dirs, files in os.walk("."):  
        for filename in files:
            print(filename)
def lls(commandName):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send(bytes("lls", "utf8"))
def put(commandName):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send(bytes(commandName, "utf8"))
    string = commandName.split(' ', 1)
    inputFile = string[1]
    with open(inputFile, 'rb') as file_to_send:
        for data in file_to_send:
            socket1.sendall(data)
    print('PUT Successful')
    socket1.close()
    return


def get(commandName):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send(bytes(commandName, "utf8"))
    string = commandName.split(' ', 1)
    inputFile = string[1]
    with open(inputFile, 'wb') as file_to_write:
        while True:
            data = socket1.recv(1024).decode()
            print(data)
            if not data:
                file_to_write.write(data)
                file_to_write.close()
        print('GET Successful')
    socket1.close()
    return

msg = 'Enter your name: '
while(1):
    print('Instruction')
    print('"put [filename]" to send the file the server ')
    print('"get [filename]" to download the file from the server ')
    print('"ls" to list all files in this directory')
    print('"lls" to list all files in the server')
    print('"quit" to exit')
    sys.stdout.write('%s> ' % msg)
    inputCommand = sys.stdin.readline().strip()
    if (inputCommand == 'quit'):
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.connect((HOST, PORT))
        socket1.send(bytes("quit", "utf8"))
        break
    elif (inputCommand == 'ls'):
        ls(inputCommand)
    elif (inputCommand == 'lls'):
        lls(inputCommand)
    else:
        string = inputCommand.split(' ', 1)
        if (string[0] == 'put'):
            put(inputCommand)
        elif (string[0] == 'get'):
            get(inputCommand)
