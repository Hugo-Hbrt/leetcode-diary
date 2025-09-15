# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Longest Consecutive Sequence | [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium |
| Valid Sudoku | [https://leetcode.com/problems/valid-sudoku/](https://leetcode.com/problems/valid-sudoku/) | Medium |
| Contains Duplicate | [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/) | Easy |
| Encode and Decode Strings | [https://leetcode.com/problems/encode-and-decode-strings/](https://leetcode.com/problems/encode-and-decode-strings/) | Medium |
| Two Sum | [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/) | Easy |
| Top k frequent elements | [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/) | Medium |
| Merge intervals | [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/) | Medium |
| Group anagrams | [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/) | Medium |
| Valid Anagram | [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/) | Easy |

## Longest Consecutive Sequence

```py

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if not (num - 1) in numSet:
                next_num = num + 1
                sequence_length = 1
                while next_num in numSet:
                    sequence_length += 1
                    next_num += 1
                longest = max(sequence_length, longest)

        return longest
```

## Valid Sudoku

```py
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                square_id = ((j//3)+1) + (i//3)*3
                val = board[i][j]
                
                if val == ".":
                    continue

                if (val in rows[i]) or (val in columns[j]) or (val in squares[square_id]):
                    return False
                rows[i].add(val)
                columns[j].add(val)
                squares[square_id].add(val)
        
        return True
```

## Contains Duplicate

```py

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenIntegers = set()
        for num in nums:
            if num in seenIntegers:
                return True
            seenIntegers.add(num)
        
        return False
```

## Encode and Decode Strings

```py

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
```

## Two Sum

```py

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

```

## Top k frequent elements

```py

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
```

## Merge intervals

```py

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

```

## Group anagrams

```py

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dictionnary = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams_dictionnary[tuple(count)].append(s)       
        return [v for k,v in anagrams_dictionnary.items()]



```

## Valid Anagram

```py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstCollection = dict()
        secondCollection = dict()
        
        for c in s:
            firstCollection[c] = firstCollection.get(c, 0) + 1
        
        for c in t:
            secondCollection[c] = secondCollection.get(c, 0) + 1
        
        return firstCollection == secondCollection
```
