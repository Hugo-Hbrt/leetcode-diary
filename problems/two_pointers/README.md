# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Valid Palindrome | [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/) | Easy |
| Two Sum II - Input Array Is Sorted | [https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium |

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
