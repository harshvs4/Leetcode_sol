class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_freq = {0: 1}  # Dictionary to store the frequency of cumulative sums

        for num in nums:
            cumulative_sum += num
            
            # Check if there is a cumulative sum that matches the current cumulative sum minus k
            if cumulative_sum - k in sum_freq:
                count += sum_freq[cumulative_sum - k]
            
            # Update the frequency of the current cumulative sum
            if cumulative_sum in sum_freq:
                sum_freq[cumulative_sum] += 1
            else:
                sum_freq[cumulative_sum] = 1

        return count
        
