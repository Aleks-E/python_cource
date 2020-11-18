from collections.abc import Callable


def cache(number_of_iterations: int) -> Callable:
    def iter_set(func: Callable) -> Callable:
        cached = []
        count_iteration = number_of_iterations

        def cached_func(*args) -> object:
            nonlocal count_iteration

            while count_iteration:
                for stored_args, result in cached:
                    if stored_args == args:
                        count_iteration -= 1
                        return result

                result = func(*args)
                cached.append((args, result))
                count_iteration = number_of_iterations
                count_iteration -= 1
                return result

        return cached_func

    return iter_set
