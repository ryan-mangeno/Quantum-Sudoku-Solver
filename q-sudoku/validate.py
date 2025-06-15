import numpy 
import math 

from collections import defaultdict
import unittest 

def validate(board : numpy.array) -> bool:
    
    n = board.shape[0]
    sqrt_n = int(math.sqrt(n))
    
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num != 0:
                # current square 
                sq_idx = (i//sqrt_n) * sqrt_n + j//sqrt_n 
                
                if num in rows[i] or num in cols[j] or num in squares[sq_idx]:
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[sq_idx].add(num)
    return True

