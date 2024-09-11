class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # Step 1: Compute the sum of the first window
        current_sum = sum(nums[:k])
        maxi = current_sum  # Initialize the maximum sum with the first window's sum

        # Step 2: Slide the window across the array
        for i in range(k, n):
            # Update the sum by adding the new element and removing the first element of the previous window
            current_sum += nums[i] - nums[i - k]
            maxi = max(maxi, current_sum)

        # Step 3: Return the maximum average
        return maxi / k

