from pathlib import Path

from hw9.task_3 import universal_file_counter

import pytest


@pytest.fixture()
def test_file():
    path = "hw9/temp/"
    Path(path).mkdir()

    def write_content(content_1, content_2):
        Path(path + "test_1.txt").write_text(content_1)
        Path(path + "test_2.txt").write_text(content_2)
        return Path(path).expanduser()

    yield write_content
    Path(path + "test_1.txt").unlink()
    Path(path + "test_2.txt").unlink()
    Path(path).rmdir()


@pytest.fixture()
def create_tokenizer():
    def tokenizer(separator):
        return lambda line: line.split(separator)

    return tokenizer


def test_all_files_consist_of_blank_lines(test_file):
    path = test_file("", "")
    assert universal_file_counter(path, "txt") == 2


def test_one_of_the_files_consists_from_blank_line(test_file):
    path = test_file("12\n34", "")
    assert universal_file_counter(path, "txt") == 3


def test_one_of_the_files_includes_blank_lines(test_file):
    path = test_file("12\n\n34", "56\n78")
    assert universal_file_counter(path, "txt") == 5


def test_call_of_function_with_tokinizer(test_file, create_tokenizer):
    path = test_file("1\n2\n3\n4", "5\n2\n3\n6")
    tokenizer = create_tokenizer("2\n3")
    assert universal_file_counter(path, "txt", tokenizer) == 4


def test_two_tokens_in_the_file_following_each_other(test_file, create_tokenizer):
    path = test_file("1\n22\n3", "")
    tokenizer = create_tokenizer("2")
    assert universal_file_counter(path, "txt", tokenizer) == 4


def test_missing_letter_combination_in_the_files(test_file, create_tokenizer):
    path = test_file("1\n2\n3\n4", "5\n2\n3\n6")
    tokenizer = create_tokenizer("q")
    assert universal_file_counter(path, "txt", tokenizer) == 2
