# Title: Container with most water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Tags: two-pointers, array
# Status: Solved
# Date: 2025-07-18

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
