#wc.py
import sys

def wc(command=sys.argv[1], filename=sys.argv[2]):
	
	count = 0

	with open(filename, "r") as f:
		
		if command == 'chars':
			for i in f.read():
				count += 1
		elif command == 'words':
			for i in f.read().split():
				count += 1
		elif command == 'lines':
			for i in f.readlines():
				count += 1
				
	return count

def main():
	print(wc())

if __name__ == '__main__':
	main()