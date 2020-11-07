"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    zero_numbers = 0
    for i in A:
        for j in B:
            for k in C:
                for l in D:
                    if i + j + k + l == 0:
                        zero_numbers += 1
                        print(i, j, k, l)
    return zero_numbers
