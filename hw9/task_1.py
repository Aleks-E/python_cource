"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from typing import Iterator, List


def merge_sorted_files(file_list: List) -> Iterator:
    def get_number(file_path: str) -> Iterator:
        with open(file_path) as text:
            for line in text:
                yield line.rstrip()

    number_iter_1 = iter(get_number(file_list[0]))
    number_iter_2 = iter(get_number(file_list[1]))

    number_1, number_2 = None, None
    while True:
        if number_1 is None:
            try:
                number_1 = next(number_iter_1)
            except StopIteration:
                ...

        if number_2 is None:
            try:
                number_2 = next(number_iter_2)
            except StopIteration:
                ...

        if number_1 is not None and number_2 is not None:
            if number_1 <= number_2:
                result_number, number_1 = number_1, None
                yield int(result_number)
            else:
                result_number, number_2 = number_2, None
                yield int(result_number)

        elif number_1 is None and number_2 is not None:
            result_number, number_2 = number_2, None
            yield int(result_number)

        elif number_2 is None and number_1 is not None:
            result_number, number_1 = number_1, None
            yield int(result_number)

        elif number_1 is None and number_2 is None:
            break
