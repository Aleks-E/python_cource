"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


# >>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List

import doctest
import pytest

# pytest --doctest-modules





# python -m doctest -v hw4/task_4.py

# pytest --doctest-glob="task_4.py"       # Запуск всех тестов



def fizzbuzz(n: int) -> List[str]:
    pass





def a(arg):
    """
    >>> a(4)
    16
    >>> a(5)
    25
    """
    return arg * arg



print(a(3))



print(2)


# print(doctest.testmod())








