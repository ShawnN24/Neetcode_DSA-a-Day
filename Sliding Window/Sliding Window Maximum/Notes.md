# Sliding Window Maximum

## Problem Statement
HARD

You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

### Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

## My Solution Journey

Approach 1: Sliding Window Brute Force
The best approach is to have two pointers for each side of the window tracking the characters in the window to see if it matches that of s1
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [max(nums)]
        
        l = 0
        res = []
        
        for r in range(len(nums)+1):
            if r - l == k:
                res.append(max(nums[l:r]))
                l += 1
        
        return res
```
Time & Space Complexity
- Time complexity: O(n * k)
- - We only loop through the string once and loop through the window of length k to find the max every time
- Space complexity: O(n)
- - We store O(n - k + 1) which simplifies to O(n)

Approach 2: Sliding Window Deque
The best approach is to have the sliding window and a queue. The queue tracking max by removing lower values and those out of the window
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [max(nums)]
        
        l, r = 0, 0
        res = []
        q = deque() # index

        while r < len(nums):
            # remove all nums in the q smaller than the curr num
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove top num if its not in the window
            if l > q[0]:
                q.popleft()

            # append the first num in the q to the response
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res
```
Time & Space Complexity
- Time complexity: O(n)
- - We only loop through the string once
- Space complexity: O(n)
- - We store O(n - k + 1) which simplifies to O(n)

## Time 
07/25/2025 | 0:18:07