# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename=sys.argv[1], numbers=sys.argv[2]):

	with open(filename, "w") as f:
		
		for i in range(int(numbers)):
			f.write(str(randint(1,1000)))
			f.write(" ")
			
def main():
    generate_numbers()

if __name__ == '__main__':
    main()