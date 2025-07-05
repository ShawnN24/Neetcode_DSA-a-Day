# Products of Array Except Self

## Problem Statement
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

### Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

### Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

## My Solution Journey

Approach 1: Brute Force
The obvious first approach would be to brute force the question by looping through the array a full time per each number to calculate its product.
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res
```
Time & Space Complexity
- Time complexity: O(n^2)
- - Loop through a full time for every number in the array
- Space complexity: O(n)
- - We store the length of the array

Approach 2: Prefix & Suffix
The best approach is to loop through the array and calculate the prefix for each number. Then loop back and calculate each suffix. Then calculating their product in the output as we iterate.
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pref = 1
        suff = 1

        for i in range(len(nums)):
            if i != 0:
                pref *= nums[i-1]
            output.append(pref)
        
        for j in range(len(nums) -1, 0, -1):
            if j != len(nums):
                suff *= nums[j]
            output[j-1] *= suff
        
        return output
```
Time & Space Complexity
- Time complexity: O(n)
- - We loop through the array twice so our time complexity is O(2n) which simplifies to O(n)
- Space complexity: O(n)
- - We store the length of the array

## Time 
07/05/2025 | 0:27:49