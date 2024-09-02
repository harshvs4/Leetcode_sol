class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:return 0
        maxi = 1

        for i in range(len(s)):
            visited = set()
            visited.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in visited:
                    visited.add(s[j])
                    maxi = max(maxi, j-i+1)
                else:
                    break
        
        return maxi

        
