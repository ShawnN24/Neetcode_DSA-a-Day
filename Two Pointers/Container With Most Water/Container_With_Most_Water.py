from typing import List


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