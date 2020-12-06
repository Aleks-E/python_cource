from hw8.task_1 import KeyValueStorage


import pytest
import os
# import string



# @pytest.fixture()
# def test_file():
#     file_path = "hw8/text.txt"
#     with open(file_path, "w"):
#         ...
#     yield file_path
#     os.remove(file_path)


def test_input_file_does_not_exsist():
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'qqq.txt'"):
        KeyValueStorage("qqq.txt")


# def test_input_file_is_empty(test_file):        # review
#     with open(test_file, "w") as data:          # Как проверить что программа выполнилась без ошибок
#         data.write("rr=rr")



# def test_wrong_input_str(test_file):
#     with open(test_file, "w") as data:
#         # data.write("name=kek\nlast_name=top")
#         data.write("name=kek")
#
#         storage = KeyValueStorage(test_file)
#         # assert storage.name == "kek"
#         assert storage["name"] == "kek"
#         # assert storage.last_name == "top"



def test_wrong_input_str():
    with open("hw8/text.txt", "w") as data:
        # data.write("name=kek\nlast_name=top")
        data.write("name=kek")

        storage = KeyValueStorage("hw8/text.txt")
        # assert storage.name == "kek"
        assert storage["name"] == "kek"
        # assert storage.last_name == "top"









