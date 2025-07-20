class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s1Map = {} # mapping: {char: count}
        windowMap = {} # mapping: {char: count}

        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        while r < len(s2):
            print("l:", l, "r:", r)
            print("windowMap:", windowMap, "=? s1Map:", s1Map)
            windowMap[s2[r]] = windowMap.get(s2[r], 0) + 1
            r += 1
            if (r - l) > len(s1):
                windowMap[s2[l]] = windowMap.get(s2[l], 0) - 1
                if windowMap[s2[l]] == 0:
                    del windowMap[s2[l]]
                l += 1
            if windowMap == s1Map:
                print("windowMap:", windowMap, "== s1Map:", s1Map)
                return True
        
        return False