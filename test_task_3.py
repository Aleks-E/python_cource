from typing import List

from hw2.task_3 import combinations

import pytest

data = [1, 2], [3, 4]
result = [[1, 3], [1, 4], [2, 3], [2, 4]]


@pytest.mark.parametrize(
    ("inp", "expected_result"),
    [
        (data, result),
    ],
)
def test_ombinations(inp: List[int], expected_result: (list, list, list, list)):
    actual_result = combinations(inp)

    assert actual_result == expected_result
