# Longest Substring Without Repeating Characters

## Problem Statement
MEDIUM

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

### Example 1:

Input: s = "zxyzxyz"

Output: 3

### Explanation

Explanation: The string "xyz" is the longest without duplicate characters.

### Example 2:

Input: s = "xxxx"

Output: 1

## My Solution Journey

Approach 1: Brute Force-
The obvious first approach is to brute force by iterating through the string for every character until you find a duplicate
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
```
Time & Space Complexity
- Time complexity: O(n * m)
- - We only loop through the array a whole time and for each substring of unique characters
- Space complexity: O(m)
- - We store up to the length of the longest substring of unique characters

Approach 2: Two Pointers
The best approach is to have two pointers, one to track the front of the substrings and one to trail behind closing the gap on any previous duplicates.
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstr = 0
        j = 0

        if len(s) <= 1:
            return len(s)

        for i in range(len(s)):
            if s[i] in s[j:i]:
                # Keep removing till we find the prev duplicate
                while s[i] in s[j:i]:
                    j += 1
            longestSubstr = max(longestSubstr, len(s[j:i]))
            print("longestSubstr:",s[j:i+1])

        return longestSubstr + 1
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the array once
- Space complexity: O(m)
- - We store up to the length of the longest substring of unique characters

## Time 
07/14/2025 | 0:53:25