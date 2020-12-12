from hw7.task_1 import find_occurrences

import pytest


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    # fmt: off
    [({}, 0),

     ({"1": [],
       "2": {},
       "3": set(),
       "4": ()}, 0),

     ({"1": [{}, [], set(), ()],
       "2": {"1": {}, "2": [], "3": set(), "4": ()}}, 0)],
    # fmt: on
)
def test_tree_with_empty_values(tree, expected_result):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    [
        (
            {
                "1": [{"1": "blue"}, ["blue"], {"blue"}, ("blue",), "blue"],
                "2": {
                    "1": {"1": "blue"},
                    "2": ["blue"],
                    "3": {"blue"},
                    "4": ("blue",),
                    "5": "blue",
                },
                "3": {("blue",), "blue"},
                "4": ({"1": "blue"}, ["blue"], {"blue"}, ("blue",), "blue"),
                "5": "blue",
            },
            0,
        )
    ],
)
def test_mismatching_tree_value_and_required_value(tree, expected_result):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    [
        ({"1": "blue", "2": "red"}, 1),
        ({"1": ["blue", "red"]}, 1),
        ({"1": [["blue", "red"]]}, 1),
        ({"1": [{"1": "blue", "2": "red"}]}, 1),
        ({"1": [{"blue", "red"}]}, 1),
        ({"1": [("blue", "red")]}, 1),
        ({"1": {"1": ["blue", "red"]}}, 1),
        ({"1": {"1": ("blue", "red")}}, 1),
        ({"1": {"1": {"blue", "red"}}}, 1),
        ({"1": {"1": {"1": "blue", "2": "red"}}}, 1),
        ({"1": ("blue", "red")}, 1),
        ({"1": ({"1": "blue", "2": "red"})}, 1),
        ({"1": (("blue", "red"),)}, 1),
        ({"1": {"blue", "red"}}, 1),
        ({"1": {("blue", "red")}}, 1),
    ],
)
def test_the_correctness_of_the_work_of_finding_the_required_value_with_other_values_in_the_tree(
    tree, expected_result
):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    [
        ({"1": "red", "2": "red"}, 2),
        ({"1": ["red", "red"]}, 2),
        ({"1": [["red", "red"]]}, 2),
        ({"1": [("red", "red")]}, 2),
        ({"1": {"1": "red", "2": "red"}}, 2),
        ({"1": {"1": ["red", "red"]}}, 2),
        ({"1": {"1": {"1": "red", "2": "red"}}}, 2),
        ({"1": {"1": ("red", "red")}}, 2),
        ({"1": ("red", "red")}, 2),
        ({"1": {("red", "red")}}, 2),
    ],
)
def test_the_required_value_is_repeated_more_than_once_in_a_definite_branch_of_the_tree(
    tree, expected_result
):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result


def test_count_occurences():
    tree = {
        "1": "red",
        "2": ["red", ["red"], {"1": "red"}, ("red",), {"red"}],
        "3": {"1": "red", "2": ["red"], "3": {"1": "red"}, "4": ("red",), "5": {"red"}},
        "4": ("red", ["red"], {"1": "red"}, ("red",), {"red"}),
        "5": {"red", ("red",)},
    }
    actual_result = find_occurrences(tree, "red")
    assert actual_result == 18
