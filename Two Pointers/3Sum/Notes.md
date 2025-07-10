# 3Sum

## Problem Statement
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

### Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

### Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

### Example 2:

Input: nums = [0,1,1]

Output: []

### Explanation:
Explanation: The only possible triplet does not sum up to 0.

### Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

### Explanation:
Explanation: The only possible triplet sums up to 0.

## My Solution Journey

Approach 1: Two Pointers
The best approach is to loop through the sorted list once and loop through the rest using two pointers to compare the threeSum 
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # prevent duplicates
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0: 
                    l += 1 
                elif threeSum > 0: 
                    r -= 1 
                else:
                    triplets.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return triplets
```
Time & Space Complexity
- Time complexity: O(n^2)
- - Loop through the list once for every number in the list
- Space complexity: O(n)
- - O(n) or O(1): Storage depended on sorting algorithm
- - O(m): Space for the output list

## Time 
07/10/2025 | 0:53:53