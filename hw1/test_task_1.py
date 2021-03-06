import pytest

from hw1.task_1 import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (65536, True),
        (16384, True),
        (128, True),
        (1, True),
        (0, False),
        (10000, False),
        (3000, False),
        (10, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
