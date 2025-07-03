from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hashmap: mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                # grab ascii of character and subtract it from ascii of a
                count[ord(c) - ord("a")] += 1
                print("COUNT["+c+"]:",count[ord(c) - ord("a")])

            res[tuple(count)].append(s)
            print("RES:", res[tuple(count)])

        return list(res.values())