# Container With Most Water

## Problem Statement
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

### Example 2:

Input: height = [2,2,2]

Output: 4

## My Solution Journey

Approach 1: Two Pointers
The best approach is to have two pointers and calculate the container size and moving the pointers based on which is taller
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestContainer = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            container = min(heights[l], heights[r]) * (r - l)
            bestContainer = max(container, bestContainer)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return bestContainer
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the array once
- Space complexity: O(1)
- - Constant time

## Time 
07/11/2025 | 0:07:10