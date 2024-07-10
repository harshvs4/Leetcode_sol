class Solution:
    def cp(self, i, j, m, n, dp):
        # Base case: if the current position is out of bounds
        if i >= m or j >= n:
            return 0
        # Base case: if the current position is the bottom-right cell
        if i == m - 1 and j == n - 1:
            return 1
        # If this subproblem is already solved, return the stored result
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Recursive calls: calculate the number of paths by moving right and down
        down = self.cp(i + 1, j, m, n, dp)
        right = self.cp(i, j + 1, m, n, dp)
        
        # Store the result in the dp array
        dp[i][j] = down + right
        
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the DP table with -1
        dp = [[-1 for j in range(n)] for i in range(m)]
        # Start the recursive function from the top-left cell
        return self.cp(0, 0, m, n, dp)
