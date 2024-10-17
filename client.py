import sys
import os
import hashlib
import glob
import time
import socket

prevListLength = -1
prevList= []
prevListHashes = []


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
            elif (hash != currentHash):
                hash = currentHash
                print("Hash Changed")
                fileChanged = True
                currentList = len(glob.glob(os.path.join(dir, '*'))) 
                if (currentList > prevListLength):
                    print("file added")
                    actionNeeded = "add"
                elif (currentList < prevListLength):
                    print("file removed")
                    actionNeeded = "remove"
                else:
                    print("file changed")
                    actionNeeded = "replace"
            else:
                print("Files unchanged.")
            
            prevList = glob.glob(os.path.join(dir, '*'))
            prevListLength = len(glob.glob(os.path.join(dir, '*')))

            hashFunc = hashlib.new('sha256')
            prevListHashes = []
            for file in prevList:
                if os.path.isfile(file):
                    with open(file, 'rb') as f:
                        while chunk := f.read(8192):
                            hashFunc.update(chunk)
                        prevListHashes.append(hashFunc.hexdigest())


            time.sleep(1)


        print("action needed: " + actionNeeded)
        currentHash = []
        currentList = glob.glob(os.path.join(dir, '*')) 

        if (actionNeeded == "replace"):
            hashFunc = hashlib.new('sha256')
            for file in currentList:
                if os.path.isfile(file):
                    with open(file, 'rb') as f:
                        while chunk := f.read(8192):
                            hashFunc.update(chunk)
                        currentHash.append(hashFunc.hexdigest())
                
            
        print("prev file hashes:" + str(prevListHashes))
        print("current file hashes: " + str(currentHash))



        host = socket.gethostname()
        port = 5000

        clientSocket = socket.socket()
        clientSocket.connect((host, port))

        clientSocket.send(("hello world!").encode())










    

    else:
        print("Invalid directory. Please try again.")
    
else:
    print("Please input a directory.")



