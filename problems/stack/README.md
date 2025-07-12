# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Evaluate Reverse Polish Notation | [https://leetcode.com/problems/evaluate-reverse-polish-notation/](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium |
| Valid Parentheses | [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/) | Easy |
| Min Stack | [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/) | Medium |

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
