from hw8.task_1 import KeyValueStorage


import pytest
import os
# import string



@pytest.fixture()
def test_file():
    file_path = "hw8/test.txt"
    with open(file_path, "w"):
        ...
    yield file_path
    os.remove(file_path)


# @pytest.mark.parametrize(
#     ("text"),
#     [
#         ("name=kek"),
#     ],
# )
# def test_wrong_input_str(test_file, text):
#     with open(test_file, "w") as data:
#         # data.write("name=kek\nlast_name=top")
#         data.write(text)
#
#         # storage = KeyValueStorage(test_file)
#     storage = KeyValueStorage("hw8/test.txt")
#
#         # assert storage.name == "kek"
#     assert storage["name"] == "kek"
#         # assert storage.last_name == "top"




def test_input_file_does_not_exsist():
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'qqq.txt'"):
        KeyValueStorage("qqq.txt")



def test_input_file_is_empty(test_file):        # review
    with open(test_file, "w") as data:          # Как проверить что программа выполнилась без ошибок
        data.write("rr=rr")



def test_right_input_str(test_file):
    with open(test_file, "w") as data:
        data.write("name=kek\nlast_name=top")

    storage = KeyValueStorage(test_file)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage.name == "kek"
    assert storage.last_name == "top"



def test_file_included_empty_lines(test_file):
    with open(test_file, "w") as data:
        data.write("\n\nname=kek\n\nlast_name=top\n\n")

    storage = KeyValueStorage(test_file)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage.name == "kek"
    assert storage.last_name == "top"





@pytest.mark.parametrize(
    ("invalid_key_name"),
    [
        (" name"),
        ("1name"),
        ("!name"),
        ("!name ")
    ],
)
def test_file_includes_lines_with_invalid_key_attributes(test_file, invalid_key_name):
    with open(test_file, "w") as data:
        data.write(f"{invalid_key_name}=kek")

    with pytest.raises(ValueError, match=f"Invalid Key Name: '{invalid_key_name}'"):
        KeyValueStorage(test_file)













