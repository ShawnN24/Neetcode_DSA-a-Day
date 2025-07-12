# Trapping Rain Water

## Problem Statement
HARD

You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

### Example 1:

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

## My Solution Journey

Approach 1: Brute Force
The obvious first approach is to brute force by iterating through the array from the left calculating the max at the given point, then from the right and determining the smallest to calc area.
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
                
            res += min(leftMax, rightMax) - height[i]
        return res
```
Time & Space Complexity
- Time complexity: O(n^2)
- - We only loop through the array twice
- Space complexity: O(1)
- - Constant time

Approach 2: Two Pointers
The best approach is to have two pointers, and move them based on which is smaller. Then calculating whether it dips from that sides local max and adding to the area.
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                maxArea += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxArea += maxR - height[r]
        
        return maxArea
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the array once
- Space complexity: O(1)
- - Constant time

## Time 
07/12/2025 | 0:58:44