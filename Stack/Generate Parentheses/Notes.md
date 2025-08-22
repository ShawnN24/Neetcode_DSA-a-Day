# Generate Parentheses

## Problem Statement
MEDIUM

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

### Example 1:

Input: n = 1

Output: ["()"]

### Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

## My Solution Journey

Approach 1: Stack
The best approach is to have a stack to track the current number of parenthesis and poping after recursion to replace any posible open with closed parethesis
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(opened, closed):
            # base case
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                backtrack(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()

        # start with 0 opened & 0 closed parenthesis
        backtrack(0, 0)
        
        return res
```
Time & Space Complexity
- Time complexity: O(4^n/sqrt(n))
- - We recursivly loop through the list of parethesis for every possibly open and closed
- Space complexity: O(n)
- - We store up to the length of the list

## Time 
08/22/2025 | 0:29:40