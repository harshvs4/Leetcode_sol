class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:return True
        i = 0
        if s == "":return True

        for char in t:
            if s[i] == char:
                i+=1
            if i == len(s):
                return True
        return False
            

        
