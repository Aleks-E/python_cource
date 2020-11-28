from hw2.task_5 import custom_range

import pytest


@pytest.mark.parametrize(
    ("args", "expected_result"),
    [
        (("",), ([])),
        (("0123",), (["0", "1", "2"])),
        (("012345", "2"), (["2", "3", "4"])),
        (("012345", "2", "4"), (["2", "3"])),
        (("012345", "0", "4", 2), (["0", "2"])),
        (("012345", "4", "1", -2), (["4", "2"])),
    ],
)
def test_of_custom_range_function_work_with_different_parameters(args, expected_result):
    actual_result = custom_range(*args)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("args", "expected_result"),
    [
        (([],), ([])),
        (([0, 1, 2, 3, 4, 5], 0, 4, 2), ([0, 2])),
        (((),), ([])),
        (((0, 1, 2, 3, 4, 5), 0, 4, 2), ([0, 2])),
    ],
)
def test_of_custom_range_function_work_with_objects_different_types(
    args, expected_result
):
    actual_result = custom_range(*args)

    assert actual_result == expected_result
