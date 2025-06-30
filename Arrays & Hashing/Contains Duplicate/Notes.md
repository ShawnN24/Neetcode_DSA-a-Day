# Contains Duplicate

## Problem Statement
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

### Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

### Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

## My Solution Journey

Approach 1: Brute Force
Obvious first approach was a brute force method, which involves constantly comparing two pointers as they iterate through the array
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
```
Time & Space Complexity
- Time complexity: O(n^2)
- - We iterate in array n times for every n nums
- Space complexity: O(1)
- - We store nothing so our space complexity is linear 

Approach 2: Hash Set
The best approach utilizes a set (unordered collection of unique elements) iterating through the array only once and checking if it already exists in the set
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curVals = set()
        for num in nums:
            if num in curVals:
                return True
            curVals.add(num)
        return False
```
Time & Space Complexity
- Time complexity: O(n)
- - We iterate the array up to the length of the array
- Space complexity: O(n)
- - We store up to the length of the array

## Time 
06/29/2025 | 0:09:42