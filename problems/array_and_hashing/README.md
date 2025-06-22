# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Contains Duplicate | [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/) | Easy |
| Top k frequent elements | [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/) | Medium |
| Two Sum | [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/) | Easy |
| Valid Anagram | [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/) | Easy |
| Group anagrams | [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/) | Medium |

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
