from songs import Song
from random import randint
import json


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs_list = []
        self.index = 0
        self.already_played = []

    def add_song(self, song):
        if type(song) is not Song:
            raise TypeError("Not valid type!")

        self.songs_list.append(song)

    def remove_song(self, song):
        if type(song) is not Song:
            raise TypeError("Not valid type!")

        self.songs_list.remove(song)

    def add_songs(self, songs):
        if type(songs) is not list:
            raise TypeError("Not valid type!")

        for song in songs:
            if type(song) is not Song:
                raise TypeError("Not valid type!")

        self.songs_list.extend(songs)

    def format_length(self, seconds, minutes, hours):
        if minutes > 0 or hours > 0:
            minutes = "{}:".format(minutes)
        else:
            minutes = ""

        if hours > 0:
            hours = "{}:".format(hours)
        else:
            hours = ""

        return "{}{}{}".format(hours, minutes, seconds)

    def total_length(self):
        all_seconds = 0
        all_minutes = 0
        all_hours = 0

        for song in self.songs_list:
            all_seconds += song._length(seconds=True)
            all_minutes += song._length(minutes=True)
            all_hours += song._length(hours=True)

        all_minutes += all_seconds // 60
        all_seconds %= 60
        all_hours += all_minutes // 60
        all_minutes %= 60

        total_length_formated = self.format_length(all_seconds,
                                                   all_minutes,
                                                   all_hours)

        return total_length_formated

    def artists(self):
        artists_histogram = {}

        for song in self.songs_list:
            if song.artist in artists_histogram:
                artists_histogram[song.artist] += 1
            else:
                artists_histogram[song.artist] = 1

        return artists_histogram

    def choose_random_song(self, already_played):
        random_index = randint(0, len(self.songs_list))
        while random_index in already_played:
            random_index = randint(0, len(self.songs_list))

        return random_index

    def next_song(self):
        if self.repeat and self.index == len(self.songs_list):
            next_song = 0
            self.index = 1
        elif self.shuffle:
            random_index = self.choose_random_song(self.already_played)
            if len(self.already_played) == len(self.songs_list):
                already_played = []
            next_song = random_index
            already_played.append(next_song)
        else:
            next_song = self.index
            self.index += 1

        return self.songs_list[next_song]

    def pprint(self):
        for song in self.songs_list:
            print(song)

    def save(self):
        playlist_name = self.name.replace(' ', '-')

        data = self.create_json_dict()

        with open(playlist_name, 'w') as f:
            json.dump(data, f, indent=4)

    def create_json_dict(self):
        list_songs = []
        for i in range(0, len(self.songs_list)):
            list_songs.append(self.songs_list[i].__dict__)

        json_dict = {}
        json_dict['name'] = self.name
        json_dict['repeat'] = self.repeat
        json_dict['shuffle'] = self.shuffle
        json_dict['songs_list'] = list_songs

        return json_dict

    @classmethod
    def load_from_dict(cls, dict_data):
        list_songs = []
        for song in dict_data['songs_list']:
            list_songs.append(Song(artist=song['artist'],
                                   title=song['title'],
                                   album=song['album'],
                                   length=song['length']))

        new_playlist = cls(dict_data['name'], repeat=dict_data['repeat'],
                           shuffle=dict_data['shuffle'])
        new_playlist.add_songs(list_songs[:])
        return new_playlist

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        return Playlist.load_from_dict(data)


if __name__ == '__main__':
    main()
