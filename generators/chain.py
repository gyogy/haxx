def chain(iter1, iter2):
    concatenated_iter = list(iter1) + list(iter2)

    return concatenated_iter


def chain_marto(iter1, iter2):
    for x in iter1:
        yield x

    for x in iter2:
        yield x


def main():
    print(tuple(chain_marto(range(0, 4), range(4, 8))))


if __name__ == '__main__':
    main()
