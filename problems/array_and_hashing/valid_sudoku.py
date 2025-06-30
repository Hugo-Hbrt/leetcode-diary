# Title: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium
# Tags: array, hash-table
# Status: Solved
# Date: 2025-06-30
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                square_id = ((j//3)+1) + (i//3)*3
                val = board[i][j]
                
                if val == ".":
                    continue

                if (val in rows[i]) or (val in columns[j]) or (val in squares[square_id]):
                    return False
                rows[i].add(val)
                columns[j].add(val)
                squares[square_id].add(val)
        
        return True