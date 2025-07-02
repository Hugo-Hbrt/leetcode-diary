# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Length of Last Word | [https://leetcode.com/problems/length-of-last-word/](https://leetcode.com/problems/length-of-last-word/) | Easy |

## Length of Last Word

```py

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)

        for i in range(l-1, -1, -1):
            if s[i] != " ":
                j = i
                while s[j-1] != " " and j > 0:
                    j -= 1
                return i - j + 1
```
