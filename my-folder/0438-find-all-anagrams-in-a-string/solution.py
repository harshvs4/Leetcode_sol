from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        
        # If the string p is longer than s, no anagrams are possible
        if np > ns:
            return []

        # Frequency counter for p
        p_count = Counter(p)
        
        # Frequency counter for the first window of size np in s
        s_count = Counter(s[:np - 1])
        
        result = []
        
        # Sliding window over s
        for i in range(np - 1, ns):
            # Add the new character to the current window's count
            s_count[s[i]] += 1
            
            # Check if the current window's frequency matches with p's frequency
            if s_count == p_count:
                result.append(i - np + 1)
            
            # Remove the character that is sliding out of the window
            s_count[s[i - np + 1]] -= 1
            # If the count becomes 0, remove it from the dictionary to maintain clean comparisons
            if s_count[s[i - np + 1]] == 0:
                del s_count[s[i - np + 1]]
        
        return result

