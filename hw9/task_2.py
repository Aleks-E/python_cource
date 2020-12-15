"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
from contextlib import contextmanager
from typing import Iterator, TypeVar

ExcVal = TypeVar("ExcVal")
ExcType = TypeVar("ExcType")
ExcTb = TypeVar("ExcTb")


class SuppressorClass:
    def __init__(self, exc_val: ExcVal):
        self.exc_val = exc_val

    def __enter__(self):
        ...

    def __exit__(self, exc_type: ExcType, exc_val: ExcVal, exc_tb: ExcTb):
        return isinstance(exc_val, self.exc_val)


@contextmanager
def suppressor_gen(exc_type: ExcType) -> Iterator:
    try:
        yield
    except exc_type:
        ...
