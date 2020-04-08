def compress(iterable, mask):
    all_true_elements = []

    for i in range(len(mask)):
        if mask[i]:
            all_true_elements.append(iterable[i])

    return all_true_elements


def compress2(iterable, mask):
    for i in range(len(mask)):
        if mask[i]:
            yield iterable[i]


def main():
    iterable = ['Ivo', 'Rado', 'Язе']
    mask = [True, False, True]

    print(list(compress2(iterable, mask)))


if __name__ == '__main__':
    main()
