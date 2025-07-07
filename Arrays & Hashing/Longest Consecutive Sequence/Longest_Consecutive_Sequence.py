from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for num in nums:
            if (num-1) not in nums:
                tempLen = 1
                while (num+tempLen) in nums:
                    tempLen += 1
                longestSequence = max(longestSequence, tempLen)

        return longestSequence