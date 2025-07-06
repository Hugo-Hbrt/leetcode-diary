# Title: Min Stack
# Link: https://leetcode.com/problems/min-stack/
# Difficulty: Medium
# Tags: Stack
# Status: Solved
# Date: 2025-07-06

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min_val = self.min_val - pop

    def top(self) -> int:
        val = self.stack[-1]

        if val > 0:
            return val + self.min_val 
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val
        
