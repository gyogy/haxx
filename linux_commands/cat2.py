# cat2.py
import sys

files = [x for x in sys.argv[1:]]

def cat2(arguments=files):
    
    for i in files:
    	with open(i, "r") as f:
    		print(f.read())

def main():
    cat2()

if __name__ == '__main__':
    main()