import os

target_folder = "C:\\Users\\leoca\\Music\\320kbps"

print(target_folder)

if os.path.exists(target_folder):
    print("That location exists")
    if os.path.isfile(target_folder):
        print("That is a file")
    elif os.path.isdir(target_folder):
        print("That is a folder")
    else:
        print("Not a file or folder")
else:
    print("That location doesn't exist")

print("")

try:
    for i, file in enumerate(os.listdir(target_folder)):
        #print(f"File {i} is {file}")
        file_truncated = file[:10]
        for j, file2 in enumerate(os.listdir(target_folder)):
            file_truncated2 = file2[:10]
            #print(f"File {i} is {file}")
            if i != j and file_truncated == file_truncated2:
                print(f"{file} is a duplicate")
            #else:
                #print()
                #print(f"No other file by this name")

except Exception as e:
    print("Something went wrong")
    print(e)












'''
songName = 0
songFinder = 0

def songFinder(name):
    print("looking for matching track...")
    for i in len(folder)

if songName = songFinder(name):'''