import json
from utils import *
from mixins import JsonParser


class Song(JsonParser):

    def __init__(self, title, artist, album, length_str):
        self.title = title
        self.artist = artist
        self.album = album
        self.length_str = length_str

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length_str}'

    def __eq__(self, other):

        song_value = (self.title, self.album, self.length_str)

        other_song_value = (other.title, other.album, other.length_str)

        return song_value == other_song_value

    def __hash__(self):

        return hash((self.title, self.artist, self.album, self.length_str))

    def duration(self, seconds=False, minutes=False, hours=False):

        time = length_str_to_time_object(self.length_str)

        if seconds:
            return time.hour * 60 * 60 + time.minute * 60 + time.second

        elif minutes:
            return time.hour * 60 + time.minute

        elif hours:
            return time.hour
        else:
            return self.length_str


class Playlist(JsonParser):

    def __init__(self, name, repeat=False, shuffle=False, plist=None, unplayed_songs=None, played_songs=None):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.plist = plist
        self.unplayed_songs = unplayed_songs
        self.played_songs = played_songs

    def __getitem__(self, index):
        return self.plist[index]

    def add_song(self, song):
        if self.plist is None:
            self.plist = []
            self.unplayed_songs = []
            self.played_songs = []

        self.plist.append(song)
        self.unplayed_songs.append(song)

    def add_songs(self, songs):
        if self.plist is None:
            self.plist = []
            self.unplayed_songs = []
            self.played_songs = []

        for song in songs:
            self.plist.append(song)
            self.unplayed_songs.append(song)

    def remove_song(self, song):
        self.plist.remove(song)

        if song in self.unplayed_songs:
            self.unplayed_songs.remove(song)

        if song in self.played_songs:
            self.played_songs.remove(song)

    def next_song(self):
        result = next_up_in(self)

        self.unplayed_songs = result[0]
        self.played_songs = result[1]
        next_song = result[2]

        return str(next_song)

    def total_length(self):
        return total_p_time(self.plist)

    def artists(self):
        artists = []

        for song in self.plist:
            artists.append(song.artist)

        histogram = {i: artists.count(i) for i in artists}

        return histogram

    def save(self):
        with open(f'/home/gyogy/code/dev/hackbg/music_library/playlists/{self.name}.json', 'w') as fp:
            fp.write(self.to_json())

    def load(self):

        from_json()


def main():
    s1 = Song(title="Machine Gun Funk", artist="Biggie Smalls", album="Ready to Die", length_str="4:15")
    s2 = Song(title="Bozhure, bokluk skapan!", artist="ork. Orki", album="Zhig-tak", length_str="5:33")
    s3 = Song(title="Mass in B minor", artist="Johann Sebastian Bach", album="N/A", length_str="1:50:03")
    songs = [s1, s2, s3]
    p = Playlist("Hitachki")
    p.add_songs(songs)
    p.save()


if __name__ == '__main__':
    main()
