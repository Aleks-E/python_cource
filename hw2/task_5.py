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


def custom_range(iterable: Union[str, list, tuple], *args: (int,)) -> list:
    if len(args) == 1:
        index_start = 0
        index_stop = iterable.index(args[0])
        index_step = 1

    elif len(args) == 2:
        index_start = iterable.index(args[0])
        index_stop = iterable.index(args[1])
        index_step = 1

    elif len(args) == 3:
        index_start = iterable.index(args[0])
        index_stop = iterable.index(args[1])
        index_step = args[2]

    return list(iterable[index_start:index_stop:index_step])
