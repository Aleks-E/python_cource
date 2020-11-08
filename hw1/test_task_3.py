import pytest

from hw1.task_3 import find_maximum_and_minimum

with open("test_task_3_data_0.txt", "w") as data:
    data.write("0")

with open("test_task_3_data_1.txt", "w") as data:
    data.write("1\n1\n1\n1")

with open("test_task_3_data_2.txt", "w") as data:
    data.write("4\n8\n3\n2")

with open("test_task_3_data_3.txt", "w") as data:
    data.write("4\n8\n8\n2\n1\n2")

with open("test_task_3_data_4.txt", "w") as data:
    data.write("4\n8\n1\n8\n2\n1\n2")

with open("test_task_3_data_5.txt", "w") as data:
    data.write("4\n8\n1\n8\n2\n2\n1")

with open("test_task_3_data_6.txt", "w") as data:
    data.write("8\n1\n8\n2\n2\n1")


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test_task_3_data_0.txt", (0, 0)),
        ("test_task_3_data_1.txt", (1, 1)),
        ("test_task_3_data_2.txt", (8, 2)),
        ("test_task_3_data_3.txt", (8, 1)),
        ("test_task_3_data_4.txt", (8, 1)),
        ("test_task_3_data_5.txt", (8, 1)),
        ("test_task_3_data_6.txt", (8, 1)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: (int, int)):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
