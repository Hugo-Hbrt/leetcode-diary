# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Valid Palindrome | [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/) | Easy |

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
