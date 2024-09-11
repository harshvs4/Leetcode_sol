class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')  # Using a set for O(1) lookup
        n = len(s)
        current_count = 0
        maxi = 0

        # Initialize the count for the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        maxi = current_count  # Set the initial maximum

        # Slide the window across the string
        for i in range(k, n):
            # Remove the effect of the character going out of the window
            if s[i - k] in vowels:
                current_count -= 1
            # Add the effect of the new character entering the window
            if s[i] in vowels:
                current_count += 1

            # Update the maximum
            maxi = max(maxi, current_count)

        return maxi

