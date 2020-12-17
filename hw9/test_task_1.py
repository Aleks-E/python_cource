import os

from hw9.task_1 import merge_sorted_files

import pytest


@pytest.fixture()
def test_file():
    file_path_1 = "hw9/test_1.txt"
    file_path_2 = "hw9/test_2.txt"

    def write_content(content_1, content_2):
        with open(file_path_1, "w") as data:
            data.write(content_1)

        with open(file_path_2, "w") as data:
            data.write(content_2)

        return file_path_1, file_path_2

    yield write_content
    os.remove(file_path_1)
    os.remove(file_path_2)


def test_both_files_is_empty(test_file):
    file_path = test_file("", "")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == []


def test_one_of_the_files_is_empty(test_file):
    file_path = test_file("1", "")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1]
    file_path = test_file("", "1")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1]


def test_files_with_different_lengths(test_file):
    file_path = test_file("1\n2\n3", "1")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 1, 2, 3]
    file_path = test_file("1", "1\n2\n3")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 1, 2, 3]


def test_all_numbers_in_one_file_is_less_than_all_numbers_in_second_file(test_file):
    file_path = test_file("1\n2", "4\n5")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 4, 5]
    file_path = test_file("4\n5", "1\n2")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 4, 5]


def test_numbers_in_both_files_grows_in_turn(test_file):
    file_path = test_file("1\n3", "2\n4")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 3, 4]
    file_path = test_file("2\n4", "1\n3")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 3, 4]


def test_one_of_the_files_has_the_same_numbers(test_file):
    file_path = test_file("1\n1", "2\n3")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 1, 2, 3]
    file_path = test_file("2\n3", "1\n1")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 1, 2, 3]


def test_both_files_have_the_same_numbers(test_file):
    file_path = test_file("1\n2", "2")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 2]
    file_path = test_file("2", "1\n2")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [1, 2, 2]


def test_checking_if_strings_or_numbers_are_compared(test_file):
    file_path = test_file("11", "2")
    assert list(merge_sorted_files([file_path[0], file_path[1]])) == [2, 11]
