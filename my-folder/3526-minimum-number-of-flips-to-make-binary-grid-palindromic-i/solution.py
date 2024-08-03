class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def flips_for_palindrome(arr: List[int]) -> int:
            flips = 0
            left, right = 0, len(arr) - 1
            while left < right:
                if arr[left] != arr[right]:
                    flips += 1
                left += 1
                right -= 1
            return flips

        def total_flips_for_rows(grid: List[List[int]]) -> int:
            total_flips = 0
            for row in grid:
                total_flips += flips_for_palindrome(row)
            return total_flips

        def total_flips_for_columns(grid: List[List[int]]) -> int:
            total_flips = 0
            for col in range(len(grid[0])):
                column_values = [grid[row][col] for row in range(len(grid))]
                total_flips += flips_for_palindrome(column_values)
            return total_flips

        return min(total_flips_for_rows(grid), total_flips_for_columns(grid))
