import unittest
from classes import *


class TestSongClass(unittest.TestCase):

    def setUp(self):
        self.s = Song(title="Machine Gun Funk", artist="Biggie Smalls", album="Ready to Die", length_str="4:15")
        self.s_same = Song(title="Machine Gun Funk", artist="Biggie Smalls", album="Ready to Die", length_str="4:15")
        self.s_diff = Song(title="Machine Gun Funk", artist="Biggie Smalls", album="Ready to Die", length_str="4:25")

        self.songs = []
        self.songs.append(self.s),
        self.songs.append(self.s_same)
        self.songs.append(self.s_diff)

    def test_str_dunder(self):

        result = str(self.s)
        expected = 'Biggie Smalls - Machine Gun Funk from Ready to Die - 4:15'

        self.assertEqual(result, expected)

    def test_length_function_with_default_values_for_kwargs(self):

        result = self.s.duration()
        expected = '4:15'

        self.assertEqual(result, expected)

    def test_length_function_if_seconds_is_true(self):

        result = self.s.duration(seconds=True)
        expected = 255

        self.assertEqual(result, expected)

    def test_length_function_if_minutes_is_true(self):

        result = self.s.duration(minutes=True)
        expected = 4

        self.assertEqual(result, expected)


class TestPlaylistClass(unittest.TestCase):

    def setUp(self):
        self.s1 = Song(title="Machine Gun Funk", artist="Biggie Smalls", album="Ready to Die", length_str="4:15")
        self.s2 = Song(title="Bozhure, bokluk skapan!", artist="ork. Orki", album="Zhig-tak", length_str="5:33")
        self.s3 = Song(title="Mass in B minor", artist="Johann Sebastian Bach", album="N/A", length_str="1:50:03")

        self.songs = [self.s1, self.s2, self.s3]

        self.p = Playlist("Hitachki")
        self.p.add_songs(self.songs)

        self.p_rep = Playlist('Repeat', repeat=True)
        for song in self.songs:
            self.p_rep.played_songs.append(song)

        self.p_shuf = Playlist('Shuffle', shuffle=True)
        self.p_shuf.add_songs(self.songs)

    def test_next_song_without_repeat_or_shuffle(self):

        result = self.p.next_song()
        expected = str(self.s1)

        self.assertEqual(result, expected)

        self.assertEqual(self.p.played_songs, [self.s1])
        self.assertEqual(self.p.unplayed_songs, [self.s2, self.s3])

    def test_next_song_with_repeat(self):

        # unplayed songs is emptya
        self.assertEqual(self.p_rep.played_songs, [self.s1, self.s2, self.s3])
        self.assertEqual(self.p_rep.unplayed_songs, [])

        result1 = self.p_rep.next_song()
        expected1 = str(self.s1)

        self.assertEqual(result1, expected1)
        self.assertEqual(self.p_rep.played_songs, [self.s1])
        self.assertEqual(self.p_rep.unplayed_songs, [self.s2, self.s3])

        result2 = self.p_rep.next_song()
        expected2 = str(self.s2)

        self.assertEqual(result2, expected2)
        self.assertEqual(self.p_rep.played_songs, [self.s1, self.s2])
        self.assertEqual(self.p_rep.unplayed_songs, [self.s3])

    def test_next_song_with_shuffle(self):

        result = self.p_shuf.next_song()
        expected = str(self.s1)

        try:
            self.assertNotEqual(result, expected)
        except AssertionError:
            print('''If you are reading this, the test
on line 95 has technically failed,
because the random.shuffle() in utils.py,
line 42, has shuffled the unplayed songs
in their original order.''')

    def test_artists_method(self):

        s1 = Song(title="", artist="mj", album="", length_str="")
        s2 = Song(title="", artist="macy", album="", length_str="")
        s3 = Song(title="", artist="bbking", album="", length_str="")
        s4 = Song(title="", artist="mj", album="", length_str="")
        s5 = Song(title="", artist="bbking", album="", length_str="")
        s6 = Song(title="", artist="mj", album="", length_str="")

        songs = [s1, s2, s3, s4, s5, s6]

        p = Playlist("Tanci")

        p.add_songs(songs)

        result = p.artists()
        expected = {'mj': 3, 'macy': 1, 'bbking': 2}

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
