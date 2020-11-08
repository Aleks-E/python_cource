"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import List


def fib_gen() -> int:
    number_prev_1, number_prev = 0, 1
    yield number_prev_1
    yield number_prev
    while True:
        number = number_prev + number_prev_1
        number_prev_1, number_prev = number_prev, number
        yield number


def check_fibonacci(data: List[int]) -> bool:
    gen = fib_gen()
    for i in data:
        if i != next(gen):
            return False
    return True
