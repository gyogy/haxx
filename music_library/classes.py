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
    s1 = Song(title="Smooth Criminal", 
        artist="MJ", 
        album="Thriller", 
        length="3:21")

    s2 = Song(title="I've Commited Murder", 
        artist="Macy Gray", 
        album="On How Life is", 
        length="4:36")

    s3 = Song(title="Champagne and Reefer", 
        artist="BB King", 
        album="Greatest Hits", 
        length="5:02")

    s4 = Song(title="Billie Jean", 
        artist="MJ", 
        album="Off The Wall", 
        length="2:37")

    s5 = Song(title="Dust My Broom", 
        artist="BB King", 
        album="Greatest Hits", 
        length="2:47")

    s6 = Song(title="Thriller", 
        artist="MJ", 
        album="Thriller", 
        length="7:08")

    songs = [s1, s2, s3, s4, s5, s6]
    p = Playlist("Karachernev")
    p.add_songs(songs)

if __name__ == '__main__':
    main()