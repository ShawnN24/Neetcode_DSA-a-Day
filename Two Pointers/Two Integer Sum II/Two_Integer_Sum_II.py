from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            result = numbers[l] + numbers[r]
            if result == target:
                return [l+1,r+1]
            if result > target:
                r -= 1
                continue
            if result < target:
                l += 1
                continue
        
        return []