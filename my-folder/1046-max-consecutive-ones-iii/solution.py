class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer for the sliding window
        zero_count = 0  # To count how many zeroes have been flipped
        maxi = 0  # To track the maximum length of the window

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # If zero_count exceeds k, move the left pointer to shrink the window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Shrink the window from the left

            # Update the maximum length of the window
            maxi = max(maxi, right - left + 1)

        return maxi

