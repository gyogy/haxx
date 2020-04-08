def compress(iterable, mask):
    all_true_elements = []

    for i in range(len(mask)):
        if mask[i]:
            all_true_elements.append(iterable[i])

    return all_true_elements


def main():
    iterable = ['Ivo', 'Rado', 'Язе']
    mask = [False, False, True]

    print(list(compress(iterable, mask)))


if __name__ == '__main__':
    main()
