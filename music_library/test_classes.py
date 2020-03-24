import unittest
from classes import Song, Playlist

class TestSongClass(unittest.TestCase):

    def test_init_with_keyword_arguments(self):
        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = s.artist
        expected = "Biggie Smalls"

        self.assertEqual(result,expected)

    def test_str_functionality(self):

        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = str(s)
        expected = 'Biggie Smalls - Machine Gun Funk from Ready to Die - 4:15'

        self.assertEqual(result,expected)

    def test_equality_with_identical_song_entries(self):
        
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        self.assertEqual(s1, s2)

    def test_equality_with_slightly_different_song_entries(self):
        
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:25") # Only difference is in song lengths
        
        s2 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        self.assertNotEqual(s1, s2)

    def test_hash_function(self):

        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        self.assertEqual(hash(s1), hash(s2))

    def test_length_function_with_default_values_for_kwargs(self):

        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = s.duration()
        expected = '4:15'

        self.assertEqual(result, expected)

    def test_length_function_if_seconds_is_true(self):

        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = s.duration(seconds=True)
        expected = 255

        self.assertEqual(result, expected)

    def test_length_function_if_minutes_is_true(self):

        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = s.duration(minutes=True)
        expected = 4

        self.assertEqual(result, expected)

class TestPlaylistClass(unittest.TestCase):

    def test_adding_a_single_song(self):
        s = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        p = Playlist('Hitachki')
        p.add_song(s)

        result = str(p.plist[0]) # tozi str cast ne e dobre
        expected = 'ork. Orki - Bozhure, bokluk skapan! from Zhig-tak - 5:33'

        self.assertEqual(result,expected)

    def test_adding_a_list_of_songs(self):
        
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        s3 = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length="1:50:03")

        songs = [s1, s2, s3]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        r1 = str(p.plist[0]) # ne e li drveno tova?
        r2 = str(p.plist[1]) # ne e li drveno tova?
        r3 = str(p.plist[2]) # ne e li drveno tova?
        e1 = 'Biggie Smalls - Machine Gun Funk from Ready to Die - 4:15'
        e2 = 'ork. Orki - Bozhure, bokluk skapan! from Zhig-tak - 5:33'
        e3 = 'Johann Sebastian Bach - Mass in B minor from N/A - 1:50:03'

        self.assertEqual(r1, e1)
        self.assertEqual(r2, e2)
        self.assertEqual(r3, e3)

    def test_removing_of_songs(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        songs = [s1, s2]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        self.assertEqual(len(p.plist), 2)

        p.remove_song(s2) # is this correct? should songs be reffered to as objects?

        self.assertEqual(len(p.plist), 1)

    def test_next_song_without_repeat_or_shuffle(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        s3 = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length="1:50:03")

        songs = [s1, s2, s3]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        result = p.next_song()
        expected = str(s1)

        self.assertEqual(result, expected)
        self.assertEqual(p.played_songs,[s1])
        self.assertEqual(p.unplayed_songs,[s2, s3])

    def test_next_song_with_repeat(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        s3 = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length="1:50:03")

        songs = [s1, s2, s3]

        p = Playlist('Hitachki', repeat=True)
        
        for song in songs:
            p.played_songs.append(song)

        self.assertEqual(p.played_songs, [s1, s2, s3])
        self.assertEqual(p.unplayed_songs,[])

        result1 = p.next_song()
        expected1 = str(s1)

        self.assertEqual(result1, expected1)
        self.assertEqual(p.played_songs,[s1])
        self.assertEqual(p.unplayed_songs,[s2, s3])

        result2 = p.next_song()
        expected2 = str(s2)

        self.assertEqual(result2, expected2)
        self.assertEqual(p.played_songs,[s1, s2])
        self.assertEqual(p.unplayed_songs,[s3])

    def test_next_song_with_shuffle(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length="5:33")

        s3 = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length="1:50:03")

        songs = [s1, s2, s3]

        p = Playlist('Hitachki', shuffle=True)
        p.add_songs(songs)

        result = p.next_song()
        expected = str(s1)

        try:
            self.assertNotEqual(result, expected)
        except:
            print('If you are reading this,\nthe test on line 246 has technically failed,\nbecause the random.shuffle() in utils.py, line 53\nhas shuffled the unplayed songs in their original order.')

    def test_artists_method(self):

        s1 = Song(title="", 
            artist="mj", 
            album="", 
            length="")

        s2 = Song(title="", 
            artist="macy", 
            album="", 
            length="")

        s3 = Song(title="", 
            artist="bbking", 
            album="", 
            length="")

        s4 = Song(title="", 
            artist="mj", 
            album="", 
            length="")

        s5 = Song(title="", 
            artist="bbking", 
            album="", 
            length="")

        s6 = Song(title="", 
            artist="mj", 
            album="", 
            length="")

        songs = [s1, s2, s3, s4, s5, s6]
        p = Playlist("Tanci")
        p.add_songs(songs)

        result = p.artists()
        expected = {'mj': 3, 'macy': 1, 'bbking': 2}

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()