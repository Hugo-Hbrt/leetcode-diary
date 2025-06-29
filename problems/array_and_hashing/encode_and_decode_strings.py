# Title: Encode and Decode Strings
# Link: https://leetcode.com/problems/encode-and-decode-strings/
# Difficulty: Medium
# Tags: array, string
# Status: Solved
# Date: 2025-06-22

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = ""
           
            for j in range(i, len(s)):
                c = s[j]
                if c == "#":
                    start = j+1
                    end = start+int(l)-1
                    res.append(s[start:end+1])
                    i = end+1
                    break
                else:
                    l += str(c)
        return res