#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, N):
    """
    Solve the N Queens problem using backtracking.
    """
    # Base case: If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1, N)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0

    return False


def print_solution(board):
    """
    Print the board configuration as a list of coordinates.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
