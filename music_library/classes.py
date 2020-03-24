import json

from utils import songs_duration, total_p_time, next_up_in

class Song():   
    
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __eq__(self, other):
        return (self.title, self.artist, self.album, self.length) == (other.title, other.artist, other.album, other.length)

    def __hash__(self):
      return hash((self.title, self.artist, self.album, self.length))

    def duration(self, seconds=False, minutes=False, hours=False):
        return songs_duration(self.length, seconds, minutes, hours)

class Playlist():

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.plist = []
        self.unplayed_songs = []
        self.played_songs = []

    def __getitem__(self, index):
        return self.plist[index]

    def add_song(self, song):
        self.plist.append(song)
        self.unplayed_songs.append(song)

    def add_songs(self, songs):
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

        histogram = {i:artists.count(i) for i in artists}

        return histogram

    def save(self):
        with open(f'/home/gyogy/hackbg/music_library/playlists/{self.name}.json', 'w') as f:
            json.dump(self, f)

    def load(self):
        pass

def main():
    pass
    
if __name__ == '__main__':
    main()