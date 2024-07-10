class Solution:
    def cp(self, i, j, m, n, dp, grid):
        if i == m-1 and j == n-1 and grid[i][j] == 0:
            return 1
        if i >= m or j >= n:
            return 0
        if grid[i][j] == 1:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        down = self.cp(i+1, j, m , n, dp, grid)
        right = self.cp(i, j+1, m, n, dp, grid)

        dp[i][j] = down+right

        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for j in range(n)] for i in range(m)]
        return self.cp(0,0,m,n,dp,obstacleGrid)
        
