from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    p += 4
                    if i > 0 and grid[i-1][j] == 1:  # Check the cell above
                        p -= 1
                    if i < n - 1 and grid[i+1][j] == 1:  # Check the cell below
                        p -= 1
                    if j > 0 and grid[i][j-1] == 1:  # Check the cell to the left
                        p -= 1
                    if j < m - 1 and grid[i][j+1] == 1:  # Check the cell to the right
                        p -= 1
                        
        return p

