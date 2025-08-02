# Evaluate Reverse Polish Notation

## Problem Statement
MEDIUM

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

### Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

## My Solution Journey

Approach 1: Stack
My best approach is to have a stacks to track the values as they appear and popping them when needed to perform an operation and pushing the result to the stack
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif t == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif t == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            elif t == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(t))
            print(stack)

        return stack.pop()
```
Time & Space Complexity
- Time complexity: O(n)
- - We loop through the list once
- Space complexity: O(n)
- - We store up to the length of the list

## Time 
08/01/2025 | 0:11:44