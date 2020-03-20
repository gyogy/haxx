import sys
import os

def reduce_file_path(path=sys.argv[1]):
    print(os.path.abspath(path))

def main():
	reduce_file_path()

if __name__ == '__main__':
	main()