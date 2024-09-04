class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        tcount = 0

        # Loop over all substrings of length 3
        for i in range(len(s) - 2):
            substring = s[i:i + 3]  # Get the substring of length 3
            if len(set(substring)) == 3:  # Check if all characters are unique
                tcount += 1

        return tcount

