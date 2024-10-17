import sys
import os
import hashlib
import glob
import time
import socket

prevListLength = -1


#HASHING FUNCTION

def hashDir (dir):
        files = glob.glob(os.path.join(dir, '*'))

        hashFunc = hashlib.new('sha256')


       # for file in files:
        #    print(file)   
            
        for file in files:
            if os.path.isfile(file):
                with open(file, 'rb') as f:
                    while chunk := f.read(8192):
                        hashFunc.update(chunk)
                    
        return (hashFunc.hexdigest())



#MAIN PROGRAM

if len(sys.argv) > 1:
    hash = -1
    dir = sys.argv[1]  # Get the directory path passed as an argument
    fileChanged = False
    if os.path.isdir(dir): 
        print(f"Valid directory passed: {dir}")
        while not(fileChanged):
            currentHash = hashDir(dir)
            if (hash == -1):
                hash = currentHash
                prevList = len(glob.glob(os.path.join(dir, '*')))
            elif (hash != currentHash):
                hash == currentHash
                print("Hash Changed")
                fileChanged = True
                if (len(glob.glob(os.path.join(dir, '*'))) > prevListLength):
                    print("file added")
                elif (len(glob.glob(os.path.join(dir, '*'))) < prevListLength):
                    print("file removed")
                else:
                    print("file changed")
            else:
                print("Files unchanged.")
            prevListLength = len(glob.glob(os.path.join(dir, '*')))
            time.sleep(1)


        
        host = socket.gethostname()
        port = 5000

        clientSocket = socket.socket()
        clientSocket.connect((host, port))

        clientSocket.send(("hello world!").encode())










    

    else:
        print("Invalid directory. Please try again.")
    
else:
    print("Please input a directory.")



