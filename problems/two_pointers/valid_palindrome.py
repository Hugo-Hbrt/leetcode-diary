# Title: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Tags: two-pointers, string
# Status: Solved
# Date: 2025-06-30

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        left, right = 0, len(s) - 1

        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1

        return True