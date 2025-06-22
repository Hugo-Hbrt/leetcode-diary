# Title: Top k frequent elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Tags: Array, Hashing
# Status: Solved
# Date: 2025-06-22

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequencies = [[] for i in range(n+1)]
        count = dict()
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            frequencies[cnt].append(num)

        most_frequent_nums = []
        for i in range(len(frequencies)-1, 0, -1):
            for num in frequencies[i]:
                most_frequent_nums.append(num)
                if len(most_frequent_nums) == k: 
                    return most_frequent_nums