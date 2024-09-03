from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_map = Counter(nums)  # Create a frequency map
        max_length = 0

        # Iterate over the numbers in the frequency map
        for num in freq_map:
            if num + 1 in freq_map:  # Check if the next consecutive number exists
                # Calculate the length of the subsequence formed by num and num + 1
                length = freq_map[num] + freq_map[num + 1]
                max_length = max(max_length, length)  # Update the max length if necessary

        return max_length

