# Title: Car Fleet
# Link: https://leetcode.com/problems/car-fleet/
# Difficulty: Medium
# Tags: Stack
# Status: Solved
# Date: 2025-07-19

from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        speed = [s for _, s in sorted(zip(position, speed))]
        position = sorted(position)

        steps = [((target - p)/s) for p, s in zip(position, speed)]
        stack = []
        stack.append(steps[0])

        for step in steps[1:]:
            while stack and step >= stack[-1]:
                stack.pop()        
            stack.append(step)
        
        return len(stack)