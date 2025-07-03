# Group Anagrams

## Problem Statement
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

### Example 2:

Input: strs = ["x"]

Output: [["x"]]

### Example 3:

Input: strs = [""]

Output: [[""]]

## My Solution Journey

Approach 1: List of Hash Maps
My approach utilized a temporary hashmap to store the char buckets. If the character buckets matched up, I would add it to the output based on the index their variation was stored.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        variationList = []
        
        for string in strs:
            tempCharMap = {} # {char: count}
            for char in string:
                tempCharMap[char] = tempCharMap.get(char, 0) + 1
            if tempCharMap in variationList:
                print(tempCharMap)
                index = variationList.index(tempCharMap)
                output[index].append(string)
            else:
                variationList.append(tempCharMap)
                output.append([string])
        
        return output
```
Time & Space Complexity
- Let: 
- - n = number of strings in strs
- - k = maximum length of any string
- Time complexity: O(n^2 * k)
- - For each of the n strings, we iterate over all chars O(k) and check if the map exists in the variationList which can contain up to n maps O(n * k). So, O(n^2 * k)
- Space complexity: O(n * k)
- - We store the char map for each string O(k) for each map O(n). So, O(n * k)

Approach 2: Hash Table
The best approach utilizes a hashmap to store the charCount to list of Anagrams
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hashmap: mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                # grab ascii of character and subtract it from ascii of a
                count[ord(c) - ord("a")] += 1
                print("COUNT["+c+"]:",count[ord(c) - ord("a")])

            res[tuple(count)].append(s)
            print("RES:", res[tuple(count)])

        return list(res.values())
```
Time & Space Complexity
- Let: 
- - n = number of strings in strs
- - k = maximum length of any string
- Time complexity: O(n * k)
- - For each of the n strings, we iterate over all chars O(k). So, O(n * k)
- Space complexity:
- - O(n) extra space
- - O(n * k) space for the output list

## Time 
07/02/2025 | 1:09:09