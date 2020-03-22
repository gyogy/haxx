from utils import songs_duration, total_p_time

# hash vs eq

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

    def __hash__(self): # neshto ne e v red
      return hash((self.title, self.artist, self.album, self.length))

    def duration(self, seconds=False, minutes=False, hours=False):
        return songs_duration(self.length, seconds, minutes, hours)

class Playlist():

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.plist = []

    def __getitem__(self, index):
        return self.plist[index]

    def add_song(self, song):
        self.plist.append(song)

    def add_songs(self, songs):
        for i in songs:
            self.plist.append(i)

    def remove_song(self, song):
        self.plist.remove(song)

    def next_song(self):
        pass

    def total_length(self):
        return total_p_time(self.plist)

    def artists(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()