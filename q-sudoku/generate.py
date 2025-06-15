import numpy as np
from typing import Tuple

def create_sudoku_puzzle(n) -> Tuple[np.array, np.array]:
    """
    Generates a solvable n^2 x n^2 Sudoku puzzle and its solution.
    returns puzzle,solution being both np arrays
    """
    if n == 2:
        # A known valid, solved 4x4 board
        solution = np.array([
            [2, 1, 4, 3],
            [4, 3, 1, 2],
            [1, 2, 3, 4],
            [3, 4, 2, 1]
        ])
        # A corresponding puzzle with some numbers removed (represented by 0)
        puzzle = np.array([
            [0, 0, 4, 0],
            [0, 3, 0, 0],
            [0, 2, 0, 4],
            [3, 0, 0, 0]
        ])
        return puzzle, solution

    elif n == 3:   
        solution = np.array([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ])

        puzzle = np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        return puzzle, solution
    else:
        raise ValueError("This function only supports n=2 (4x4) or n=3 (9x9).")


if __name__ == '__main__':
    #  Generate and Save  Puzzles 
    n_4x4 = 2
    puzzle_4x4, solution_4x4 = create_sudoku_puzzle(n_4x4)
    np.savetxt("puzzle_4x4.txt", puzzle_4x4, fmt='%d')
    np.savetxt("solution_4x4.txt", solution_4x4, fmt='%d')
    print("Generated and saved 'puzzle_4x4.txt' and 'solution_4x4.txt'")
    print("4x4 Puzzle:\n", puzzle_4x4)

    n_9x9 = 3
    puzzle_9x9, solution_9x9 = create_sudoku_puzzle(n_9x9)
    np.savetxt("puzzle_9x9.txt", puzzle_9x9, fmt='%d')
    np.savetxt("solution_9x9.txt", solution_9x9, fmt='%d')
    print("Generated and saved 'puzzle_9x9.txt' and 'solution_9x9.txt'")
    print("9x9 Puzzle:\n", puzzle_9x9)
