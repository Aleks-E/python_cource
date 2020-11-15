# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions: list):
        self.functions = functions

    def apply(self, data: dict) -> list:
        return [
            item
            for item in data
            if all(functions(item) for functions in self.functions)
        ]


# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords: dict) -> object:
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(key: str, value: dict) -> None:
            def keyword_filter_func_inner(input_item: dict) -> bool:
                return False if key not in input_item else True if input_item[key] == value else False

            filter_funcs.append(keyword_filter_func_inner)

        keyword_filter_func(key, value)

    return Filter(filter_funcs)


# def a(x):
#     if x in [1, 2, 3]:
#         return True
#     return False
#
# print(a(4))


