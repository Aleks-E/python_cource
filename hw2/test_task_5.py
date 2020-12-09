from hw2.task_5 import custom_range

import pytest


@pytest.mark.parametrize(
    ("iterable", "args", "expected_result"),
    [
        ("012345", ("4",), ["0", "1", "2", "3"]),
        ("012345", ("2", "4"), ["2", "3"]),
        ("012345", ("0", "4", 2), ["0", "2"]),
        ("012345", ("4", "1", -2), ["4", "2"]),
    ],
)
def test_of_custom_range_function_work_with_different_parameters(
    iterable, args, expected_result
):
    actual_result = custom_range(iterable, *args)
    assert actual_result == expected_result


def test_of_custom_range_function_work_with_list_objects():
    iterable = [0, 1, 2, 3, 4, 5]
    assert custom_range(iterable, 0, 4, 2) == [0, 2]


def test_of_custom_range_function_work_with_tuple_objects():
    iterable = (0, 1, 2, 3, 4, 5)
    assert custom_range(iterable, 0, 4, 2) == [0, 2]
