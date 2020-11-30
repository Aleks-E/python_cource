"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""

from typing import List


def backspace_compare(first: str, second: str) -> bool:
    def text_processing(input_sequence: str) -> List[str]:
        list_of_symbols = []
        for symbol in input_sequence:
            if symbol == "#" and list_of_symbols:
                list_of_symbols.pop()
            if symbol != "#":
                list_of_symbols.append(symbol)
        return list_of_symbols

    return text_processing(first) == text_processing(second)
