# Valid Palindrome

## Problem Statement
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

### Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

### Example 2:

Input: s = "tab a cat"

Output: false

## My Solution Journey

Approach 1: Two Pointers
The best approach is to use two pointers to iterate on either side of the palindrome comparing each alpha numeric character
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        iOffset = 0
        jOffset = 0
        
        for l in range(len(s) // 2):
            i = l + iOffset
            j = len(s) - 1 - l + jOffset
            while i < len(s) and not s[i].isalnum():
                iOffset += 1
                i = l + iOffset
            while j > 0 and not s[j].isalnum():
                jOffset -= 1
                j = len(s) - 1 - l + jOffset
            if i >= len(s) or j <= 0:
                return True
            if s[i] != s[j]:
                return False
        return True
```
Time & Space Complexity
- Time complexity: O(n)
- - Loop through the string once
- Space complexity: O(1)
- - Storage is constant time

## Time 
07/08/2025 | 0:13:20