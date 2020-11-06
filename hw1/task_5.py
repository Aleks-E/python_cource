"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """ Function calculates sum of sub-array elements """
    if nums == []:
        print("empty list")
        return -1
    elif k > len(nums):
        print("k > nums")
        return -1
    elif k <= 0:
        print("k <= 0")
        return -1
    else:
        subarray_sum_maximum = subarray_sum_current = sum(nums[0:k])
        while len(nums) > k:
            subarray_sum_current -= nums[0]
            nums = nums[1:]
            subarray_sum_current += nums[k - 1]
            if subarray_sum_current > subarray_sum_maximum:
                subarray_sum_maximum = subarray_sum_current
        return subarray_sum_maximum


nums = [1, 3, -1, 9, 5, 3, 6, 7]
k = 3

print(find_maximal_subarray_sum(nums, k))
