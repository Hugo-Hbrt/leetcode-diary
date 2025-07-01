# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Valid Parentheses | [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/) | Easy |

## Valid Parentheses

```py

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding_opener = {
            ")": "(",
            "}" :"{",
            "]": "["
        }
        
        for c in s:
            if c in corresponding_opener.keys():
                if len(stack) < 1 or (stack.pop() != corresponding_opener[c]):
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

```
