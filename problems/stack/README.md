# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Largest Rectangle in Histogram | [https://leetcode.com/problems/largest-rectangle-in-histogram/](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard |
| Car Fleet | [https://leetcode.com/problems/car-fleet/](https://leetcode.com/problems/car-fleet/) | Medium |
| Evaluate Reverse Polish Notation | [https://leetcode.com/problems/evaluate-reverse-polish-notation/](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium |
| Valid Parentheses | [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/) | Easy |
| Daily Temperatures | [https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/) | Medium |
| Min Stack | [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/) | Medium |

## Largest Rectangle in Histogram

```py

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        
        for i,h in enumerate(heights):
            i_offset = i
            if len(stack) > 0: 
                while stack and stack[-1][1] > h:
                    (old_i, old_h) = stack.pop()
                    area = (i - old_i) * old_h
                    max_area = max(max_area, area)
                    i_offset = old_i
                
            stack.append((i_offset,h))
        
        n = len(heights)
        for (i, h) in stack:
            area = h * (n - i)
            max_area = max(max_area, area)
        
        return max_area
```

## Car Fleet

```py

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
```

## Evaluate Reverse Polish Notation

```py

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(str(int(eval(op1 + token + op2))))
            else:
                stack.append(token)
        
        return int(stack.pop())
```

## Valid Parentheses

```py

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding_opener = {
            ")": "(",
            "}" :"{",
            "]": "["
        }
        
        for c in s:
            if c in corresponding_opener.keys():
                if len(stack) < 1 or (stack.pop() != corresponding_opener[c]):
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

```

## Daily Temperatures

```py

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                oldTemp, oldIdx = stack.pop()
                result[oldIdx] = i - oldIdx
            stack.append((temp, i))            
        
        return result
            
```

## Min Stack

```py

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min_val = self.min_val - pop

    def top(self) -> int:
        val = self.stack[-1]

        if val > 0:
            return val + self.min_val 
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val
        

```
