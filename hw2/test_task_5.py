from hw2.task_5 import custom_range

import pytest


@pytest.mark.parametrize(
    ("iterable", "kwargs", "expected_result"),
    [
        ("", {}, []),
        ("0123", {}, ["0", "1", "2"]),
        ("012345", {"start": "2"}, ["2", "3", "4"]),
        ("012345", {"start": "2", "stop": "4"}, ["2", "3"]),
        ("012345", {"start": "0", "stop": "4", "step": 2}, ["0", "2"]),
        ("012345", {"start": "4", "stop": "1", "step": -2}, ["4", "2"]),
    ],
)
def test_of_custom_range_function_work_with_different_parameters(
    iterable, kwargs, expected_result
):
    actual_result = custom_range(iterable, **kwargs)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("iterable", "kwargs", "expected_result"),
    [
        ([], {}, []),
        ([0, 1, 2, 3, 4, 5], {"start": 0, "stop": 4, "step": 2}, [0, 2]),
        ((), {}, []),
        ((0, 1, 2, 3, 4, 5), {"start": 0, "stop": 4, "step": 2}, [0, 2]),
    ],
)
def test_of_custom_range_function_work_with_objects_different_types(
    iterable, kwargs, expected_result
):
    actual_result = custom_range(iterable, **kwargs)
    assert actual_result == expected_result
