import os
import shutil

source = "C:\\Users\\leoca\\OneDrive\\Desktop\\OriginFolder\\"
destination = "C:\\Users\\leoca\\OneDrive\\Desktop\\MovedFolder\\"

files = os.listdir(source)


try:
    for f in files:
        shutil.move(source + f, destination + f)
    print("Files Transferred")
except FileNotFoundError:
    print(source+" was not found")