"""
Homework 1:
============


We have a file that works as key-value storage, each like is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
import string


class KeyValueStorage:
    def __init__(self, file_path: str):
        with open(file_path, "r") as data:
            self.storage = {}
            for line in data:
                if line == "\n":
                    continue
                key, value = line.rstrip().split("=")

                self.key_name_checker(key)

                if value.isdigit():
                    value = int(value)

                if key not in self.__dir__():
                    setattr(self, key, value)
                    self.storage.__setitem__(key, value)

    def __setitem__(self, key: str, value: str):
        self.storage[key] = value

    def __getitem__(self, key: str):
        return self.storage[key]

    def key_name_checker(self, key: str) -> None:
        if bool(
            [
                letter
                for letter in key
                if letter not in (*string.ascii_letters, "_", *string.digits)
            ]
        ):
            raise ValueError(f"Invalid Key Name: '{key}'")

        if key == "":
            raise ValueError(f"Invalid Key Name: '{key}'")

        if key[0].isdigit():
            raise ValueError(f"Invalid Key Name: '{key}'")
