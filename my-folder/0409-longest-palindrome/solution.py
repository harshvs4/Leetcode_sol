class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}

        # Count frequency of each character
        for char in s:
            if char not in hmap:
                hmap[char] = 1
            else:
                hmap[char] += 1

        length = 0
        odd_found = False

        # Calculate the length of the longest palindrome
        for freq in hmap.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True

        # If there's an odd frequency character, it can be placed in the center
        if odd_found:
            length += 1

        return length

