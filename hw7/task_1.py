"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

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
"""

from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    tree_temp = list(tree.values())
    count_occurrences = 0
    while tree_temp:
        tree_new = []
        for item in tree_temp:
            if isinstance(item, (list, set, tuple)):
                tree_new.extend(item)
            elif isinstance(item, dict):
                tree_new.extend(list(item.values()))
            elif item == element:
                count_occurrences += 1
        tree_temp = tree_new
    return count_occurrences