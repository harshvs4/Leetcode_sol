class Solution:
    def path(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float('inf')

        if dp[i][j] != -1:return dp[i][j]

        up = grid[i][j] + self.path(i-1, j, grid, dp)
        left = grid[i][j] + self.path(i, j-1, grid, dp)

        dp[i][j] = min(up, left)

        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prev = [0]*m

        for i in range(n):
            temp = [0]*m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[j] = grid[0][0]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up = float('inf')
                    left = grid[i][j]
                    if j > 0:
                        left += temp[j-1]
                    else:
                        left = float('inf')
                    
                    temp[j] = min(up, left)
            prev = temp

        return prev[m-1]
        
