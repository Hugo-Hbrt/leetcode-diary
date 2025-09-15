# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Search a 2D Matrix | [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/) | Medium |
| Koko Eating Bananas | [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/) | Medium |
| Guess Number Higher or Lower | [https://leetcode.com/problems/guess-number-higher-or-lower/](https://leetcode.com/problems/guess-number-higher-or-lower/) | Easy |
| Binary Search | [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/) | Easy |
| First Bad Version | [https://leetcode.com/problems/first-bad-version/](https://leetcode.com/problems/first-bad-version/) | Easy |

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

## Koko Eating Bananas

```py

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k: int) -> bool:
            return sum([ceil(n/k) for n in piles]) <= h
        
        l, r = 1, max(piles)

        while l <= r:
            m = (l+r)//2

            if canEatAll(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
```

## Guess Number Higher or Lower

```py

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2

            if guess(m) < 0:
                r = m - 1
            elif guess(m) > 0:
                l = m + 1
            else:
                return m

```

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

## First Bad Version

```py

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l+r)//2

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
```
