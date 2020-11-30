from hw7.task_1 import find_occurrences
import pytest


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    [({}, 0), ({"1": [], "2": {}}, 0), ({"1": [{}, []], "2": {"1": {}, "2": []}}, 0)],
)
def test_tree_with_empty_values(tree, expected_result):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result


def test_mismatching_tree_item_and_required_item():
    tree = {
        "1": [{"1": "blue"}, ["blue"], "blue"],
        "2": {"1": {"1": "blue"}, "2": ["blue"], "3": "blue"},
    }
    actual_result = find_occurrences(tree, "red")
    assert actual_result == 0


@pytest.mark.parametrize(
    ("tree", "expected_result"),
    ({"1": "red"}, 1),
)
def test_matching_tree_item_and_required_item(tree, expected_result):
    actual_result = find_occurrences(tree, "red")
    assert actual_result == expected_result





# def test_finding_item_in_the_top_level_of_the_tree():
#     tree = {"1": [], "2": {}, "3": "red"}
#     actual_result = find_occurrences(tree, "red")
#     assert actual_result == 1
#
#
# def test_finding_item_in_the_nested_level_of_the_tree():
#     tree = {"1": ["red"]}
#     actual_result = find_occurrences(tree, "red")
#     assert actual_result == 1


"""
1 empty tree
2 empty values with nested empty values
3 mismatching item
4 matching item in the root of the tree
5 matching item in the list values
6 matching item in the dict values
7 matching nested item in the dict values



"""
