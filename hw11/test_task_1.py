from hw11.task_1 import simplified_enum

import pytest


@pytest.fixture()
def colors_enum():
    class ColorsEnum(metaclass=simplified_enum):
        RED = "RED"
        BLUE = "BLUE"

    return ColorsEnum


def test_new_class_attributes(colors_enum):
    assert colors_enum.RED == "RED"
    assert colors_enum.BLUE == "BLUE"
