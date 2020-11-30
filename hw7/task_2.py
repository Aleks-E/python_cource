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
