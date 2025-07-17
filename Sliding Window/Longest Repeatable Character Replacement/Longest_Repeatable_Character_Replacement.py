class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # mapping {char: count}
        l = 0
        maxCount = 0
        biggestWindow = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])

            while (r - l + 1) - maxCount > k: # window - maxCount > k
                count[s[l]] -= 1
                l += 1
            
            biggestWindow = max(biggestWindow, r - l + 1)
        
        return biggestWindow