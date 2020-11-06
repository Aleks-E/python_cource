import pytest

from hw1.task_3 import find_maximum_and_minimum

with open("data_0.txt", "w") as data:
    data.write("0")

with open("data_1.txt", "w") as data:
    data.write("1\n1\n1\n1")

with open("data_2.txt", "w") as data:
    data.write("4\n8\n3\n2")

with open("data_3.txt", "w") as data:
    data.write("4\n8\n8\n2\n1\n2")

with open("data_4.txt", "w") as data:
    data.write("4\n8\n1\n8\n2\n1\n2")

with open("data_5.txt", "w") as data:
    data.write("4\n8\n1\n8\n2\n2\n1")

with open("data_6.txt", "w") as data:
    data.write("8\n1\n8\n2\n2\n1")


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("data_0.txt", (0, 0)),
        ("data_1.txt", (1, 1)),
        ("data_2.txt", (8, 2)),
        ("data_3.txt", (8, 1)),
        ("data_4.txt", (8, 1)),
        ("data_5.txt", (8, 1)),
        ("data_6.txt", (8, 1)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: (int, int)):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
