from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: 
            return [strs] 

        res = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)

        return list(res.values())

