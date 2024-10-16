import os
import sys
import socket

if len(sys.argv) <= 1:
     print("Please input a directory.")
else:
    dir = sys.argv[1] 
    if not(os.path.isdir(dir)): 
        print("Please input a valid directory.")
    else:
        print("Inputted directory is valid!")



        host = socket.gethostname()
        port = 5000

        serverSocket = socket.socket()
        serverSocket.bind((host, port))

        serverSocket.listen(2)
        conn, address = serverSocket.accept()
        print("Connection from: " + str(address))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
        print(str(data))

