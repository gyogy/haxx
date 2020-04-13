import datetime
import random
import string


def word_maker(case='lower'):
    LETTERS = string.ascii_uppercase
    letters = string.ascii_lowercase
    word_len = random.randint(2, 12)

    if case == 'lower':
        yield ''.join(random.choices(letters, k=word_len))
    else:
        Word = []
        Word.append(random.choice(LETTERS))

        for char in random.choices(letters, k=word_len - 1):
            Word.append(char)

        yield ''.join(Word)


def chapter_maker(chap_len):
    word_count = random.randint(int(0.1 * chap_len), chap_len)
    chapter = ''

    for i in range(word_count):
        if i == 0:
            chapter += next(word_maker('upper')) + ' '
        if i == word_count - 1:
            chapter += next(word_maker()) + '.\n'
        else:
            chapter += next(word_maker()) + ' '

    yield chapter


def book_maker(chap_cnt=1000, chap_len=10000):

    counter = 1
    title = input('Enter book title: ')

    with open(title + '.txt', 'a') as book:

        for i in range(chap_cnt):
            chapter = next(chapter_maker(chap_len))

            book.write(f'#CHAPTER {counter}\n')
            book.write(chapter)
            book.write('\n')

            counter += 1


def main():
    start = datetime.datetime.now()
    book_maker()
    end = datetime.datetime.now()
    with open('log.txt', 'a') as log:
        log.write(f'Gen way took {(end - start).total_seconds()} seconds.\n')


if __name__ == '__main__':
    main()
