# cat.py
import sys

filename = sys.argv[1]

def cat(arguments=filename):

	with open(arguments, "r") as f:
		print(f.read())

def main():
    cat()

if __name__ == '__main__':
    main()