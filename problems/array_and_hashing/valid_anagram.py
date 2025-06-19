# Title: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Tags: array, hash-table, string
# Status: Solved
# Date: 2025-06-19

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstCollection = dict()
        secondCollection = dict()
        
        for c in s:
            firstCollection[c] = firstCollection.get(c, 0) + 1
        
        for c in t:
            secondCollection[c] = secondCollection.get(c, 0) + 1
        
        return firstCollection == secondCollection