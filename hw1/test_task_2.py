from collections.abc import Sequence

import pytest

from hw1.task_2 import check_fibonacci

data_0 = []
data_1 = [2]
data_2 = [0]
data_3 = [0, 3]
data_4 = [1, 1]
data_5 = [0, 1]
data_6 = [
    1,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]
data_7 = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    1441,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]
data_8 = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    67651,
]
data_9 = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (data_0, False),
        (data_1, False),
        (data_2, True),
        (data_3, False),
        (data_4, False),
        (data_5, True),
        (data_6, False),
        (data_7, False),
        (data_8, False),
        (data_9, True),
    ],
)
def test_check_fibonacci(data: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
