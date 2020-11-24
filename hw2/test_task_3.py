from hw2.task_3 import combinations
from typing import List, Any
import pytest

@pytest.mark.parametrize(
    ("args", "expected_result"),
    [
        (([],), ([])),
        (([], []), ([])),
        # (([1, 2]), ([[1], [2]])),
        (([1, 2], [3, 4]), ([[1, 3], [1, 4], [2, 3], [2, 4]]))
    ],
)


def test_combinations(args: List[Any], expected_result: List[List]):
    actual_result = combinations(*args)

    assert actual_result == expected_result