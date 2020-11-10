"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


# def combinations(*args: List[Any]) -> List[List]:
#     a = []
#     # for i in args:
#     #     # print(i)
#     #     a.append(i)
#     #     return a
#
#     return args[0]



# d = [1, 2, 3], [4, 5, 6], [7, 8, 9]
#
# def a(*d):
#     for i in d:
#         for j in i:
#             print(j)





# a(d)        # ([1, 2], [3, 4])


from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))   # 10





 # assert None == ([1, 3], [1, 4], [2, 3], [2, 4])


# assert [([1, 2], [3, 4])] == ([1, 3], [1, ...2, 3], [2, 4])


