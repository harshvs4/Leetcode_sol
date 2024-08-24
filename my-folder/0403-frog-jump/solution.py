class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
    
        # Dictionary to hold the stones and their possible jump lengths
        dp = {stone: set() for stone in stones}
        dp[0].add(0)  # Start at stone 0 with a jump of 0
        
        # Iterate over each stone in the list
        for i in range(len(stones)):
            for k in dp[stones[i]]:
                # Possible jump distances: k-1, k, k+1
                for step in [k-1, k, k+1]:
                    if step > 0 and (stones[i] + step) in dp:
                        dp[stones[i] + step].add(step)
        
        # Check if the last stone has any possible jump lengths to reach it
        return bool(dp[stones[-1]])
