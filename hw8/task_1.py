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

import os


# with open("text.txt", "w") as text:
#     text.write("name=kek\nlast_name=top\nsong_name=shadilay\npower=9001\nnn")
# text.write("name=kek\nlast_name=top\nsong_name=shadilay\npower=9001\n1=something\n__init__=3")
# text.write("name=kek")
# text.write("\n\n name=kek\n\nname1=kek1")
# text.write("\n")

# os.remove("text.txt")


# with open("text.txt", "w") as text:
#     text.write("=name")


class KeyValueStorage:
    def __init__(self, path_to_file):
        with open(path_to_file, "r") as data:
            self.storage = {}
            for line in data:
                if line == "\n":
                    continue
                key, value = line.rstrip().split("=")

                if not (
                    not bool([
                        letter
                        for letter in key
                        if letter not in (*string.ascii_letters, "_", *string.digits)
                    ])
                    and not key.startswith((*string.digits,))
                    and key != ""
                ):
                    raise ValueError(f"Invalid Key Name: '{key}'")

                # *string.whitespace, string.punctuation

                if value.isdigit():
                    value = int(value)

                if key not in self.__dir__():
                    setattr(self, key, value)
                    self.storage.__setitem__(key, value)

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        return self.storage[key]



# KeyValueStorage('text.txt')






#
# 'not enough values to unpack (expected 2, got 1)' does not match
# 'not enough values to unpack (expected 2, got 1)'




q = "qw=er=ty"

q = q.split('=')
print(q)











