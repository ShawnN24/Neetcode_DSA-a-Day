# Valid Parentheses

## Problem Statement
EASY

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

### Example 1:

Input: s = "[]"

Output: true

### Example 2:

Input: s = "([{}])"

Output: true

### Example 3:

Input: s = "[(])"

Output: false

### Explanation

Explanation: The brackets are not closed in the correct order.

## My Solution Journey

Approach 1: Stack
The best approach is to have two pointers for each side of the window tracking the characters in the window to see if it matches that of s1
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack

        for c in s:
            if c == '(' or c == '{' or c == '[':
                print("APPENDED:",c)
                stack.append(c)
            elif c == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    print("POPPED:",c)
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
```
Simplified solution code:
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the string once
- Space complexity: O(n)
- - We store up to the O(n/2) which simplifies to O(n)

## Time 
07/27/2025 | 0:10:59