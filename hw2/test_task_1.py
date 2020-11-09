import pytest

from hw2.task_1 import get_longest_diverse_words

with open("hw2/test_task_1_data.txt", "w") as test_data:
    test_data.write("aaaaa\n" "tabc\n" "abd fgthy abf ab.g wey fvs qhy zxc. hjy")


result = ["fgthy", "tabc", "abd", "abf", "abg", "wey", "fvs", "qhy", "zxc", "hjy"]


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    (("hw2/test_task_1_data.txt", result),),
)
def test_get_longest_diverse_words(file_name: str, expected_result: list):
    actual_result = get_longest_diverse_words(file_name)

    assert actual_result == expected_result
