import pytest

from hw1.task_1 import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (65536, False),
        (16384, False),
        (128, False),
        (1, False),
        (0, False),
        (10000, True),
        (3000, True),
        (10, True),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
