class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a DP array where dp[i] means whether s[0:i] can be segmented.
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string can always be segmented.
        
        # Loop through the string s
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # Check if the current word fits in the substring ending at i
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break  # No need to check further if we found a valid segmentation
        
        # The last element in dp will be True if the whole string can be segmented.
        return dp[-1]

