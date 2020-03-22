import unittest
import datetime
from classes import Song, Playlist
from utils import length_as_time_object, songs_duration

class TestLengthAsTimeObjectFunction(unittest.TestCase):
    
    def test_length_as_time_object_for_length_less_than_24_hours(self):
        length = '5:13:06'

        result = length_as_time_object(length)
        expected = datetime.time(5,13,6)

        self.assertEqual(result, expected)

    # def test_length_as_time_object_for_length_greater_than_24_hours(self):
    #     length = '25:13:06'

    #     result = length_as_time_object(length)
    #     expected = datetime.time(25,13,6)

    #     self.assertEqual(result, expected)

class TestSongsDurationFunction(unittest.TestCase):

    def test_with_song_shorter_than_an_hour(self):
        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = songs_duration(s.length)
        expected = '4:15'

        self.assertEqual(result, expected)

    def test_with_song_longer_than_an_hour(self):
        s = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length="1:50:03")

        result = songs_duration(s.length)
        expected = '1:50:03'

        self.assertEqual(result, expected)

    def test_songs_duration_if_seconds_is_true(self):
        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length="4:15")

        result = songs_duration(s.length, seconds=True)
        expected = 255

        self.assertEqual(result, expected)

class TestTotalPTimeFunction(unittest.TestCase):

    def test_total_p_time(self):
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

        result = p.total_length()
        expected = '0:9:48'

        self.assertEqual(result,expected)

    def test_total_plist_length_for_plist_longer_than_24_hours(self):
        s1 = Song(title="proba", 
            artist="test", 
            album="se_taq", 
            length="12:45:15")
        
        s2 = Song(title="Bozhure", 
            artist="opa", 
            album="hey", 
            length="15:33:02")

        songs = [s1, s2]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        result = p.total_length()
        expected = '28:18:17'

        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()
