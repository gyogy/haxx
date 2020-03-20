# sum_numbers.py
import sys

def sum_numbers(filename=sys.argv[1]):

	result = 0

	with open(filename, "r") as f:
		for i in f.read().strip().split(" "):
			result += int(i)

	print(result)

def main():
    sum_numbers()

if __name__ == '__main__':
    main()