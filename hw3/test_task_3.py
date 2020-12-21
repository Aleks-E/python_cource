from hw3.task_3 import make_filter


def test_matching_input_data_and_filter_data():
    data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "polly", "type": "bird"},
    ]
    expected_result = [{"name": "polly", "type": "bird"}]
    actual_result = make_filter(name="polly", type="bird").apply(data)
    assert actual_result == expected_result


def test_mismatching_input_data_key_and_filter_data_key():
    data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name_1": "polly", "type": "bird"},
    ]
    assert [] == make_filter(name="polly", type="bird").apply(data)


def test_mismatching_input_data_value_and_filter_data_value():
    data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "polly_1", "type": "bird"},
    ]
    assert [] == make_filter(name="polly", type="bird").apply(data)


def test_missing_key_filters_item():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly"}]
    assert [] == make_filter(name="polly", type="bird").apply(data)


def test_missing_input_data_item():
    data = [{"name": "Bill", "last_name": "Gilbert"}]
    assert [] == make_filter(name="polly", type="bird").apply(data)


def test_wrong_input_filter_key():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name_1="polly").apply(data)
    assert actual_result == []


def test_wrong_input_filter_value():
    data = [{"name": "Bill", "last_name": "Gilbert"}, {"name": "polly", "type": "bird"}]
    actual_result = make_filter(name="polly_1").apply(data)
    assert actual_result == []
