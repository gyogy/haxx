def chain(iter1, iter2):
    concatenated_iter = list(iter1) + list(iter2)

    return concatenated_iter


def main():
    print(tuple(chain(range(0, 4), range(4, 8))))


if __name__ == '__main__':
    main()
