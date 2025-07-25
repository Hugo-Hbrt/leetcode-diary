# Title: First Bad Version
# Link: https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy
# Tags: Binary Search
# Status: Solved
# Date: 2025-07-12

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l+r)//2

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        
        return l