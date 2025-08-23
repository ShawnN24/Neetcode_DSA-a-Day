# Daily Temperatures

## Problem Statement
MEDIUM

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

### Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

### Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]

## My Solution Journey

Approach 1: Stack
The best approach is to have a stack to track pairs of temp and index. Iterating forward and poping any tempuratures that are greater than the top of the stack and recording the cur index with the last popped index 
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((temp, i))
        return res
```
Time & Space Complexity
- Time complexity: O(n)
- - We loop through the array once popping at most the entire array with is O(2n) which simplifies to O(n)
- Space complexity: O(n)
- - We store up to the length of the array

## Time 
08/23/2025 | 1:01:45