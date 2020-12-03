"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    # >>> f()
    # ? 1
    # '1'
    # >>> f()     # will remember previous value
    # '1'
    # >>> f()     # but use it up to two times only
    # '1'
    # >>> f()
    # ? 2
    # '2'
"""

from collections.abc import Callable


def cache(number_of_iterations: int) -> Callable:
    def iter_set(func: Callable) -> Callable:
        count_iteration = 0
        result = None

        def cached_func(*args: object) -> object:
            nonlocal count_iteration
            nonlocal result
            while True:
                if count_iteration == 0:
                    result = func(*args)
                    count_iteration = number_of_iterations
                    return result
                if count_iteration > 0:
                    count_iteration -= 1
                    return result

        return cached_func

    return iter_set
