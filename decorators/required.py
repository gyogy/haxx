def required(method):

    def wrapper(*args):
        if method(*args) is super().method(*args):
            raise Exception('Must override!')

    return wrapper


class Animal:
    def __init__(self):
        pass

    def eat(self):
        pass


class Panda(Animal):
    pass


def main():
    p = Panda()


if __name__ == '__main__':
    main()
