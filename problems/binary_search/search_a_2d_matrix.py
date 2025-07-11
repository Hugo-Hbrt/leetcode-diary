# Title: Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium
# Tags: Binary Search, Matrix
# Status: Solved
# Date: 2025-07-11

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS, ROWS = len(matrix[0]) , len(matrix) 
        
        l, r = 0, ROWS * COLS - 1
        
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // COLS, mid % COLS
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        
        return False

       