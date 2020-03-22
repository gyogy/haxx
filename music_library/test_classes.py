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

#     # def test_hash_function(self): # THIS WORKS IN REPL, BUT NOT AS A TEST

#     #     s1 = Song(title="Machine Gun Funk", 
#     #         artist="Biggie Smalls", 
#     #         album="Ready to Die", 
#     #         length="4:15")
        
#     #     s2 = Song(title="Machine Gun Funk", 
#     #         artist="Biggie Smalls", 
#     #         album="Ready to Die", 
#     #         length="4:15")

#     #     self.assertIs(s1, s2)

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

        songs = [s1, s2]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        r1 = str(p.plist[0]) # tozi str cast ne e dobre
        r2 = str(p.plist[1]) # tozi str cast ne e dobre
        e1 = 'Biggie Smalls - Machine Gun Funk from Ready to Die - 4:15'
        e2 = 'ork. Orki - Bozhure, bokluk skapan! from Zhig-tak - 5:33'

        self.assertEqual(r1, e1)
        self.assertEqual(r2, e2)

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

if __name__ == "__main__":
    unittest.main()
