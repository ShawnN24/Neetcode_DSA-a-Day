class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstr = 0
        j = 0

        if len(s) <= 1:
            return len(s)

        for i in range(len(s)):
            if s[i] in s[j:i]:
                # Keep removing till we find the prev duplicate
                while s[i] in s[j:i]:
                    j += 1
            longestSubstr = max(longestSubstr, len(s[j:i]))
            print("longestSubstr:",s[j:i+1])

        return longestSubstr + 1