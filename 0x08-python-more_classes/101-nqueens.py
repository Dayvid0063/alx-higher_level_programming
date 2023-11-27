#!/usr/bin/python3
"""program that solves the N queens problem"""

import sys


def init_board(n):
    """Initialize n chessboard"""
    board = []
    [board.append([]) for u in range(n)]
    [row.append(' ') for u in range(n) for row in board]
    return board


def board_deepcopy(board):
    """Return a deepcopy"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Return the solution list"""
    solution = []
    for m in range(len(board)):
        for n in range(len(board)):
            if board[m][n] == "Q":
                solution.append([m, n])
                break
    return solution


def xout(board, row, col):
    """xout positions on a chessboard"""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively fix an N-queens"""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for n in range(len(board)):
        if board[row][n] == " ":
            tmp_solution = board_deepcopy(board)
            tmp_solution[row][n] = "Q"
            xout(tmp_solution, row, n)
            solutions = recursive_solve(tmp_solution, row + 1,
                                        queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
