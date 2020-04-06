from random import randint


def silence(fname='errors.txt'):

    def inner(func):

        def err_logger(*args):
            try:
                func(*args)
            except ValueError as val:
                with open(fname, 'a') as f:
                    f.write(f'Calling {func.__name__} raised a ValueError: \'{val}\'. Provided arguments: {args}.\n')
            else:
                return

        return err_logger

    return inner


@silence()
def foo(x):

    if x > 30:
        raise ValueError('So big!')
    else:
        return 'So small :('


def main():
    for i in range(8):
        foo(randint(10, 40))


if __name__ == '__main__':
    main()
