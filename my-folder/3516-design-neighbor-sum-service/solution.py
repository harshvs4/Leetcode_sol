from typing import List

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.position_map = {}
        # Create a map from value to its (i, j) position in the grid
        for i in range(self.n):
            for j in range(self.n):
                self.position_map[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        i, j = self.position_map[value]
        adjacent_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        adjacent_sum = 0
        
        for di, dj in adjacent_directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                adjacent_sum += self.grid[ni][nj]
                
        return adjacent_sum

    def diagonalSum(self, value: int) -> int:
        if value not in self.position_map:
            return 0
        
        i, j = self.position_map[value]
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        diagonal_sum = 0
        
        for di, dj in diagonal_directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                diagonal_sum += self.grid[ni][nj]
                
        return diagonal_sum

# Example usage:
# grid = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# obj = neighborSum(grid)
# print(obj.adjacentSum(4))  # Should return 12 (1+3+5+7)
# print(obj.diagonalSum(4))  # Should return 20 (0+2+6+8)

