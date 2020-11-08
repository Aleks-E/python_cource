import pytest

from hw1.task_5 import find_maximal_subarray_sum_1

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 20
data_0 = nums, k

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
data_1 = nums, k

nums = [1, 3, -1, 9, 5, 3, 6, 7]
k = 3
data_2 = nums, k

nums = [100, 3, -1, 9, 5, 3, 6, 7]
k = 3
data_3 = nums, k


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (data_0, -1),
        (data_1, 16),
        (data_2, 17),
        (data_3, 102),
    ],
)
def test_find_maximal_subarray_sum_1(data: tuple, expected_result: int):
    actual_result = find_maximal_subarray_sum_1(*data)

    assert actual_result == expected_result
