class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # This set keeps track of unique characters in the current window
        left = 0  # Left pointer of the sliding window
        maxi = 0  # Maximum length of substring without repeating characters

        # Right pointer of the sliding window
        for right in range(len(s)):
            # If the character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length found
            maxi = max(maxi, right - left + 1)
        
        return maxi

