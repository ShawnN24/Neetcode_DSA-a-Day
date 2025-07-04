# Encode and Decode Strings

## Problem Statement
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

### Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

### Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

## My Solution Journey

Approach 1: Best
The best approach is to store the string length along with an indicator like a # at the beginning of every string. This way we can decode by reading that number and jumping to the end.
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strLen = int(s[i:j])
            i = j + 1
            j = i + strLen
            decodedList.append(s[i:j])
            i = j
        
        return decodedList
```
Time & Space Complexity
- Let:
- - m = sum of lengths of all strings
- - n = number of strings
- Time complexity: O(m)
- - For encode and decode
- Space complexity: O(m + n)
- - For encode and decode

## Time 
07/04/2025 | 0:35:05