import datetime
import random
import string


def string_maker():
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for i in range(random.randint(1, 15)))


def book_generator(chapters=3, chap_length_in_words=50):
    book_name = input('Enter book name: ')
    chap_count = 1

    with open(book_name + '.txt', 'a') as book:
        for chap in range(chapters):
            book.write(f'#CHAPTER {chap_count}\n')

            chap_len = random.randint(int(0.1 * chap_length_in_words), chap_length_in_words)
            for l in range(chap_len):
                r = random.randint(0, 100)
                if r % 2 == 0 and r % 11 == 0:
                    book.write('\n')
                else:
                    word = string_maker()
                    book.write(word + ' ')

            book.write('\n')
            book.write('\n')
            chap_count += 1


def main():
    start = datetime.datetime.now()
    book_generator(chapters=1000, chap_length_in_words=10000)
    end = datetime.datetime.now()
    with open('log.txt', 'a') as log:
        log.write(f'Old way took {(end - start).total_seconds()} seconds.\n')


if __name__ == '__main__':
    main()
