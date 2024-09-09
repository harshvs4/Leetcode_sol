class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        s = [0]*(n+m)
        i = x = y = 0

        while x < n and y < m:
            if i % 2 == 0:
                s[i] = word1[x]
                x+=1
            else:
                s[i] = word2[y]
                y+=1
            i+=1
        
        while x < n:
            s[i] = word1[x]
            x+=1
            i+=1
        
        while y < m:
            s[i] = word2[y]
            y+=1
            i+=1

        return "".join(s)



        
