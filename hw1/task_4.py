"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    zero_numbers = 0
    for i in a[0]:
        for j in b[1]:
            for k in c[2]:
                for n in d[3]:
                    if i + j + k + n == 0:
                        zero_numbers += 1
    return zero_numbers
