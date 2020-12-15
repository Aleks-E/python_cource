from contextlib import contextmanager
from typing import Iterator, TypeVar

from hw9.task_2 import SuppressorClass, suppressor_gen

import pytest

ExceptionType = TypeVar("ExceptionType")
Expectation = TypeVar("Expectation")


@contextmanager
def does_not_raise() -> Iterator:
    yield


@pytest.mark.parametrize(
    ("exception_type", "expectation"),
    [
        (IndexError, does_not_raise()),
        (AttributeError, pytest.raises(IndexError)),
        (NameError, pytest.raises(IndexError)),
    ],
)
def test_suppressor_class_catch_index_error_exception(
    exception_type: ExceptionType, expectation: Expectation
) -> None:
    with expectation:
        with SuppressorClass(exception_type):
            [][2]


@pytest.mark.parametrize(
    ("exception_type", "expectation"),
    [
        (NameError, does_not_raise()),
        (AttributeError, pytest.raises(NameError)),
        (IndexError, pytest.raises(NameError)),
    ],
)
def test_suppressor_class_catch_name_error_exception(
    exception_type: ExceptionType, expectation: Expectation
) -> None:
    with expectation:
        with SuppressorClass(exception_type):
            a - 1


@pytest.mark.parametrize(
    ("exception_type", "expectation"),
    [
        (IndexError, does_not_raise()),
        (AttributeError, pytest.raises(IndexError)),
        (NameError, pytest.raises(IndexError)),
    ],
)
def test_suppressor_gen_catch_index_error_exception(
    exception_type: ExceptionType, expectation: Expectation
) -> None:
    with expectation:
        with suppressor_gen(exception_type):
            [][2]


@pytest.mark.parametrize(
    ("exception_type", "expectation"),
    [
        (NameError, does_not_raise()),
        (AttributeError, pytest.raises(NameError)),
        (IndexError, pytest.raises(NameError)),
    ],
)
def test_suppressor_gen_catch_name_error_exception(
    exception_type: ExceptionType, expectation: Expectation
) -> None:
    with expectation:
        with suppressor_gen(exception_type):
            a - 1
