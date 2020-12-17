from contextlib import contextmanager

from hw9.task_2 import SuppressorClass, suppressor_gen

import pytest


@contextmanager
def does_not_raise():
    yield


def test_suppressor_class_catch_index_error_when_catch_index_error_is_required():
    with does_not_raise():
        with SuppressorClass(IndexError):
            [][2]


def test_suppressor_class_raises_index_error_when_catch_attribute_error_is_required():
    with pytest.raises(IndexError):
        with SuppressorClass(AttributeError):
            [][2]


def test_suppressor_class_raises_index_error_when_catch_name_error_is_required():
    with pytest.raises(IndexError):
        with SuppressorClass(NameError):
            [][2]


def test_suppressor_class_catch_name_error_when_catch_name_error_is_required():
    with does_not_raise():
        with SuppressorClass(NameError):
            a - 1


def test_suppressor_class_raises_name_error_when_catch_attribute_error_is_required():
    with pytest.raises(NameError):
        with SuppressorClass(AttributeError):
            a - 1


def test_suppressor_class_raises_name_error_when_catch_index_error_is_required():
    with pytest.raises(NameError):
        with SuppressorClass(IndexError):
            a - 1


def test_suppressor_gen_catch_index_error_when_catch_index_error_is_required():
    with does_not_raise():
        with suppressor_gen(IndexError):
            [][2]


def test_suppressor_gen_raises_index_error_when_catch_attribute_error_is_required():
    with pytest.raises(IndexError):
        with suppressor_gen(AttributeError):
            [][2]


def test_suppressor_gen_raises_index_error_when_catch_name_error_is_required():
    with pytest.raises(IndexError):
        with suppressor_gen(NameError):
            [][2]


def test_suppressor_gen_catch_name_error_when_catch_name_error_is_required():
    with does_not_raise():
        with suppressor_gen(NameError):
            a - 1


def test_suppressor_gen_raises_name_error_when_catch_attribute_error_is_required():
    with pytest.raises(NameError):
        with suppressor_gen(AttributeError):
            a - 1


def test_suppressor_gen_raises_name_error_when_catch_index_error_is_required():
    with pytest.raises(NameError):
        with suppressor_gen(IndexError):
            a - 1
