from typing import List


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