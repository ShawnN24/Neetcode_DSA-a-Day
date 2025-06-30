class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramDict = {}

        if len(s) != len(t):
            return False

        for char in s:
            anagramDict[char] = anagramDict.get(char, 0) + 1
        print(anagramDict)
        
        for char in t:
            if char not in anagramDict:
                return False
            if anagramDict[char] == 0:
                return False
            anagramDict[char] = anagramDict.get(char, 0) -1
        print(anagramDict)
        
        return True