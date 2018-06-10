from mutagen.mp3 import MP3
import os
from mutagen.easyid3 import EasyID3
from songs import Song
from playlist import Playlist


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def generate_mp3(song_name):
        song_obj = MP3(song_name, ID3=EasyID3)
        seconds = int(song_obj.info.length)
        hours = seconds / 3600
        seconds %= 3600
        minutes = seconds / 60
        seconds %= 60
        length = "{}:{}:{}".format(hours, minutes, seconds)

        return Song(artist=song_obj['artist'][0], title=song_obj['title'][0],
                    album=song_obj['album'][0], length=length)

    def generate_playlist(self):
        playlist = Playlist("Default")

        file_names = []
        os.chdir(self.path)
        for _, _, files in os.walk(self.path):
            file_names.extend(files)

        for file in file_names:
            if file.endswith('.mp3'):
                new_song = MusicCrawler.generate_mp3(file)
                playlist.songs_list.append(new_song)

        return playlist


if __name__ == '__main__':
    main()
