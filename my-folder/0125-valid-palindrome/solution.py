class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:return True
        s = s.lower()
        sen = ''.join(char for char in s if char.isalnum())
        i = 0
        j = len(sen)-1

        while i <= j:
            if sen[i]!=sen[j]:
                return False
            i+=1
            j-=1
        return True


