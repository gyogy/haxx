from contextlib import contextmanager
from decimal import *


@contextmanager
def change_precision(prec=1):
    default_prec = getcontext().prec

    assert 0 < prec < MAX_PREC, f'Precison must be a positive integer between 1 and {MAX_PREC}'
    getcontext().prec = prec

    yield

    getcontext().prec = default_prec


class ChangePrecision():

    def __init__(self, prec=1):
        assert 0 < prec < MAX_PREC, f'Precison must be a positive integer between 1 and {MAX_PREC}'
        self.prec = prec

    def __enter__(self):
        self.default_prec = getcontext().prec
        getcontext().prec = self.prec
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        getcontext().prec = self.default_prec


def main():
    with change_precision(2):
        print(Decimal('1.123132132') + Decimal('2.23232'))

    print(Decimal('1.123132132') + Decimal('2.23232'))


if __name__ == '__main__':
    main()
