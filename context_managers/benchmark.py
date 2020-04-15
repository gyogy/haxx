from datetime import datetime


class MeasurePerformance():

    def __init__(self):
        self._start = datetime.now()
        self._restart = datetime.now()
        self._bm_count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        if exc_tb:
            print(f'{exc_type}')
            print(f'{exc}')

        delta = datetime.now() - self._start
        print(f'Finished in {delta.total_seconds()}')

    def benchmark(self, bm_str=None, restart=False):
        self._bm_count += 1
        delta = datetime.now() - self._restart

        if bm_str is not None:
            print(bm_str + ':', delta.total_seconds())
        else:
            print(f'Benchmark No. {self._bm_count}:', delta.total_seconds())

        if restart:
            self._restart = datetime.now()


def main():
    pass


if __name__ == '__main__':
    main()
