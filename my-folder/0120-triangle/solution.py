class Solution:
    def countp(self, i, j, n, dp, grid):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == n-1:
            return grid[i][j]

        down = grid[i][j] + self.countp(i+1, j, n, dp, grid)
        downr = grid[i][j] + self.countp(i+1, j+1, n, dp, grid)

        dp[i][j] = min(down, downr)

        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(n)] for i in range(n)]
        return self.countp(0, 0, n, dp, triangle)


        
