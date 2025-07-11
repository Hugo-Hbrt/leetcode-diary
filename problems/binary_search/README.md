# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Binary Search | [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/) | Easy |
| Search a 2D Matrix | [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/) | Medium |

## Binary Search

```py

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1 
```

## Search a 2D Matrix

```py

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

       
```
