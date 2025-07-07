# Longest Consecutive Sequence

## Problem Statement
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

### Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4

### Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

## My Solution Journey

Approach 1: Brute Force
The obvious first approach would be to brute force the question by looping through for each value to grab its streak
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
```
Time & Space Complexity
- Time complexity: O(n^2)
- - Loop through the list once for every num
- Space complexity: O(n)
- - We store the set of nums

Approach 2: Hash Set
The best approach is to loop through the list once determining which nums are starter nums and how long their sequences are
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for num in nums:
            if (num-1) not in nums:
                tempLen = 1
                while (num+tempLen) in nums:
                    tempLen += 1
                longestSequence = max(longestSequence, tempLen)

        return longestSequence
```
Time & Space Complexity
- Time complexity: O(n)
- - Loop through the list once
- Space complexity: O(n)
- - We store the set of nums

## Time 
07/07/2025 | 0:32:04