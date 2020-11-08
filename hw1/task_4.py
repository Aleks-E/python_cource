"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    numbers_sum = [
        i + j + k + n for i in [1, 2] for j in [-1, 2] for k in [1, 2] for n in [-1, 2]
    ]
    zero_numbers = 0
    for i in numbers_sum:
        if i == 0:
            zero_numbers += 1
    return zero_numbers
