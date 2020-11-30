from hw7.task_2 import backspace_compare

import pytest


@pytest.mark.parametrize(
    ("input_data", "expected_result"),
    [
        (("", ""), True),
        (("", "##"), True),
        (("##", ""), True),
        (("abc", "abc"), True),
        (("qw##c", "ab##c"), True),
        (("ab##c", "c"), True),
        (("c", "ab##c"), True),
        (("", "abc"), False),
        (("abc", ""), False),
        (("abc", "ab"), False),
        (("ab", "abc"), False),
        (("abc", "abc#"), False),
        (("abc#", "abc"), False),
    ],
)
def test_backspace_compare(input_data, expected_result):
    actual_result = backspace_compare(*input_data)

    assert actual_result == expected_result
