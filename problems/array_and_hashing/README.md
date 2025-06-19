# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Contains Duplicate | [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/) | Easy |
| Two Sum | [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/) | Easy |
| Valid Anagram | [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/) | Easy |

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

## Two Sum

```py

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

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
