# Contains Duplicate

## Problem Statement
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:

Input: s = "racecar", t = "carrace"

Output: true

### Example 2:

Input: s = "jar", t = "jam"

Output: false

## My Solution Journey

Approach 1: Brute Force
Obvious first approach was a brute force method. This method would iterate string t for every char in string s matching them one for one.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        for char_s in s:
            if char_s in t:
                t = t.replace(char_s, "", 1)
            else:
                return False
        
        return True
```
Time & Space Complexity
- Time complexity: O(n*m)
- - We iterate string len t (m), string len s (n) number of times 
- Space complexity: O(1)
- - We store nothing so our space complexity is linear 

Approach 2: Hash Map
The best approach utilizes a hash map (a list of key: value pairs). Firstly iterating through string s, and couting them up. Then iterating through string t and counting them down.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramDict = {}

        if len(s) != len(t):
            return False

        for char in s:
            anagramDict[char] = anagramDict.get(char, 0) + 1
        print(anagramDict)
        
        for char in t:
            if char not in anagramDict:
                return False
            if anagramDict[char] == 0:
                return False
            anagramDict[char] = anagramDict.get(char, 0) -1
        print(anagramDict)
        
        return True
```
Time & Space Complexity
- Time complexity: O(n+m)
- - We iterate both the strings once, so it would be the len s (n) + len t (m)
- Space complexity: O(1)
- - Since we have at most 26 characters in the alphabet, storage is linear

## Time 
06/30/2025 | 0:26:10