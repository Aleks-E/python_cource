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
    def cache_variables(func: Callable) -> Callable:
        cached_result = {}
        number_of_returned_results = {}

        def cached_func(*args: any, **kwargs: any) -> any:
            if (args, tuple(kwargs.items())) not in cached_result:
                number_of_returned_results[(args, tuple(kwargs.items()))] = 0

            if number_of_returned_results[(args, tuple(kwargs.items()))] == 0:
                cached_result[(args, tuple(kwargs.items()))] = func(*args, **kwargs)
                number_of_returned_results[
                    (args, tuple(kwargs.items()))
                ] = number_of_iterations

            elif number_of_returned_results[(args, tuple(kwargs.items()))] > 0:
                number_of_returned_results[(args, tuple(kwargs.items()))] -= 1

            return cached_result[(args, tuple(kwargs.items()))]

        return cached_func

    return cache_variables
