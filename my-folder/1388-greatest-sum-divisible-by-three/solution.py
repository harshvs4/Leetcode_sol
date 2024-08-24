class Solution:
    def maxSumDivThree(self, arr: List[int]) -> int:
        # Initialize dp array
        dp = [-float('inf')] * 3
        dp[0] = 0
        
        for num in arr:
            # Make a copy of dp array to store new values
            new_dp = dp[:]
            for j in range(3):
                new_dp[(j + num) % 3] = max(new_dp[(j + num) % 3], dp[j] + num)
            dp = new_dp
        
        # The answer is the maximum sum that is divisible by 3
        return dp[0]
        
