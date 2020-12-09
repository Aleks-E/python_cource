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
    with open(test_file, "w") as data:
        data.write(f"{key_name}=kek")

    with pytest.raises(ValueError, match=f"Invalid Key Name: '{key_name}'"):
        KeyValueStorage(test_file)


def test_file_includes_strings_with_missing_separator(test_file):
    with open(test_file, "w") as data:
        data.write("nn")

    with pytest.raises(ValueError, match="not enough values to unpack"):
        KeyValueStorage(test_file)



# @pytest.mark.parametrize(
#     ("string"),
#     [
#         ("nn=rr="),
#         ("nn==rr"),
#     ],
# )
# def test_too_many_values_to_unpack(test_file, string):
#     with open(test_file, "w") as data:
#         data.write(f"{string}")
#
#     with pytest.raises(ValueError, match="too many values to unpack"):
#         KeyValueStorage(test_file)












# ----------------



def test_input_file_is_empty(test_file):        # review
    with open(test_file, "w") as data:          # Как проверить что программа выполнилась без ошибок
        data.write("rr=rr")







@pytest.mark.parametrize(
    ("file_content"),
    [
        ("name=kek\nlast_name=top"),
        ("\n\nname=kek\n\nlast_name=top\n\n"),
    ],
)
def test_right_input_str(test_file, file_content):
    with open(test_file, "w") as data:
        data.write(file_content)

    storage = KeyValueStorage(test_file)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage.name == "kek"
    assert storage.last_name == "top"















# @pytest.mark.parametrize(
#     ("string"),
#     [
#         ("nn=rr="),
#         ("nn==rr"),
#     ],
# )
# def test_too_many_values_to_unpack(test_file, string):
#     with open(test_file, "w") as data:
#         data.write(f"{string}")
#
#     with pytest.raises(ValueError, match="too many values to unpack"):
#         KeyValueStorage(test_file)







# @pytest.fixture()
# def ValueError_message():
#     return "key_name"





# @pytest.mark.parametrize(
#     ("ValueError_message", "ValueError_Message"),
#     [
#         ("", f"Invalid Key Name: '{ValueError_message}'"),
#         # (" name", f"Invalid Key Name: '{key_name}'"),
#         # ("1name", f"Invalid Key Name: '{key_name}'"),
#         # ("!name", f"Invalid Key Name: '{key_name}'"),
#         # ("na!me", f"Invalid Key Name: '{key_name}'"),
#         # ("na me", f"Invalid Key Name: '{key_name}'"),
#         # ("name ", f"Invalid Key Name: '{key_name}'"),
#         # ("name!", f"Invalid Key Name: '{key_name}'")
#     ],
# )

















# def test_missing_key_attribute(test_file):
#     with open(test_file, "w") as data:
#         key_name = "name "
#         data.write("=kek")
#
#     # storage = KeyValueStorage(test_file)
#     assert storage["name"] == "kek"
#
#     with pytest.raises(ValueError, match=f"Invalid Key Name: '{key_name}'"):
#         KeyValueStorage(test_file)

    # with














