# from collections.abc import Callable
#
#
# def cache(number_of_iterations: int) -> Callable:
#     def iter_set(func: Callable) -> Callable:
#         cached = []
#         count_iteration = number_of_iterations
#
#         def cached_func(*args: object) -> object:
#             nonlocal count_iteration
#
#             while count_iteration:
#                 for stored_args, result in cached:
#                     if stored_args == args:
#                         count_iteration -= 1
#                         return result
#
#                 result = func(*args)
#                 cached.append((args, result))
#                 count_iteration = number_of_iterations
#                 count_iteration -= 1
#                 return result
#
#         return cached_func
#
#     return iter_set



from collections.abc import Callable


# def cache(number_of_iterations: int) -> Callable:
#     def iter_set(func: Callable) -> Callable:
#         cached = []
#         count_iteration = number_of_iterations
#
#         def cached_func(*args: object) -> object:
#             nonlocal count_iteration
#
#             # while count_iteration:
#             if count_iteration > 1:
#                 for stored_args, result in cached:
#                     if stored_args == args:
#                         count_iteration -= 1
#                         return result
#
#                 result = func(*args)
#                 cached.append((args, result))
#                 count_iteration = number_of_iterations
#                 count_iteration -= 1
#                 return result
#             else:
#                 count_iteration = number_of_iterations
#                 result = func(*args)
#                 return result
#
#
#         return cached_func
#
#     return iter_set



# -----------------------------------------------
def cache(number_of_iterations: int) -> Callable:
    def iter_set(func: Callable) -> Callable:
        # count_iteration = number_of_iterations
        count_iteration = 0
        result = None
        def cached_func(*args: object) -> object:
            nonlocal count_iteration
            nonlocal result
            while True:

                if count_iteration == 0:
                    result = func(*args)
                    count_iteration = number_of_iterations
                if count_iteration > 0:
                    count_iteration -= 1
                    return result

                # count_iteration += 3
                # return count_iteration



        return cached_func


    return iter_set






# @cache(number_of_iterations=2)
def func(number):
    print('ok')
    return number + 1



# def func():
#     return input('? ')


# def func():
#     print('ok')
#     return 44




func_1 = cache(number_of_iterations=4)(func)

print(func_1(1))
print(func_1(10))
print(func_1(15))
print(func_1(10))
print(func_1(11))
print(func_1(10))
print(func_1(1))
print(func_1(1))
print(func_1(1))
print(func_1(1))
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())
# print(func_1())



def A():
    ...






