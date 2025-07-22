# Title: Largest Rectangle in Histogram
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Difficulty: Hard
# Tags: Stack, Array, Monotonic Stack
# Status: Solved
# Date: 2025-07-22

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        
        # First pass
        for i,h in enumerate(heights):
            i_offset = i
            if len(stack) > 0: 
                while stack and stack[-1][1] > h:
                    (old_i, old_h) = stack.pop()
                    area = (i - old_i) * old_h
                    max_area = max(max_area, area)
                    i_offset = old_i
                
            stack.append((i_offset,h))
        
        # Compute areas with remaining element in stack
        # Those element could reach the end of the histogram
        n = len(heights)
        for (i, h) in stack:
            area = h * (n - i)
            max_area = max(max_area, area)
        
        return max_area