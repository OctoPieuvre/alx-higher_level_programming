#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard
"""


import sys


def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def can_place(row, col, queens):
        return all(
            row != r and col != c and row + col != r + c and row - col != r - c
            for r, c in queens
        )

    def backtrack(queens):
        if len(queens) == n:
            print(sorted(queens))
        else:
            row = len(queens)
            for col in range(n):
                if can_place(row, col, queens):
                    backtrack(queens + [(row, col)])

    backtrack([])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solve_n_queens(n)
