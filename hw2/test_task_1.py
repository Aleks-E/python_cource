from hw2.task_1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    count_punctuation_chars_alternative_1,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("aaaaa\n" "tabc\n" "abd fgthy abf ab.g wey fvs qhy zxc. hjy")
    expected_result = [
        "fgthy",
        "tabc",
        "abd",
        "abf",
        "abg",
        "wey",
        "fvs",
        "qhy",
        "zxc",
        "hjy",
    ]
    actual_result = get_longest_diverse_words("hw2/test_task_1_data.txt")
    assert actual_result == expected_result


def test_get_rarest_char():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("111222!333!444")
    expected_result = "!"
    actual_result = get_rarest_char("hw2/test_task_1_data.txt")
    assert actual_result == expected_result


def test_count_punctuation_chars():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("111222!333!444")
    expected_result = 2
    actual_result = count_punctuation_chars("hw2/test_task_1_data.txt")
    assert actual_result == expected_result


def test_count_punctuation_chars_alternative_1():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("111222!333!444")
    expected_result = 2
    actual_result = count_punctuation_chars_alternative_1("hw2/test_task_1_data.txt")
    assert actual_result == expected_result


def test_count_non_ascii_chars():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("111222\\u2014333\\u2014444")
    expected_result = 2
    actual_result = count_non_ascii_chars("hw2/test_task_1_data.txt")
    assert actual_result == expected_result


def test_get_most_common_non_ascii_char():
    with open("hw2/test_task_1_data.txt", "w") as test_data:
        test_data.write("111222\\u00bb333\\u00bbbbb\\u00df")
    expected_result = "»"
    actual_result = get_most_common_non_ascii_char("hw2/test_task_1_data.txt")
    assert actual_result == expected_result