#duhs.py
import sys
import os

def duhs(path=sys.argv[1]):

	total = 0

	for i in os.scandir(path):

		# if i.name.startswith('t'):
		# 	total += i.stat().st_size
			
		# 	with open('all_the_ts.txt', 'a') as f:
		# 		f.write(str(i))

		if i.is_file():
			total += i.stat().st_size

		elif i.is_dir():
			total += 2 * 4096 
			total += duhs(i.path)		
	
	total_in_gb = total/1073741824

	return total

def main():

	# with open('/home/gyogy/hackbg/all_the_ts.txt', "r") as f:
	# 	for i in f.read().split('<DirEntry '):
	# 		print(i.strip('>'))

	print("Size is", round(duhs() / 1073741824, 2), "G")

if __name__ == '__main__':
	main()