import unittest
import numpy as np
from collections import defaultdict
import math

from validate import validate

class TestValidateFunction(unittest.TestCase):

    def test_valid_sudoku(self):
        board = np.array([
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ])
        self.assertTrue(validate(board))

    def test_invalid_row_duplicate(self):
        board = np.array([
            [5,3,1,0,7,0,0,0,0],  # Duplicate 5 in row
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,5,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ])
        self.assertFalse(validate(board))

    def test_invalid_col_duplicate(self):
        board = np.array([
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [2,9,8,0,0,0,0,6,0],  # Duplicate 5 in column
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [5,0,0,0,8,0,0,7,9]
        ])
        self.assertFalse(validate(board))

    def test_invalid_square_duplicate(self):
        board = np.array([
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,5,0,0,0,0,6,0],  # Duplicate 5 in top-left square
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ])
        self.assertFalse(validate(board))

    def test_empty_board(self):
        board = np.zeros((9, 9), dtype=int)
        self.assertTrue(validate(board))

    def test_filled_valid_board(self):
        # This is a valid, complete Sudoku solution
        board = np.array([
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ])
        self.assertTrue(validate(board))


if __name__ == '__main__':
    unittest.main()
