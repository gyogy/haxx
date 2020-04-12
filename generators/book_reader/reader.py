from glob import glob
from os import system
import sys
import termios
import tty


def chapter_generator(book_files):

    for file in book_files:

        with open(file, 'r') as f:

            chapters = f.read().split('#')
            for chapter in chapters:

                if chapter.strip() == '':
                    pass
                else:
                    yield chapter.strip()


def main():

    book_path = input('Enter path to the book files: ')
    book_files = sorted(glob(book_path + '/*.txt'))
    generator = chapter_generator(book_files)

    og_stdin_settings = termios.tcgetattr(sys.stdin.fileno())
    # Saves the terminal's attributes at program runtime
    tty.setcbreak(sys.stdin)
    # Sets terminal input to CBREAK mode, so that user doesn't have to press ENTER after pressing SPACE
    system('clear')

    for chapter in generator:
        print('Press SPACE for next chapter.')
        print('All other keys close the book.')

        x = sys.stdin.readline(1)  # The 1 here is the number of bytes to be read. 1B == 1 character.
        if x == chr(32):  # Unicode 32 == SPACE
            system('clear')
            print(chapter)
            print()

        else:
            print('=== BOOK CLOSED ===')
            break

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, og_stdin_settings)
    # Restores terminal's attributes to their default


if __name__ == '__main__':
    main()
