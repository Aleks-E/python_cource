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

from itertools import cycle


def fizzbuzz(number_of_items: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    """
    fizz_iter = cycle(["", "", "Fizz"])
    buzz_iter = cycle(["", "", "", "", "Buzz"])
    items_list = []

    for iteration in range(1, number_of_items + 1):
        fizz_buzz_item = next(fizz_iter) + next(buzz_iter)
        item = [fizz_buzz_item, str(iteration)]
        item.sort()
        items_list.append(item[1])
    return items_list


print(fizzbuzz(20))


# pytest --doctest-glob="*.py"      # Проверяем во всех папках

# pytest -v --doctest-modules hw4/task_4.py     # Запускаем doctest
# pytest --doctest-modules hw4/task_4.py     # Запускаем doctest


#pytest --doctest-modules hw4/task_4.py hw4/test_task_4.py

#pytest hw4/test_task_4.py --doctest-modules hw4/task_4.py



