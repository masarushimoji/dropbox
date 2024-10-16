import sys
import os
import hashlib
import glob
import time

def hashDir (dir):
    if os.path.isdir(dir): 
        print(f"Valid directory passed: {dir}")

        files = glob.glob(os.path.join(dir, '*'))

        hashFunc = hashlib.new('sha256')


        for file in files:
            print(file)   
            
        for file in files:
            if os.path.isfile(file):
                with open(file, 'rb') as f:
                    while chunk := f.read(8192):
                        hashFunc.update(chunk)
                    
        return (hashFunc.hexdigest())

    else:
        return("Invalid directory. Please try again.")



#MAIN PROGRAM

if len(sys.argv) > 1:
    hash = -1
    dir = sys.argv[1]  # Get the directory path passed as an argument
    
    for x in range(5):
        print(hashDir(dir))
        time.sleep(1)
    
    print("test")
    
else:
    print("Please input a directory.")



