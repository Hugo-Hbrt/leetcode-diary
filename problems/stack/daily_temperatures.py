# Title: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Tags: Stack, Array
# Status: Solved
# Date: 2025-07-16

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                oldTemp, oldIdx = stack.pop()
                result[oldIdx] = i - oldIdx
            stack.append((temp, i))            
        
        return result
            