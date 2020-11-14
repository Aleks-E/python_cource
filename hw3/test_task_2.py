import timeit

from hw3.task_2 import sum_of_numbers

import pytest


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (0, 0),
        (1, 2785),
        (501, 1025932),
    ],
)
def test_sum_of_numbers(value: int, expected_result: int):
    actual_result = sum_of_numbers(value)

    assert actual_result == expected_result


def test_time_sum_of_numbers():
    start_time = timeit.default_timer()
    sum_of_numbers(501)
    end_time = timeit.default_timer()
    assert end_time - start_time < 60
