class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        i = 0
        n = len(s)-1

        while i <= n:
            s[i], s[n] = s[n], s[i]
            i+=1
            n-=1
        
        return ' '.join(s)
        
