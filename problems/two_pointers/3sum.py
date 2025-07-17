# Title: 3Sum
# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Tags: Array, Two Pointers
# Status: Solved
# Date: 2025-07-17

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def tripletsAreEqual(firstTriplet, secondTriplet):
            a1 = sorted(firstTriplet)
            a2 = sorted(secondTriplet)

            for i in range(3):
                if a1[i] != a2[i]:
                    return False 

            return True
        
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j<k:
                s = nums[j] + nums[k]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    alreadyInRes = False
                    for triplet in res:
                        alreadyInRes |= tripletsAreEqual(triplet, [nums[i], nums[j], nums[k]])
                    
                    if not alreadyInRes:
                        res.append([nums[i], nums[j], nums[k]])
                    j+=1
        return res