from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        product = 1
        left = 0

        for right in range(len(nums)):
            product *= nums[right]

            # Shrink the window from the left if the product is greater or equal to k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # Add the number of subarrays ending at `right`
            count += right - left + 1

        return count

