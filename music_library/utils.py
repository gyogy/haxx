from random import shuffle
from datetime import datetime

def length_as_time_object(length):

	if len(length.split(':')) == 2:
		song_time = datetime.strptime(length, '%M:%S').time()
	else:
		song_time = datetime.strptime(length, '%H:%M:%S').time()

	return song_time

def songs_duration(length, seconds=False, minutes=False, hours=False):

	song_time = length_as_time_object(length)
	
	if seconds:
		return song_time.hour*60*60 + song_time.minute*60 + song_time.second
	
	elif minutes:
		return song_time.hour*60 + song_time.minute
	
	elif hours:
		return song_time.hour
	else:
		return length

def total_p_time(songs):
    hours = 0
    minutes = 0
    seconds = 0

    for song in songs:
       song_time = length_as_time_object(song.length)
       
       hours += song_time.hour
       minutes += song_time.minute
       seconds += song_time.second

    if seconds > 60:
    	minutes += seconds // 60
    	seconds = seconds % 60

    if minutes > 60:
    	hours += minutes // 60
    	minutes = minutes % 60

    return f'{hours}:{minutes}:{seconds}'

def next_up_in(playlist):
	
	if playlist.shuffle:
		shuffle(playlist.unplayed_songs)
		
	try:
		playlist.played_songs.append(playlist.unplayed_songs[0])
		playlist.unplayed_songs.remove(playlist.unplayed_songs[0])

		return playlist.unplayed_songs, playlist.played_songs, playlist.played_songs[-1]

	except IndexError:
		if playlist.repeat:
			for song in playlist.played_songs:
				playlist.unplayed_songs.append(song)

			playlist.played_songs = []

			return next_up_in(playlist)

		else:	
			# An IndexError here means that playlist.unplayed_songs list is empty.
			return playlist.unplayed_songs, playlist.played_songs,'Reached end of playlist.'

def shuffler(playlist):
	shuffled_songs = set(playlist.unplayed_songs)
	return list(shuffled_songs)



if __name__ == '__main__':
	main()