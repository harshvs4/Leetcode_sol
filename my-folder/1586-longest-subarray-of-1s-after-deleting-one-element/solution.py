class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        zero_count = 0
        count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            count = max(count, right-left+1)

        return count-1



        
