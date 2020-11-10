from hw2.task_2 import major_and_minor_elem


def test_major_and_minor_elem():
    data = [2, 1, 3, 2, 3, 2]
    expected_result = (2, 1)
    actual_result = major_and_minor_elem(data)

    assert actual_result == expected_result
