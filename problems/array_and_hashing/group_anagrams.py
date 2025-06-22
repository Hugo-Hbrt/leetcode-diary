# Title: Group anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Tags: array, hash-table
# Status: Solved
# Date: 2025-06-21

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dictionnary = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams_dictionnary[tuple(count)].append(s)       
        return [v for k,v in anagrams_dictionnary.items()]


