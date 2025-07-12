# Title: Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty: Easy
# Tags: Binary Search
# Status: Solved
# Date: 2025-07-12

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2

            if guess(m) < 0:
                r = m - 1
            elif guess(m) > 0:
                l = m + 1
            else:
                return m
