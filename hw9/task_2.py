"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
from contextlib import contextmanager
from typing import Iterator


class SuppressorClass:
    def __init__(self, exc_val: any):
        self.exc_val = exc_val

    def __enter__(self):
        ...

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any):
        return isinstance(exc_val, self.exc_val)


@contextmanager
def suppressor_gen(exc: any) -> Iterator:
    try:
        yield
    except exc:
        ...
