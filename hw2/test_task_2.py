import pytest

from hw2.task_2 import major_and_minor_elem

from typing import List, Tuple

data = [2, 1, 3, 2, 3, 2]
result = (2, 1)


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        (data, result),
    ],
)
def test_major_and_minor_elem(inp: List, expected_result: (int, int)):
    actual_result = major_and_minor_elem(inp)

    assert actual_result == expected_result
