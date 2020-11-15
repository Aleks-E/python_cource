from hw3.task_3 import make_filter

import pytest


data_0 = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
result_0 = [{"name": "polly", "type": "bird"}]

data_1 = [{"name": "Bill", "last_name": "Gilbert"}, {"name_1": "polly", "type": "bird"}]
result_1 = []

data_2 = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly_1", "type": "bird"}]
result_2 = []

data_3 = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly"}]
result_3 = []

data_4 = [{"name": "Bill", "last_name": "Gilbert"}]
result_4 = []


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (data_0, result_0),
        (data_1, result_1),
        (data_2, result_2),
        (data_3, result_3),
        (data_4, result_4),
    ],
)
def test(data, expected_result):
    actual_result = make_filter(name="polly", type="bird").apply(data)
    assert actual_result == expected_result


def test_1():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name_1="polly").apply(data)
    assert actual_result == []


def test_2():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name="polly_1").apply(data)
    assert actual_result == []
