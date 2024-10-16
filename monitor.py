import sys
import os
import hashlib
import glob

if len(sys.argv) > 1:
    hash = -1
    dir = sys.argv[1]  # Get the directory path passed as an argument
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
                    
        print (hashFunc.hexdigest())

    else:
        print("Invalid directory. Please try again.")
else:
    print("Please input a directory.")
