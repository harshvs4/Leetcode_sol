from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))  
        cnt = 0
        left = 0
        freq_map = defaultdict(int)
        
        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            
            # Shrink the window from the left until it is no longer complete
            while len(freq_map) == distinct_count:
                cnt += len(nums) - right  # All subarrays ending at 'right' index are valid
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1
        
        return cnt

