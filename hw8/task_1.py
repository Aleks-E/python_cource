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


with open("text.txt", "w") as text:
    # text.write("name=kek\nlast_name=top\nsong_name=shadilay\npower=9001\n1=something")
    # text.write("name=kek\nlast_name=top\nsong_name=shadilay\npower=9001\n1=something\n__init__=3")
    # text.write("name=kek")
    # text.write("\n\n name=kek\n\nname1=kek1")
    text.write("\n")

os.remove("text.txt")

class KeyValueStorage:
    def __init__(self, path_to_file):
        with open(path_to_file, "r") as data:
            self.storage = {}
            for line in data:
                # print('line', line)
                if line == "\n":
                    # print('1234')
                    continue
                key, value = line.rstrip().split("=")
                print('key', list(key), key[0])


                if not (key.startswith((*string.ascii_letters, "_")) and key.endswith(
                    (*string.ascii_letters, "_", *string.digits))
                ):
                    raise ValueError(f"Invalid Key Name: '{key}'")

                if value.isdigit():
                    value = int(value)

                if key not in self.__dir__():
                    setattr(self, key, value)
                    self.storage.__setitem__(key, value)

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        return self.storage[key]









# a = "qwerty"

# print(a.startswith(("1", "q")))


# print((*string.ascii_letters,))

# try:
#     storage = KeyValueStorage("text.txt")
# except:
#     print('ok')

# storage = KeyValueStorage("te1xt.txt")
# print(dir(storage))

# print(storage. )
# print(storage[" "])


# print(string.ascii_letters)
# print(len(string.ascii_letters))



# a = ' '

# print(a.startswith('q'))



# print(storage.name)
# print(storage["name"])
# print(storage.name1)
# print(storage["name1"])


# print(storage.qqq)
# print(storage['qqq'])

# print(storage.__init__)

# print(dir(storage))


# print(storage.__dir__())


# print(storage.name)
# print(storage['name'])
# print(storage['power'])
# print(storage['__init__'])
# print(storage.__init__)


# storage = KeyValueStorage("text.txt")


# print(storage.name)
# print(storage['name'])
# print(storage['power'])
# print(storage['__init__'])


"""
dict

['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values']
"""


"""
class

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__']
"""


"""
Какие методы обычный класс не имеет по сравнению с dict


'__class_getitem__', 
'__contains__', 
'__delitem__', 
'__getitem__', 
'__ior__', 
'__iter__', 
'__len__', 
'__or__', 
'__reversed__', 
'__ror__', 
'__setitem__', 
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values'

"""


"""





# class KeyValueStorage(dict):
#     def __init__(self, path_to_file):
#         super().__init__()
#         with open(path_to_file, "r") as data:
#             for line in data:
#                 key, value = line.rstrip().split("=")
#
#
#
#
#                 if value.isdigit():
#                     value = int(value)
#
#                 setattr(self, key, value)
#                 self[key] = value
#
#
#
#
#
# storage = KeyValueStorage("text.txt")
#
# print(storage.name)
# print(storage.last_name)
# print(storage.song_name)
# print(storage.power)
# print(storage.__init__)
#
#
# print(storage['name'])
# print(storage['last_name'])
# print(storage['song_name'])
# print(storage['power'])
# print(storage['1'])




# print("storage", storage)

# print(dir(storage))

# print(storage.__dict__)



# a = "123456"
#
# print("a", a.isalnum())



# print(dir(string))
#
# print('ascii_letters', string.ascii_letters)
# print('ascii_lowercase', string.ascii_lowercase)
# print('ascii_uppercase', string.ascii_uppercase)
# print('capwords', string.capwords('1'))
# print('digits', string.digits)
# print('hexdigits', string.hexdigits)
# print('punctuation', string.punctuation)
# print('whitespace', string.whitespace)
# print(string.whitespace == "  ")
# for i in string.whitespace:
#     print(i)

"""
