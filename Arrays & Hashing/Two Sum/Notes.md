# Two Sum

## Problem Statement
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

### Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

### Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]

### Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]

## My Solution Journey

Approach 1: Brute Force
Obvious first approach was a brute force method, which involves two pointers, one to track the current value and another to iterate the list for its match
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return []
```
Time & Space Complexity
- Time complexity: O(n^2)
- - We iterate in array n times for every n nums
- Space complexity: O(1)
- - We store nothing so our space complexity is linear 

Approach 2: Hash Set
The best approach utilizes a hash map to store key value pairs consisting of (expected value, index of pair). This allows us to iterate only once and grab the index of the match if it matches any of the expected values in the hash map.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHashMap = {}

        for i in range(len(nums)):
            if nums[i] in numHashMap:
                return [numHashMap[nums[i]], i]
            numHashMap[target-nums[i]] = i
```
Time & Space Complexity
- Time complexity: O(n)
- - We iterate the array up to the length of the array
- Space complexity: O(n)
- - We store up to the length of the array

## Time 
07/01/2025 | 0:13:16