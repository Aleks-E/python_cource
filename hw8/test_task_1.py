import os

from hw8.task_1 import KeyValueStorage

import pytest


@pytest.fixture()
def test_file():
    file_path = "hw8/test.txt"

    def write_content(content):
        with open(file_path, "w") as data:
            data.write(content)
            return file_path

    yield write_content
    os.remove(file_path)


@pytest.mark.parametrize(
    ("key_name"),
    [
        (""),
        (" name"),
        ("1name"),
        ("!name"),
        ("na!me"),
        ("na me"),
        ("name "),
        ("name!"),
    ],
)
def test_file_includes_strings_with_invalid_key_attributes(test_file, key_name):
    file_patch = test_file(key_name + "=kek")
    with pytest.raises(ValueError, match=f"Invalid Key Name: '{key_name}'"):
        KeyValueStorage(file_patch)


def test_file_includes_strings_with_missing_separator(test_file):
    file_patch = test_file("nn")
    with pytest.raises(ValueError, match="not enough values to unpack"):
        KeyValueStorage(file_patch)


def test_file_includes_strings_with_more_than_one_separator(test_file):
    file_patch = test_file("nn=nn=")
    with pytest.raises(ValueError, match="too many values to unpack"):
        KeyValueStorage(file_patch)


def test_file_includes_strings_with_two_separators_following_each_other(test_file):
    file_patch = test_file("nn==nn")
    with pytest.raises(ValueError, match="too many values to unpack"):
        KeyValueStorage(file_patch)


def test_file_includes_valid_strings(test_file):
    file_patch = test_file("name=kek\nlast_name=top")
    storage = KeyValueStorage(file_patch)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage.name == "kek"
    assert storage.last_name == "top"


def test_file_includes_valid_strings_with_empty_strings(test_file):
    file_patch = test_file("\n\nname=kek\n\nlast_name=top\n\n")
    storage = KeyValueStorage(file_patch)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage.name == "kek"
    assert storage.last_name == "top"


def test_convert_string_value_to_number_if_the_value_is_number(test_file):
    file_patch = test_file("name=1")
    storage = KeyValueStorage(file_patch)
    assert isinstance(storage["name"], int)
    assert isinstance(storage.name, int)
