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


