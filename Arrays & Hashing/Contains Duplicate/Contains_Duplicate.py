from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curVals = set()

        for num in nums:
            if num in curVals:
                return True
            curVals.add(num)
        
        return False