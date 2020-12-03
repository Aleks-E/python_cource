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
