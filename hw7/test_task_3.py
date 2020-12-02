from hw7.task_3 import tic_tac_toe_checker

import pytest


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["x", "x", "x"],
          ["o", "o", "x"],
          ["o", "o", "-"]], "x wins!"),

        ([["o", "o", "-"],
          ["x", "x", "x"],
          ["-", "-", "o"]], "x wins!"),

        ([["o", "o", "-"],
          ["x", "x", "x"],
          ["-", "-", "-"]], "x wins!"),

        ([["x", "o", "-"],
          ["x", "x", "x"],
          ["o", "o", "-"]], "x wins!"),
    ],
    # fmt: on
)
def test_winner_in_a_horizontal_row(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["x", "o", "o"],
          ["x", "o", "o"],
          ["x", "x", "-"]], "x wins!"),

        ([["o", "x", "-"],
          ["o", "x", "-"],
          ["-", "x", "o"]], "x wins!"),

        ([["o", "x", "-"],
          ["o", "x", "-"],
          ["-", "x", "-"]], "x wins!"),

        ([["x", "x", "o"],
          ["o", "x", "o"],
          ["-", "x", "-"]], "x wins!"),
    ],
    # fmt: on
)
def test_winner_in_a_vertical_row(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["x", "o", "-"],
          ["o", "x", "-"],
          ["o", "o", "x"]], "x wins!"),

        ([["x", "x", "-"],
          ["o", "x", "-"],
          ["o", "o", "x"]], "x wins!"),

        ([["o", "o", "x"],
          ["o", "x", "-"],
          ["x", "o", "-"]], "x wins!"),

        ([["o", "o", "x"],
          ["o", "x", "-"],
          ["x", "x", "-"]], "x wins!"),
    ],
    # fmt: on
)
def test_winner_in_a_diagonal_row(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["x", "x", "x"],
          ["o", "-", "-"],
          ["o", "o", "-"]], "x wins!"),

        ([["o", "o", "o"],
          ["x", "-", "-"],
          ["x", "x", "-"]], "o wins!"),
    ],
    # fmt: on
)
def test_results_with_different_winners(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]], "unfinished!"),

        ([["x", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]], "unfinished!"),

        ([["x", "o", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]], "unfinished!"),

        ([["x", "o", "-"],
          ["x", "-", "-"],
          ["-", "-", "-"]], "unfinished!"),

        ([["x", "o", "-"],
          ["x", "-", "-"],
          ["o", "-", "-"]], "unfinished!"),
    ],
    # fmt: on
)
def test_unfinished_board(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    # fmt: off
    ("board", "expected_result"),
    [
        ([["x", "o", "o"],
          ["o", "x", "x"],
          ["x", "-", "o"]], "draw!"),

        ([["x", "o", "o"],
          ["o", "x", "x"],
          ["x", "x", "o"]], "draw!"),
    ],
    # fmt: on
)
def test_draw(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result
