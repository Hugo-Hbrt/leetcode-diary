# Title: Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Tags: string
# Status: Solved
# Date: 2025-07-02

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)

        for i in range(l-1, -1, -1):
            if s[i] != " ":
                j = i
                while s[j-1] != " " and j > 0:
                    j -= 1
                return i - j + 1