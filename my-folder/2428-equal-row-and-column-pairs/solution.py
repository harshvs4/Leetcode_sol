class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = {}
        col = {}

        x = len(grid)
        y = len(grid[0])

        for i in range(x):
            row[i] = grid[i]

        print(row)

        for i in range(y):
            arr = []
            for j in range(x):
                arr.append(grid[j][i])
            col[i] = arr

        
        count_common = 0

        # Compare each row to each column and count matches
        for r in row.values():
            for c in col.values():
                if r == c:
                    count_common += 1

        return count_common
