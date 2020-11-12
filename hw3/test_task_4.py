from hw3.task_4 import is_armstrong

import pytest


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (153, True),
        (371, True),
        (407, True),
        (111, False),
        (1000, False),
        (3200, False),
    ],
)
def test_is_armstrong(data: int, expected_result: bool):
    actual_result = is_armstrong(data)

    assert actual_result == expected_result
