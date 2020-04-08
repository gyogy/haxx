def cycle(iterable):

    while True:

        for i in iterable:
            print(i)


def cycle2(iterable):

    while True:

        for i in iterable:
            yield i


def main():
    endless = cycle2(range(0, 10))
    for item in endless:
        print(item)


if __name__ == '__main__':
    main()
