# Title: Merge intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium
# Tags: Array, Sorting
# Status: Solved
# Date: 2025-09-15

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        merged = []
        prev = sorted_intervals[0]

        for interval in sorted_intervals[1::]:
            [start, end] = interval
            [prev_start, prev_end] = prev
            
            if (prev_end >= start):
                new_interval = [prev_start, max(end, prev_end)]
                prev = new_interval
            else:
                merged.append(prev)
                prev = [start, end]
        merged.append(prev)

        return merged
