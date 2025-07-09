# Two Integer Sum II

## Problem Statement
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

### Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

### Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

## My Solution Journey

Approach 1: Two Pointers
The best approach is to use two pointers to iterate on either side of the list to find the two numbers that sum to the target
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            result = numbers[l] + numbers[r]
            if result == target:
                return [l+1,r+1]
            if result > target:
                r -= 1
                continue
            if result < target:
                l += 1
                continue
        
        return []
```
Time & Space Complexity
- Time complexity: O(n)
- - Worse case is you loop through the length of the list
- Space complexity: O(1)
- - Storage is constant time

## Time 
07/09/2025 | 0:09:45