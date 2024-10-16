import os
import sys

if len(sys.argv) <= 1:
     print("Please input a directory.")
else:
    dir = sys.argv[1] 
    if not(os.path.isdir(dir)): 
        print("Please input a vaslid directory.")
    else:
        print("hurrah")
