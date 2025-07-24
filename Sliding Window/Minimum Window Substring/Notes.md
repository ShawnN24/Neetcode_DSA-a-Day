# Minimum Window Substring

## Problem Statement
HARD

Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

### Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

### Explanation

Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

### Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"

### Example 3:

Input: s = "x", t = "xy"

Output: ""


## My Solution Journey

Approach 1: Sliding Window Hash Map
The best approach is to have two pointers for each side of the window tracking the characters in the window to see if it matches that of s1
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} # mapping {char: count}
        windowMap = {} # mapping {char: count}
        window, windowLen = [-1, -1], float("infinity")
        l = 0

        if t == "":
            return ""

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        have, need = 0, len(tMap)

        for r in range(len(s)):
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1

            if s[r] in tMap and windowMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < windowLen:
                    window = [l, r]
                    windowLen = r - l + 1
                
                windowMap[s[l]] -= 1
                if s[l] in tMap and windowMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        l, r = window
        return s[l:r+1] if windowLen != float("infinity") else ""
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the string once
- Space complexity: O(m)
- - We store up to m number of unique characters in s and t

## Time 
07/23/2025 | 1:11:11