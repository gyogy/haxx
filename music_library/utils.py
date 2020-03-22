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

if __name__ == '__main__':
	main()