"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import List


def check_fibonacci(data: List[int]) -> bool:
    if data == [0]:
        return True
    if data == [0, 1]:
        return True
    while data[2:]:
        if data[2] != data[0] + data[1]:
            return False
        data = data[1:]
    return True
