#determine title and artist to find other duplicates rather than just file name
import os
#from mutagen.mp3 import MP3
import mutagen


from_folder = "C:\\Users\\Dj Laptop\\Desktop\\from_folder"
to_folder = "C:\\Users\\Dj Laptop\\Desktop\\to_folder"
example_file = "6419138_Muy Tranquilo_(Original Mix).mp3"
example_file_path = from_folder + "\\" + to_folder

print(mutagen.File(example_file_path))
def showDetails():

    fileData = os.path.splitext(filename)



'''
import mutagen

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1

mp3_file_path = "C:\\Users\\leoca\\Music\\320kbps\\6419138_Muy Tranquilo_(Original Mix).mp3"

def get_artist_name(mp3_file_path):
    audio = MP3(mp3_file_path, ID3=ID3)
    try:
        artist = audio.get('TPE1')  # TPE1 is the ID3 frame for the artist
        if artist:
            return artist.text[0]
        else:
            return "No artist information found"
    except Exception as e:
        return f"Error: {str(e)}"

mp3_file = "6419138_Muy Tranquilo_(Original Mix).mp3"
artist_name = get_artist_name(mp3_file)
print(f"Artist: {artist_name}")'''