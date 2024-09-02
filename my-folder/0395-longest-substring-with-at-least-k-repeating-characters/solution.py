class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        # Count the frequency of each character in the string
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Find the first character that occurs fewer than k times
        for i, char in enumerate(s):
            if freq[char] < k:
                # Recur for the substring segments
                left_substring = self.longestSubstring(s[:i], k)
                right_substring = self.longestSubstring(s[i+1:], k)
                return max(left_substring, right_substring)
        
        # If every character occurs at least k times, the whole string is valid
        return len(s)
