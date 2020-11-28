"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Union


def custom_range(
    iterable: Union[str, list, tuple],
    start: Union[str, int] = None,
    stop: Union[str, int] = None,
    step: int = 1,
) -> list:
    index_start = iterable.index(start) if start is not None else 0
    index_stop = iterable.index(stop) if stop is not None else -1
    return list(iterable[index_start:index_stop:step])
