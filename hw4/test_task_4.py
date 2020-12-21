from hw4.task_4 import fizzbuzz

import pytest


@pytest.mark.parametrize(
    "ordinal_number",
    [
        3,
        6,
        9,
        12,
        18,
        21,
        24,
        27,
    ],
)
def test_function_returns_fizz_every_third_item_except_for_every_fifteenth_item(
    ordinal_number,
):
    assert fizzbuzz(100)[ordinal_number - 1] == "Fizz"


@pytest.mark.parametrize(
    "ordinal_number",
    [
        5,
        10,
        20,
        25,
    ],
)
def test_function_returns_buzz_every_fifth_item_except_for_every_fifteenth_item(
    ordinal_number,
):
    assert fizzbuzz(100)[ordinal_number - 1] == "Buzz"


@pytest.mark.parametrize(
    "ordinal_number",
    [
        15,
        30,
        45,
    ],
)
def test_function_returns_fizzbuzz_every_fifteenth_item(ordinal_number):
    assert fizzbuzz(100)[ordinal_number - 1] == "FizzBuzz"


@pytest.mark.parametrize(
    "ordinal_number",
    [
        1,
        2,
        4,
        7,
        8,
        11,
        13,
        14,
    ],
)
def test_function_returns_the_ordinal_number_of_item_whose_ordinal_number_is_not_a_multiple_of_three_and_five(
    ordinal_number,
):
    assert fizzbuzz(100)[ordinal_number - 1] == str(ordinal_number)
