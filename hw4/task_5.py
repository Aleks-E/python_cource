"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import Iterator


def fizzbuzz(number_of_items: int) -> Iterator:
    fizz_iter = cycle(["", "", "Fizz"])
    buzz_iter = cycle(["", "", "", "", "Buzz"])

    for iteration in range(1, number_of_items + 1):
        fizz_buzz_item = next(fizz_iter) + next(buzz_iter)
        item = [fizz_buzz_item, str(iteration)]
        item.sort()
        yield item[1]
