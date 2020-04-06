from time import sleep
from datetime import datetime


def performance(filename='log.txt'):

    def inner(func):

        def log(n):
            start = datetime.now()
            func(n)
            end = datetime.now()
            delta = end - start

            with open(filename, 'a') as f:
                f.write(f'{func.__name__} was called and took {round(delta.total_seconds(),3)} seconds to finish.\n')

            return

        return log

    return inner


@performance()
def heavy_funkk(n):
    sleep(n)
    print("All done!")


def main():
    heavy_funkk(3.1)


if __name__ == '__main__':
    main()
