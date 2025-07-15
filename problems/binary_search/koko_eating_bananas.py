# Title: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Tags: Binary Search, Array
# Status: Solved
# Date: 2025-07-15

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k: int) -> bool:
            return sum([ceil(n/k) for n in piles]) <= h
        
        l, r = 1, max(piles)

        while l <= r:
            m = (l+r)//2

            if canEatAll(m):
                r = m - 1
            else:
                l = m + 1
        
        return l