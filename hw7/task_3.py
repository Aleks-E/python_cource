"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(input_board: List[List]) -> str:
    row_results = []

    def row_checker(checking_row: list) -> str:
        if len(set(checking_row)) == 1 and "-" not in checking_row:
            return "win"
        elif len(set(checking_row)) in (1, 2) and "-" in checking_row:
            return "row_unfinished"
        return "row_finished"

    horizontal_rows = input_board

    vertical_rows = list(zip(*input_board))

    diagonal_row_left_top = [input_board[i][i] for i in range(len(input_board))]

    board_reversed = list(reversed(input_board))
    diagonal_row_left_down = [board_reversed[i][i] for i in range(len(input_board))]

    rows = [
        *horizontal_rows,
        *vertical_rows,
        diagonal_row_left_top,
        diagonal_row_left_down,
    ]
    for row in rows:
        result_of_the_row = row_checker(row)
        if result_of_the_row == "win":
            return row[0] + " " + "wins!"
        row_results.append(result_of_the_row)

    return "unfinished!" if "row_unfinished" in row_results else "draw!"
