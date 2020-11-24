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
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    result_combinations = [[]]

    for item in args:
        if not item:
            continue
        new_combinations = []
        for result_item in result_combinations:
            for inner_item in item:
                new_combinations.append([*result_item, inner_item])
        result_combinations = new_combinations
    return result_combinations
