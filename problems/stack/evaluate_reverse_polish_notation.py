# Title: Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium
# Tags: Stack
# Status: Solved
# Date: 2025-07-07

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(str(int(eval(op1 + token + op2))))
            else:
                stack.append(token)
        
        return int(stack.pop())