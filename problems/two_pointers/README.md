# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Valid Palindrome | [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/) | Easy |
| 3Sum | [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/) | Medium |
| Two Sum II - Input Array Is Sorted | [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium |
| Container with most water | [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/) | Medium |
| Trapping Rain Water | [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/) | Hard |

## Valid Palindrome

```py

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        left, right = 0, len(s) - 1

        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1

        return True
```

## 3Sum

```py

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def tripletsAreEqual(firstTriplet, secondTriplet):
            a1 = sorted(firstTriplet)
            a2 = sorted(secondTriplet)

            for i in range(3):
                if a1[i] != a2[i]:
                    return False 

            return True
        
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j<k:
                s = nums[j] + nums[k]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    alreadyInRes = False
                    for triplet in res:
                        alreadyInRes |= tripletsAreEqual(triplet, [nums[i], nums[j], nums[k]])
                    
                    if not alreadyInRes:
                        res.append([nums[i], nums[j], nums[k]])
                    j+=1
        return res
```

## Two Sum II - Input Array Is Sorted

```py

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]
        

```

## Container with most water

```py

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        max_area = 0
        l, r = 0, n

        while l < r:
            max_area = max(min(heights[l], heights[r]) * (r-l), max_area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return max_area

```

## Trapping Rain Water

```py

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
       
        res = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        
        while l <= r:
            if max_left < max_right:
                max_left = max(height[l], max_left)
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(height[r], max_right)
                res += max_right - height[r]
                r -= 1
        
        return res
```
