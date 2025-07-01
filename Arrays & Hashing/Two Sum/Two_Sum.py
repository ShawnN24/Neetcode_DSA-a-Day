from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHashMap = {}

        for i in range(len(nums)):
            if nums[i] in numHashMap:
                return [numHashMap[nums[i]], i]
            numHashMap[target-nums[i]] = i