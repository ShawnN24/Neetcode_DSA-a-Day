class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {} # mapping {char: count}
        windowMap = {} # mapping {char: count}
        window, windowLen = [-1, -1], float("infinity")
        l = 0

        if t == "":
            return ""

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        have, need = 0, len(tMap)

        for r in range(len(s)):
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1

            if s[r] in tMap and windowMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < windowLen:
                    window = [l, r]
                    windowLen = r - l + 1
                
                windowMap[s[l]] -= 1
                if s[l] in tMap and windowMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        l, r = window
        return s[l:r+1] if windowLen != float("infinity") else ""