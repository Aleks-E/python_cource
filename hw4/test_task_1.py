import os

from hw4.task_1 import read_magic_number


import pytest


@pytest.fixture()
def test_file():
    file_path = "hw4/test.txt"

    def write_content(content):
        with open(file_path, "w") as data:
            data.write(content)
            return file_path

    yield write_content
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
    file_patch = test_file(text)
    actual_result = read_magic_number(file_patch)
    assert expected_result == actual_result


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
    file_patch = test_file(text)
    actual_result = read_magic_number(file_patch)
    assert expected_result == actual_result


def test_read_str_is_empty(test_file):
    file_patch = test_file("")
    with pytest.raises(ValueError, match="could not convert string to float: ''"):
        read_magic_number(file_patch)


def test_read_str_is_not_number(test_file):
    file_patch = test_file("q")

    with pytest.raises(ValueError, match="could not convert string to float: 'q'"):
        read_magic_number(file_patch)
