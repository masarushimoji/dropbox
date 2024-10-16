import sys
import os
import hashlib
import glob

if len(sys.argv) > 1:
    dir = sys.argv[1]  # Get the directory path passed as an argument
    if os.path.isdir(dir): 
        print(f"Valid directory passed: {dir}")

        files = glob.glob(os.path.join(dir, '*'))

        for file in files:
            print(file)        

    else:
        print("Invalid directory. Please try again.")
else:
    print("Please input a directory.")
