class Solution:
    def maxOperations(self, s: str) -> int:
        cnt = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            elif i > 0 and s[i - 1] == '1':
                res += cnt
        return res
        
