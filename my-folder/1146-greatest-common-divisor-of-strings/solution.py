import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are the same
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of the two strings
        gcd_len = math.gcd(len(str1), len(str2))
        
        # Return the prefix of str1 (or str2) of length gcd_len
        return str1[:gcd_len]

