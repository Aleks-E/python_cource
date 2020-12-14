"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from typing import Callable, Optional


# def universal_file_counter(
#     dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
# ) -> int:
#     pass


def universal_file_counter(
    dir_path: str, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    checked_str = ""
    parts = 0
    for path_next in dir_path.rglob(f"*.{file_extension}"):
        parts += 1
        with open(path_next, "r") as data:
            while True:
                symbol = data.read(1)
                checked_str += symbol
                str_part = (
                    checked_str.split("\n")
                    if tokenizer is None
                    else tokenizer(checked_str)
                )

                if len(str_part) > 1:
                    checked_str = str_part[-1]
                    parts = parts + len(str_part) - 1

                if not symbol:
                    checked_str = ""
                    break

    return parts
