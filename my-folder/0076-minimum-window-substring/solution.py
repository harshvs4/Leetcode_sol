from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # Create a frequency count for the target string
        target_count = Counter(t)
        current_count = Counter()

        required = len(target_count)
        formed = 0
        
        left = 0
        min_len = float('inf')
        min_window = ""
        
        for right in range(len(s)):
            char = s[right]
            current_count[char] += 1
            
            # If the current character's frequency matches the target's frequency
            if char in target_count and current_count[char] == target_count[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be valid
            while left <= right and formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right+1]
                
                # The character at the left pointer
                char = s[left]
                current_count[char] -= 1
                if char in target_count and current_count[char] < target_count[char]:
                    formed -= 1
                
                # Move the left pointer ahead
                left += 1
        
        return min_window if min_len != float('inf') else ""


