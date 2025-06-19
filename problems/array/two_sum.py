# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Map
# Status: Solved ✅

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
