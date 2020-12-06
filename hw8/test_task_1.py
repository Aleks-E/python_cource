from hw8.task_1 import KeyValueStorage


import pytest
import os


@pytest.fixture()
def test_file():
    file_path = "text.txt"
    with open(file_path, "w"):
        ...
    yield file_path
    os.remove(file_path)



def test_input_file_does_not_exsist():
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'text.txt'"):
        KeyValueStorage("text.txt")




def test_input_file_is_empty(test_file):
    with open(test_file)








