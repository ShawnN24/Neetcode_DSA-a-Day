from collections import deque
from typing import List


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