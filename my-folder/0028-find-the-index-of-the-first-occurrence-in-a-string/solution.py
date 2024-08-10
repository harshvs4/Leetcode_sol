class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ind = -1
        n = len(haystack)

        if n < len(needle):return -1

        for i in range(n):
            if haystack[i] == needle[0]:
                x = haystack[i:i+len(needle)]
                if x == needle:
                    return i
        
        return ind
        
        
