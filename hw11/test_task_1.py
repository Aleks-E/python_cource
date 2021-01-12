from hw11.task_1 import simplified_enum


def test_colors_enum():
    class ColorsEnum(metaclass=simplified_enum):
        __keys = ("RED", "BLUE")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
