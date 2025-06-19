# Title: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Tags: array, hash-table
# Status: Solved
# Date: 2025-06-19

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenIntegers = set()
        for num in nums:
            if num in seenIntegers:
                return True
            seenIntegers.add(num)
        
        return False