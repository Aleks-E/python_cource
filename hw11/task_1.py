MyClass = type('MyClass', (object,), {'my_attribute': 0})
"""
'MyClass' - имя класса
(object,) - родители (может быть пустым)
{'my_attribute': 0} - словарь атрибутов (может быть пустым)
"""
# print(type(MyClass))        # <class 'type'>
# -------------------------------------

def my_class_init(self, attr_value):
    self.my_attribute = attr_value


MyClass = type('MyClass', (object,), {'__init__': my_class_init})
o = MyClass('test')
# print(o.my_attribute)       # test



# -------------------------------------
"""
Создание класса с методом
"""
def a1():
    return 22

A = type('A', (), {'a': a1})

# print(A.a())    # 22
# -------------------------------------


def func(self, attr):
    return attr ** 2

A = type('A', (), {'func': func})

a = A()

# print(a.func(9))       # 81
# -------------------------------------


class A:
    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def upper(self):
        my_list = []
        for i in self.__dict__:
            my_list.append(i)
        for i in my_list:
            setattr(self, i.upper(), self.__dict__[i])
            delattr(self, i)


a = A(22, 33)
# print(a.__dict__)     # {'attr_1': 22, 'attr_2': 33}
a.upper()
# print(a.__dict__)     # {'ATTR_1': 22, 'ATTR_2': 33}
# -------------------------------------


class A:
    def __init__(self):
        print("A.__init__")
        self.upper()

    def upper(self):
        my_list = []
        for i in self.__dict__:
            my_list.append(i)
        for i in my_list:
            setattr(self, i.upper(), self.__dict__[i])
            delattr(self, i)


class B(A):
    def __init__(self, attr_1):
        print("B.__init__")
        self.attr_1 = attr_1
        super().__init__()


# a = B(11)
# print(a.__dict__)
# -------------------------------------


class A:
    def __init__(self):
        self.keys = []
        self.set_attr()

    def set_attr(self):
        for i in self.__dict__:
            self.keys.append(self.__dict__[i])


class B(A):
    def __init__(self):
        self.attr_1 = 'attr_1'
        super().__init__()


a = B()

# print(a.__dict__)
# -------------------------------------


def my_class_init(self):
    print("self")



MyClass = type('MyClass', (), {'__init__': my_class_init})


class NewClass(MyClass):
    ...


# a = NewClass()
# -------------------------------------


def my_metaclass(name, parents, attributes):
    return 'Hello'


class C(metaclass=my_metaclass):
    ...


# print(C)            # Hello
# print(type(C))      # <class 'str'>
# -------------------------------------


def my_metaclass(name, parents, attributes):
    for attr in attributes:
        print(attr)


# class C(metaclass=my_metaclass):
#     attr_1 = 1

# -------------------------------------

def SimplifiedEnum(name, parents, attributes):
    keys = []
    for attr in attributes:
        if not attr.startswith("_"):
            keys.append(attributes[attr])

    # print('name', name)
    # print('parents', parents)
    # print('attributes', attributes)

    return type(name, parents, attributes | {'__keys': tuple(keys)})



class ColorsEnum(metaclass=SimplifiedEnum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(metaclass=SimplifiedEnum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"



# print(C.__dict__)

# print(dir(C))

# print(type(ColorsEnum))


print(ColorsEnum.__keys)
print(ColorsEnum.RED)

print(SizesEnum.__keys)
print(SizesEnum.XL)

assert ColorsEnum.RED == "RED"

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"



# assert ColorsEnum.RED == "RED"      # AssertionError

# print(ColorsEnum.RED)











