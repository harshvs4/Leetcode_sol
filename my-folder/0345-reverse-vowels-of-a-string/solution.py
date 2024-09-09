class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Use a set for faster lookup and handle both lowercase and uppercase vowels
        s = list(s)  # Convert the string to a list since strings are immutable
        i, j = 0, len(s) - 1  # Two pointers

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                # Swap the vowels
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1

        return ''.join(s)  # Convert the list back to a string

