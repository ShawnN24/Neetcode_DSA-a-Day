from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strLen = int(s[i:j])
            i = j + 1
            j = i + strLen
            decodedList.append(s[i:j])
            i = j
        
        return decodedList