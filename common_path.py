import sys
import os

def common_path(paths=sys.argv[1:]):

	# gives you the absolute paths
	for i in paths:
		print(i)
		print(os.path.abspath(i))

		print()

	# gives you top common folder
	for i in paths:
		print(paths)
		print(os.path.commonprefix(paths))

		print()		




def main():
	common_path()

if __name__ == '__main__':
	main()