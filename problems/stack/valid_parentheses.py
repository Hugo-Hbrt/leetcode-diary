# Title: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Tags: stack
# Status: Solved
# Date: 2025-07-01

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
