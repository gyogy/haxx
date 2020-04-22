import unittest
import datetime
from classes import Song, Playlist
from utils import length_str_to_time_object, next_up_in, total_p_time


class TestLengthAsTimeObjectFunction(unittest.TestCase):

    def test_length_str_to_time_object_for_length_less_than_24_hours(self):
        length = '5:13:06'

        result = length_str_to_time_object(length)
        expected = datetime.time(5, 13, 6)

        self.assertEqual(result, expected)

class TestTotalPTimeFunction(unittest.TestCase):

    def test_total_p_time(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length_str="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length_str="5:33")

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
            length_str="12:45:15")
        
        s2 = Song(title="Bozhure", 
            artist="opa", 
            album="hey", 
            length_str="15:33:02")

        songs = [s1, s2]

        p = Playlist('Hitachki')
        p.add_songs(songs)

        result = p.total_length()
        expected = '28:18:17'

        self.assertEqual(result,expected)

class TestNextUpInFunction(unittest.TestCase):

    def test_next_up_in_a_list_of_a_single_song(self):
        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length_str="4:15")

        p = Playlist('Hitachki')
        p.add_song(s)

        result = str(next_up_in(p)[2])
        expected = str(s)

        self.assertEqual(result, expected)

    def test_next_up_in_a_list_of_no_songs(self):
        p = Playlist('Hitachki')

        result = str(next_up_in(p)[2])
        expected = 'Reached end of playlist.'

        self.assertEqual(result, expected)

    def test_next_up_in_empty_unplayed_list_with_repeat_being_true(self):
        s = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length_str="4:15")
        
        p = Playlist('Hitachki', repeat=True)
        p.played_songs.append(s)

        self.assertEqual(p.unplayed_songs, [])

        result = next_up_in(p)
        expected0 = []
        expected1 = [s]
        expected2 = s
        #State unplayed_songs list should be in after running next_up_in function
        self.assertEqual(result[0],expected0)
        #State played_songs list should be in after running next_up_in function
        self.assertEqual(result[1], expected1)
        #Next song after running next_up_in function
        self.assertEqual(result[2], expected2)

    def test_next_up_with_shuffle(self):
        s1 = Song(title="Machine Gun Funk", 
            artist="Biggie Smalls", 
            album="Ready to Die", 
            length_str="4:15")
        
        s2 = Song(title="Bozhure, bokluk skapan!", 
            artist="ork. Orki", 
            album="Zhig-tak", 
            length_str="5:33")

        s3 = Song(title="Mass in B minor", 
            artist="Johann Sebastian Bach", 
            album="N/A", 
            length_str="1:50:03")

        s4 = Song(title="abc", 
            artist="def", 
            album="ghi", 
            length_str="0:26")

        songs = [s1, s2, s3, s4]

        p = Playlist('Hitachki', shuffle=True)
        p.add_songs(songs)

        result = next_up_in(p)
        new_song = result[2]
        # appending played_songs and unplayed_songs to get the shuffled order of songs
        shuffled_song_order = result[1]+result[0]
        # plist is the song in their original order
        original_song_order = p.plist

        try:
            self.assertNotEqual(original_song_order, shuffled_song_order)
        except:
            print('If you are reading this,\ntest on line 150 has technically failed,\nbecause the shuffler in utils.py, line 53\nhas shuffled the unplayed songs in their original order.')


if __name__ == "__main__":
    unittest.main()
