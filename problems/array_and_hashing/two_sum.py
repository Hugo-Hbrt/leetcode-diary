# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: array, hash-table
# Status: Solved
# Date: 2025-06-19

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
