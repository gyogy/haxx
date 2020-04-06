
def accepts(*args):

    def inner(func):

        def validate(*argv):

            if all(type(argv[i]) is args[i] for i in range(len(argv))):
                return func(*argv)
            else:
                raise TypeError('One or more arguments of invalid type.')

        return validate

    return inner


@accepts(str)
def say_hello(name):
    print(f'Hello, I am {name}!')


@accepts(str, int)
def deposit(name, money):
    print(f'{name} sends ${money}!')


def main():
    deposit('Pesho', 50)
    # deposit(50, 'Pesho')
    say_hello('Gogi')
    # say_hello(5)


if __name__ == '__main__':
    main()
