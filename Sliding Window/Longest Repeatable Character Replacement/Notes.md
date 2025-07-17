# Longest Repeatable Character Replacement

## Problem Statement
MEDIUM

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

### Example 1:

Input: s = "XYYX", k = 2

Output: 4

### Explanation

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

### Example 2:

Input: s = "AAABABB", k = 1

Output: 5

## My Solution Journey

Approach 1: Brute Force-
The obvious first approach is to brute force by iterating through the string for every substring until it breaks.
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
```
Time & Space Complexity
- Time complexity: O(n^2)
- - We loop through the string once for each character in the string
- Space complexity: O(m)
- - We store up to the number of unique characters

Approach 2: Two Pointers
The best approach is to have two pointers for each side of the window tracking when the window breaks the k replacements and the biggest window size achieved. 
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # mapping {char: count}
        l = 0
        maxCount = 0
        biggestWindow = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])

            while (r - l + 1) - maxCount > k: # window - maxCount > k
                count[s[l]] -= 1
                l += 1
            
            biggestWindow = max(biggestWindow, r - l + 1)
        
        return biggestWindow
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the string once
- Space complexity: O(m)
- - We store up to the number of unique characters

## Time 
07/17/2025 | 0:51:51