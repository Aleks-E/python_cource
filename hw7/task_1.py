"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    ...


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6



def find_occurrences(tree: dict, element: Any) -> int:
    tree_temp = list(tree.values())
    tree_new = []
    count_occurrences = 0
    while tree_temp:
        for item in tree_temp:
            if isinstance(item, list):
                tree_new.extend(item)
            if isinstance(item, dict):
                tree_new.append(list(item.values()))
            if item == element:
                count_occurrences += 1
        tree_temp = tree_new
        tree_new = []
    return count_occurrences





print(find_occurrences(example_tree, "RED"))
print(find_occurrences(example_tree, "simple"))
print(find_occurrences(example_tree, "of"))

