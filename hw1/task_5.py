"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum_1(nums: List[int], k: int) -> int:
    a = []
    for n in range(1, k + 1):
        a.append(find_maximal_subarray_sum(nums, k))
    return max(a)


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) == 1 and k == 1:
        return max(List)
    if len(nums) >= k and k > 0:
        subarray_sum_maximum = subarray_sum_current = sum(nums[0:k])
        while len(nums) > k:
            subarray_sum_current -= nums[0]
            nums = nums[1:]
            subarray_sum_current += nums[k - 1]
            if subarray_sum_current > subarray_sum_maximum:
                subarray_sum_maximum = subarray_sum_current
        return subarray_sum_maximum
    return -1
