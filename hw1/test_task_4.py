from typing import List

import pytest

from hw1.task_4 import check_sum_of_four

data_0 = [1, 1], [1, 1], [1, 1], [1, 1]
data_1 = [1, 1], [1, 1], [1, 1], [1, -3]
data_2 = [1, 1], [1, 1], [1, 1], [-3, 1]
data_3 = [1, 1], [1, 1], [1, 1], [-3, -3]

data_4 = [1, 1], [1, 1], [1, -3], [1, 1]
data_5 = [1, 1], [1, 1], [-3, 1], [1, 1]
data_6 = [1, 1], [1, 1], [-3, -3], [1, 1]

data_7 = [1, 1], [1, -3], [1, 1], [1, 1]
data_8 = [1, 1], [-3, 1], [1, 1], [1, 1]
data_9 = [1, 1], [-3, -3], [1, 1], [1, 1]

data_10 = [1, -3], [1, 1], [1, 1], [1, 1]
data_11 = [-3, 1], [1, 1], [1, 1], [1, 1]
data_12 = [-3, -3], [1, 1], [1, 1], [1, 1]

data_13 = [1, 1], [1, 1], [-1, -1], [-1, -1]
data_14 = [1, 1], [-1, -1], [-1, -1], [1, 1]
data_15 = [-1, -1], [-1, -1], [1, 1], [1, 1]
data_16 = [-1, -1], [1, 1], [-1, -1], [1, 1]
data_17 = [-1, -1], [1, 1], [1, 1], [-1, -1]


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (data_0, 0),
        (data_1, 8),
        (data_2, 8),
        (data_3, 16),
        (data_4, 8),
        (data_5, 8),
        (data_6, 16),
        (data_7, 8),
        (data_8, 8),
        (data_9, 16),
        (data_10, 8),
        (data_11, 8),
        (data_12, 16),
        (data_13, 16),
        (data_14, 16),
        (data_15, 16),
        (data_16, 16),
        (data_17, 16),
    ],
)
def test_check_sum_of_four(
    data: (List[int], List[int], List[int], List[int]), expected_result: int
):
    actual_result = check_sum_of_four(*data)

    assert actual_result == expected_result
