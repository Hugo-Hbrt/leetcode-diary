# Title: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Tags: array, hash-table
# Status: Solved
# Date: 2025-07-01

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if not (num - 1) in numSet:
                # Can be start of a sequence
                next_num = num + 1
                sequence_length = 1
                while next_num in numSet:
                    sequence_length += 1
                    next_num += 1
                longest = max(sequence_length, longest)

        return longest