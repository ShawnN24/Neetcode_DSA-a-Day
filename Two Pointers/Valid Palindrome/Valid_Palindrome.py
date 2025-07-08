class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        iOffset = 0
        jOffset = 0
        
        for l in range(len(s) // 2):
            i = l + iOffset
            j = len(s) - 1 - l + jOffset
            while i < len(s) and not s[i].isalnum():
                iOffset += 1
                i = l + iOffset
            while j > 0 and not s[j].isalnum():
                jOffset -= 1
                j = len(s) - 1 - l + jOffset
            if i >= len(s) or j <= 0:
                return True
            if s[i] != s[j]:
                return False
        return True