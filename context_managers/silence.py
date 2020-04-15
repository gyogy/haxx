from contextlib import contextmanager


@contextmanager
def silence_exception(exc_type, exc=None):
    try:
        yield
    except exc_type as e:
        if exc is not None and str(e) != exc:
            raise e


class SilenceException():

    def __init__(self, exc_type, exc=None):
        self.exc_type = exc_type
        self.exc = exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        expected_exc_type = self.exc_type == exc_type
        expected_exc = self.exc is None or self.exc == str(exc)

        return expected_exc_type and expected_exc


def main():
    pass


if __name__ == '__main__':
    main()
