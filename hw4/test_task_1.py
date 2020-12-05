import os

from hw4.task_1 import read_magic_number


import pytest


@pytest.fixture()
def test_file():
    file_path = "hw4/test.txt"
    with open(file_path, "w"):
        ...
    yield file_path
    os.remove(file_path)


@pytest.mark.parametrize(
    ("text", "expected_result"),
    [
        ("1", True),
        ("1.5", True),
        ("1.5\nq", True),
    ],
)
def test_number_in_the_diapazone(test_file, text, expected_result):
    with open(test_file, "w") as data:
        data.write(text)

    actual_result = read_magic_number(test_file)
    assert actual_result


@pytest.mark.parametrize(
    ("text", "expected_result"),
    [
        ("-3", False),
        ("0", False),
        ("3", False),
        ("4", False),
    ],
)
def test_number_is_not_in_the_diapazone(test_file, text, expected_result):
    with open(test_file, "w") as data:
        data.write(text)

    actual_result = read_magic_number(test_file)
    assert not actual_result


def test_read_str_is_empty(test_file):
    with open(test_file, "w") as data:
        data.write("")

    with pytest.raises(ValueError, match="could not convert string to float: ''"):
        read_magic_number(test_file)


def test_read_str_is_not_number(test_file):
    with open(test_file, "w") as data:
        data.write("q")

    with pytest.raises(ValueError, match="could not convert string to float: 'q'"):
        read_magic_number(test_file)


def test_file_did_not_exist():
    with pytest.raises(ValueError, match="file is not exist"):
        read_magic_number("hw4/test.txt")
