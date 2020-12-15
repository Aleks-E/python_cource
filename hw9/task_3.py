"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

# def universal_file_counter(
#     dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
# ) -> int:
#     pass
"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    checked_str = ""
    parts_counter = 0
    for path_next in dir_path.rglob(f"*.{file_extension}"):
        parts_counter += 1
        with open(str(path_next), "r") as data:
            for line in data:
                checked_str += line

                str_part = (
                    checked_str.split("\n")
                    if tokenizer is None
                    else tokenizer(checked_str)
                )

                if len(str_part) > 1:
                    checked_str = str_part[-1]
                    parts_counter = parts_counter + len(str_part) - 1

    return parts_counter
