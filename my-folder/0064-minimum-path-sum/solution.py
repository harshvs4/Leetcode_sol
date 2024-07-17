class Solution:
    def countp(self, i, j, dp, grid):
            if i == 0 and j == 0: return grid[0][0]

            if i < 0 or j < 0: return float('inf')

            if dp[i][j] != -1: return dp[i][j]

            up = grid[i][j] + self.countp(i-1, j, dp, grid)
            
            left = grid[i][j] + self.countp(i, j-1, dp, grid)
            
            dp[i][j] = min(up, left)
            return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for j in range(m)] for i in range(n)]
        return self.countp(n-1, m-1, dp, grid)
        
