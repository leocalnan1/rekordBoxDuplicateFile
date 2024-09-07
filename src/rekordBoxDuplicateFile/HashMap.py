import os
import shutil
import mutagen
import rekordBoxDuplicateFile

originalFolder = "C:\\Users\\leoca\\Music\\320kbps\\"

destinationFolder = "C:\\Users\\leoca\\Music\\MovedFiles\\"

#print(originalFolder)

trackFolder = {}
tracks = []

for i, file in enumerate(os.listdir(originalFolder)):
    fileTruncated = file.lower()
    tracks += [f"{file}"]
    trackFolder["320kbpsFolder"] = []
    trackFolder["320kbpsFolder"] += tracks
    print(f"file {i} is {fileTruncated}")

print(trackFolder)


track = {}

duplicateTracks = []