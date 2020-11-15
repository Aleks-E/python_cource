from hw3.task_3 import make_filter

import pytest


right_input_and_filter_data = [
    {"name": "Bill", "last_name": "Gilbert"},
    {"name": "polly", "type": "bird"},
]
result_right_input_and_filter_data = [{"name": "polly", "type": "bird"}]

incorrect_input_initial_key = [
    {"name": "Bill", "last_name": "Gilbert"},
    {"name_1": "polly", "type": "bird"},
]
result_incorrect_input_initial_key = []

incorrect_input_initial_value = [
    {"name": "Bill", "last_name": "Gilbert"},
    {"name": "polly_1", "type": "bird"},
]
result_incorrect_input_initial_value = []

missing_input_value = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly"}]
result_missing_input_value = []

missing_input_item = [{"name": "Bill", "last_name": "Gilbert"}]
result_missing_input_item = []


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (right_input_and_filter_data, result_right_input_and_filter_data),
        (incorrect_input_initial_key, result_incorrect_input_initial_key),
        (incorrect_input_initial_value, result_incorrect_input_initial_value),
        (missing_input_value, result_missing_input_value),
        (missing_input_item, result_missing_input_item),
    ],
)
def test_make_filter(data, expected_result):
    actual_result = make_filter(name="polly", type="bird").apply(data)
    assert actual_result == expected_result


def test_wrong_input_filter_key():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name_1="polly").apply(data)
    assert actual_result == []


def test_wrong_input_filter_value():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name="polly_1").apply(data)
    assert actual_result == []
