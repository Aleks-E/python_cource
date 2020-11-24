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

def combinations(*args: List[Any]) -> List[List]:
    # print('args', args)
    # print('*args', *args)
    a = [[]]

    for y in args:
        b = y
        m = []
        for i in a:
            for j in b:
                m.append([*i, j])
        a = m
    return a





# print(combinations([]))
# a = ([], [])
# print(combinations(*a))
#
# a = ([],)
# print(combinations(*a))
#
#
# print(combinations([], []))
# print(combinations([1, 2], [3, 4]))


print(combinations([1, 2], [], [3, 4]))








