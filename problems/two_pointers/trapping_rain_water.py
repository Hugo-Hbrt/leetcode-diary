# Title: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
# Tags: Array, Two Pointers
# Status: Solved
# Date: 2025-07-18

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
       
        res = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        
        while l <= r:
            if max_left < max_right:
                max_left = max(height[l], max_left)
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(height[r], max_right)
                res += max_right - height[r]
                r -= 1
        
        return res