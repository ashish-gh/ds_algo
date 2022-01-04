from typing import DefaultDict, List
from collections import defaultdict


# Time Complexity: O(m* n * 26) : 
# 26 = characters in string 
# m = total number of input strings
# n = average length of each string


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[str]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] +=1
            
            res[tuple(count)].append(s)
        return list(res.values())
            

sl = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res = sl.group_anagrams(strs)
print(res)
