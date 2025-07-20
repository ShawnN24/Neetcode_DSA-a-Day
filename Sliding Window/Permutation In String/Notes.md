# Permutation in String

## Problem Statement
MEDIUM

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

### Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true

### Explanation

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

### Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false


## My Solution Journey

Approach 1: Brute Force-
The obvious first approach is to brute force by iterating through the string for every substring
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False
```
Time & Space Complexity
- Time complexity: O(n^3 log n)
- - We loop through the string once for each character in the string O(n^2) and we sort each time O(n log n)
- Space complexity: O(m)
- - We store up to the number of unique characters

Approach 2: Sliding Window Hash Map
My best approach is to have two pointers for each side of the window tracking the characters in the window to see if it matches that of s1
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s1Map = {} # mapping: {char: count}
        windowMap = {} # mapping: {char: count}

        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        while r < len(s2):
            print("l:", l, "r:", r)
            print("windowMap:", windowMap, "=? s1Map:", s1Map)
            windowMap[s2[r]] = windowMap.get(s2[r], 0) + 1
            r += 1
            if (r - l) > len(s1):
                windowMap[s2[l]] = windowMap.get(s2[l], 0) - 1
                if windowMap[s2[l]] == 0:
                    del windowMap[s2[l]]
                l += 1
            if windowMap == s1Map:
                print("windowMap:", windowMap, "== s1Map:", s1Map)
                return True
        
        return False
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the string once
- Space complexity: O(1)
- - We can store up to 26 different characters because we are limited to lower case a - z

## Time 
07/20/2025 | 0:30:27