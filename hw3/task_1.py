def number_of_iter_set(number_of_iterations: int) -> object:
    def cache(func: object) -> object:
        count_iteration = number_of_iterations
        cached_number = 0

        def iter_check() -> int:
            nonlocal count_iteration
            nonlocal cached_number
            while True:
                while count_iteration:
                    if count_iteration == number_of_iterations:
                        cached_number = func()
                        count_iteration -= 1
                        return cached_number
                    else:
                        count_iteration -= 1
                        return cached_number
                count_iteration = number_of_iterations

        return iter_check

    return cache


@number_of_iter_set(number_of_iterations=4)
def input_number() -> int:
    return int(input("? "))
